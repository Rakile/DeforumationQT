import queue
import threading
import wave
import speech_recognition as sp
from array import array

import pyaudio
from PySide6.QtCore import QMetaObject, Qt, Q_ARG
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QPushButton


class Deforumation_Speech():

    def __init__(self, parent=None):
        self.parent = parent
        self.is_recording = False
        # Use a stream with a callback in non-blocking mode
        self.CHUNK_SIZE = 1024
        self.MIN_VOLUME = 500
        self.is_recording = False
        self.BUF_MAX_SIZE = self.CHUNK_SIZE * 10
        self.pyAudio = pyaudio.PyAudio()





    def setComponetValues(self):
        #Get all voice bindings
        header = "speech_binding_"
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "start_prompt_word")
        if val != None:
            self.parent.ui.speech_prompt_start_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "pan_left_word")
        if val != None:
            self.parent.ui.speech_panning_left_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "pan_right_word")
        if val != None:
            self.parent.ui.speech_panning_right_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "pan_up_word")
        if val != None:
            self.parent.ui.speech_panning_up_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "pan_down_word")
        if val != None:
            self.parent.ui.speech_panning_down_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "rotate_left_word")
        if val != None:
            self.parent.ui.speech_rotate_h_left_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "rotate_right_word")
        if val != None:
            self.parent.ui.speech_rotate_h_right_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "rotate_up_word")
        if val != None:
            self.parent.ui.speech_rotate_v_up_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "rotate_down_word")
        if val != None:
            self.parent.ui.speech_rotate_v_down_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "tilt_left_word")
        if val != None:
            self.parent.ui.speech_tilt_cc_bind.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "tilt_right_word")
        if val != None:
            self.parent.ui.speech_tilt_cw_bind.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "zoom_in_word")
        if val != None:
            self.parent.ui.speech_zoom_forwards_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "zoom_out_word")
        if val != None:
            self.parent.ui.speech_zoom_backwards_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "add_to_sentence")
        if val != None:
            self.parent.ui.speech_add_to_prompt_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "cancel_voice_sentence")
        if val != None:
            self.parent.ui.speech_cancel_prompt_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "reset_panning")
        if val != None:
            self.parent.ui.speech_reset_panning_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "reset_zoom")
        if val != None:
            self.parent.ui.speech_reset_zoom_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "reset_rotation")
        if val != None:
            self.parent.ui.speech_reset_rotation_binding.setText(val)
        val = self.parent.deforumation_settings.getGuiConfigValue(header + "reset_tilt")
        if val != None:
            self.parent.ui.speech_reset_tilt_binding.setText(val)

    def saveBindingValues(self, object, event):
        print("Saving bindings.")
        start_prompt_word = self.parent.ui.speech_prompt_start_binding.text()
        pan_left_word = self.parent.ui.speech_panning_left_binding.text()
        pan_right_word = self.parent.ui.speech_panning_right_binding.text()
        pan_up_word = self.parent.ui.speech_panning_up_binding.text()
        pan_down_word = self.parent.ui.speech_panning_down_binding.text()
        rotate_left_word = self.parent.ui.speech_rotate_h_left_binding.text()
        rotate_right_word = self.parent.ui.speech_rotate_h_right_binding.text()
        rotate_up_word = self.parent.ui.speech_rotate_v_up_binding.text()
        rotate_down_word = self.parent.ui.speech_rotate_v_down_binding.text()
        tilt_left_word = self.parent.ui.speech_tilt_cc_bind.text()
        tilt_right_word = self.parent.ui.speech_tilt_cw_bind.text()
        zoom_in_word = self.parent.ui.speech_zoom_forwards_binding.text()
        zoom_out_word = self.parent.ui.speech_zoom_backwards_binding.text()
        add_to_sentence = self.parent.ui.speech_add_to_prompt_binding.text()
        cancel_voice_sentence = self.parent.ui.speech_cancel_prompt_binding.text()
        reset_panning = self.parent.ui.speech_reset_panning_binding.text()
        reset_zoom = self.parent.ui.speech_reset_zoom_binding.text()
        reset_rotation = self.parent.ui.speech_reset_rotation_binding.text()
        reset_tilt = self.parent.ui.speech_reset_tilt_binding.text()

        header = "speech_binding_"
        #value = 0
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "start_prompt_word", start_prompt_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "pan_left_word", pan_left_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "pan_right_word", pan_right_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "pan_up_word", pan_up_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "pan_down_word", pan_down_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "rotate_left_word", rotate_left_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "rotate_right_word", rotate_right_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "rotate_up_word", rotate_up_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "rotate_down_word", rotate_down_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "tilt_left_word", tilt_left_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "tilt_right_word", tilt_right_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "zoom_in_word", zoom_in_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "zoom_out_word", zoom_out_word)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "add_to_sentence", add_to_sentence)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "cancel_voice_sentence", cancel_voice_sentence)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "reset_panning", reset_panning)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "reset_zoom", reset_zoom)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "reset_rotation", reset_rotation)
        self.parent.deforumation_settings.writeDeforumationGuiValuesToConfig(header + "reset_tilt", reset_tilt)
    def createAndCleanArray(self, speech_array):
        speech_array = speech_array.split(",")
        index = 0
        for n in speech_array:
            speech_array[index] = speech_array[index].lstrip().rstrip()
            index += 1
        return speech_array

    def propagateAllComponents(self, sender, original_component_name, value):
        #self.parent.deforumationwidgets.getWidgetContainer()[sender.objectName()].isActivated = value

        #original_component_name = sender.objectName()

        for component in self.parent.deforumationwidgets.getWidgetContainer():
            if component.startswith(original_component_name):
                if type(sender) == QPushButton:
                    button = self.parent.deforumationwidgets.getWidgetContainer()[component].widget
                    if value == True:
                        self.parent.deforumationwidgets.getWidgetContainer()[component].isActivated = True
                        button.setIcon(self.parent.deforumationwidgets.getWidgetContainer()[component].icon.pixmap(button.iconSize(), QIcon.Normal, QIcon.On))
                    else:
                        self.parent.deforumationwidgets.getWidgetContainer()[component].isActivated = False
                        button.setIcon(self.parent.deforumationwidgets.getWidgetContainer()[component].icon.pixmap(button.iconSize(), QIcon.Normal, QIcon.Off))

    def toggleRecording(self, event, sender, original_component_name):
        if self.is_recording == False:
            self.is_recording = True

            self.propagateAllComponents(sender, original_component_name, True)
            #self.parent.deforumationwidgets.getWidgetContainer()[sender.objectName()].isActivated = True
            #sender.setIcon(self.parent.deforumationwidgets.getWidgetContainer()[sender.objectName()].icon.pixmap(sender.iconSize(), QIcon.Normal, QIcon.On))

            stopped = threading.Event()
            q = queue.Queue(maxsize=int(round(self.BUF_MAX_SIZE / self.CHUNK_SIZE)))

            listen_t = threading.Thread(target=self.listen, args=(stopped, q))
            listen_t.start()
            record_t = threading.Thread(target=self.record, args=(stopped, q))
            record_t.start()

        else:
            self.is_recording = False
            self.propagateAllComponents(sender, original_component_name, False)
            #self.parent.deforumationwidgets.getWidgetContainer()[sender.objectName()].isActivated = False
            #sender.setIcon(self.parent.deforumationwidgets.getWidgetContainer()[sender.objectName()].icon.pixmap(sender.iconSize(), QIcon.Normal, QIcon.Off))

            #bmp = wx.Bitmap("./images/record_off.bmp", wx.BITMAP_TYPE_BMP)
            # bmp = scale_bitmap(bmp, 22, 22)
        #self.record_button.SetBitmap(bmp)
    def record(self, stopped, q):
        # the file name output you want to record into
        filename = "Recording.wav"
        # set the chunk size of 1024 samples
        framesperbuffer = 1024
        # sample format
        FORMAT = pyaudio.paInt16
        # mono, change to 2 if you want stereo
        channels = 1
        # 44100 samples per second
        sample_rate = 44100
        record_seconds = 0.5
        # initialize PyAudio object
        # p = pyaudio.PyAudio()
        frames = []

        voice_detected = 0
        should_begin_recording = False
        showRecordingOnce = False
        while self.is_recording:
            if stopped.wait(timeout=0):
                break
            chunk = q.get()
            vol = max(chunk)
            if vol >= self.MIN_VOLUME:
                if voice_detected == 0:
                    frames = []
                    should_begin_recording = True
                voice_detected = 50

            if voice_detected > 0 and should_begin_recording and not showRecordingOnce:
                #bmp = wx.Bitmap("./images/record_recording.bmp", wx.BITMAP_TYPE_BMP)
                #self.record_button.SetBitmap(bmp)
                #print("Recording")
                showRecordingOnce = True
            if voice_detected > 0 and should_begin_recording:
                data = chunk
                # if you want to hear your voice while recording
                # stream.write(data)
                frames.append(data)
                # TODO: write to file
                # print("O")
                voice_detected = voice_detected - 1
            else:
                if should_begin_recording:
                    should_begin_recording = False
                    showRecordingOnce = False
                    wf = wave.open(filename, "wb")
                    # set the channels
                    wf.setnchannels(channels)
                    # set the sample format
                    wf.setsampwidth(self.pyAudio.get_sample_size(FORMAT))
                    # set the sample rate
                    wf.setframerate(sample_rate)
                    # write the frames as bytes
                    wf.writeframes(b"".join(frames))
                    # close the file
                    wf.close()
                    recognizer = sp.Recognizer()
                    filename = "./Recording.wav"
                    with sp.AudioFile(filename) as source:
                        try:
                            # listen for the data (load audio to memory)
                            audio_data = recognizer.record(source)
                            # recognize (convert from speech to text)
                            text = recognizer.recognize_google(audio_data)

                            #print("Got the sentence:\"" + str(text) + "\"")
                            # self.rotation_3d_x_right_button
                            # self.rotation_3d_y_up_button
                            start_prompt_word = ['prompt', 'begin']

                            start_prompt_word = self.parent.ui.speech_prompt_start_binding.text()
                            start_prompt_word = self.createAndCleanArray(start_prompt_word)

                            pan_left_word = self.parent.ui.speech_panning_left_binding.text()
                            pan_left_word = self.createAndCleanArray(pan_left_word)
                            pan_right_word = self.parent.ui.speech_panning_right_binding.text()
                            pan_right_word = self.createAndCleanArray(pan_right_word)
                            pan_up_word = self.parent.ui.speech_panning_up_binding.text()
                            pan_up_word = self.createAndCleanArray(pan_up_word)
                            pan_down_word = self.parent.ui.speech_panning_down_binding.text()
                            pan_down_word = self.createAndCleanArray(pan_down_word)

                            rotate_left_word = self.parent.ui.speech_rotate_h_left_binding.text()
                            rotate_left_word = self.createAndCleanArray(rotate_left_word)
                            rotate_right_word = self.parent.ui.speech_rotate_h_right_binding.text()
                            rotate_right_word = self.createAndCleanArray(rotate_right_word)

                            rotate_up_word = self.parent.ui.speech_rotate_v_up_binding.text()
                            rotate_up_word = self.createAndCleanArray(rotate_up_word)
                            rotate_down_word = self.parent.ui.speech_rotate_v_down_binding.text()
                            rotate_down_word = self.createAndCleanArray(rotate_down_word)

                            tilt_left_word = self.parent.ui.speech_tilt_cc_bind.text()
                            tilt_left_word = self.createAndCleanArray(tilt_left_word)
                            tilt_right_word = self.parent.ui.speech_tilt_cw_bind.text()
                            tilt_right_word = self.createAndCleanArray(tilt_right_word)

                            zoom_in_word = self.parent.ui.speech_zoom_forwards_binding.text()
                            zoom_in_word = self.createAndCleanArray(zoom_in_word)
                            zoom_out_word = self.parent.ui.speech_zoom_backwards_binding.text()
                            zoom_out_word = self.createAndCleanArray(zoom_out_word)

                            add_to_sentence = self.parent.ui.speech_add_to_prompt_binding.text()
                            add_to_sentence = self.createAndCleanArray(add_to_sentence)

                            cancel_voice_sentence = self.parent.ui.speech_cancel_prompt_binding.text()
                            cancel_voice_sentence = self.createAndCleanArray(cancel_voice_sentence)
                            reset_panning = self.parent.ui.speech_reset_panning_binding.text()
                            reset_panning = self.createAndCleanArray(reset_panning)
                            reset_zoom = self.parent.ui.speech_reset_zoom_binding.text()
                            reset_zoom = self.createAndCleanArray(reset_zoom)
                            reset_rotation = self.parent.ui.speech_reset_rotation_binding.text()
                            reset_rotation = self.createAndCleanArray(reset_rotation)
                            reset_tilt = self.parent.ui.speech_reset_tilt_binding.text()
                            reset_tilt = self.createAndCleanArray(reset_tilt)


                            if any(word in text for word in cancel_voice_sentence):
                                #print("Canceling the spoken sentence!")
                                pass
                            elif text.startswith(tuple(reset_tilt)):
                                #print("Resetting tilt")
                                value = 0
                                args = ["Tilt"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                            elif text.startswith(tuple(reset_rotation)):
                                #print("Resetting rotation")
                                value = 0
                                args = ["Rot_H"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                                args = ["Rot_V"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

                            elif text.startswith(tuple(reset_panning)):
                                #print("Resetting panning")
                                value = 0
                                args = ["Pan_X"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                                args = ["Pan_Y"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                            elif text.startswith(tuple(reset_zoom)):
                                #print("Resetting zoom")
                                self.parent.DeforumationMotions.Translation_Z = 0
                                value = 0 #self.parent.DeforumationMotions.Translation_Z  # zoom - float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Zoom"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                            elif text.startswith(tuple(tilt_left_word)):
                                #print("Tilting left")
                                tilt = float(self.parent.ui.rotate_z_value.text())
                                value = tilt + float(self.parent.ui.motion_tilt_granularity.text())
                                args = ["Tilt"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                            elif text.startswith(tuple(tilt_right_word)):
                                #print("Tilting right")
                                tilt = float(self.parent.ui.rotate_z_value.text())
                                value = tilt - float(self.parent.ui.motion_tilt_granularity.text())
                                args = ["Tilt"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))
                            elif text.startswith(tuple(rotate_left_word)):
                                #print("Rotate left")
                                rotate = float(self.parent.ui.rotate_x_value.text())
                                value = -1 #rotate - float(self.parent.ui.motion_rotate_granularity.text())
                                args = ["Rot_H"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))

                            elif text.startswith(tuple(rotate_right_word)):
                                #print("Rotate right")
                                rotate = float(self.parent.ui.rotate_x_value.text())
                                value = 1 #rotate + float(self.parent.ui.motion_rotate_granularity.text())
                                args = ["Rot_H"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(rotate_up_word)):
                                #print("Rotate up")
                                rotate = float(self.parent.ui.rotate_y_value.text())
                                value = 1 #rotate + float(self.parent.ui.motion_rotate_granularity.text())
                                args = ["Rot_V"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(rotate_down_word)):
                                #print("Rotate down")
                                rotate = float(self.parent.ui.rotate_y_value.text())
                                value = -1 #rotate - float(self.parent.ui.motion_rotate_granularity.text())
                                args = ["Rot_V"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(pan_left_word)):
                                #print("Panning left")
                                pan = float(self.parent.ui.pan_x_value.text())
                                value = -1 #pan - float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Pan_X"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(pan_right_word)):
                                #print("Panning right")
                                pan = float(self.parent.ui.pan_x_value.text())
                                value = 1 #pan + float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Pan_X"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(pan_up_word)):
                                #print("Panning up")
                                pan = float(self.parent.ui.pan_y_value.text())
                                value = 1 #pan + float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Pan_Y"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(pan_down_word)):
                                #print("Panning down")
                                pan = float(self.parent.ui.pan_y_value.text())
                                value = -1 #pan - float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Pan_Y"]
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(zoom_in_word)):
                                # self.zoom_slider.SetValue(self.zoom_slider.GetValue() + 20)
                                print("Zooming In")
                                granularity = float(self.parent.ui.motion_zoom_granularity_special.text())
                                self.parent.DeforumationMotions.Translation_Z = round(self.parent.DeforumationMotions.Translation_Z + granularity, 2)
                                value = 1 #self.parent.DeforumationMotions.Translation_Z #zoom - float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Zoom"]
                                print("Value is:" + str(value))
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(zoom_out_word)):
                                # self.zoom_slider.SetValue(self.zoom_slider.GetValue() + 20)
                                #words = text.split(' ')
                                print("Zooming Out")
                                granularity = float(self.parent.ui.motion_zoom_granularity_special.text())
                                self.parent.DeforumationMotions.Translation_Z = round(self.parent.DeforumationMotions.Translation_Z - granularity, 2)
                                value = -1 #self.parent.DeforumationMotions.Translation_Z #zoom - float(self.parent.ui.motion_pan_granularity.text())
                                args = ["Zoom"]
                                print("Value is:" + str(value))
                                QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)), Q_ARG("QString", str(1)))
                            elif text.startswith(tuple(add_to_sentence)):
                                #print("Add to text prompt")
                                what_word = ""
                                for n in add_to_sentence:
                                    if n in text:
                                        what_word = n
                                        break
                                args= [str(text[len(what_word):])]
                                QMetaObject.invokeMethod(self.parent, "addTextToPrompt", Qt.QueuedConnection, Q_ARG("QVariantList", args))

                            elif text.startswith(tuple(start_prompt_word)):
                                #print("Set text prompt")
                                what_word = ""
                                for n in start_prompt_word:
                                    if n in text:
                                        what_word = n
                                        break
                                args= [str(text[len(what_word):])]
                                QMetaObject.invokeMethod(self.parent, "setTextToPrompt", Qt.QueuedConnection, Q_ARG("QVariantList", args))

                        except Exception as e:
                            # Normally lands here if no valid words could be recognized
                            print(str(e))
                    #bmp = wx.Bitmap("./images/record_on.bmp", wx.BITMAP_TYPE_BMP)
                    #self.record_button.SetBitmap(bmp)
        # print("Done recording")

    def listen(self, stopped, q):
        # FORMAT = pyaudio.paInt16
        stream = self.pyAudio.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=44100,
            input=True,
            frames_per_buffer=1024,
        )

        while self.is_recording:
            if stopped.wait(timeout=0):
                break
            try:
                q.put(array('h', stream.read(self.CHUNK_SIZE)))
            except queue.Full:
                pass  # discard
        # print("Exiting Recorder listen")