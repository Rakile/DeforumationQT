import os

from PySide6.QtCore import QEvent, QPoint, QMetaObject, QFileInfo, QRect, QCoreApplication
from PySide6.QtGui import QIcon, Qt, QAction, QFont
from PySide6.QtWidgets import (QFileDialog, QWidgetAction, QFrame, QDateEdit, QVBoxLayout, QLabel, QSlider, QPushButton, QTextEdit, QWidget, QDial, QScrollArea, QLineEdit, QCheckBox, QProgressBar, QComboBox, QTableView, QRadioButton)

def handleEventValueChanged(self, item):
    if item.objectName().startswith("movie_slider"):
        # self.currentSliderPosition = item.value()
        value_with_granularity = item.value() * self.VideoImageContainer.preview_compression_rate
        self.ui.movie_slider_frame_number.setText(str(value_with_granularity)) #item.value()))
        self.setMovieSlidePosition(item, item.value())
        self.currentSliderPosition = item.value()
        self.setMovieSliderFrameNumber(item, value_with_granularity)#item.value())

        # self.ui.movie_slider.setValue(item.value())
        # self.setPositionMovieFrame(item, item.value())
        # Show the frame in the preview window
        current_movie_tab_height = self.ui.preview_screen.height()
        frame_image = self.VideoImageContainer.getImage(0).getpixmap()
        frameSize = frame_image.size()
        framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_movie_tab_height
        shouldusethisheight = current_movie_tab_height
        shouldusethiswidth = framesizeScaledWidth
        self.ui.preview_image.setMaximumHeight(shouldusethisheight)
        self.ui.preview_image.setMaximumWidth(shouldusethiswidth)
        self.ui.preview_image.setPixmap(self.VideoImageContainer.getImage(0).getpixmap(False))
    elif item.objectName().startswith("syrup_pan_motion_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("syrup_rotate_motion_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("syrup_zoom_motion_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("syrup_tilt_motion_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("motion_zoom_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("motion_fov_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("step_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("strength_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("cfg_slider"):
        self.DeforumationMotions.slider_changed(item)
    elif item.objectName().startswith("cadence_slider"):
        self.DeforumationMotions.setCurrentCadenceValueOnly(item)
    elif item.objectName().startswith("noise_slider"):
        self.DeforumationMotions.slider_changed(item)

    elif item.objectName().startswith("preview_compression_slider"):
        old_compression_rate = self.VideoImageContainer.getPreviewCompression()
        old_left_frame = old_compression_rate * self.ui.movie_slider.value()
        self.VideoImageContainer.setPreviewCompression(item, self.ui.movie_slider, self.total_number_of_frames_generated)
        self.update_movie_strip(True)
        self.setMovieSlidePosition(self.ui.movie_slider_frame_number, old_left_frame) #video_frame_number)
        self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, old_left_frame) #video_frame_number)

    elif item.objectName().startswith("motion_zoom_granularity"):
        self.DeforumationMotions.set_zoom_granularity(item)
    elif item.objectName().startswith("morph_slider"):
        self.DeforumationPrompts.setCurrentPromptWeight(item)  # self.ui.morph_slider.value())
        self.DeforumationPrompts.saveCurrentPrompt()
    elif item.objectName().startswith("CN_"):
        self.DeforumationControlNets.slider_changed(item)
        #print("CN:"+str(item.value()))
    elif item.objectName().startswith("morph_prompt_slider"):
        #This function only updates the prompt morph slider value (it does not execute anything else until mouse release... See "handleMouseReleaseEvent")
        self.DeforumationPrompts.setCurrentMorphPromptWeightValueOnly(item) #slider_changed(item)
    elif item.objectName().startswith("syrup_prompt_morph_slider"):
        self.DeforumationPrompts.setCurrentPromptMorphSyrupValue(item)

    else:
        if self.is_verbose:
            print("<Not implemented yet>, Slider changed:" + str(item.objectName()))

def handleEventReturnPressed(self):
    sender = self.sender()
    if sender.objectName().startswith("movie_slider_frame_number"):
        self.setMovieSlidePosition(sender, int(sender.text()))
        self.setMovieSliderFrameNumber(sender, int(sender.text()))
    elif sender.objectName().startswith("syrup_pan_motion_slider_frame_number"):
        self.DeforumationMotions.setSyrupPanningMotion(int(sender.text()))
    elif sender.objectName().startswith("syrup_zoom_motion_slider_frame_number"):
        self.DeforumationMotions.setSyrupZoomingMotion(int(sender.text()))
    elif sender.objectName().startswith("syrup_rotate_motion_slider_frame_number"):
        self.DeforumationMotions.setSyrupRotationMotion(int(sender.text()))
    elif sender.objectName().startswith("syrup_tilt_motion_slider_frame_number"):
        self.DeforumationMotions.setSyrupTiltMotion(int(sender.text()))
    elif sender.objectName().startswith("replay_fps_input_box"):
        self.VideoImageContainer.saveFPStoConfig(sender)
        self.AudioWaveContainer.showAudioWave()
    elif sender.objectName().startswith("crf_input_box"):
        self.VideoImageContainer.saveCRFtoConfig(sender)
    elif sender.objectName().startswith("amplitude_value_box") or sender.objectName().startswith("shift_value_box") or sender.objectName().startswith("ampshift_value_box") or sender.objectName().startswith("shift_leftright_value_box"):
        self.AudioWaveContainer.clicked_button(sender)

    elif sender.objectName().startswith("metronome_trigger_over_value_box") or sender.objectName().startswith("metronome_trigger_under_value_box"):
        self.AudioWaveContainer.clicked_metronome_button(sender)
    else:
        if self.is_verbose:
            print("<NOT IMPLEMENTED YET, Pressed return>:" + str(sender.objectName()))

def handleMouseReleaseEvent(self, object, event):
    if event.type() == QEvent.MouseButtonRelease:
        if object.objectName().startswith("morph_prompt_slider"):
            self.DeforumationPrompts.setCurrentMorphPromptWeight(object)
        elif object.objectName().startswith("cadence_slider"):
            self.DeforumationMotions.slider_changed(object)
            if self.ui.cadence_audio_line_show_checkbox.isChecked():
                self.AudioWaveContainer.showAudioWave(shouldUpdateAll=True)


def handleEvent(self, object, event):
    #This is for restoring icons in a strange way, and should be removed in further release
    #if object.objectName() == "iter_RadioButton":
    #print("Action:" + str(event.type()) + "    --  Object Name:" + str(object.objectName()))
    #if event.type() == QEvent.ContextMenu:
    #    print("Action!!!:" + str(event.type()) + "    --  Object Name!!!:" + str(object.objectName()))

    if (event.type() == QEvent.Wheel): #  This part is a *HACK* and is only here to prevent the scroll-wheel to work when hovering the mouse over a Prompt Morph Slider (the slider value can thus only be changed by dragging the slider).
        #print("Mouse WHEEL! " + str(object.objectName()))
        if object.objectName().startswith("morph_prompt_slider"):
            QCoreApplication.sendEvent(self.ui.scrollArea_Prompt_Morph_bindings.verticalScrollBar(), event)
            return True
        elif object.objectName().startswith("cadence_slider"):
            self.DeforumationMotions.slider_changed(object)
            if self.ui.cadence_audio_line_show_checkbox.isChecked():
                self.AudioWaveContainer.showAudioWave(shouldUpdateAll=True)


    if object.objectName() in self.deforumationwidgets.getWidgetContainer():
        # print("Object Name:" + str(object.objectName()))
        if event.type() == QEvent.Enter and type(object) == QPushButton:
            if self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon != None:
                if self.deforumationwidgets.getWidgetContainer()[object.objectName()].isActivated == False:
                    object.setIcon(self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon.pixmap(object.iconSize(), QIcon.Normal, QIcon.On))
                # print("Icon On:" + str(object.icon))
        elif event.type() == QEvent.Leave and type(object) == QPushButton:
            if self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon != None:
                if self.deforumationwidgets.getWidgetContainer()[object.objectName()].isActivated == False:
                    object.setIcon(self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon.pixmap(object.iconSize(), QIcon.Normal, QIcon.Off))
                # print("Icon Off:" + str(object.icon))
        # self.ui.cookie_button.setIcon(QPixmap(u"images/pan_right_on.png"))

    #Handle "lost focus" on mainly QLineEdit components
    handleFocusOut(self, object, event)
    #Handle mouse button press events
    handleMouseButtonPress(self, object, event)
    #Handle mouse button release events
    handleMouseButtonRelease(self, object, event)
    #Handle context menu (popup menu)
    handleContextMenu(self, object, event)
    #Handle Mouse Release event
    handleMouseReleaseEvent(self, object, event)

    return False

def handleContextMenu(self, object, event):
    if (object.objectName().startswith("prompt1") or object.objectName().startswith("prompt2") or object.objectName().startswith("negative_prompt")) and event.type() == QEvent.MouseButtonPress:
        if event.button() == Qt.RightButton:
            #print("AAAPRROROROMMPPT:" +str(object.objectName()) + str(event.type()))
            popMenu = None
            if object.objectName().startswith("prompt1"):
                popMenu = self.popMenu_prompt1
            elif object.objectName().startswith("prompt2"):
                popMenu = self.popMenu_prompt2
            elif object.objectName().startswith("negative_prompt"):
                popMenu = self.popMenu_negative1

            if popMenu != None:
                menuPosition = object.mapToGlobal(event.pos())
                # print("Show context menu")
                popMenu.clear()

                #popMenu.setStyleSheet(u"QMenu {border: 10px; border-radius: 0px;} QFrame {border: 0px; border-radius: 0px;}")
                # Create a custom widget to hold the actions
                containerWidget = QWidget()
                containerLayout = QVBoxLayout()
                containerLayout.setSpacing(0)
                containerLayout.setObjectName(u"verticalLayout_rsdffdsf")
                containerLayout.setContentsMargins(0, 0, 0, 0)
                # Add actions to the container widget
                #popMenu = QMenu(self.ui.prompt2)
                #popMenu.setMask(QRect(0, 0, 800, 800))
                popMenu.setStyleSheet(u"QMenu {border: 0px;}")
                morphPromptMenuLabelStyle = u"QLabel {\n    background-color: rgb(220,220,220); /* Matching the tab's base color */\n     color: rgb(0,0,0);\n    border-left: 0px solid rgb(220,220,220);\n    border-right: 0px solid rgb(220,220,220);\n    border-top: 0px solid rgb(220,220,220);\n    border-bottom: 2px solid rgb(220,220,220);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(150,150,200); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n	border:0\n}"
                morphPromptMenuStandardLabelStyleFinal = u"QLabel {\n    background-color: rgb(50,50,50); /* Matching the tab's base color */\n     color: rgb(220,220,220);\n    border-left: 0px solid rgb(50,50,50);\n    border-right: 0px solid rgb(50,50,50);\n    border-top: 0px solid rgb(50,50,50);\n    border-bottom: 2px solid rgb(180,140,180);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(80,80,140); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(80,80,140); /* Similar to the selected tab color */\n	border:0\n}"
                morphPromptMenuStandardLabelStyle = u"QLabel {\n    background-color: rgb(50,50,50); /* Matching the tab's base color */\n     color: rgb(220,220,220);\n    border-left: 0px solid rgb(50,50,50);\n    border-right: 0px solid rgb(50,50,50);\n    border-top: 0px solid rgb(50,50,50);\n    border-bottom: 2px solid rgb(50,50,50);\n	border-radius:0;\n    padding:0;\n}\n\nQLabel:hover {\n    background-color: rgb(80,80,140); /* Matching the tab's base color */\n    color: rgb(0, 100, 0); /* Matching the tab's base color */\n    color: rgb(0,0,0);\n	border:0\n}\n\nQLabel:pressed {\n    background-color: rgb(80,80,140); /* Similar to the selected tab color */\n	border:0\n}"
                # First add cut and paste in the menu
                standardtextedititems = ["Cut", "Copy", "Paste"]
                for standarditem in standardtextedititems:
                    self.anItem = QLabel()
                    self.anItem.setText(standarditem)
                    self.anItem.setObjectName(u"morph_standard_" + standarditem)
                    self.anItem.setGeometry(QRect(0, 0, 100, 40))
                    font12 = QFont()
                    font12.setPointSize(11)
                    self.anItem.setFont(font12)
                    if standarditem != "Paste":
                        self.anItem.setStyleSheet(morphPromptMenuStandardLabelStyle)
                    else:
                        self.anItem.setStyleSheet(morphPromptMenuStandardLabelStyleFinal)

                    self.anItem.mousePressEvent = lambda event, item=standarditem, popMenu=popMenu: self.mousePressEventMorphPromptLabelStandard(event, item, popMenu)
                    containerLayout.addWidget(self.anItem)

                for index in self.DeforumationPrompts.prompt_morphing_container:
                    item = self.DeforumationPrompts.prompt_morphing_container[index]

                    if item.morph_prompt_binding.text() != "":
                        self.prompt_morph_binding_action_label = QLabel()
                        self.prompt_morph_binding_action_label.setObjectName(u"morph_choice"+str(item))
                        self.prompt_morph_binding_action_label.setGeometry(QRect(0, 0, 100, 40))
                        font12 = QFont()
                        font12.setPointSize(11)
                        self.prompt_morph_binding_action_label.setFont(font12)
                        self.prompt_morph_binding_action_label.setStyleSheet(morphPromptMenuLabelStyle)

                        self.prompt_morph_binding_action_label.setText(item.morph_prompt_binding.text())
                        self.prompt_morph_binding_action_label.mousePressEvent =  lambda event, item=item, popMenu=popMenu : self.mousePressEventMorphPromptLabel(event, item, popMenu)
                        containerLayout.addWidget(self.prompt_morph_binding_action_label)

                containerWidget.setLayout(containerLayout)
                # Create a scroll area and add the container widget to it
                scrollArea = QScrollArea()
                scrollArea.setStyleSheet("QScrollArea {border: 0px;}")
                scrollArea.setWidgetResizable(True)
                scrollArea.setWidget(containerWidget)
                scrollArea.setMinimumWidth(200)
                scrollArea.setMaximumHeight(600)
                # Create a QWidgetAction and set the scroll area as its default widget
                scrollWidgetAction = QWidgetAction(popMenu)
                scrollWidgetAction.setDefaultWidget(scrollArea)
                popMenu.addAction(scrollWidgetAction)
                # point = event.globalPos()
                popMenu.popup(menuPosition)
    if event.type() == QEvent.ContextMenu and (object.objectName() == "Movement_Tab" or object.objectName() == "Misc_Tab_A" or object.objectName() == "Misc_Tab_B" or object.objectName() == "Slider_Tab" or object.objectName() == "Settings_Tab" or object.objectName().startswith("prompt")):

        if self.noMoreMovement == 0:
            if self.skipContextMenu == False:
                menuPosition = object.mapToGlobal(event.pos())
                popMenu = None
                if object.objectName() == "Movement_Tab":
                    popMenu = self.popMenu_movement_tab
                elif object.objectName() == "Misc_Tab_A":
                    popMenu = self.popMenu_misc_a_tab
                elif object.objectName() == "Misc_Tab_B":
                    popMenu = self.popMenu_misc_b_tab
                elif object.objectName() == "Slider_Tab":
                    popMenu = self.popMenu_slider_tab
                elif object.objectName() == "Settings_Tab":
                    popMenu = self.popMenu_settings_tab
                if popMenu != None:
                    # print("Show context menu")
                    popMenu.clear()
                    # Create a custom widget to hold the actions
                    containerWidget = QWidget()
                    containerLayout = QVBoxLayout()
                    # Add actions to the container widget
                    for item in self.deforumationwidgets.getWidgetContainer():
                        # print(str(item))
                        if item.endswith("_poppable"):
                            action = QAction(item, self)
                            action.triggered[()].connect(lambda chk=False, item=item: self.printItem(self.deforumationwidgets.getWidgetContainer()[item].widget, popMenu))
                            button = QPushButton(item[:len(item) - 9])
                            button.setStyleSheet(u"QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 5px; /* Consistent with the tab's rounded corners */\n    padding: 6px 12px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n    transition: background-color 0.3s, transform 0.2s; /* Smooth transition for hover and press effects */\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n    cursor: pointer; /* Changes cursor to a hand symbol to indicate it's clickable */\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n    transform: translateY(2px); /* Gives a feeling of being pressed down */\n}\n")
                            button.clicked.connect(action.trigger)
                            if self.deforumationwidgets.getWidgetContainer()[item].icon != None:
                                button.setIcon(self.deforumationwidgets.getWidgetContainer()[item].icon)
                                button.setLayoutDirection(Qt.RightToLeft)
                            containerLayout.addWidget(button)

                    containerWidget.setLayout(containerLayout)
                    # Create a scroll area and add the container widget to it
                    scrollArea = QScrollArea()
                    scrollArea.setWidgetResizable(True)
                    scrollArea.setWidget(containerWidget)
                    scrollArea.setMinimumWidth(300)
                    scrollArea.setMaximumHeight(400)
                    # Create a QWidgetAction and set the scroll area as its default widget
                    scrollWidgetAction = QWidgetAction(popMenu)
                    scrollWidgetAction.setDefaultWidget(scrollArea)
                    popMenu.addAction(scrollWidgetAction)
                    # point = event.globalPos()
                    popMenu.popup(menuPosition)
            else:
                # print("Restoring skipContextMenu")
                self.skipContextMenu = False
    elif event.type() == QEvent.ContextMenu and  object.objectName().startswith("prompt_modifier_table"):
        pos = event.pos()
        pos_new = QPoint(pos.x(), pos.y() - 24)
        index = self.table.indexAt(pos_new)
        print(f"Clicked position: {pos}, Index: {index.row()}, {index.column()}")  # Debug print

        # Check if the index is valid and the click is not on the header
        if index.isValid() and index.row() >= 0:
            if index.column() == 0:
                row = index.row() + 1
                label = f"X{row}"
                print(label)  # Print the label of the cell
                self.model.removeRow(index.row())
                widgetContainer = self.deforumationwidgets.getWidgetContainer()
                if "X" + str(row)+"_slider" in widgetContainer:
                    widget = widgetContainer["X" + str(row)+"_slider"].widget
                    self.deforumationwidgets.removeWidgetAndItsChildren(widget)
            else:
                row = index.row() +1
                model = self.table.model()
                text = str(model.data(index, Qt.DisplayRole))
                label = f"You are clicking on row: X{row} with text: {text}"
                print(label)  # Print the label of the cell
        else:
            print("Clicked outside the item bounds or on the header")
    elif event.type() == QEvent.ContextMenu and object.objectName().startswith("morph_prompt_frame") and type(object) == QFrame:
        self.DeforumationPrompts.remove_prompt_morph_frame(object)


    # elif event.type() == QEvent.MouseButtonRelease:
    #    print("R Release")


def handleFocusOut(self, object, event):
    if event.type() == QEvent.Type.FocusOut:
        if type(object) == QLineEdit:
            if object.objectName().startswith("replay_fps_input_box"):
                self.VideoImageContainer.saveFPStoConfig(object)
                self.AudioWaveContainer.showAudioWave()
            elif object.objectName().startswith("crf_input_box"):
                self.VideoImageContainer.saveCRFtoConfig(object)
            elif object.objectName().startswith("motion_") and "_granularity" in object.objectName():
                self.DeforumationMotions.setMotionGranularity(object)
            elif object.objectName().startswith("pathToAudioFile_value"):
                self.VideoImageContainer.setPathToAudioFile()
            elif object.objectName().startswith("pathToFFMPEG_value"):
                self.VideoImageContainer.setPathToFFMPEG()
            elif object.objectName().startswith("replay_from_input_box"):
                if object.text().isdigit():
                    self.VideoImageContainer.setFFmpegIN(object)
                else:
                    object.setText("-1")
                    self.VideoImageContainer.setFFmpegIN(object)
                    object.setText("")
            elif object.objectName().startswith("replay_to_input_box"):
                if object.text().isdigit():
                    self.VideoImageContainer.setFFmpegOUT(object)
                else:
                    object.setText("-1")
                    self.VideoImageContainer.setFFmpegOUT(object)
                    object.setText("")
            elif object.objectName().startswith("morph_prompt_binding") or object.objectName().startswith("morph_promptA") or object.objectName().startswith("morph_promptB") or object.objectName().startswith("morph_prompt_min") or object.objectName().startswith("morph_prompt_max") or object.objectName().startswith("morph_prompt_step") or object.objectName().startswith("morph_prompt_value"):
                self.DeforumationPrompts.set_prompt_morph_input_text(object)
            elif object.objectName().startswith("amplitude_value_box") or object.objectName().startswith("shift_value_box") or object.objectName().startswith("ampshift_value_box") or object.objectName().startswith("shift_leftright_value_box"):
                self.AudioWaveContainer.clicked_button(object, event)
            elif object.objectName().startswith("metronome_trigger_over_value_box") or object.objectName().startswith("metronome_trigger_under_value_box"):
                self.AudioWaveContainer.clicked_metronome_button(object, event)
            else:
                if self.is_verbose:
                    print("<Not implemented yet>, FocusOut:" + str(object.objectName()))


def handleMouseButtonPress(self, object, event):
    if event.type() == QEvent.MouseButtonPress:

        if event.button() == Qt.LeftButton:
            ######################################################################################################################################################################################################
            # LEFT MOUSE-CLICK PRESS EVENTS
            ##############################################################################################
            sender = object
            ########################################################################################################################################################
            if self.noMoreMovement == 0:  # If 0, then we can move the widget
                # sender.mousePressEvent = lambda event, w=widget: self.mousePressEventWidgetButton2(event, w)
                if not self.component_is_being_dragged and event.button() == Qt.LeftButton:
                    #print("Actual widget:" + str(sender.objectName()))
                    if sender.objectName() != "MainWindow":
                        if 'poppable' not in sender.parentWidget().objectName():
                            name = sender.objectName()
                            if sender.hasTabletTracking():
                                self.component_is_being_dragged = True
                                # print("XWill now drag:" + str(sender.objectName()))
                                # print("No poppable parent")
                                # print("Left Button Clicked"+str(self.widgetObject.objectName()))
                                self.first_click_pos = event.scenePosition().toPoint()  # event.windowPos().toPoint()
                                gp = sender.parentWidget().mapToGlobal(QPoint(0, 0))
                                self.realPos = sender.mapFromGlobal(gp) * -1
                                # print("Real position:"+str(self.realPos))
                                self.dragged_component = [sender, None]
                                sender.move(self.realPos)
                                sender.mouseMoveEvent = lambda event, w=sender: self.mouseMoveEventWidgetButton(event, w)
                                # sender.setEnabled(False)
                        else:
                            # print("Has poppable parent")
                            sender = sender.parentWidget()
                            if sender.hasTabletTracking():
                                self.component_is_being_dragged = True
                                # print("YWill now drag:" + str(sender.objectName()))
                                # print("Left Button Clicked"+str(self.widgetObject.objectName()))
                                self.first_click_pos = event.scenePosition().toPoint()  # event.windowPos().toPoint()
                                gp = sender.parentWidget().mapToGlobal(QPoint(0, 0))
                                self.realPos = sender.mapFromGlobal(gp) * -1
                                # print("Real position:"+str(self.realPos))
                                if type(object) == QSlider:
                                    self.dragged_component = [object, object.pageStep()]
                                    object.setPageStep(0)
                                    # print("Setting slider to pagestep 0")
                                else:
                                    self.dragged_component = [object, None]
                                sender.move(self.realPos)
                                object.mouseMoveEvent = lambda event, w=sender: self.mouseMoveEventWidgetButton(event, w)
                                # sender.setEnabled(False)
                    else:
                        print("Reached MainWindow")
            ########################################################################################################################################################
            if type(sender) == QPushButton:
                sender.setIcon(self.deforumationwidgets.getWidgetContainer()[sender.objectName()].icon.pixmap(sender.iconSize(), QIcon.Active, QIcon.On))
        elif event.button() == Qt.MiddleButton:
            print("Middle button clicked on:" + str(object.objectName()))
def handleMouseButtonRelease(self, object, event):
    if event.type() == QEvent.MouseButtonRelease:
        self.component_is_being_dragged = False
        if event.button() == Qt.RightButton:
            if object.objectName().startswith("motion_"):
                self.DeforumationMotions.clicked_button(event, object)
            elif object.objectName().startswith("morph_slider"):
                object.setSliderPosition(0)
                self.DeforumationPrompts.setCurrentPromptWeight(object)  # self.ui.morph_slider.value())
                self.DeforumationPrompts.saveCurrentPrompt()
            elif self.noMoreMovement == 0:
                if 'poppable' in object.objectName():
                    if self.DeforumationMotions.isComponentAduplicated(object.objectName()):
                        self.deforumationwidgets.removeWidgetAndItsChildren(object)
                        self.skipContextMenu = True
                        # print("Removed widget and blocked context menu")

                # elif self.skipContextMenu:
                #    # Set this in order for the context menu to not show when right clicking on a widget to remove it
                #    self.skipContextMenu = False
        if event.button() == Qt.LeftButton:

            ######################################################################################################################################################################################################
            # LEFT MOUSE-CLICK RELEASE EVENTS
            ##############################################################################################
            sender = object
            ########################################################################################################################################################
            if self.noMoreMovement == 0:
                # print("Original MouseMoveEvent after released:" + str(self.deforumationwidgets.getWidgetContainer()[sender.objectName()].MouseMoveEvent))
                if self.dragged_component != None:
                    if self.dragged_component[0].objectName() in self.deforumationwidgets.getWidgetContainer():
                        self.dragged_component[0].mouseMoveEvent = self.deforumationwidgets.getWidgetContainer()[self.dragged_component[0].objectName()].MouseMoveEvent
                        if self.dragged_component[1] != None:
                            # print("Restoring slider to pagestep:" + str(self.dragged_component[1]))
                            self.dragged_component[0].setPageStep(self.dragged_component[1])
                        self.dragged_component = None

            ########################################################################################################################################################
            # First see to it that the button icon returns to the "hover"-icon
            if type(sender) == QPushButton:
                sender.setIcon(self.deforumationwidgets.getWidgetContainer()[sender.objectName()].icon.pixmap(sender.iconSize(), QIcon.Normal, QIcon.On))
            # Now take care of all the functionality that entails all the buttons
            if sender.objectName() == "dissablemovements_button":
                self.noMoreMovement = 1
                for widgetName in self.deforumationwidgets.widgetContainer:
                    aWidget = self.deforumationwidgets.getWidgetContainer()[widgetName]
                    if type(aWidget.widget) == QSlider:
                        aWidget.widget.mousePressEvent = aWidget.MousePressEvent
                        aWidget.widget.mouseReleaseEvent = aWidget.MouseReleaseEvent
                        aWidget.widget.mouseMoveEvent = aWidget.MouseMoveEvent
            elif sender.objectName() == "enablemovements_button":
                self.noMoreMovement = 0
                self.enumerateAllWidgetsInAllWindows()
            elif sender.objectName() == "Save_Settings":
                self.saveAndWriteScreenPositionToConfigFile()
            elif sender.objectName() == "Save_Settings_To_File":
                self.saveAndWriteScreenPositionToOtherConfigFile()
            elif sender.objectName() == "Load_Settings_From_File":
                self.removeAllComponentsFromGui()
                QMetaObject.invokeMethod(self, "restoreFromConfigFile", Qt.QueuedConnection)
            elif sender.objectName() == "Restore_Settings":
                self.removeAllComponentsFromGui()
                QMetaObject.invokeMethod(self, "restoreComponentPosition", Qt.QueuedConnection)
                QMetaObject.invokeMethod(self, "restoreScreenPosition", Qt.QueuedConnection)

            elif sender.objectName().startswith("revert_UI_to_original"):
                self.ShouldRestoreOriginalDeforumationGui = True
                self.close()
            elif sender.objectName().startswith("refresh_controller_list"):
                self.Deforumation_Joystick.initJoystickAndKeyboardManager()
            elif sender.objectName().startswith("joystick_panning_left_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Pan_L")
            elif sender.objectName().startswith("joystick_panning_right_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Pan_R")
            elif sender.objectName().startswith("joystick_panning_up_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Pan_U")
            elif sender.objectName().startswith("joystick_panning_down_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Pan_D")
            elif sender.objectName().startswith("joystick_rotate_h_left_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Rot_H_L")
            elif sender.objectName().startswith("joystick_rotate_h_right_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Rot_H_R")
            elif sender.objectName().startswith("joystick_rotate_v_up_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Rot_V_U")
            elif sender.objectName().startswith("joystick_rotate_v_down_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Rot_V_D")
            elif sender.objectName().startswith("joystick_zoom_forwards_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Zoom_F")
            elif sender.objectName().startswith("joystick_zoom_backwards_binding_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Zoom_B")
            elif sender.objectName().startswith("joystick_tilt_cw_bind_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender,"Tilt_CW")
            elif sender.objectName().startswith("joystick_tilt_cc_bind_button"):
                self.Deforumation_Joystick.setJoystickBinding(sender, "Tilt_CC")



            # All below buttons should be dissabled while user is able to move around buttons
            elif self.noMoreMovement:
                moveableTypes = [QPushButton, QLabel, QDateEdit, QDial, QLineEdit, QCheckBox, QTextEdit, QProgressBar, QComboBox, QTableView, QRadioButton]
                if type(sender) in moveableTypes: #This is done to skip forwarding audio needle when pushing a button or other (see above "moveableTypes") component
                    self.skipSetMovieSlidePosition = True
                    #print("Setting skipSetMovieSlidePosition:" + str(sender.objectName()))
                if sender.objectName().startswith("motion_"):
                    self.DeforumationMotions.clicked_button(event, sender)
                elif sender.objectName().startswith("pan_middle_button"):
                    self.DeforumationMotions.clicked_button(event, sender)
                elif sender.objectName().startswith("rotate_middle_button"):
                    self.DeforumationMotions.clicked_button(event, sender)
                elif sender.objectName().startswith("tilt_middle_button"):
                    self.DeforumationMotions.clicked_button(event, sender)

                elif sender.objectName().startswith("goto_start_button"):
                    self.setMovieSlidePosition(self.ui.movie_slider_frame_number, 0)
                    self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, 0)
                elif sender.objectName().startswith("goto_end_button"):
                    self.setMovieSlidePosition(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
                    self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
                elif sender.objectName().startswith("stop_button"):
                    self.deforumationnamedpipes.writeValue("is_paused_rendering", True)
                elif sender.objectName().startswith("play_button"):
                    self.deforumationnamedpipes.writeValue("is_paused_rendering", False)
                elif sender.objectName().startswith("exponential_pan_motion"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "exponential_pan_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_pan_motion", False)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "exponential_pan_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_pan_motion", True)
                    self.propagateAllCheckboxes(sender, "exponential_pan_motion")
                elif sender.objectName().startswith("exponential_rotate_motion"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "exponential_rotate_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_rotate_motion", False)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "exponential_rotate_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_rotate_motion", True)
                    self.propagateAllCheckboxes(sender, "exponential_rotate_motion")

                elif sender.objectName().startswith("exponential_tilt_motion"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "exponential_tilt_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_tilt_motion", False)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "exponential_tilt_motion", False, False)
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_tilt_motion", True)
                    self.propagateAllCheckboxes(sender, "exponential_tilt_motion")
                elif sender.objectName().startswith("save_positive_prompt"):
                    self.DeforumationPrompts.saveCurrentPrompt()
                elif sender.objectName().startswith("play_preview"):
                    self.VideoImageContainer.playVideo()
                elif sender.objectName().startswith("open_Deforum_folder"):
                    path = self.VideoImageContainer.get_current_image_path()
                    if path != None:
                        path = path + '/'
                        if os.path.isdir(path):
                            os.startfile(os.path.dirname(path))
                        else:
                            print("Could not find current Deforum generation folder:" + str(path))
                    else:
                        print("No active render session.")
                elif sender.objectName().startswith("browse_ffmpeg_file"):
                    file_name, _ = QFileDialog.getOpenFileName(self, "Path to FFMPEG executable", "", "All (*.*)")
                    self.ui.pathToFFMPEG_value.setText(file_name)
                elif sender.objectName().startswith("browse_audio_file"):
                    file_name, _ = QFileDialog.getOpenFileName(self, "Open Media File", "", "Media Files (*.mp4 *.mp3 *.wav *.ogg)")
                    self.ui.pathToAudioFile_value.setText(file_name)
                elif sender.objectName().startswith("Left_Frame") or sender.objectName().startswith("Right_Frame") or sender.objectName().endswith("_Tab") or "_Tab_" in sender.objectName() or sender.objectName().startswith("audio_settings_interface") or sender.objectName().startswith("Preview_Frame"):
                    if sender.objectName().startswith("Audio_Tab") or sender.objectName().startswith("audio_settings_interface") or sender.objectName().startswith("Preview_Frame"):
                        self.skipSetMovieSlidePosition = True
                    elif not self.skipSetMovieSlidePosition and (sender.objectName().startswith("Left_Frame") or sender.objectName().startswith("Right_Frame")):
                        #print("Reached movieslider update through:" + str(sender.objectName()))
                        self.setMovieSlidePosition(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
                        self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
                    else:
                        if sender.objectName().startswith("Left_Frame") or sender.objectName().startswith("Right_Frame"):
                            #print("Setting skipSetMovieSlidePosition to False again through:" + str(sender.objectName()))
                            self.skipSetMovieSlidePosition = False
                elif sender.objectName().startswith("Create_Language_Config"):
                    file_name, _ = QFileDialog.getSaveFileName(self, "Save Language File", "", "Language Files(*.json)")
                    if file_name != "":
                        self.deforumationwidgets.extractLabelWidgetsAndAddToConfig(self, self.ui.centralwidget, self.lp)
                        self.deforumation_settings.writeToLanguageConfig(file=file_name)
                elif sender.objectName().startswith("Load_Language_Config"):
                    file_name, _ = QFileDialog.getOpenFileName(self, "Open Language File", "", "Language Files (*.json)")
                    if file_name != "":
                        self.deforumation_settings.openLanguageConfig(file=file_name)
                        self.lp = self.deforumation_settings.getLanguageConfiguaration()
                        self.deforumationwidgets.extractLabelWidgetsAndChangeToConfig(self, self.ui.centralwidget, self.lp)
                        # Write to config so that language file is used on next session
                        only_file_name = QFileInfo(file_name).fileName()
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig("language_file", "./languages/" + only_file_name)
                elif sender.objectName().startswith("Restore_To_Language"):
                    self.deforumation_settings.deleteGuiConfigKey("language_file")
                    self.deforumation_settings.writeDeforumationGuiValuesToConfig(None)  # Just write to config, no extra values should be set.
                    self.ShouldOnlyRestartDeforumationGui = True
                    self.close()
                elif sender.objectName().startswith("use_deforumation_prompt_scheduling_checkbox"):
                    if sender.isChecked():
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(False)
                    else:
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(True)
                        self.DeforumationPrompts.addPromptAfterDeforum(0)
                        self.DeforumationPrompts.addPromptBeforeDeforum(0)
                        self.ui.add_prompt_before_checkbox.setChecked(False)
                        self.ui.add_prompt_after_checkbox.setChecked(False)
                elif sender.objectName().startswith("steps_active_checkbox"):
                    self.propagateAllCheckboxes(sender, "steps_active_checkbox")
                elif sender.objectName().startswith("strength_active_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_strength", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_strength", False, True, {"strength": self.DeforumationMotions.strength})
                    self.propagateAllCheckboxes(sender, "strength_active_checkbox")
                elif sender.objectName().startswith("cfg_active_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_cfg", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_cfg", False, True, {"cfg": self.DeforumationMotions.cfg})
                    self.propagateAllCheckboxes(sender, "cfg_active_checkbox")
                elif sender.objectName().startswith("cadence_active_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_cadence", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_cadence", False, True, {"cadence": self.DeforumationMotions.cadence})
                    self.propagateAllCheckboxes(sender, "cadence_active_checkbox")
                elif sender.objectName().startswith("noise_multiplier_active_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_noise", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_noise", False, True, {"noise_multiplier": self.DeforumationMotions.noise_multiplier})
                    self.propagateAllCheckboxes(sender, "noise_multiplier_active_checkbox")
                elif sender.objectName().startswith("controller_mode_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_game_mode", False,  configType="gui")
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_game_mode", False,  configType="gui")
                    self.propagateAllCheckboxes(sender, "controller_mode_checkbox")
                elif sender.objectName().startswith("add_prompt_before_checkbox"):
                    if sender.isChecked():
                        self.DeforumationPrompts.addPromptBeforeDeforum(0)
                    else:
                        self.DeforumationPrompts.addPromptBeforeDeforum(1)
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(False)
                        self.ui.use_deforumation_prompt_scheduling_checkbox.setChecked(False)
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(False)
                        self.ui.use_deforumation_prompt_scheduling_checkbox.setChecked(False)
                    self.propagateAllCheckboxes(sender, "add_prompt_before_checkbox")
                elif sender.objectName().startswith("add_prompt_after_checkbox"):
                    if sender.isChecked():
                        self.DeforumationPrompts.addPromptAfterDeforum(0)
                    else:
                        self.DeforumationPrompts.addPromptAfterDeforum(1)
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(False)
                        self.ui.use_deforumation_prompt_scheduling_checkbox.setChecked(False)
                        self.DeforumationPrompts.setShouldUseDeforumationPrompts(False)
                        self.ui.use_deforumation_prompt_scheduling_checkbox.setChecked(False)
                    self.propagateAllCheckboxes(sender, "add_prompt_after_checkbox")
                elif sender.objectName().startswith("Motion_panning_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_panning", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_panning", False, True)
                elif sender.objectName().startswith("Motion_rotation_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_rotation", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_rotation", False, True)
                elif sender.objectName().startswith("Motion_zoom_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_zoom", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_zoom", False, True)

                elif sender.objectName().startswith("Motion_fow_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_fov", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_fov", False, True)
                elif sender.objectName().startswith("Motion_tilt_checkbox"):
                    if sender.isChecked():
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_use_deforumation_tilt", False, True)
                    else:
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_use_deforumation_tilt", False, True)
                elif sender.objectName().startswith("stay_on_top_checkbox"):
                    if sender.isChecked():
                        self.makeAllWindowsOnTop(False)
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, False, "should_stay_on_top", True, configType="gui")
                    else:
                        self.makeAllWindowsOnTop(True)
                        self.DeforumationMotions.setShouldUseDeforumationParameter(sender, True, "should_stay_on_top", True, configType="gui")
                elif sender.objectName().startswith("cn_udcn"):
                    if sender.isChecked():
                        self.DeforumationControlNets.switchCNcheckbox(sender, False)
                    else:
                        self.DeforumationControlNets.switchCNcheckbox(sender, True)
                elif sender.objectName().startswith("AddPromptMorp_Button"):
                    self.DeforumationPrompts.add_prompt_morph_blending_frame()
                elif sender.objectName().startswith("morph_prompt_blending_checkbox"):
                        self.DeforumationPrompts.set_prompt_morph_type(sender)
                elif sender.objectName().startswith("morph_prompt_checkbox_on_off"):
                    self.DeforumationPrompts.set_prompt_morph_on_off(sender)
                elif sender.objectName().startswith("morph_prompt_smooth_motion_enabled_checkbox"):
                    self.DeforumationPrompts.set_prompt_morph_smooth_motion_on_off(sender)
                elif sender.objectName().startswith("save_morph_data"):
                    self.DeforumationPrompts.savePromptMorphingToFile()
                elif sender.objectName().startswith("load_morph_data"):
                    self.DeforumationPrompts.loadPromptMorphingFromFile()
                elif sender.objectName().startswith("update_seed_button") or sender.objectName().startswith("update_seed_iter_n_button"):
                    self.DeforumationMotions.setSeedAndScheme(event, sender)
                elif sender.objectName().startswith("iter_RadioButton") or sender.objectName().startswith("fixed_RadioButton") or sender.objectName().startswith("random_RadioButton") or sender.objectName().startswith("ladder_RadioButton") or sender.objectName().startswith("alternate_RadioButton") or sender.objectName().startswith("scheduled_RadioButton"):
                    self.DeforumationMotions.setSeedAndScheme(event, sender)
                elif sender.objectName().startswith("audio_synq_strength_selection") or sender.objectName().startswith("audio_synq_zoom_selection"):
                    self.AudioWaveContainer.setEditableCurve(event, sender)
                elif sender.objectName().startswith("loop_button"):
                    self.DeforumationMotions.toggleLoopBack(event, sender)
                elif sender.objectName().startswith("openWaveFileButton"):
                    self.AudioWaveContainer.openFileDialog()
                elif sender.objectName().startswith("amplitude_increase_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("amplitude_decrease_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("ampshift_increase_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("ampshift_decrease_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("shift_increase_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("shift_decrease_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("shift_left_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("shift_right_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_increase_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_decrease_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_high_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_middle_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_low_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_zero_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_org_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("change_audio_value_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("cadence_change_audio_value_button"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("editable_curve_checkbox") or sender.objectName().startswith("show_curve_checkbox"):
                    original_component_name = self.deforumationtools.getOriginalComponentName(sender)
                    self.AudioWaveContainer.handleCheckBoxes(event, sender, original_component_name)
                    #self.propagateAllCheckboxes(sender, sender.objectName())
                elif sender.objectName().startswith("metronome_trigger_over_value_checkbox") or sender.objectName().startswith("metronome_trigger_under_value_checkbox") or sender.objectName().startswith("metronome_trigger_cadence_value_checkbox"):
                    original_component_name = self.deforumationtools.getOriginalComponentName(sender)
                    self.AudioWaveContainer.handleCheckBoxesMetronome(event, sender, original_component_name)
                elif sender.objectName().startswith("audio_synq_strength_deforum_checkbox") or sender.objectName().startswith("audio_synq_zoom_deforum_checkbox") or sender.objectName().startswith("audio_synq_panlr_deforum_checkbox") or sender.objectName().startswith("audio_synq_panud_deforum_checkbox") or sender.objectName().startswith("audio_synq_rotatev_deforum_checkbox") or sender.objectName().startswith("audio_synq_rotateh_deforum_checkbox") or sender.objectName().startswith("audio_synq_tilt_deforum_checkbox"):
                    original_component_name = self.deforumationtools.getOriginalComponentName(sender)
                    self.AudioWaveContainer.handleCheckBoxesGraphSynq(event, sender, original_component_name)
                elif sender.objectName().startswith("metronome_trigger_over_value_increase_button"):
                    self.AudioWaveContainer.clicked_metronome_button(sender, event)
                elif sender.objectName().startswith("metronome_trigger_over_value_decrease_button"):
                    self.AudioWaveContainer.clicked_metronome_button(sender, event)
                elif sender.objectName().startswith("metronome_trigger_under_value_increase_button"):
                    self.AudioWaveContainer.clicked_metronome_button(sender, event)
                elif sender.objectName().startswith("metronome_trigger_under_value_decrease_button"):
                    self.AudioWaveContainer.clicked_metronome_button(sender, event)
                elif sender.objectName().startswith("cadence_audio_line_show_checkbox"):
                    original_component_name = self.deforumationtools.getOriginalComponentName(sender)
                    self.AudioWaveContainer.handleCheckBoxesMisc(event, sender, original_component_name)
                elif sender.objectName().startswith("Save_Audio_Settings"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("Load_Audio_Settings"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("Convert_MP3_to_Wave"):
                    self.AudioWaveContainer.clicked_button(sender, event)
                elif sender.objectName().startswith("AutoScroll_checkbox"):
                    self.VideoImageContainer.handleCheckBoxes(sender,event)
                elif sender.objectName().startswith("reset_current_graph_button"):
                    self.AudioWaveContainer.resetGraph()
                elif sender.objectName().startswith("delete_current_graph_button"):
                    self.AudioWaveContainer.deleteGraph()
                elif sender.objectName().startswith("create_audio_beats_button"):
                    self.AudioWaveContainer.createAudioBeat()

                else:
                    #self.skipSetMovieSlidePosition = False
                    if self.is_verbose:
                        print("<Not implemented yet>, Button clicked:" + str(object.objectName()))

        elif event.button() == Qt.MiddleButton:
            print("Middle button clicked on:" + str(object.objectName()))


