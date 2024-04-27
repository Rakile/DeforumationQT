import os
import queue
import subprocess
import threading
import time

from PySide6 import QtGui
from PySide6.QtCore import (QMetaObject, QObject,QSize, Qt, Signal)
from PySide6.QtGui import (QPainter, QPixmap,QMouseEvent, QPen)
from PySide6.QtWidgets import (QGridLayout, QLabel)
"""from PySide6 import QtGui
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer
from helpers.named_pipes import Deforumation_Named_Pipes
#from helpers.video_player import Deforumation_Video_Player
from helpers.video_player_deforumation import Deforumation_Video_Player"""
outdir = "H:/stable-diffusion-webui/outputs/img2img-images/Deforum_20230817140718"
resume_timestring = "20230817140718"

class Worker(QObject):
    finished = Signal()  # Signal to indicate completion
    open_window = Signal()  # Signal to open a new window

    def run(self):
        # Perform some task
        # ...

        # Emit signal to open a window
        self.open_window.emit()

        # Emit signal to indicate completion
        self.finished.emit()

class Video_Image(QLabel):
    clicked = Signal(object)  # You can send any object as data with the signal

    def __init__(self, identifier, pixmap, parent=None):
        super().__init__(parent)
        self.identifier = identifier
        #self.setPixmap(pixmap)
        self.image_path = None
        self.image_width = 0
        self.image_height = 0
        #self.pixmap = None
        self.shouldCache = False
        self.pathnumber = 0

    def setIdentifier(self, identifier):
        self.identifier = identifier
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.clicked.emit(self.identifier)  # Emit the signal with the identifier
    def setpathnumber(self, pathnumber):
        self.pathnumber = pathnumber
    def getpathnumber(self):
        return self.pathnumber
    def setpath(self, path):
        self.image_path = path
    def getpath(self):
        return self.image_path
    def setpixmap(self, pixmap):
        #self.pixmap_org = pixmap.copy()
        self.pixmap = pixmap
        self.pixmap_without_frame_number = pixmap.copy()

        qp = QPainter(self.pixmap)  # self.pixmap)
        custom_font = QtGui.QFont("Segoe UI Light", 100)
        #qp.save()
        qp.setFont(custom_font)
        pen = QPen(Qt.red, 30)
        qp.setPen(pen)
        # qp.drawLine(10, 10, 50, 50)
        qp.drawText(10, 10, 260, 200, Qt.AlignLeft | Qt.AlignTop, str(self.pathnumber))
        qp.end()
        self.setPixmap(self.pixmap)
    def getpixmap(self, shouldIncludeFrameNumber = True):
        #shouldIncludeFrameNumber = True
        if not shouldIncludeFrameNumber:
            '''pixmap_incluided_frame_number = self.pixmap.copy()
            qp = QPainter(pixmap_incluided_frame_number)#self.pixmap)
            custom_font = QtGui.QFont("Segoe UI Light", 40)
            qp.save()
            qp.setFont(custom_font)
            pen = QPen(Qt.red, 40)
            qp.setPen(pen)
            # qp.drawLine(10, 10, 50, 50)
            qp.drawText(10, 10, 200, 200, Qt.AlignLeft | Qt.AlignTop, str("1"))
            qp.end()'''
            #self.setPixmap(self.pixmap_without_frame_numer)
            # Include with frame number (normal frame strip image)
            return self.pixmap_without_frame_number
        #self.setPixmap(self.pixmap)
        qp = QPainter(self.pixmap)  # self.pixmap)
        custom_font = QtGui.QFont("Segoe UI Light", 100)
        #qp.save()
        qp.setFont(custom_font)
        pen = QPen(Qt.red, 30)
        qp.setPen(pen)
        # qp.drawLine(10, 10, 50, 50)
        qp.drawText(10, 10, 260, 200, Qt.AlignLeft | Qt.AlignTop, str(self.pathnumber))
        qp.end()
        #self.setPixmap(self.pixmap)
        return self.pixmap
    def setwidth(self, width):
        self.resize(width, self.height())
        self.image_width = width
    def setheight(self, height):
        self.resize(self.width(), height)
        self.image_height = height
    def cacheimage(self):
        self.shouldCache = True
    def uncacheimage(self):
        self.shouldCache = False
    def iscachedimage(self):
        return self.shouldCache

    '''def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)

        image = QImage('im.png')
        qp.drawImage(QPoint(), image)

        pen = QPen(Qt.red)
        pen.setWidth(2)
        qp.setPen(pen)

        font = QFont()
        font.setFamily('Times')
        font.setBold(True)
        font.setPointSize(24)
        qp.setFont(font)

        qp.drawText(150, 250, "X")

        qp.end()'''
