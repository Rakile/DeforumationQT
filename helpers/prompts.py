import random
import time
import pickle
import re
import numpy as np
from PySide6.QtCore import QRect, QSize
from PySide6.QtGui import Qt, QFont, QColor, QTextCursor
from PySide6.QtWidgets import QCheckBox, QLabel, QLineEdit, QSlider, QFrame, QPushButton, QFileDialog, QProgressBar
from pyeaze import pyeaze


class Deforumation_Prompt_Morphing_Frame():
    def __init__(self, index, parent=None, promptMorphConfigFrame=None):
        #super().__init__(parent)
        self.parent = parent
        self.identifier = index
        self.isPromptBlending = None
        self.morph_prompt_frame = None
        self.morph_binding_label = None
        self.morph_prompt_binding = None
        self.morph_promptA_label = None
        self.morph_promptA = None
        self.morph_promptB_label = None
        self.morph_promptB = None
        self.morph_prompt_blending_checkbox = None
        self.morph_prompt_slider = None
        self.morph_prompt_minmax_frame = None
        self.morph_prompt_min_label = None
        self.morph_prompt_max_label = None
        self.morph_prompt_min = None
        self.morph_prompt_max = None
        self.morph_prompt_value = None
        self.morph_prompt_enabled = False
        self.morph_prompt_enabled_checkbox = None
        self.OnOff_label = None
        self.morph_prompt_progressbar_frame = None
        self.morph_prompt_progressbar = None
        self.morph_prompt_progress_value = None
        self.morph_prompt_smooth_motion_enabled = False
        self.morph_prompt_smooth_motion_enabled_checkbox = None
        self.morph_prompt_smooth_motion_enabled_label = None
        self.Prompt_Morph_Syrup_Value = 0
        #self.remove_morph_prompt = None
        self.slider_style = "QSlider{ border: none;}\nQSlider::groove:horizontal {\n    border-image: url(images/groove_230_m.png) ; /* Adjust slicing and stretch as needed */\n    border: none;\n    height: 29px; /* The height of your image */\n    width: 240px; /* Width of the handle - adjust as needed */\n}\n\nQSlider::handle:horizontal {\n    background-image: url(images/handle_off.png); /* The path to your handle image */\n  background-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:hover {\n\n    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:pressed {\n    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n  \n}\n\nQSlider::add-page:horizontal {\n    background: none;\n border: none;\n}\n\nQSlider::sub-page:horizontal {\n    background: none;\n border: none;\n}\n"
        self.qlineedit_style = "/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n\n\n\nQLineEdit {\n    background-color: rgb(42, 42, 42); /* Dark background */\n    color: rgb(0, 255, 0); /* Bright green text */\n    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n    border-radius: 5px; /* Rounded corners */\n    padding-top: 1px; /* Top padding to push the text down */\n    padding-bottom: 1px; /* Bottom padding for even spacing */\n    padding-left: 1px; /* Left padding */\n    padding-right: 1px; /* Right padding */\n    text-align: center; /* Center the text horizontally */\n}"
        self.qcheckbox_style = "QCheckBox {\n    border: none; /* No border for the checkbox */\nbackground-color: rgb(108,108,118); /* Fallback color */\nborder-radius:5;\n}\n\nQCheckBox::indicator {\n    width: 24px; /* Width of the checkbox */\n    height: 12px; /* Height of the checkbox */\n    background-color: transparent; /* Ensures background is transparent */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:unchecked {\n    background-image: url(images/check_off_half_small.png); /* Image for unchecked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:checked {\n    background-image: url(images/check_on_half_small.png); /* Image for checked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n"
        self.frame_style = "background-color: rgb(80, 80, 80); border: 2px solid rgb(22, 22, 22); border-radius: 10px;"
        self.qbutton_style = "QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 0px; /* Consistent with the tab's rounded corners */\n    padding: 0px 0px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n"
        self.progressbar_style = "QProgressBar {\n    text-align: center;\n    color: rgb(0, 0, 0);\n    border-width: 2px;\n    border-radius: 6px;\n    border-color: rgb(58, 58, 58);\n    border-style: inset;\n    background-color: rgb(77, 77, 77);\n}\nQProgressBar::chunk {\n    border-radius: 6px;\n    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, /* Vertical gradient */\n                                 stop: 0 #00ff00,   /* Green at the start */\n                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n                                 stop: 1 #ff0000 ); /* Red at the end */\n}\nQProgressBar[orientation='vertical'] {\n    text-align: center;\n    color: rgb(0, 0, 0);\n    border-width: 2px;\n    border-radius: 2px;\n    border-color: rgb(58, 58, 58);\n    border-style: inset;\n    background-color: rgb(77, 77, 77);\n}"



        """if promptMorphConfigFrame != None:
            self.add_prompt_morph_blending_frame(promptMorphConfigFrame[0])
            self.morph_prompt_binding.setText(promptMorphConfigFrame[1])
            self.morph_promptA.setText(promptMorphConfigFrame[2])
            self.morph_promptB.setText(promptMorphConfigFrame[3])
            self.morph_prompt_min.setText(promptMorphConfigFrame[4])
            self.morph_prompt_max.setText(promptMorphConfigFrame[5])
            self.morph_prompt_value.setText(promptMorphConfigFrame[6])"""

    def set_prompt_morphing_on_off(self, status, shouldSwitchState = True):
        self.morph_prompt_enabled = status
        if shouldSwitchState:
            if self.morph_prompt_enabled:
                #print("Enabling prompt morphing")
                self.morph_prompt_enabled_checkbox.setChecked(True)
            else:
                #print("Disabling prompt morphing")
                self.morph_prompt_enabled_checkbox.setChecked(False)

    def set_prompt_morphing_smooth_motion_on_off(self, status, shouldSwitchState = True):
        self.morph_prompt_smooth_motion_enabled = status
        if shouldSwitchState:
            if self.morph_prompt_smooth_motion_enabled:
                #print("Enabling prompt morphing")
                self.morph_prompt_smooth_motion_enabled_checkbox.setChecked(True)
            else:
                #print("Disabling prompt morphing")
                self.morph_prompt_smooth_motion_enabled_checkbox.setChecked(False)


    def set_prompt_morphing_type(self, isPromptBlending): #0 == No prompt blending, 1 == Prompt blending
        if isPromptBlending != self.isPromptBlending:
            print("Converting to status: " + str(isPromptBlending))
            self.convert_to_prompt_morphing(isPromptBlending)

    def setValuesFromConfig(self, promptMorphConfigFrame):
        if promptMorphConfigFrame != None:
            self.add_prompt_morph_blending_frame_to_container(promptMorphConfigFrame[2])
            self.morph_prompt_binding.setText(promptMorphConfigFrame[3])
            self.morph_promptA.setText(promptMorphConfigFrame[4])
            self.morph_promptB.setText(promptMorphConfigFrame[5])
            self.morph_prompt_min.setText(promptMorphConfigFrame[6])
            self.morph_prompt_max.setText(promptMorphConfigFrame[7])
            self.morph_prompt_value.setText(promptMorphConfigFrame[8])
            self.morph_prompt_slider.setMinimum(int(float(promptMorphConfigFrame[6]) * 100))
            self.morph_prompt_slider.setMaximum(int(float(promptMorphConfigFrame[7]) * 100))
            self.morph_prompt_slider.setValue(int(float(promptMorphConfigFrame[8]) * 100))
            self.set_prompt_morphing_on_off(promptMorphConfigFrame[0])
            self.set_prompt_morphing_smooth_motion_on_off(promptMorphConfigFrame[1])
    def convert_to_prompt_morphing(self, isPromptBlending):
        self.isPromptBlending = isPromptBlending
        if isPromptBlending:
            self.morph_promptA.setGeometry(QRect(123, 25, 100, 23))
        else:
            self.morph_promptA.setGeometry(QRect(123, 25, 289, 23))
        self.morph_promptA.setStyleSheet(self.qlineedit_style)

        if isPromptBlending:
            if self.morph_promptB ==  None:
                self.morph_promptB = QLineEdit(self.morph_prompt_frame)
                self.morph_promptB.setObjectName(u"morph_promptB" + str(self.identifier))
            self.morph_promptB.setGeometry(QRect(263, 25, 100, 23))
            self.morph_promptB.setStyleSheet(self.qlineedit_style)
            self.morph_promptB.show()

            if self.morph_promptB_label == None:
                self.morph_promptB_label = QLabel(self.morph_prompt_frame)
                self.morph_promptB_label.setObjectName(u"morph_promptB_label" + str(self.identifier))
            self.morph_promptB_label.setGeometry(QRect(261, 4, 89, 18))
            self.morph_promptB_label.setMinimumSize(QSize(0, 0))
            self.morph_promptB_label.setStyleSheet(u"border: none;")
            self.morph_promptB_label.setText(u"Prompt B")
            self.morph_promptB_label.show()
            self.parent.deforumationtools.propagateAllComponents(self.morph_promptB, shouldHide=False)
            self.parent.deforumationtools.propagateAllComponents(self.morph_promptB_label, shouldHide=False)
        else:
            self.morph_promptB.hide()
            self.morph_promptB_label.hide()
            self.parent.deforumationtools.propagateAllComponents(self.morph_promptB, shouldHide=True)
            self.parent.deforumationtools.propagateAllComponents(self.morph_promptB_label, shouldHide=True)
            #del self.morph_promptB
            #self.morph_promptB = None

        if isPromptBlending:
            self.morph_prompt_slider.setMaximum(100)
            self.morph_prompt_slider.setMinimum(0)
            self.morph_prompt_slider.setValue(50)
        else:
            self.morph_prompt_slider.setMaximum(200)
            self.morph_prompt_slider.setMinimum(0)
            self.morph_prompt_slider.setValue(100)

        if isPromptBlending:
            self.morph_prompt_value.setText("0.5")
        else:
            self.morph_prompt_value.setText("1.0")

        if isPromptBlending:
            self.morph_prompt_max.setText("1.0")
        else:
            self.morph_prompt_max.setText("2.0")

        if isPromptBlending:
            self.morph_prompt_min.setText("0.0")
        else:
            self.morph_prompt_min.setText("0.0")
        """if isPromptBlending:
            self.add_prompt_morph_blending_frame(isPromptBlending)
        else:
            self.remove_prompt_morph_blending_frame()"""

    def remove_prompt_morph_frame(self):
        self.morph_prompt_frame.hide()
        self.morph_prompt_frame.deleteLater()
        morph_prompt_area_size_height = self.parent.ui.horizontalWidget.maximumHeight()
        self.parent.ui.horizontalWidget.setMaximumHeight(morph_prompt_area_size_height - 85)
        morph_prompt_area_size_height = self.parent.ui.scrollAreaWidgetContentsPromptMorph.minimumHeight()
        self.parent.ui.scrollAreaWidgetContentsPromptMorph.setMinimumHeight(morph_prompt_area_size_height - 87)
    def add_prompt_morph_blending_frame_to_container(self, isPromptBlending):
        self.isPromptBlending = isPromptBlending

        self.morph_prompt_frame = QFrame(self.parent.ui.horizontalWidget)
        self.morph_prompt_frame.setObjectName(u"morph_prompt_frame" + str(self.identifier))
        self.morph_prompt_frame.setMinimumSize(QSize(0, 85))
        self.morph_prompt_frame.setMaximumSize(QSize(16777215, 85))
        self.morph_prompt_frame.setStyleSheet(self.frame_style)
        self.morph_prompt_frame.setFrameShape(QFrame.StyledPanel)
        self.morph_prompt_frame.setFrameShadow(QFrame.Raised)


        morph_prompt_area_size_height = self.parent.ui.horizontalWidget.maximumHeight()
        self.parent.ui.horizontalWidget.setMaximumHeight(morph_prompt_area_size_height + 87)

        morph_prompt_area_size_height = self.parent.ui.scrollAreaWidgetContentsPromptMorph.minimumHeight()
        self.parent.ui.scrollAreaWidgetContentsPromptMorph.setMinimumHeight(morph_prompt_area_size_height + 87)

        self.morph_prompt_binding = QLineEdit(self.morph_prompt_frame)
        self.morph_prompt_binding.setObjectName(u"morph_prompt_binding" + str(self.identifier))
        self.morph_prompt_binding.setGeometry(QRect(8, 25, 92, 23))
        self.morph_prompt_binding.setStyleSheet(self.qlineedit_style)

        self.morph_binding_label = QLabel(self.morph_prompt_frame)
        self.morph_binding_label.setObjectName(u"morph_binding_label" + str(self.identifier))
        self.morph_binding_label.setGeometry(QRect(9, 4, 89, 18))
        self.morph_binding_label.setMinimumSize(QSize(0, 0))
        self.morph_binding_label.setStyleSheet(u"border: none;")
        self.morph_binding_label.setText(u"Bindings Name")


        self.morph_promptA_label = QLabel(self.morph_prompt_frame)
        self.morph_promptA_label.setObjectName(u"morph_promptA_label" + str(self.identifier))
        self.morph_promptA_label.setGeometry(QRect(124, 4, 89, 18))
        self.morph_promptA_label.setMinimumSize(QSize(0, 0))
        self.morph_promptA_label.setStyleSheet(u"border: none;")
        self.morph_promptA_label.setText(u"Prompt A")

        self.morph_promptA = QLineEdit(self.morph_prompt_frame)
        self.morph_promptA.setObjectName(u"morph_promptA" + str(self.identifier))
        if isPromptBlending:
            self.morph_promptA.setGeometry(QRect(123, 25, 130, 23))
        else:
            self.morph_promptA.setGeometry(QRect(123, 25, 269, 23))
        self.morph_promptA.setStyleSheet(self.qlineedit_style)

        self.morph_promptB = QLineEdit(self.morph_prompt_frame)
        self.morph_promptB.setObjectName(u"morph_promptB" + str(self.identifier))
        self.morph_promptB.setGeometry(QRect(263, 25, 130, 23))
        self.morph_promptB.setStyleSheet(self.qlineedit_style)

        self.morph_promptB_label = QLabel(self.morph_prompt_frame)
        self.morph_promptB_label.setObjectName(u"morph_promptB_label" + str(self.identifier))
        self.morph_promptB_label.setGeometry(QRect(261, 4, 89, 18))
        self.morph_promptB_label.setMinimumSize(QSize(0, 0))
        self.morph_promptB_label.setStyleSheet(u"border: none;")
        self.morph_promptB_label.setText(u"Prompt B")
        if not isPromptBlending:
            self.morph_promptB.hide()
            self.morph_promptB_label.hide()



        self.morph_prompt_slider = QSlider(self.morph_prompt_frame)
        self.morph_prompt_slider.setObjectName(u"morph_prompt_slider" + str(self.identifier))
        self.morph_prompt_slider.setGeometry(QRect(174, 54, 220, 28))
        self.morph_prompt_slider.setStyleSheet(self.slider_style)
        self.morph_prompt_slider.setOrientation(Qt.Horizontal)
        if isPromptBlending:
            self.morph_prompt_slider.setMaximum(100)
            self.morph_prompt_slider.setMinimum(0)
            self.morph_prompt_slider.setValue(50)
        else:
            self.morph_prompt_slider.setMaximum(200)
            self.morph_prompt_slider.setMinimum(0)
            self.morph_prompt_slider.setValue(100)

        self.morph_prompt_blending_checkbox = QCheckBox(self.morph_prompt_frame)
        self.morph_prompt_blending_checkbox.setObjectName(u"morph_prompt_blending_checkbox" + str(self.identifier))
        self.morph_prompt_blending_checkbox.setGeometry(QRect(125, 50, 100, 14))
        self.morph_prompt_blending_checkbox.setMinimumSize(QSize(34, 16))
        self.morph_prompt_blending_checkbox.setMaximumSize(QSize(34, 16))
        font11 = QFont()
        font11.setPointSize(8)
        self.morph_prompt_blending_checkbox.setFont(font11)
        self.morph_prompt_blending_checkbox.setStyleSheet(u"QCheckBox {\n    border: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator {\n    width: 54px; /* Width of the checkbox */\n    height: 29px; /* Height of the checkbox */\n    background-color: transparent; /* Ensures background is transparent */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:unchecked {\n    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:checked {\n    background-image: url(images/check_on_small.png); /* Image for checked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n") #self.qcheckbox_style)
        #self.morph_prompt_blending_checkbox.setText(u"P-blend")
        if isPromptBlending:
            self.morph_prompt_blending_checkbox.setChecked(True)
        else:
            self.morph_prompt_blending_checkbox.setChecked(False)

        self.morph_prompt_blending_checkbox_label = QLabel(self.morph_prompt_frame)
        self.morph_prompt_blending_checkbox_label.setObjectName(u"morph_prompt_blending_checkbox_label" + str(self.identifier))
        self.morph_prompt_blending_checkbox_label.setGeometry(QRect(112, 70, 32, 9))
        self.morph_prompt_blending_checkbox_label.setMinimumSize(QSize(64, 9))
        font11 = QFont()
        font11.setPointSize(7)
        self.morph_prompt_blending_checkbox_label.setFont(font11)
        self.morph_prompt_blending_checkbox_label.setStyleSheet(u"border:0")
        self.morph_prompt_blending_checkbox_label.setText("Prompt - Blend")

        self.morph_prompt_enabled_checkbox = QCheckBox(self.morph_prompt_frame)
        self.morph_prompt_enabled_checkbox.setObjectName(u"morph_prompt_checkbox_on_off" + str(self.identifier))
        self.morph_prompt_enabled_checkbox.setGeometry(QRect(10, 50, 16, 10))
        self.morph_prompt_enabled_checkbox.setMinimumSize(QSize(34, 16))
        self.morph_prompt_enabled_checkbox.setMaximumSize(QSize(34, 16))
        self.morph_prompt_enabled_checkbox.setStyleSheet(u"QCheckBox {\n    border: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator {\n    width: 54px; /* Width of the checkbox */\n    height: 29px; /* Height of the checkbox */\n    background-color: transparent; /* Ensures background is transparent */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:unchecked {\n    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:checked {\n    background-image: url(images/check_on_small.png); /* Image for checked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n")
        if self.morph_prompt_enabled:
            self.morph_prompt_enabled_checkbox.setChecked(True)
        else:
            self.morph_prompt_enabled_checkbox.setChecked(False)
        self.OnOff_label = QLabel(self.morph_prompt_frame)
        self.OnOff_label.setObjectName(u"OnOff_label" + str(self.identifier))
        self.OnOff_label.setGeometry(QRect(10, 70, 32, 9))
        self.OnOff_label.setMinimumSize(QSize(36, 9))
        font11 = QFont()
        font11.setPointSize(7)
        self.OnOff_label.setFont(font11)
        self.OnOff_label.setStyleSheet(u"border:0")
        self.OnOff_label.setText("On/Off")


        self.morph_prompt_smooth_motion_enabled_checkbox = QCheckBox(self.morph_prompt_frame)
        self.morph_prompt_smooth_motion_enabled_checkbox.setObjectName(u"morph_prompt_smooth_motion_enabled_checkbox" + str(self.identifier))
        self.morph_prompt_smooth_motion_enabled_checkbox.setGeometry(QRect(64, 50, 16, 10))
        self.morph_prompt_smooth_motion_enabled_checkbox.setMinimumSize(QSize(34, 16))
        self.morph_prompt_smooth_motion_enabled_checkbox.setMaximumSize(QSize(34, 16))
        self.morph_prompt_smooth_motion_enabled_checkbox.setStyleSheet(u"QCheckBox {\n    border: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator {\n    width: 54px; /* Width of the checkbox */\n    height: 29px; /* Height of the checkbox */\n    background-color: transparent; /* Ensures background is transparent */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:unchecked {\n    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n\nQCheckBox::indicator:checked {\n    background-image: url(images/check_on_small.png); /* Image for checked state */\n    background-repeat: no-repeat; /* Prevents the image from repeating */\nbackground-position: left; /* Left the image */\nborder: none; /* No border for the checkbox */\n}\n")
        if self.morph_prompt_smooth_motion_enabled:
            self.morph_prompt_smooth_motion_enabled_checkbox.setChecked(True)
        else:
            self.morph_prompt_smooth_motion_enabled_checkbox.setChecked(False)
        self.morph_prompt_smooth_motion_enabled_label = QLabel(self.morph_prompt_frame)
        self.morph_prompt_smooth_motion_enabled_label.setObjectName(u"morph_prompt_smooth_motion_enabled_label" + str(self.identifier))
        self.morph_prompt_smooth_motion_enabled_label.setGeometry(QRect(64, 70, 32, 9))
        self.morph_prompt_smooth_motion_enabled_label.setMinimumSize(QSize(36, 9))
        font11 = QFont()
        font11.setPointSize(7)
        self.morph_prompt_smooth_motion_enabled_label.setFont(font11)
        self.morph_prompt_smooth_motion_enabled_label.setStyleSheet(u"border:0")
        self.morph_prompt_smooth_motion_enabled_label.setText("SOn/SOff")



        self.morph_prompt_minmax_frame = QFrame(self.morph_prompt_frame)
        self.morph_prompt_minmax_frame.setObjectName(u"morph_prompt_minmax_frame" + str(self.identifier))
        self.morph_prompt_minmax_frame.setGeometry(QRect(396, 8, 81, 73))
        self.morph_prompt_minmax_frame.setStyleSheet(u"border:0")
        self.morph_prompt_minmax_frame.setFrameShape(QFrame.StyledPanel)
        self.morph_prompt_minmax_frame.setFrameShadow(QFrame.Raised)

        self.morph_prompt_value = QLineEdit(self.morph_prompt_minmax_frame)
        self.morph_prompt_value.setObjectName(u"morph_prompt_value" + str(self.identifier))
        self.morph_prompt_value.setGeometry(QRect(3, 49, 41, 23))
        self.morph_prompt_value.setStyleSheet(self.qlineedit_style)
        self.morph_prompt_progress_value = QLabel(self.morph_prompt_minmax_frame)
        self.morph_prompt_progress_value.setObjectName(u"morph_prompt_progress_value" + str(self.identifier))
        self.morph_prompt_progress_value.setGeometry(QRect(48, 49, 38, 23))
        self.morph_prompt_progress_value.setMinimumSize(QSize(36, 9))

        if isPromptBlending:
            self.morph_prompt_value.setText("0.5")
            self.morph_prompt_progress_value.setText("0.5")
        else:
            self.morph_prompt_value.setText("1.0")
            self.morph_prompt_progress_value.setText("1.0")


        self.morph_prompt_max = QLineEdit(self.morph_prompt_minmax_frame)
        self.morph_prompt_max.setObjectName(u"morph_prompt_max" + str(self.identifier))
        self.morph_prompt_max.setGeometry(QRect(45, 17, 28, 23))
        self.morph_prompt_max.setStyleSheet(self.qlineedit_style)
        if isPromptBlending:
            self.morph_prompt_max.setText("1.0")
        else:
            self.morph_prompt_max.setText("2.0")

        self.morph_prompt_minmaxbetween_label = QLabel(self.morph_prompt_minmax_frame)
        self.morph_prompt_minmaxbetween_label.setObjectName(u"morph_prompt_minmaxbetween_label" + str(self.identifier))
        self.morph_prompt_minmaxbetween_label.setGeometry(QRect(35, 16, 10, 18))
        self.morph_prompt_minmaxbetween_label.setMinimumSize(QSize(0, 0))
        self.morph_prompt_minmaxbetween_label.setStyleSheet(u"border: none;")
        self.morph_prompt_minmaxbetween_label.setText(u"-")

        self.morph_prompt_min = QLineEdit(self.morph_prompt_minmax_frame)
        self.morph_prompt_min.setObjectName(u"morph_prompt_min" + str(self.identifier))
        self.morph_prompt_min.setGeometry(QRect(3, 17, 28, 23))
        self.morph_prompt_min.setStyleSheet(self.qlineedit_style)
        if isPromptBlending:
            self.morph_prompt_min.setText("0.0")
        else:
            self.morph_prompt_min.setText("0.0")

        self.morph_prompt_min_label = QLabel(self.morph_prompt_minmax_frame)
        self.morph_prompt_min_label.setObjectName(u"morph_prompt_min_label" + str(self.identifier))
        self.morph_prompt_min_label.setGeometry(QRect(4, -4, 25, 18))
        self.morph_prompt_min_label.setStyleSheet(u"border: none;")
        self.morph_prompt_min_label.setText(u"Min:")

        self.morph_prompt_max_label = QLabel(self.morph_prompt_minmax_frame)
        self.morph_prompt_max_label.setObjectName(u"morph_prompt_max_label" + str(self.identifier))
        self.morph_prompt_max_label.setGeometry(QRect(46, -4, 25, 18))
        #self.morph_prompt_max_label.setMinimumSize(QSize(30, 0))
        self.morph_prompt_max_label.setStyleSheet(u"border: none;")
        self.morph_prompt_max_label.setText(u"Max:")


        self.morph_prompt_progressbar_frame = QFrame(self.morph_prompt_frame)
        self.morph_prompt_progressbar_frame.setObjectName(u"morph_prompt_progressbar_frame" + str(self.identifier))
        self.morph_prompt_progressbar_frame.setGeometry(QRect(475, 6, 36, 73))
        self.morph_prompt_progressbar_frame.setStyleSheet(u"border:0")
        self.morph_prompt_progressbar_frame.setFrameShape(QFrame.StyledPanel)
        self.morph_prompt_progressbar_frame.setFrameShadow(QFrame.Raised)

        self.morph_prompt_progressbar = QProgressBar(self.morph_prompt_progressbar_frame)
        self.morph_prompt_progressbar.setObjectName(u"morph_prompt_progressbar" + str(self.identifier))
        self.morph_prompt_progressbar.setGeometry(QRect(0, 0, 34, 73))
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(True)
        self.morph_prompt_progressbar.setFont(font8)
        self.morph_prompt_progressbar.setLayoutDirection(Qt.LeftToRight)
        self.morph_prompt_progressbar.setStyleSheet(self.progressbar_style)
        self.morph_prompt_progressbar.setValue(100)
        self.morph_prompt_progressbar.setTextVisible(True)
        self.morph_prompt_progressbar.setTextDirection(QProgressBar.TopToBottom)
        self.morph_prompt_progressbar.setOrientation(Qt.Vertical)


        self.parent.ui.gridLayout_29.addWidget(self.morph_prompt_frame, self.identifier, 0, 1, 1)


    def resizeEvent_morph_frame(self, verticalFrame_prompt_width):
        PromptAsize = verticalFrame_prompt_width - 552
        if PromptAsize > 0:

            geo = self.morph_promptA.geometry()
            if self.isPromptBlending:
                self.morph_promptA.setGeometry(geo.x(),geo.y(), 130+int(PromptAsize/2), geo.height())
            else:
                self.morph_promptA.setGeometry(geo.x(),geo.y(), 269+int(PromptAsize/1), geo.height())

            if self.isPromptBlending:
                geo = self.morph_promptB_label.geometry()
                self.morph_promptB_label.setGeometry(263 + int(PromptAsize/2), geo.y(), geo.width(), geo.height())

                geo = self.morph_promptB.geometry()
                self.morph_promptB.setGeometry(263 + int(PromptAsize/2), geo.y(), 130 + int(PromptAsize/2), geo.height())

            geo = self.morph_prompt_minmax_frame.geometry()
            self.morph_prompt_minmax_frame.setGeometry(396 + int(PromptAsize/1),geo.y(), geo.width(), geo.height())

            geo = self.morph_prompt_progressbar_frame.geometry()
            self.morph_prompt_progressbar_frame.setGeometry(475 + int(PromptAsize / 1), geo.y(), geo.width(), geo.height())

            geo = self.morph_prompt_slider.geometry()
            self.morph_prompt_slider.setGeometry(geo.x(),geo.y(), 220+int(PromptAsize/1), geo.height())
            #morp_prompt_slider_style_sheet = "QSlider{ border: none;}\nQSlider::groove:horizontal {\n    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n    border: none;\n    height: 29px; /* The height of your image */\n    width: "+str(240+int(PromptAsize/1))+"px; /* Width of the handle - adjust as needed */\n}\n\nQSlider::handle:horizontal {\n    background-image: url(images/handle_off.png); /* The path to your handle image */\n  background-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:hover {\n\n    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:pressed {\n    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n  \n}\n\nQSlider::add-page:horizontal {\n    background: none;\n border: none;\n}\n\nQSlider::sub-page:horizontal {\n    background: none;\n border: none;\n}\n "
            #self.morph_prompt_slider.setStyleSheet(self.slider_style)
            morp_prompt_slider_style_sheet = "QSlider{ border: none;}\nQSlider::groove:horizontal {\n    border-image: url(images/groove_230_m.png) ; /* Adjust slicing and stretch as needed */\n    border: none;\n    height: 29px; /* The height of your image */\n    width: " + str(220 + int(PromptAsize / 1)) + "px; /* Width of the handle - adjust as needed */\n}\n\nQSlider::handle:horizontal {\n    background-image: url(images/handle_off.png); /* The path to your handle image */\n  background-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:hover {\n\n    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n}\n\nQSlider::handle:horizontal:pressed {\n    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\nbackground-repeat: no-repeat;\n    border: none; /* Remove the border if you don't need it */\n    width: 32px; /* Width of the handle - adjust as needed */\n    height: 32px; /* Height of the handle - adjust as needed */\n    margin: -2px 0; /* Optional: Adjust the margin if needed */\n  \n}\n\nQSlider::add-page:horizontal {\n    background: none;\n border: none;\n}\n\nQSlider::sub-page:horizontal {\n    background: none;\n border: none;\n}\n "
            self.morph_prompt_slider.setStyleSheet(morp_prompt_slider_style_sheet)