class Video_Image_Container():

    def __init__(self, parent, namedpipes = None, deforumation_settings=None, deforumation_tools=None):
        #super().__init__(parent)
        self.deforumation_settings = deforumation_settings
        self.deforumation_tools=deforumation_tools
        self.config = self.deforumation_settings.getGuiConfig()
        self.deforumationnamedpipes = namedpipes
        self.parent = parent
        self.image_path = None
        self.image_width = 0
        self.image_height = 0
        self.preview_compression_rate = 1
        self.image_container = {}
        self.true_image_container = {}
        self.image_grid_container = {}
        self.image_number_grid_container = {}
        self.current_scale_w = None
        self.current_scale_h = None
        #self.deforumationnamedpipes = Deforumation_Named_Pipes()
        self.outdir = None
        self.resume_timestring = None
        self.player = None
        self.occupied = False
        self.doneFFMPEGing = True
        self.replayFPS = 30
        self.replayCRF = 20
        self.pathToAudioFile = ""
        self.pathToFFMPEG = ""
        self.imageNumberCurrentlySelected = -1
        self.ffmpegIN = -1
        self.ffmpegOUT = -1
        self.auto_scroll = False
        self.setInitValues()

    def setFFmpegIN(self, object):
        if len(object.text()) > 0:
            self.ffmpegIN = int(object.text())
        else:
            self.ffmpegIN = -1
        self.deforumation_tools.propagateAllComponents(object, self.ffmpegIN)
        self.preserveSpecialPurposeFrameLooks(0)
    def setFFmpegOUT(self, object):
        if len(object.text()) > 0:
            self.ffmpegOUT = int(object.text())
        else:
            self.ffmpegOUT = -1
        self.deforumation_tools.propagateAllComponents(object, self.ffmpegOUT)
        self.preserveSpecialPurposeFrameLooks(0)
    def setCurrentlySelectedImage(self, imageNumber):
        self.imageNumberCurrentlySelected = imageNumber
    def getCurrentlySelectedImage(self):
        return self.imageNumberCurrentlySelected
    def makeClickedImageSelected(self, identifier):
        #Unmark all other frames
        #self.removeStyleSheetAllFrames(u"border-style: outset; border-width: 0px; border-color: red; border-radius: 0px;")
        #Mark the currently clicked frames (red square around it)
        #identifier.setStyleSheet(u"border-style: outset; border-width: 2px; border-color: red; border-radius: 0px;")
        self.preserveSpecialPurposeFrameLooks(0)
        current_movie_tab_height = self.parent.ui.preview_screen.height()
        frame_image = identifier.getpixmap() #FIXIT
        frameSize = frame_image.size()
        framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_movie_tab_height
        shouldusethisheight = current_movie_tab_height  # int(frameSize.height() / 4)
        shouldusethiswidth = framesizeScaledWidth  # int(frameSize.width() / 2)
        #print("shouldusethisheight:" + str(shouldusethisheight) + " shouldusethiswidth:" + str(shouldusethiswidth))
        self.parent.ui.preview_image.setMaximumHeight(shouldusethisheight)
        self.parent.ui.preview_image.setMaximumWidth(shouldusethiswidth)
        self.parent.ui.preview_image.setPixmap(identifier.getpixmap(False))
        if self.parent.detachedPreviewWindow != None:
            self.parent.dettachedPreviewImage.setPixmap(identifier.getpixmap(False))

        """if self.ffmpegIN != -1 and self.ffmpegOUT != -1:
            if identifier.getpathnumber() >= self.ffmpegIN and identifier.getpathnumber() <= self.ffmpegOUT:
                identifier.setStyleSheet( u"border-style: outset; border-width: 2px; border-top-color : red; border-left-color : blue; border-right-color : blue; border-bottom-color : red; border-radius: 0px;")"""

    def handleCheckBoxes(self,sender, event):
        if sender.objectName().startswith("AutoScroll_checkbox"):
            if sender.isChecked():
                self.auto_scroll = False
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("auto_scroll", False)
            else:
                self.auto_scroll = True
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("auto_scroll", True)

    def setInitValues(self):
        auto_scroll = self.deforumation_settings.getGuiConfigValue("auto_scroll")
        if auto_scroll != None:
            self.auto_scroll = auto_scroll

        replayFPS = self.deforumation_settings.getGuiConfigValue("replay_fps")
        if replayFPS != None:
            self.replayFPS = replayFPS
        replayCRF = self.deforumation_settings.getGuiConfigValue("replay_crf")
        if replayCRF != None:
            self.replayCRF = replayCRF
        pathToAudioFile = self.deforumation_settings.getGuiConfigValue("path_to_audio_file")
        if pathToAudioFile != None:
            self.pathToAudioFile = pathToAudioFile
        pathToFFMPEG = self.deforumation_settings.getGuiConfigValue("path_to_ffmpeg")
        if pathToFFMPEG != None:
            self.pathToFFMPEG = pathToFFMPEG

        self.parent.ui.pathToAudioFile_value.setText(self.pathToAudioFile)
        self.parent.ui.pathToFFMPEG_value.setText(str(self.pathToFFMPEG))
        self.parent.ui.replay_fps_input_box.setText(str(self.replayFPS))
        self.parent.ui.crf_input_box.setText(str(self.replayCRF))
        self.parent.ui.AutoScroll_checkbox.setChecked(self.auto_scroll)

    def setPreviewCompression(self, identifier, movie_slider, total_number_of_frames_generated, preview_compression_rate=1):
        if identifier is None:
            self.preview_compression_rate = preview_compression_rate
        else:
            self.preview_compression_rate = identifier.value()
        self.total_number_of_audiovideo_frames = self.parent.AudioWaveContainer.currentTotalAudioVideoFrames()
        if self.total_number_of_audiovideo_frames < total_number_of_frames_generated:
            movie_slider.setMaximum(int(total_number_of_frames_generated / self.getPreviewCompression()))
        else:
            movie_slider.setMaximum(int(self.total_number_of_audiovideo_frames / self.getPreviewCompression()))
        #movie_slider.setMaximum(int(total_number_of_frames_generated / self.getPreviewCompression()))

    def getPreviewCompression(self):
        return self.preview_compression_rate
    def setidentifier(self, identifier):
        self.parent = identifier
    def getImageFromPath(self, imagePath):
        if imagePath != None:
            image = QPixmap(imagePath)
        else:
          image = None
        return image
    def addImage(self, imageNumber, click_callback = None, clicked_image_menue = None, image_path_number = None, pixmap = None, total_number_of_frames_generated = 9999999):
         if image_path_number != None:
            #if not image_path_number in self.true_image_container:
            aVideoImage = Video_Image(None, None)
            imagePath = self.get_current_image_path_f(image_path_number*self.preview_compression_rate)
            #print("Image Path Number:" + str(image_path_number))
            #print("Image Path Number * preview_compression_rate:" + str(image_path_number * self.preview_compression_rate))
            #print("total_number_of_frames_generated:" + str(total_number_of_frames_generated))
            if total_number_of_frames_generated < (image_path_number * self.preview_compression_rate): #image_path_number:
                imagePath = None
            if imagePath == None:
                #Set dummy image (as it currently does not exist)
                if self.current_scale_w != None and self.current_scale_h != None:
                    image = QPixmap(self.current_scale_w, self.current_scale_h)
                else:
                    image = QPixmap(512, 512)
                image.fill(Qt.black)
                aVideoImage.setpathnumber(image_path_number*self.preview_compression_rate)
                aVideoImage.setpath(imagePath)
                aVideoImage.setpixmap(image)
                aVideoImage.setwidth(image.size().width())
                aVideoImage.setheight(image.size().height())
                aVideoImage.setScaledContents(True)
            else:
                image = QPixmap(imagePath)

                img_width = image.size().width()
                img_height = image.size().height()
                if img_width == 0 or img_height == 0:
                    image = QPixmap(self.current_scale_w, self.current_scale_h)
                #Set all the images properties
                aVideoImage.setpathnumber(image_path_number*self.preview_compression_rate)
                aVideoImage.setpath(imagePath)
                aVideoImage.setpixmap(image)
                aVideoImage.setwidth(image.size().width())
                aVideoImage.setheight(image.size().height())
                if self.image_width == 0 or self.image_height == 0:
                    self.image_width = image.size().width()
                    self.image_height = image.size().height()
                aVideoImage.setScaledContents(True)
                #aVideoImage.cacheimage()
                if self.current_scale_w == None or self.current_scale_h == None:
                    self.current_scale_w = image.size().width()
                    self.current_scale_h = image.size().height()
            if click_callback != None:
                aVideoImage.setIdentifier(aVideoImage)
                aVideoImage.clicked.connect(click_callback)
                aVideoImage.mouseReleaseEvent = lambda event, w=aVideoImage: clicked_image_menue(event, w)
            #self.true_image_container[image_path_number] = aVideoImage
            #self.true_image_container[image_path_number].setObjectName(f"movie_frame_image_{image_path_number}")
            self.image_container[imageNumber] = aVideoImage
            self.image_container[imageNumber].setObjectName(f"movie_frame_image_{image_path_number*self.preview_compression_rate}")
            self.image_container[imageNumber].setpathnumber(image_path_number*self.preview_compression_rate)
            #else:
            #    print("Using cached image number" + str(imageNumber))
            #    self.image_container[imageNumber] = self.true_image_container[image_path_number]
            #    self.image_container[imageNumber].setObjectName(f"movie_frame_image_{image_path_number}")

    def addImageGridContainer(self, imageNumber, movie_frame, movie_frame_number = None):
        self.image_grid_container[imageNumber] = QGridLayout(movie_frame)
        self.image_grid_container[imageNumber].setSpacing(0)
        self.image_grid_container[imageNumber].setObjectName(f"movie_gridLayout_{imageNumber}")
        self.image_grid_container[imageNumber].setContentsMargins(1, 0, 1, 0)
        self.image_grid_container[imageNumber].addWidget(self.image_container[imageNumber], 0, 0, 1, 1)
        #Also add include image_frame_label_grid_container
        '''if movie_frame_number != None:
            self.image_number_grid_container[imageNumber] = QGridLayout(movie_frame)
            self.image_number_grid_container[imageNumber].setSpacing(0)
            self.image_number_grid_container[imageNumber].setObjectName(f"movie_gridLayout_{imageNumber}")
            self.image_number_grid_container[imageNumber].setContentsMargins(1, 0, 1, 0)
            self.image_number_grid_container[imageNumber].addWidget(self.image_container[imageNumber], 0, 0, 1, 1)'''


    def removeImageGridContainer(self, imageNumber):
        #print("Removing gridframecontainer:" + str(imageNumber))
        del self.image_grid_container[imageNumber]
    #def returnTrueImageContainer(self):
    #    return self.true_image_container
    def removeImage(self, imageNumber):
        if not self.image_container[imageNumber].iscachedimage():
            #print("Removing frameimage:" + str(imageNumber))
            del self.image_container[imageNumber]
            #del self.image_container[imageNumber]
        else:
            pass
            #print("Not removing frameimage (because cached):" + str(imageNumber))
            #del self.image_container[imageNumber]

    def getImageGridContainer(self, imageNumber):
        return self.image_grid_container[imageNumber]
    def preserveSpecialPurposeFrameLooks(self, imageNumber):
        imageNumber = 0
        for frame in self.image_container:
            if imageNumber in self.image_container:
                image = self.image_container[imageNumber]
                if image.getpathnumber() == self.imageNumberCurrentlySelected:
                    #print("Returning selected image:" + str(image.getpathnumber()) + ", To visible preview slot:" + str(imageNumber))
                    self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 2px; border-color: red; border-radius: 0px;")
                else:
                    if image.getpathnumber() == self.ffmpegIN and image.getpathnumber() == self.ffmpegOUT:
                        self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 2px; border-color: pink; border-radius: 0px;")
                    elif image.getpathnumber() == self.ffmpegIN:
                        self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 2px; border-color: green; border-radius: 0px;")
                    elif image.getpathnumber() == self.ffmpegOUT:
                        self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 2px; border-color: yellow; border-radius: 0px;")
                    elif image.getpathnumber() >= self.ffmpegIN and image.getpathnumber() <= self.ffmpegOUT and self.ffmpegIN != -1:
                        self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 2px; border-color: blue; border-radius: 0px;")
                    else:
                        self.setStyleSheetOnFrame(imageNumber, u"border-style: outset; border-width: 0px; border-color: red; border-radius: 0px;")

            imageNumber += 1
    def getImage(self, imageNumber):
        #print("Getting image:" + str(imageNumber))
        if imageNumber in self.image_container:
            return self.image_container[imageNumber]
        else:
            #Some how the image can't be found in the dictionary, so create it (as a black image)
            #print("Returning temporary black image (film_strip_frame: " + str(imageNumber) + "), because it could not be found")
            if self.current_scale_w != None and self.current_scale_h != None:
                image = QPixmap(self.current_scale_w, self.current_scale_h)
            else:
                image = QPixmap(512, 512)
            image.fill(Qt.black)
            aVideoImage = Video_Image(None, None)
            aVideoImage.setpath(None)
            aVideoImage.setpixmap(image)
            aVideoImage.setwidth(image.size().width())
            aVideoImage.setheight(image.size().height())
            aVideoImage.setScaledContents(True)
            self.image_container[999999] = aVideoImage
            return self.image_container[999999]

    def removeStyleSheetAllFrames(self, style):
        for frame in self.image_container:
            #print("Removing stylesheet number:" + str(frame))
            self.image_container[frame].setStyleSheet(style)

    def setStyleSheetOnFrame(self, imageNumber, style):
        self.image_container[imageNumber].setStyleSheet(style)

    def get_current_image_path(self):
        return self.outdir
    def set_current_image_path_from_mediator(self):
        self.outdir = str(self.deforumationnamedpipes.readValue("frame_outdir")).replace('\\', '/').replace('\n', '')
        self.resume_timestring = str(self.deforumationnamedpipes.readValue("resume_timestring"))

    def get_current_image_path_f(self, frame_num):
        if self.outdir == None:
            self.outdir = str(self.deforumationnamedpipes.readValue("frame_outdir")).replace('\\', '/').replace('\n', '')
            if self.outdir == '':
                self.outdir = None
        if self.resume_timestring == None:
            self.resume_timestring = str(self.deforumationnamedpipes.readValue("resume_timestring"))
            if self.resume_timestring == '':
                self.resume_timestring = None

        imagePath = str(self.outdir) + "/" + str(self.resume_timestring) + "_" + str(frame_num).zfill(9) + ".png"
        if not os.path.isfile(imagePath):
            return None
        else:
            return imagePath

    def create_ffmpeg_image_string(self):
        outdir = str(self.deforumationnamedpipes.readValue("frame_outdir")).replace('\\', '/').replace('\n', '')
        resume_timestring = str(self.deforumationnamedpipes.readValue("resume_timestring"))
        imagePath = outdir + "/" + resume_timestring + "_%09d.png"
        return imagePath
    def setPathToAudioFile(self):
        self.pathToAudioFile = str(self.parent.ui.pathToAudioFile_value.text())
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("path_to_audio_file", self.pathToAudioFile)
    def setPathToFFMPEG(self):
        self.pathToFFMPEG = str(self.parent.ui.pathToFFMPEG_value.text())
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("path_to_ffmpeg", self.pathToFFMPEG)
    def saveCRFtoConfig(self, object):
        if object.text().isdigit():
            self.replayCRF = int(object.text())
            self.deforumation_tools.propagateAllComponents(object, self.replayCRF)
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("replay_crf", self.replayCRF)
    def saveFPStoConfig(self, object):
        if object.text().isdigit():
            self.replayFPS = int(object.text())
            self.deforumation_tools.propagateAllComponents(object, self.replayFPS)
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("replay_fps", self.replayFPS)
    def playVideo(self):
        if self.doneFFMPEGing == True:
            if self.occupied == True:
                print("Already previewing. Trying to close preview.")
                if self.player != None:
                    self.player.close()
                    self.player = None
            inMark = self.ffmpegIN
            outMark = self.ffmpegOUT
            if inMark == -1:
                print("No preview start frame given, so starting from frame 0")
                inMark = 0
            if outMark == -1:
                print("No preview end frame given, so ending on last generated frame (" + str(self.parent.total_number_of_frames_generated) + ")")
                outMark = self.parent.total_number_of_frames_generated

            if inMark > outMark:
                print("FFMPEG preview start is greater than FFMPEG preview end.")
                return
            if outMark > self.parent.total_number_of_frames_generated:
                print("There is no current record of so many frames having been generated yet. Changing out mark to max generated frames(" + str(self.parent.total_number_of_frames_generated) + ")")
                outMark = self.parent.total_number_of_frames_generated
            if inMark > self.parent.total_number_of_frames_generated or outMark > self.parent.total_number_of_frames_generated:
                print("There is no current record of so many frames having been generated yet. Changing in mark to max generated frames(" + str(self.parent.total_number_of_frames_generated) + ")")
                inMark = self.parent.total_number_of_frames_generated
            self.doneFFMPEGing = False

            #if self.ffmpegIN == -1:
            #    print("No preview start frame given, so starting from frame 0")
            #    replayFrom = "0"
            #else:
            replayFrom = str(inMark) #str(self.parent.ui.replay_from_input_box.text())
            replayFrom = replayFrom.zfill(9)

            #if self.ffmpegOUT == -1:
            #    print("No preview end frame given, so ending on last generated frame (" + str(self.parent.total_number_of_frames_generated) + ")")
            #    replayTo = str(self.parent.total_number_of_frames_generated)
            #else:
            replayTo = str(outMark) #str(self.parent.ui.replay_to_input_box.text())
            replayTo = replayTo.zfill(9)
            ffmpeg_image_path = self.create_ffmpeg_image_string()
            audio_path = str(self.parent.ui.pathToAudioFile_value.text())
            ffmpegPath = "ffmpeg"
            self.replayFPS = int(self.parent.ui.replay_fps_input_box.text())
            self.replayCRF = int(self.parent.ui.crf_input_box.text())

            # Connect signals and slots
            """self.thread = QThread()  # Create a QThread object
            self.worker = Worker()  # Create a worker object
            self.worker.moveToThread(self.thread)  # Move worker to the thread
            self.thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.thread.finished.connect(self.thread.deleteLater)
            movie_size = QSize(self.image_width, self.image_height)
            self.worker.open_window.connect(lambda chk=False, ffmpegPath=ffmpegPath, replayFPS=self.replayFPS, replayFrom=replayFrom, replayTo=replayTo, ffmpeg_image_path = ffmpeg_image_path: self.open_player_window(ffmpegPath, replayFPS, replayFrom, replayTo, ffmpeg_image_path, movie_size, audio_path, self.replayCRF))
            self.thread.start()  # Start the thread"""

            # Start the live view thread
            CHUNK_SIZE = 1024
            BUF_MAX_SIZE = CHUNK_SIZE * 10
            movie_size = QSize(self.image_width, self.image_height)
            self.live_view_stopped = threading.Event()
            self.live_view_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
            self.liveview_t = threading.Thread(target=self.liveView, args=(self.live_view_stopped, self.live_view_q, ffmpegPath, self.replayFPS, replayFrom, replayTo, ffmpeg_image_path, movie_size, audio_path, self.replayCRF))
            self.liveview_t.start()


    def liveView(self, stopped, q, ffmpegPath, replayFPS, replayFrom, replayTo, ffmpeg_image_path, movie_size, audio_path, replayCRF):
        self.stitch_video(ffmpegPath, replayFPS, replayFrom, replayTo, ffmpeg_image_path, audio_path, replayCRF)
        QMetaObject.invokeMethod(self.parent, "show_media_player", Qt.QueuedConnection) # We need to invoke the method on the main thread (sad but a must)
        self.doneFFMPEGing = True

    def ffmpeg_stitch_video(self, ffmpeg_location=None, fps=None, outmp4_path=None, stitch_from_frame=0, stitch_to_frame=None, imgs_path=None, audio_path=None, crf = 20):
        time.sleep(0.5)
        # start_time = time.time()
        #print(f"Got a request to stitch frames to video using FFmpeg.\nFrames:\n{imgs_path}\nTo Video:\n{outmp4_path}")
        msg_to_print = f"Stitching *video*..."
        #print("Stitching *video*...")
        if stitch_to_frame == -1:
            stitch_to_frame = 999999999
        if os.path.isfile(outmp4_path):
            #print("removing temp video")
            os.remove(outmp4_path)
        try:
            cmd = [
                ffmpeg_location,
                '-start_number', str(stitch_from_frame),
                # '-framerate', str(float(fps)),
                # '-thread_queue_size 4096',
                '-r', str(float(fps)),
                '-i', imgs_path,
                '-frames:v', str(stitch_to_frame),
                #'-c:v', 'libx264',
                #'-pix_fmt', 'yuv420p10le',
                '-pix_fmt', 'yuv420p',
                '-crf', str(crf),
                '-pattern_type', 'sequence'
            ]
            cmd.append(outmp4_path)
            # ffmpeg -y -r 30 -start_number 0 -i H:\stable-diffusion-webui\outputs/img2img-images\Deforum_20230705125910\20230705125910_%09d.png -frames:v 800 -c:v libx264 -vf fps=25 -pix_fmt yuv420p -crf 17 -preset veryslow -pattern_type sequence -vcodec png E:\Tools\Python_Scripts\deforum_remote\out.mp4
            # ffmpeg -y -start_number 0 -framerate 25 -r 25 -i H:\stable-diffusion-webui\outputs/img2img-images\Deforum_20230705125910\20230705125910_%09d.png -frames:v 200 -pix_fmt yuv420p -profile:v high -level:v 4.1 -crf:v 20 -movflags +faststart E:\Tools\Python_Scripts\deforum_remote\out.mp4
            # ffmpeg -y -i E:\Tools\Python_Scripts\deforum_remote\out.mp4 -ss 40 -i H:\Deforumation_Competition\snapshot2.wav -map 0:v -map 1:a -c:v copy -shortest E:\Tools\Python_Scripts\deforum_remote\out2.mp4

            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
            # subprocess.run(cmd)
            stdout, stderr = process.communicate()
        except FileNotFoundError:
            print("\r" + " " * len(msg_to_print), end="", flush=True)
            print(f"\r{msg_to_print}", flush=True)
            raise FileNotFoundError(
                "FFmpeg not found. Please make sure you have a working ffmpeg path under 'ffmpeg_location' parameter.")
        except Exception as e:
            print("\r" + " " * len(msg_to_print), end="", flush=True)
            print(f"\r{msg_to_print}", flush=True)
            raise Exception(f'Error stitching frames to video. Actual runtime error:{e}')
        print("Done Stitching *video*...")

        if os.path.isfile(outmp4_path + '.temp.mp4'):
            os.remove(outmp4_path + '.temp.mp4')
        if audio_path != None and audio_path != "":
            audioDelay = float(int(stitch_from_frame) / float(fps))
            try:
                cmd = [
                    ffmpeg_location,
                    '-i',
                    outmp4_path,
                    '-ss', str(audioDelay),
                    '-i',
                    audio_path,
                    '-map', '0:v',
                    '-map', '1:a',
                    '-c:v', 'copy',
                    '-shortest',
                    outmp4_path + '.temp.mp4'
                ]
                print("Stitching *audio*...")
                process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
                stdout, stderr = process.communicate()
                # subprocess.run(cmd)
                print("Done stitching *audio*...")
                if process.returncode != 0:
                    raise RuntimeError(stderr)
                os.replace(outmp4_path + '.temp.mp4', outmp4_path)
            except Exception as e:
                add_soundtrack_status = f"\rError adding audio to video: {e}"
                add_soundtrack_success = False
            #print("Done stitching *video and audio!*...")

    def stitch_video(self, ffmpegPath, replayFPS, replayFrom, replayTo, ffmpeg_image_path, audio_path=None, crf = 20):
        if self.occupied== False:
            self.occupied = True
            if self.player != None:
                self.player.close()
                print("Need to close the old player")
            if audio_path == "":
                audio_path = None
            self.ffmpegstitch = threading.Thread(target=self.ffmpeg_stitch_video, args=(ffmpegPath, replayFPS, "out.mp4", replayFrom, int(replayTo) - int(replayFrom), ffmpeg_image_path, audio_path, crf))
            self.ffmpegstitch.daemon = False
            self.ffmpegstitch.start()
            self.ffmpegstitch.join()