class Deforumation_Prompts():

    def __init__(self, parent=None, deforumationtotalrecall = None, namedpipes = None, deforumation_settings=None, deforumationwidgets=None, deforumation_tools=None):
        self.deforumation_settings = deforumation_settings
        self.deforumation_tools = deforumation_tools
        self.deforumationwidgets = deforumationwidgets
        #self.q = self.deforumation_settings.getConfiguaration()
        self.parent = parent
        self.deforumationnamedpipes = namedpipes
        self.DeforumationTotalRecall = deforumationtotalrecall #Deforumation_Total_Recall()
        self.positivePrompt1 = ""
        self.positivePrompt2 = ""
        self.negativePrompt1 = ""
        #self.setCurrentPrompts()
        self.current_prompt_weight = 0
        self.prompt_1_weight = 1.0
        self.prompt_2_weight = 1.0
        self.use_deforumation_prompts = True
        self.should_use_before_deforum_prompt = False
        self.should_use_after_deforum_prompt = False
        self.numberOfPromptMorphFrames = 0
        self.prompt_morphing_container = {}


    def add_prompt_morph_blending_frame(self):

        while self.numberOfPromptMorphFrames in self.prompt_morphing_container:
            self.numberOfPromptMorphFrames += 1
        if self.numberOfPromptMorphFrames in self.prompt_morphing_container:
            for n in range(0,200):
                print("What THE FUCK ARE YOU DOING!!! THIS FRAME ALREADY EXISTS!!! AND YOU WANT TO STEAl IT!?!?!?!?")
        self.prompt_morphing_container[self.numberOfPromptMorphFrames] = Deforumation_Prompt_Morphing_Frame(self.numberOfPromptMorphFrames, self.parent)
        self.prompt_morphing_container[self.numberOfPromptMorphFrames].add_prompt_morph_blending_frame_to_container(1)
        self.resizeEvent_morph_frames(self.parent.ui.right_prompt_tab_frame.width())
        self.parent.deforumationwidgets.enumerateWidgets(self.parent, self.prompt_morphing_container[self.numberOfPromptMorphFrames].morph_prompt_frame)
        #self.parent.deforumationwidgets.enumerateWidgets(self.parent, self.prompt_morphing_container[self.numberOfPromptMorphFrames - 1].remove_morph_prompt)
        self.savePromptMorphFrameToConfig(self.prompt_morphing_container[self.numberOfPromptMorphFrames])

    def loadMorphPromptSyrupFromConfig(self):
        self.Prompt_Morph_Syrup_Value = int(self.deforumation_settings.getGuiConfigValue("Syrupmotion_Morph_Prompt"))
        if self.Prompt_Morph_Syrup_Value < 0:
            self.Prompt_Morph_Syrup_Value = 0
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Morph_Prompt", 0)
        self.parent.ui.syrup_prompt_morph_slider.setValue(self.Prompt_Morph_Syrup_Value)
        self.parent.ui.syrup_prompt_morph_value.setText(str(self.Prompt_Morph_Syrup_Value))
    def loadMorphPromptFramesFromConfig(self, file = None):
        if file == None:
            deforumation_settings_promptmorph = self.deforumation_settings.getPromtMorphConfig()
        else:
            deforumation_settings_promptmorph = self.deforumation_settings.loadJSONconfig(file)
        deforumation_settings_promptmorph_copy = deforumation_settings_promptmorph.copy()
        for morphFrame in deforumation_settings_promptmorph_copy:
            while self.numberOfPromptMorphFrames in self.prompt_morphing_container:
                self.numberOfPromptMorphFrames += 1
            if self.numberOfPromptMorphFrames in self.prompt_morphing_container:
                for n in range(0, 200):
                    print("What THE FUCK ARE YOU DOING AGAIN!!! THIS FRAME ALREADY EXISTS!!! AND YOU WANT TO STEAl IT!?!?!?!?")

            self.deforumationnamedpipes.writeValue("remove_all_deforumation_prompt_morph", 1)

            self.prompt_morphing_container[self.numberOfPromptMorphFrames] = Deforumation_Prompt_Morphing_Frame(self.numberOfPromptMorphFrames, self.parent, deforumation_settings_promptmorph[morphFrame])
            self.prompt_morphing_container[self.numberOfPromptMorphFrames].setValuesFromConfig(deforumation_settings_promptmorph[str(morphFrame)])
            self.colorMorphingPromtsDependingOnEnabledStatus(self.prompt_morphing_container[self.numberOfPromptMorphFrames])
            #self.numberOfPromptMorphFrames += 1
            self.parent.deforumationwidgets.enumerateWidgets(self.parent, self.prompt_morphing_container[self.numberOfPromptMorphFrames].morph_prompt_frame)
        self.deforumation_settings.deletePromtMorphConfigKey()
        for morphFrame in self.prompt_morphing_container:
                self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morphFrame])
                binding = self.prompt_morphing_container[morphFrame].morph_prompt_binding.text()
                promptA = self.prompt_morphing_container[morphFrame].morph_promptA.text()
                promptB = self.prompt_morphing_container[morphFrame].morph_promptB.text()
                isPromptBlending = self.prompt_morphing_container[morphFrame].isPromptBlending
                is_enabled = self.prompt_morphing_container[morphFrame].morph_prompt_enabled
                current_value = float(self.prompt_morphing_container[morphFrame].morph_prompt_value.text())
                self.prompt_morphing_container[morphFrame].morph_prompt_progress_value.setText(str('%.2f' % float(current_value)))
                self.deforumationnamedpipes.writeValue("set_prompt_morph_values_" + str(binding), [promptA, promptB, isPromptBlending, is_enabled, current_value])

        self.resizeEvent_morph_frames(self.parent.ui.right_prompt_tab_frame.width())

    def setComponetValues(self):
        self.shouldUseDeforumationPrompts()
        self.shouldUseBeforeDeforumPrompt()
        self.shouldUseAfterDeforumPrompt()
        deforumation_settings_promptmorph = self.deforumation_settings.getPromtMorphConfig()
        for morphFrame in deforumation_settings_promptmorph:
            self.colorMorphingPromtsDependingOnEnabledStatus(self.prompt_morphing_container[int(morphFrame)])
            #self.numberOfPromptMorphFrames += 1
    def addPromptBeforeDeforum(self, value):
        #conf["should_use_before_deforum_prompt"] = value
        self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_before_deforum_prompt", value)
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)
        self.deforumationnamedpipes.writeValue("should_use_before_deforum_prompt", value)
        self.saveCurrentPrompt()
    def addPromptAfterDeforum(self, value):
        #conf["should_use_after_deforum_prompt"] = value
        self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_after_deforum_prompt", int(value))
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)
        self.deforumationnamedpipes.writeValue("should_use_after_deforum_prompt", int(value))
        self.saveCurrentPrompt()
    def shouldUseBeforeDeforumPrompt(self):
        conf = self.deforumation_settings.getSendConfig()
        if "should_use_before_deforum_prompt" in conf:
            self.should_use_before_deforum_prompt = conf["should_use_before_deforum_prompt"]
        self.addPromptBeforeDeforum(self.should_use_before_deforum_prompt)
        self.parent.ui.add_prompt_before_checkbox.setChecked(self.should_use_before_deforum_prompt)
    def shouldUseAfterDeforumPrompt(self):
        conf = self.deforumation_settings.getSendConfig()
        if "should_use_after_deforum_prompt" in conf:
            self.should_use_after_deforum_prompt = conf["should_use_after_deforum_prompt"]
        self.addPromptAfterDeforum(self.should_use_after_deforum_prompt)
        self.parent.ui.add_prompt_after_checkbox.setChecked(self.should_use_after_deforum_prompt)
    def shouldUseDeforumationPrompts(self):
        conf = self.deforumation_settings.getSendConfig()
        if "should_use_deforumation_prompts" in conf:
            self.use_deforumation_prompts = conf["should_use_deforumation_prompts"]
        if self.use_deforumation_prompts:

            self.deforumationnamedpipes.writeValue("should_use_deforumation_prompt_scheduling", 1)
            self.setCurrentPrompts(True)
        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_prompt_scheduling", 0)
            self.setCurrentPrompts(True)
        self.parent.ui.use_deforumation_prompt_scheduling_checkbox.setChecked(self.use_deforumation_prompts)
    def setShouldUseDeforumationPrompts(self, value):
        #print("!!!!!setShouldUseDeforumationPrompts function was run!!!!!")
        self.use_deforumation_prompts = value
        conf = self.deforumation_settings.getSendConfig()
        conf["should_use_deforumation_prompts"] = int(self.use_deforumation_prompts)
        if self.use_deforumation_prompts:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_prompt_scheduling", 1)
            self.setCurrentPrompts()
        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_prompt_scheduling", 0)
    def setCurrentPromptWeight(self, item):#weight):

        self.current_prompt_weight = item.value() #Slider value
        self.deforumation_tools.propagateAllComponents(item, item.value())
        if self.current_prompt_weight != 0:
            if self.current_prompt_weight > 0:
                self.prompt_1_weight = float('%.2f' % round(1.0 - (self.current_prompt_weight / 100), 2))
                self.prompt_2_weight = float('%.2f' % 1.0) #round(1.0 + (self.current_prompt_weight / 100), 2))
            else:
                self.prompt_2_weight = float('%.2f' % round(1.0 + (self.current_prompt_weight / 100), 2))
                self.prompt_1_weight = float('%.2f' % 1.0)#round(1.0 - (self.current_prompt_weight / 100), 2))
            #print("Prompt 1 weight is:" + str(self.prompt_1_weight))
            #print("Prompt 2 weight is:" + str(self.prompt_2_weight))
            self.deforumationnamedpipes.writeValue("positive_prompt_weight_1", self.prompt_1_weight)
            self.deforumationnamedpipes.writeValue("positive_prompt_weight_2", self.prompt_2_weight)
        else:
            self.deforumationnamedpipes.writeValue("positive_prompt_weight_1", 1.0)
            self.deforumationnamedpipes.writeValue("positive_prompt_weight_2", 1.0)

    def setCurrentPromptsThroughTotalRecall(self, frameNumber = -1):
        current_total_recall_frame = self.DeforumationTotalRecall.getCurrentTotalRecallFrame(frameNumber)
        if current_total_recall_frame.should_use_deforumation_prompt_scheduling:
            self.parent.ui.prompt1.setPlainText(current_total_recall_frame.positive_prompt_1)
            self.parent.ui.prompt2.setPlainText(current_total_recall_frame.positive_prompt_2)
            self.parent.ui.negative_prompt.setPlainText(current_total_recall_frame.negative_prompt_1)
        else:
            self.parent.ui.prompt1.setPlainText(current_total_recall_frame.Prompt_Positive)
            self.parent.ui.prompt2.setPlainText("")
            self.parent.ui.negative_prompt.setPlainText(current_total_recall_frame.Prompt_Negative)

    def propagateAllComponents(self, sender, value = None):
        original_component_name = self.deforumation_tools.getOriginalComponentName(sender)
        for component in self.deforumationwidgets.getWidgetContainer():
            if component.startswith(original_component_name) and not component == sender.objectName():
                if len(component) <= len(original_component_name)+3:
                    if type(sender) == QCheckBox:
                        if value == None:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.setChecked(not sender.isChecked())
                        else:
                            component.setChecked(value)
                    elif type(sender) == QLabel or type(sender) == QLineEdit:
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setText(str(sender.text()))
                    elif type(sender) == QSlider:
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setValue(sender.value())

    def setCurrentPrompts(self, readFromConfig = False):
        if readFromConfig:
            self.positivePrompt1 = self.deforumation_settings.getSendConfigValue("positive_prompt_1")
            if self.positivePrompt1 == 0:
                self.positivePrompt1 = ""
            self.positivePrompt2 = self.deforumation_settings.getSendConfigValue("positive_prompt_2")
            if self.positivePrompt2 == 0:
                self.positivePrompt2 = ""
            self.negativePrompt1 = self.deforumation_settings.getSendConfigValue("negative_prompt_1")
            if self.negativePrompt1 == 0:
                self.negativePrompt1 = ""
        else:
            should_use_deforumation_prompt_scheduling = self.deforumationnamedpipes.readValue("should_use_deforumation_prompt_scheduling")
            if int(should_use_deforumation_prompt_scheduling):
                self.positivePrompt1 = self.deforumationnamedpipes.readValue("positive_prompt_1")
                self.positivePrompt2 = self.deforumationnamedpipes.readValue("positive_prompt_2")
                self.negativePrompt1 = self.deforumationnamedpipes.readValue("negative_prompt_1")
            else:
                self.positivePrompt1 = self.deforumationnamedpipes.readValue("positive_prompt")
                self.positivePrompt2 = ""
                self.negativePrompt1 = self.deforumationnamedpipes.readValue("negative_prompt")

        self.parent.ui.prompt1.setPlainText(self.positivePrompt1)
        self.parent.ui.prompt2.setPlainText(self.positivePrompt2)
        self.parent.ui.negative_prompt.setPlainText(self.negativePrompt1)
        self.prompt_1_weight = float(self.deforumationnamedpipes.readValue("positive_prompt_weight_1"))
        self.prompt_2_weight = float(self.deforumationnamedpipes.readValue("positive_prompt_weight_2"))
        if self.prompt_1_weight == 1.0 and self.prompt_2_weight == 1.0:
            self.current_prompt_weight = 0
        elif self.prompt_1_weight - self.prompt_2_weight > 0:
            self.current_prompt_weight = -int(((self.prompt_1_weight - self.prompt_2_weight)) * 100)
        else:
            self.current_prompt_weight = int(((self.prompt_2_weight - self.prompt_1_weight)) * 100)
        self.parent.ui.morph_slider.setValue(self.current_prompt_weight)
        conf = self.deforumation_settings.getSendConfig()
        if self.use_deforumation_prompts or (self.positivePrompt1 == "" and self.positivePrompt2 == ""):
            if "positive_prompt_1" in conf:
                self.positivePrompt1 = conf["positive_prompt_1"]
            if "positive_prompt_2" in conf:
                self.positivePrompt2 = conf["positive_prompt_2"]
            if "negative_prompt" in conf:
                self.negativePrompt1 = conf["negative_prompt"]

        self.saveCurrentPrompt()

    def saveCurrentPrompt(self, prompt_weight = 0):
        self.positivePrompt1 = self.parent.ui.prompt1.toPlainText().replace('\n', ' ')
        self.positivePrompt1_modified = self.replace_with_prompt_morph_bindings(self.positivePrompt1)
        self.positivePrompt2 = self.parent.ui.prompt2.toPlainText().replace('\n', ' ')
        self.positivePrompt2_modified = self.replace_with_prompt_morph_bindings(self.positivePrompt2)
        self.negativePrompt1 = self.parent.ui.negative_prompt.toPlainText().replace('\n', ' ')
        self.negativePrompt1_modified = self.replace_with_prompt_morph_bindings(self.negativePrompt1)
        self.deforumationnamedpipes.writeValue("positive_prompt_1", self.positivePrompt1)
        self.deforumationnamedpipes.writeValue("positive_prompt_2", self.positivePrompt2)
        self.deforumationnamedpipes.writeValue("negative_prompt_1", self.negativePrompt1)
        #if self.positivePrompt2_modified:
        #    return

        if self.parent.ui.prompt1.toPlainText() != "" and self.parent.ui.prompt2.toPlainText() != "":
            if self.current_prompt_weight != 0:
                #positive_first_prompt = "(" + self.positivePrompt1_modified + ":" + str(self.prompt_1_weight) + ")"
                positive_first_prompt = "(" + self.positivePrompt1 + ":" + str(self.prompt_1_weight) + ")"
                #second_first_prompt = "(" + self.positivePrompt2_modified + ":" + str(self.prompt_2_weight) + ")"
                second_first_prompt = "(" + self.positivePrompt2 + ":" + str(self.prompt_2_weight) + ")"
                totalPossitivePromptString = positive_first_prompt + "," + second_first_prompt
            else:
                #totalPossitivePromptString = self.positivePrompt1_modified + "," + self.positivePrompt2_modified
                totalPossitivePromptString = self.positivePrompt1 + "," + self.positivePrompt2
                self.deforumationnamedpipes.writeValue("positive_prompt_weight_1", 1.0)
                self.deforumationnamedpipes.writeValue("positive_prompt_weight_2", 1.0)
        elif self.parent.ui.prompt1.toPlainText() != "":
            #totalPossitivePromptString = self.positivePrompt1_modified #self.parent.ui.prompt1.toPlainText().replace('\n', ' ')
            totalPossitivePromptString = self.positivePrompt1
        elif self.parent.ui.prompt2.toPlainText() != "":
            #totalPossitivePromptString = self.positivePrompt2_modified #self.parent.ui.prompt2.toPlainText().replace('\n', ' ')
            totalPossitivePromptString = self.positivePrompt2
        else:
            totalPossitivePromptString = ""
        #print("Current pos prompt is:" + totalPossitivePromptString)
        #print("Current neg prompt is:" + self.negativePrompt1)
        prompts = {}
        prompts["positive_prompt_1"] = self.parent.ui.prompt1.toPlainText() #self.positivePrompt1_modified
        prompts["positive_prompt_2"] = self.parent.ui.prompt2.toPlainText() #self.positivePrompt2_modified
        prompts["negative_prompt"] = self.parent.ui.negative_prompt.toPlainText() #self.negativePrompt1_modified
        self.deforumation_settings.writeDeforumSendValuesToConfig(prompts)
        self.deforumationnamedpipes.writeValue("positive_prompt", totalPossitivePromptString)
        self.deforumationnamedpipes.writeValue("negative_prompt", self.negativePrompt1_modified)
        self.deforumationnamedpipes.writeValue("prompts_touched", 1)



    def set_prompt_morph_input_text(self, item):
        self.deforumation_tools.propagateAllComponents(item) #self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value,
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len(orgName)-1:])
        if orgName.startswith("morph_prompt_max"):
            if self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.value() > int(float(item.text()) * 100):
                print("Current slider:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.objectName()) + " its value:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.value()) + " is greater than:" + str(int(float(item.text()) * 100)))
                self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.setValue(int(float(item.text()) * 100))
            self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.setMaximum(int(float(item.text())*100))
            self.deforumation_tools.propagateAllComponents(item, int(float(item.text()) * 100))
            self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider, int(float(item.text()) * 100), onlySetSizes=True)
            print("Slider:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.objectName()) + " has max:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.maximum()))
        elif orgName.startswith("morph_prompt_min"):
            if self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.value() < int(float(item.text())*100):
                print("Current slider:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.objectName()) + " its value:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.value()) + " is smaller than:" + str(int(float(item.text())*100)))
                self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.setValue(int(float(item.text())*100))
            self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.setMinimum(int(float(item.text())*100))
            self.deforumation_tools.propagateAllComponents(item, int(float(item.text()) * 100))
            self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider, int(float(item.text()) * 100), onlySetSizes = True)
            print("Slider:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.objectName()) + " has min:" + str(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.minimum()))
        elif orgName.startswith("morph_prompt_value"):
            wanted_value = int(float(item.text())*100)
            if wanted_value > self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.maximum():
                wanted_value = int(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.maximum())
                self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.setText(str('%.2f' % float(wanted_value / 100)))
                self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value)
            elif wanted_value < self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.minimum():
                wanted_value = int(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.minimum())
                self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.setText(str('%.2f' % float(wanted_value / 100)))
                self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value)
            self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider.setValue(wanted_value)
            self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider, wanted_value)
        #self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.setText(str('%.2f' % float(item.value() / 100)))
        elif orgName.startswith("morph_promptA") or orgName.startswith("morph_promptB"):
            binding = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_binding.text()
            promptA = self.prompt_morphing_container[morph_prompt_identifier].morph_promptA.text()
            promptB = self.prompt_morphing_container[morph_prompt_identifier].morph_promptB.text()
            self.deforumationnamedpipes.writeValue("set_prompt_morph_values_" + str(binding), [promptA, promptB, None, None, None])


        self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph_prompt_identifier])
        self.saveCurrentPrompt()
    def savePromptMorphFrameToConfig(self, morph_frame):
        self.deforumation_settings.writeDeforumPromptMorphValuesToConfig(str(morph_frame.identifier), [int(morph_frame.morph_prompt_enabled), int(morph_frame.morph_prompt_smooth_motion_enabled), int(morph_frame.isPromptBlending),morph_frame.morph_prompt_binding.text(), morph_frame.morph_promptA.text(),morph_frame.morph_promptB.text(),morph_frame.morph_prompt_min.text(),morph_frame.morph_prompt_max.text(),morph_frame.morph_prompt_value.text()])

    def remove_prompt_morph_frame(self, item):
        #print("Removing Frame:" + str(item.objectName()))
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_frame"):])
        self.prompt_morphing_container[morph_prompt_identifier].remove_prompt_morph_frame()
        self.parent.deforumationwidgets.removeWidgetAndItsChildren(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_frame)
        self.deforumation_settings.deletePromtMorphConfigKey(str(morph_prompt_identifier))
        #del self.prompt_morphing_container[morph_prompt_identifier]
        binding = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_binding.text()
        del self.prompt_morphing_container[morph_prompt_identifier]
        #self.numberOfPromptMorphFrames -= 1
        self.deforumation_settings.writeDeforumPromptMorphValuesToConfig()
        self.saveCurrentPrompt()
        self.deforumationnamedpipes.writeValue("deforumation_prompt_morph_remove_" + str(binding), 1)


    def remove_all_prompt_morph_frames(self):
        prompt_morphing_container_copy = self.prompt_morphing_container.copy()
        for morph_index in prompt_morphing_container_copy:

            #morph_frame = self.prompt_morphing_container[int(morph_index)]
            self.prompt_morphing_container[int(morph_index)].remove_prompt_morph_frame()
            self.parent.deforumationwidgets.removeWidgetAndItsChildren(self.prompt_morphing_container[int(morph_index)].morph_prompt_frame)
            self.deforumation_settings.deletePromtMorphConfigKey(str(morph_index))
            del self.prompt_morphing_container[int(morph_index)]
        self.numberOfPromptMorphFrames = 0
        self.deforumation_settings.writeDeforumPromptMorphValuesToConfig()
        self.saveCurrentPrompt()

    def set_prompt_morph_type(self, item):
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_blending_checkbox"):])
        new_checked_status = not item.isChecked()
        print("item checked: " + str(new_checked_status))
        self.prompt_morphing_container[morph_prompt_identifier].set_prompt_morphing_type(new_checked_status)
        self.deforumation_tools.propagateAllComponents(item)#, new_checked_status)
        self.resizeEvent_morph_frames(self.parent.ui.right_prompt_tab_frame.width())
        self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph_prompt_identifier])
        self.saveCurrentPrompt()
    def resizeEvent_morph_frames(self, verticalFrame_prompt_width):
        for morphing_frame in self.prompt_morphing_container:
            self.prompt_morphing_container[morphing_frame].resizeEvent_morph_frame(verticalFrame_prompt_width)

    def adjustSyrupPromptMorphProgressBars(self, promptMorphMotionValues):
        for promtMorph in self.prompt_morphing_container:
            binding = self.prompt_morphing_container[promtMorph].morph_prompt_binding.text()
            progbar = self.prompt_morphing_container[promtMorph].morph_prompt_progressbar
            morph_prompt_progress_value = self.prompt_morphing_container[promtMorph].morph_prompt_progress_value
            foundBinding = False
            for morphorph_binding in promptMorphMotionValues:
                if morphorph_binding[0] == binding:
                    currentStepPromptMorph = morphorph_binding[1]
                    totalStepPromptMorph = morphorph_binding[2]
                    currentStepPromptMorphValue = morphorph_binding[3]
                    progressPM = int(100 / totalStepPromptMorph * currentStepPromptMorph)
                    progbar.setValue(progressPM)
                    morph_prompt_progress_value.setText(str('%.2f' % float(currentStepPromptMorphValue)))
                    #self.ui.pan_z_value_progress.setText(str('%.2f' % self.Translation_Z))
                    foundBinding = True
                    break
            if foundBinding == False:
                progbar.setValue(100)
                current_value = float(self.prompt_morphing_container[promtMorph].morph_prompt_value.text())
                morph_prompt_progress_value.setText(str('%.2f' % float(current_value)))

    def replace_with_prompt_morph_bindings(self, promptItem):
        modified_prompt = promptItem
        for morphFrame in self.prompt_morphing_container:
            is_enabled = self.prompt_morphing_container[morphFrame].morph_prompt_enabled
            if not is_enabled:
                continue
            binding = self.prompt_morphing_container[morphFrame].morph_prompt_binding.text()
            #print("Binding:" + str(binding))
            if binding == "":
                continue
            if self.prompt_morphing_container[morphFrame].isPromptBlending:
                promptA = self.prompt_morphing_container[morphFrame].morph_promptA.text()
                promptB = self.prompt_morphing_container[morphFrame].morph_promptB.text()
                shouldContinue = True
                if promptA == "":
                    #print("No promptA found for morphFrame " + "{{" + str(binding) + "}}")
                    shouldContinue = False
                if promptB == "":
                    #print("No promptB found for morphFrame " + "{{" + str(binding) + "}}")
                    shouldContinue = False
                if shouldContinue == False:
                    modified_prompt = modified_prompt.replace("{{" + binding + "}}", "")
                    #print("Modified text:" + str(modified_prompt))
                    continue
                prompt_value = self.prompt_morphing_container[morphFrame].morph_prompt_value.text()
                substituedText = "[" + promptB + ":" + promptA + ":" + str(prompt_value) + "]"
                #print("Substituting {{" + str(binding) + "}}, with " + str(substituedText))
            else:
                promptA = self.prompt_morphing_container[morphFrame].morph_promptA.text()
                if promptA == "":
                    #print("No promptA found for morphFrame " + "{{" + str(binding) + "}}")
                    modified_prompt = modified_prompt.replace("{{" + binding + "}}", "")
                    #print("Modified text:" + str(modified_prompt))
                    continue
                prompt_value = self.prompt_morphing_container[morphFrame].morph_prompt_value.text()
                substituedText = "(" + promptA + ":" + str(prompt_value) + ")"
                #print("Substituting {{" + str(binding) + "}}, with " + str(substituedText))
            #print("Original text:" + promptItem)
            modified_prompt = modified_prompt.replace("{{" + binding + "}}", substituedText)
            #print("Modified text:" + str(modified_prompt))

        #pattern = re.escape("\{\{.*\}\}")
        match = re.findall(r'\{\{(.*?)\}\}',modified_prompt) #re.search(pattern, modified_prompt)
        for matchings in match:
            modified_prompt = modified_prompt.replace("{{" + matchings + "}}", "")
        return modified_prompt

    def setCurrentMorphPromptWeightValueOnly(self, item):
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_slider"):])
        correct_morph_frame_slider_probably = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider
        if correct_morph_frame_slider_probably != item:
            # Something very fish happened here, and we need to find the correct morph frame manually
            for morph in self.prompt_morphing_container:
                if self.prompt_morphing_container[morph].morph_prompt_slider == item:
                    morph_prompt_identifier = int(morph)
                    break
        self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.setText(str('%.2f' % float(item.value() / 100)))
    def setCurrentMorphPromptWeight(self, item):
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_slider"):])
        correct_morph_frame_slider_probably = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_slider
        if correct_morph_frame_slider_probably != item:
            #Something very fish happened here, and we need to find the correct morph frame manually
            for morph in self.prompt_morphing_container:
                if self.prompt_morphing_container[morph].morph_prompt_slider == item:
                    morph_prompt_identifier = int(morph)
                    break
        self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.setText(str('%.2f' % float(item.value()/100)))
        binding_text = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_binding.text()
        self.pmval = self.deforumationnamedpipes.readValue("deforumation_prompt_morph_value_binding_" + str(binding_text))
        if str(self.pmval) == "NONE":
            self.deforumationnamedpipes.writeValue("deforumation_prompt_morph_value_binding_" + str(binding_text), float(item.value()/100))
            self.pmval = float(item.value()/100)
        else:
            self.pmval = float(self.pmval)

        if self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_enabled:
            current_prompt_morph_component_value = float(item.value()/100)
            bezierTupple = list(((0.0, 0.0), (0, 0), (1.0, 1.0), (1.0, 1.0)))
            current_syrup_value = self.Prompt_Morph_Syrup_Value
            if self.Prompt_Morph_Syrup_Value == 0 or not self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_smooth_motion_enabled == True:
                current_syrup_value = 1
            bezierArray = pyeaze.Animator(current_value=self.pmval, target_value=(current_prompt_morph_component_value), duration=1, fps=int(current_syrup_value), easing=bezierTupple, reverse=False)

            bezierArray.values = list(np.around(np.array(bezierArray.values), 3))
            self.deforumationnamedpipes.writeValue("prepare_prompt_morph_motion_" + str(binding_text), bezierArray.values)
            promptA = self.prompt_morphing_container[morph_prompt_identifier].morph_promptA.text()
            promptB = self.prompt_morphing_container[morph_prompt_identifier].morph_promptB.text()
            isPromptBlending = self.prompt_morphing_container[morph_prompt_identifier].isPromptBlending
            is_enabled = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_enabled
            current_value = float(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.text())
            self.deforumationnamedpipes.writeValue("set_prompt_morph_values_" + str(binding_text), [promptA, promptB, isPromptBlending, is_enabled, current_value])
            self.deforumationnamedpipes.writeValue("start_prompt_morph_motion_" + str(binding_text), 1)

            #Propagation for this component is dubious
            #self.deforumation_tools.propagateAllComponents(item, item.value())
            #self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value, str('%.2f' % float(item.value()/100)))

            self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph_prompt_identifier])
            self.saveCurrentPrompt()
    def setCurrentPromptMorphSyrupValue(self, item):

        self.Prompt_Morph_Syrup_Value = item.value()
        #self.ui.syrup_pan_motion_slider.setValue(int(sender.value()))
        self.parent.ui.syrup_prompt_morph_value.setText(str(self.Prompt_Morph_Syrup_Value))
        #self.propagateAllComponents(sender, sender.value())
        #self.propagateAllComponents(self.ui.syrup_pan_motion_slider_frame_number, str(sender.value()))
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Morph_Prompt", item.value())


    def colorMorphingPromtsDependingOnEnabledStatus(self, morph_frame):
        redColor = QColor(255, 0, 0)
        whiteColor = QColor(255, 255, 255)
        greenColor = QColor(0, 255, 0)
        binding = morph_frame.morph_prompt_binding.text()
        promtWindows = [self.parent.ui.prompt1, self.parent.ui.prompt2, self.parent.ui.negative_prompt]
        for promtWindow in promtWindows:
            promtWindow.moveCursor(QTextCursor.Start)
            while promtWindow.find("{{" + binding + "}}"):
                if not morph_frame.morph_prompt_enabled:
                    promtWindow.setTextColor(redColor)
                    promtWindow.insertPlainText("{{" + binding + "}}")
                    promtWindow.setTextColor(greenColor)
                else:
                    promtWindow.setTextColor(whiteColor)
                    promtWindow.insertPlainText("{{" + binding + "}}")
                    promtWindow.setTextColor(greenColor)


    def set_prompt_morph_on_off(self, item):
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_checkbox_on_off"):])
        self.prompt_morphing_container[morph_prompt_identifier].set_prompt_morphing_on_off(not item.isChecked(), False)
        self.deforumation_tools.propagateAllComponents(item)#, item.isChecked())
        self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph_prompt_identifier])
        self.saveCurrentPrompt()
        self.colorMorphingPromtsDependingOnEnabledStatus(self.prompt_morphing_container[morph_prompt_identifier])

        promptA = self.prompt_morphing_container[morph_prompt_identifier].morph_promptA.text()
        promptB = self.prompt_morphing_container[morph_prompt_identifier].morph_promptB.text()
        isPromptBlending = self.prompt_morphing_container[morph_prompt_identifier].isPromptBlending
        is_enabled = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_enabled
        binding_text = self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_binding.text()
        current_value = float(self.prompt_morphing_container[morph_prompt_identifier].morph_prompt_value.text())
        self.deforumationnamedpipes.writeValue("start_prompt_morph_motion_" + str(binding_text), -2)
        self.deforumationnamedpipes.writeValue("set_prompt_morph_values_" + str(binding_text), [promptA, promptB, isPromptBlending, is_enabled, current_value])

    def set_prompt_morph_smooth_motion_on_off(self, item):
        orgName = self.deforumation_tools.getOriginalComponentName(item)
        morph_prompt_identifier = int(orgName[len("morph_prompt_smooth_motion_enabled_checkbox"):])
        self.prompt_morphing_container[morph_prompt_identifier].set_prompt_morphing_smooth_motion_on_off(not item.isChecked(), False)
        #self.deforumation_tools.propagateAllComponents(item)#, item.isChecked())
        self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph_prompt_identifier])
        self.saveCurrentPrompt()



    def savePromptMorphingToFile(self):
        file_name, _ = QFileDialog.getSaveFileName(self.parent, "Save current prompt bindings.", "", "Config File(*.json)")
        if file_name != "" and file_name != None:
            frame_data = {}
            index = 0
            for morph_index in self.prompt_morphing_container:
                morph_frame = self.prompt_morphing_container[morph_index]
                frame_data[index] = [int(morph_frame.morph_prompt_enabled), int(morph_frame.morph_prompt_smooth_motion_enabled), int(morph_frame.isPromptBlending), morph_frame.morph_prompt_binding.text(), morph_frame.morph_promptA.text(), morph_frame.morph_promptB.text(), morph_frame.morph_prompt_min.text(), morph_frame.morph_prompt_max.text(), morph_frame.morph_prompt_value.text()]
                index += 1
            self.deforumation_settings.writeToConfig(file_name, frame_data)

    def loadPromptMorphingFromFile(self):
        self.remove_all_prompt_morph_frames()
        file_name, _ = QFileDialog.getOpenFileName(self.parent, "Load saved prompt bindings", "", "All (*.json)")
        if file_name != "" and file_name != None:
            self.loadMorphPromptFramesFromConfig(file_name)

    def changePromptWeightByBindName(self, bindName, weight):
        for morph in self.prompt_morphing_container:
            if self.prompt_morphing_container[morph].morph_prompt_binding.text() == bindName:
                self.prompt_morphing_container[morph].morph_prompt_value.setText(str('%.2f' % float(weight)))
                self.deforumation_tools.propagateAllComponents(self.prompt_morphing_container[morph].morph_prompt_value, str('%.2f' % float(weight)))
                #self.savePromptMorphFrameToConfig(self.prompt_morphing_container[morph])
                self.saveCurrentPrompt()
                break