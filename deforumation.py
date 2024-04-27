# This Python file uses the following encoding: utf-8
import argparse
import math
import os
import socket
import sys
import queue
import threading
import time


from PySide6.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,QSize, Qt, QEvent, Slot, Signal, Q_ARG, QPointF, QAbstractTableModel, QModelIndex)
from PySide6.QtGui import (QColor, QIcon, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel, QSlider, QMainWindow, QPushButton, QWidget, QMenu, QScrollArea, QLineEdit, QTabBar, QFileDialog, QStackedWidget, QComboBox)
from PySide6 import QtGui
from PySide6.QtMultimedia import QAudioOutput, QMediaPlayer

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui.ui_deforumation import Ui_MainWindow
from helpers.video_image import Video_Image_Container
from helpers.audio_wave import Audio_Wave_Container
from helpers.config import Deforumation_Settings
from helpers.widget_container import  Deforumation_Widgets
if sys.platform.startswith('win'):
    from helpers.named_pipes import Deforumation_Named_Pipes
from helpers.deforumation_websockets import Deforumation_Websockets
from helpers.motions import Deforumation_Motions
from helpers.controlnet import Deforumation_ControlNet
from helpers.total_recall import Deforumation_Total_Recall
from helpers.prompts import Deforumation_Prompts
from helpers.live_values import Deforumation_Live_Values
from helpers.tools import Deforumation_Tools
from helpers.events import handleEvent, handleEventValueChanged, handleEventReturnPressed
from helpers.video_player_deforumation import Deforumation_Video_Player
from helpers.joystick import Deforumation_Joystick
ShouldRestoreOriginalDeforumationGui = False
ShouldOnlyRestartDeforumationGui = False
mediator_address = 'localhost'
mediator_port = '8766'
deforumation_address = 'localhost'
deforumation_port ='8767'
deforumation_self_address = 'localhost'
should_use_osc = False
osc_port = '5005'


class EditableTableModel(QAbstractTableModel):
    def __init__(self, data = [[]]):
        super().__init__()
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data)

    def columnCount(self, parent=None):
        return 4

    def data(self, index, role):
        if role == Qt.DisplayRole or role == Qt.EditRole:
            if index.column() == 0:
                return f"X{index.row() + 1}"
            elif index.column() >= 1:
                return self._data[index.row()][index.column() - 1]
        return None

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data[index.row()][index.column()-1] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsEnabled
        return super().flags(index) | Qt.ItemIsEditable

    def headerData(self, section, orientation, role):
        if role == Qt.DisplayRole and orientation == Qt.Horizontal:
            return ["Index", "PromptA", "Value","PromptB"][section]
        return None

    def addRow(self):
        # Append a new row with default values
        self.beginInsertRows(QModelIndex(), self.rowCount(), self.rowCount())
        self._data.append(["", 0, ""])
        self.endInsertRows()

    def removeRow(self, row, parent=QModelIndex()):
        if 0 <= row < self.rowCount():
            self.beginRemoveRows(parent, row, row)
            del self._data[row]
            self.endRemoveRows()
            return True
        return False

class widgetContainerClass():
    def __init__(self):
        self.widget = None
        self.MousePressEvent = None
        self.MouseMoveEvent = None
        self.iconOn = None
        self.iconOff = None
    def SetValues(self, object):
        self.widget = object
        self.MousePressEvent = object.mousePressEvent
        self.MouseMoveEvent = object.mouseMoveEvent
        if type(object) == QPushButton:
            if not object.icon().isNull():
                #print("Actually created icon for:"+str(object))
                self.iconOn = object.icon().pixmap(QSize(37, 41), QIcon.Normal, QIcon.On)
                self.iconOff = object.icon().pixmap(QSize(37, 41), QIcon.Normal, QIcon.Off)



class CustomTabBar(QTabBar):
    def __init__(self, detach_function, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.detach_function = detach_function

    def mouseDoubleClickEvent(self, event):
        index = self.parent.currentIndex() #self.tabAt(event.scenePosition().toPoint())#event.pos())
        if index >= 0:
            self.detach_function(index, self.parent)

class DetachableTabWidget():
    def __init__(self, parent=None, qttabwidget=None):
        self.qttabwidget = qttabwidget
        self.detachedTabs = {}
        self.detachedTabsIndexer = {}
        self.detachedTabsWindows = {}
        self.parent = parent
        # Create a new CustomTabBar instance
        custom_tab_bar = CustomTabBar(self.detachTab, qttabwidget)

        # Transfer tabs to the new CustomTabBar
        for i in range(qttabwidget.count()):
            tab_text = qttabwidget.tabText(i)
            custom_tab_bar.addTab(tab_text)

        # Replace the existing tab bar
        qttabwidget.setTabBar(custom_tab_bar)



    def detachTab(self, index, qttabwidget):
        widget = qttabwidget.widget(index)
        if widget:
            MainWindow = QMainWindow()
            self.centralwidget = QWidget(MainWindow)
            self.centralwidget.setObjectName(u"centralwidget")

            tabName = qttabwidget.tabText(index)
            widget.setParent(self.centralwidget)
            # Set new window as parent
            MainWindow.setCentralWidget(widget)
            MainWindow.setWindowTitle(tabName)
            MainWindow.setGeometry(100, 100, 400, 300)
            MainWindow.setStyleSheet(self.parent.styleSheet())
            MainWindow.show()
            widget.show()
            self.detachedTabs[MainWindow] = (index, tabName, widget)
            self.detachedTabsIndexer[widget.objectName()] = index
            self.detachedTabsWindows[widget.objectName()] = MainWindow
            MainWindow.closeEvent = lambda event: self.onDetachedWindowClose(event, MainWindow, qttabwidget)
            if self.parent.deforumationDetachedTabsAreOnTop:
                MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint, True)
                MainWindow.setVisible(False)  # Hide and then show to apply the change
                MainWindow.show()
            else:
                MainWindow.setWindowFlag(Qt.WindowStaysOnTopHint, False)
                MainWindow.setVisible(False)  # Hide and then show to apply the change
                MainWindow.show()

            self.parent.restoreAlreadyOpenedTabs(widget.objectName())



    def onDetachedWindowClose(self, event, detachedWindow, qttabwidget):
        if detachedWindow in self.detachedTabs:
            index, tabName, widget = self.detachedTabs.pop(detachedWindow)
            widget.setParent(qttabwidget)  # Restore original parent
            qttabwidget.insertTab(index, widget, tabName)
            del self.detachedTabsIndexer[widget.objectName()]
            del self.detachedTabsWindows[widget.objectName()]

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

class CustomTitleBar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QHBoxLayout()

        # You can add a label for the window title
        #self.titleLabel = QLabel("My Custom Window")
        #self.layout.addWidget(self.titleLabel)

        #self.pushButton = QPushButton("My Button")
        #self.layout.addWidget(self.pushButton)

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        #self.layout.addStretch(-1)

        # Mouse event variables
        self.parent = parent
        self.startPos = None
        self.clicking = False

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicking = True
            self.startPos = event.position().toPoint()

    def mouseMoveEvent(self, event):
        if self.clicking:
            self.parent.move(self.parent.pos() + event.position().toPoint() - self.startPos)

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.clicking = False
class MainWindow(QMainWindow):
    global ShouldRestoreOriginalDeforumationGui
    global ShouldOnlyRestartDeforumationGui

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ShouldRestoreOriginalDeforumationGui = False
        self.ShouldOnlyRestartDeforumationGui = False
        self.deforumation_settings = Deforumation_Settings(self)
        self.deforumation_settings.loadAllSentDeforumValuesFromConfigIntoParameters()

        #isOK = self.deforumation_settings.openDefaultConfig()
        isOK = self.deforumation_settings.openLanguageConfig()
        #self.p = self.deforumation_settings.getGuiConfig()
        self.lp = self.deforumation_settings.getLanguageConfiguaration()
        self.detachedPreviewWindow = None
        self.shouldExitLiveView = False
        self.shouldExitOSC = False
        self.skipLiveValues = False
        self.skipSetMovieSlidePosition = False
        self.noMoreMovement = 1
        self.currentlyShownMovieFrames = 0
        self.currentShownMovieStartIndex = 0
        self.currentSliderPosition = 0
        self.total_number_of_frames_generated = 0
        self.total_number_of_audiovideo_frames = 0
        self.current_movie_tab_width = 1
        self.current_movie_tab_height = 1
        self.exponential_pan_motion = False
        self.exponential_rotate_motion = False
        self.exponential_zoom_motion = False
        self.exponential_tilt_motion = False
        self.widgetObject_q = None
        self.widgetObject = None
        self.moveable_widget_pressed = False
        self.currentWidgetObjectInFocus = None
        self.dragXY = QPoint(0,0)
        self.deforumationMainWindowIsOnTop = False
        self.deforumationPreviewWindowIsOnTop = False
        self.deforumationDetachedTabsAreOnTop = False
        self.deforumationVideoPlayerIsOnTop = False
        self.skipContextMenu = False
        self.is_verbose = False
        self.component_is_being_dragged = False
        self.dragged_component = None
        self.shouldAutoScroll = False
        self.should_use_deforumation_game_mode = False
        self.controller_pan_x_touch_base = True
        self.controller_pan_y_touch_base = True
        self.controller_rot_h_touch_base = True
        self.controller_rot_v_touch_base = True
        self.controller_zoom_touch_base = True
        self.controller_tilt_touch_base = True
        self.CN_checkboxes_onoff = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #numberOfTabs = self.ui.tabWidget_CN.count()
        #for i in range(0, numberOfTabs):
        #    tabname = self.ui.tabWidget_CN.widget(i).objectName()
        #    print("Tab name (Control-Net): " + tabname)


        self.setCurrentTabPosition() #Need to be here ( and see main function) because else the correct tab will not show proerly

        self.window_title = self.windowTitle()
        #First thing to do is to connect to the mediator and get all present values
        if shouldUseNamedPipes:
            self.deforumationnamedpipes = Deforumation_Named_Pipes(self.deforumation_settings, self) #Start by instansing the named pipes class
        else:
            self.deforumationnamedpipes = Deforumation_Websockets(mediator_address, mediator_port, deforumation_address, deforumation_port, deforumation_self_address, self.deforumation_settings) #Start by instansing the web sockets class

        #Import OSC server
        if should_use_osc:
            self.Deforumation_OSC = Deforumation_OSC(osc_port, self.deforumation_settings, self)


        #Get total (if any) number of currently generated images
        self.total_number_of_frames_generated = int(self.deforumationnamedpipes.readValue("total_generated_images"))

        #Initialize Total Recall, which plays an important role in showing current values
        self.DeforumationTotalRecall =  Deforumation_Total_Recall(self, self.deforumationnamedpipes)

        #Set the current reference frame (containing all the current values that Deforum is using).
        self.DeforumationTotalRecall.setCurrentTotalRecallFrame(self.total_number_of_frames_generated)


        #Connect Deforumation Tab widgets that are part of the deforumation_tabWidget, and make them detachable and reattachable.
        ###########################################################################################
        self.deftabwidg = DetachableTabWidget(self, self.ui.deforumation_tabWidget)

        # Enumerate all widgets in Right_Frame tab and make them moveable (except certain ones)
        self.deforumationwidgets = Deforumation_Widgets(self, self.deforumation_settings)
        self.deforumationtools = Deforumation_Tools(self, self.deforumationwidgets)
        self.VideoImageContainer = Video_Image_Container(self, self.deforumationnamedpipes, self.deforumation_settings, self.deforumationtools)
        self.AudioWaveContainer = Audio_Wave_Container(self, self.VideoImageContainer, self.deforumation_settings, self.deforumationnamedpipes, self.deforumationtools)
        self.AudioWaveContainer.setComponetValues()
        self.DeforumationMotions = Deforumation_Motions(self, self.ui, self.deforumation_settings, self.deforumationwidgets, self.deforumationnamedpipes)
        self.DeforumationMotions.setComponetValues(self.DeforumationTotalRecall.getCurrentTotalRecallFrame())
        self.enumerateAllWidgetsInAllWindows()
        self.DeforumationControlNets = Deforumation_ControlNet(self.deforumation_settings, self, self.deforumationnamedpipes, self.deforumationtools)
        self.DeforumationControlNets.setComponetValues()
        #Special Button and widget handling
        #Test tabview############################################################
        """self.table = self.ui.prompt_modifier_table
        self.model = EditableTableModel([["", 0, ""]])
        self.table.setModel(self.model)
        self.setupSliders()
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        #sizePolicy5.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy5)
        self.table.resizeColumnsToContents()
        self.table.setColumnWidth(2, 150)  # Adjust as needed
        #self.table.setColumnWidth(3, 150)  # Adjust as needed
        self.table.installEventFilter(self)
        #self.addButton_prompt_modifier = QPushButton("Add Row")
        self.ui.addButton_prompt_modifier.clicked.connect(self.addRow)"""

        self.ui.right_prompt_tab_frame.resizeEvent = self.promt_params_frame_resizeEvent

        ########################################################################
        # Start Joystick manager
        self.Deforumation_Joystick = Deforumation_Joystick(self.deforumation_settings, self, self.DeforumationMotions)
        self.Deforumation_Joystick.initJoystickAndKeyboardManager()
        self.Deforumation_Joystick.startJoystickManager()

        #Prepare so that component windows can be popped in certain windows (for adding components)
        #self.deforumationwidgets.enumerateWidgets(self, self.ui.centralwidget)

        #Set allow adding widgets to Misc Window
        self.ui.Misc_Tab_A.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_misc_a_tab = QMenu(self.ui.Misc_Tab_A)
        self.ui.Misc_Tab_B.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_misc_b_tab = QMenu(self.ui.Misc_Tab_B)
        # Set allow adding widgets to Motion Window
        self.popMenu_movement_tab = QMenu(self.ui.Movement_Tab)
        self.ui.Movement_Tab.installEventFilter(self)
        # Set allow adding widgets to Live Value Window
        self.ui.Slider_Tab.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_slider_tab = QMenu(self.ui.Slider_Tab)
        # Set allow adding widgets to Settings Window
        self.ui.Settings_Tab.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_settings_tab = QMenu(self.ui.Settings_Tab)
        self.ui.prompt1.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_prompt1 = QMenu(self.ui.prompt1)
        #self.popMenu_prompt1.setStyleSheet(u"QMenu {    background-color: #000000; /* Light grey background */    border: 1px solid #f0f0f0; /* Slightly darker border */    padding: 1px; /* Padding around the menu */}QMenu::item {    padding: 4px 5px 4px 2px; /* Top, right, bottom, left padding */    background-color: transparent; /* Transparent background for items */    border-radius: 8px; /* Rounded corners */}QMenu::item:selected {    background-color: #000000; /* Light blue background for selected item */    color: #000000; /* Black text color */}QMenu QScrollArea {    border: none; /* No border for scroll area */}QMenu QScrollArea QWidget QWidget {    background-color: #000000; /* Light grey background for scroll area content */}QMenu QLabel {    background-color: #528252; /* Light grey background for labels */    color: #000000; /* Black text color */    padding: 0px; /* Padding for labels */}")
        self.ui.prompt2.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_prompt2 = QMenu(self.ui.prompt2)
        self.ui.negative_prompt.setContextMenuPolicy(Qt.CustomContextMenu)
        self.popMenu_negative1 = QMenu(self.ui.negative_prompt)

        #The movie tab is where the video strip is located
        self.ui.Movie_Tab.resizeEvent = self.movie_tab_resizeEvent
        #The preview tab is where the live preview image is displayed
        self.ui.Preview_Tab.resizeEvent = self.preview_tab_resizeEvent

        #Connect the tab window to event handling (save current tab index to config)
        self.ui.deforumation_tabWidget.currentChanged.connect(self.onTabIndexChange)

        #Instansiate Live Values
        self.deforumation_live_values = Deforumation_Live_Values(self, self.DeforumationTotalRecall, self.deforumationtools, self.deforumationwidgets, self.deforumationnamedpipes)
        self.deforumation_live_values.setLiveValues()

        #Start Live View thread
        CHUNK_SIZE = 1024
        BUF_MAX_SIZE = CHUNK_SIZE * 10
        self.DeforumationPrompts = Deforumation_Prompts(self, self.DeforumationTotalRecall, self.deforumationnamedpipes, self.deforumation_settings, self.deforumationwidgets, self.deforumationtools)

        #Load the currently chosen language
        self.load_language_file()

        #self.DeforumationPrompts.setCurrentPrompts()
        self.DeforumationPrompts.loadMorphPromptSyrupFromConfig()
        self.DeforumationPrompts.loadMorphPromptFramesFromConfig()
        self.DeforumationPrompts.setComponetValues()
        #self.DeforumationPrompts.shouldUseDeforumationPrompts()




        #Start the live view thread
        self.live_view_stopped = threading.Event()
        self.live_view_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
        self.liveview_t = threading.Thread(target=self.liveView, args=(self.live_view_stopped, self.live_view_q))
        self.liveview_t.start()

        if should_use_osc:
            #Start the osc server thread
            self.osc_stopped = threading.Event()
            self.osc_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
            self.osc_t = threading.Thread(target=self.osc, args=(self.live_view_stopped, self.live_view_q))
            self.osc_t.start()

        #print("Setting max value on slider to:" + str(self.total_number_of_frames_generated))
        self.ui.movie_slider.setMaximum(self.total_number_of_frames_generated)
        #self.value_changed_slider(self.ui.movie_slider)
        QMetaObject.invokeMethod(self, "update_movie_strip", Qt.QueuedConnection)

        #self.ui.deforumation_tabWidget.setMovable(True)
        self.ui.motion_syrup_progressbar_x.setValue(100)
        self.ui.motion_syrup_progressbar_y.setValue(100)

        #Handle keyboard events
        #self.eventFilter = KeyPressFilter(parent=self)
        self.installEventFilter(self)

        #Special case LoopBack Button
        self.DeforumationMotions.setLoobackButtonState()


    #def setupSliders(self):
    #    for row in range(self.model.rowCount()):
    #        self.addSliderToRow(row)

    """def addSliderToRow(self, row):
        sliderLayout = QHBoxLayout()
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(-100)
        slider.setMaximum(100)
        slider.setObjectName("X" + str(row+1)+"_slider")
        label = QLabel("0")
        slider.valueChanged.connect(lambda value, lbl=label: (lbl.setText(str(value)), self.onSliderChanged(row, value)))
        sliderLayout.addWidget(slider)
        sliderLayout.addWidget(label)
        sliderLayout.setContentsMargins(0, 0, 0, 0)

        container = QWidget()
        container.setLayout(sliderLayout)
        self.table.setIndexWidget(self.model.index(row, 2), container)
        self.deforumationwidgets.enumerateWidgets(self, self.ui.prompt_modifier_table)

    def onSliderChanged(self, row, value):
        self.model.setData(self.model.index(row, 2), value, Qt.EditRole)

    def addRow(self):
        row = self.model.rowCount()
        self.model.addRow()
        self.addSliderToRow(row)"""

    def onTabIndexChange(self, i):
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("current_tab_index", i)
    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        if self.VideoImageContainer.occupied == True:
            print("Closing Video Player.")
            if self.VideoImageContainer.player != None:
                self.VideoImageContainer.player.close()
                self.VideoImageContainer.player = None
        #Close AudioPlayer if open
        self.AudioWaveContainer.audioDataContainer.shouldPlayAudio = False
        self.AudioWaveContainer.audioDataContainer.shouldCloseAudioPlayer = True

        #Exit all dettached screens
        if self.detachedPreviewWindow != None:
            self.detachedPreviewWindow.close()
        tabWindowDict = self.deftabwidg.detachedTabsWindows.copy()
        for dtabWindows in tabWindowDict:
            self.deftabwidg.detachedTabsWindows[dtabWindows].close()

        self.shouldExitLiveView = True
        self.deforumationnamedpipes.CloseCommunicationThread()
        #Shut down any running Joystick manager
        self.Deforumation_Joystick.stopJoystickAndKeyboardManager()

        if should_use_osc:
            #Closing OSC server
            self.Deforumation_OSC.stopServer()
            self.shouldExitOSC = True
            if ShouldRestoreOriginalDeforumationGui:
                print("OSC deamon-threads behave a bit wonkey, so it might be this restart messes up.... If it does, just manually restart DMQT again.")
            index = 1
            print("Waiting for OSC")
            while self.shouldExitOSC and index < 6:
                time.sleep(1.0)
                print("." * index)
                index += 1

        event.accept()

    def osc(self, stopped, q):
        self.Deforumation_OSC.startServer()
        while self.shouldExitOSC == False:
            time.sleep(1.0)
        self.shouldExitOSC = False
        print("Exiting OSC Server")
    #This is the live view thread. It waits for incoming generated frames (generated by Deforum),
    #it then shows that frame and populates the GUI where current values are displayed
    def liveView(self, stopped, q):
        while self.shouldExitLiveView == False:
            #print("Waiting for frame from Mediator")
            #Using named pipe
            #current_frame = self.deforumationnamedpipes.waitForNewImageFromDeforum()
            #Using websockets
            current_frame = self.deforumationnamedpipes.waitForNewImageFromDeforum()
            if self.shouldExitLiveView:
                break
            #print("Current frame is:" + str(current_frame))
            imagePath = self.VideoImageContainer.get_current_image_path_f(current_frame)
            current_movie_tab_height = self.ui.preview_screen.height()
            frame_image = self.VideoImageContainer.getImage(0).getpixmap()
            frameSize = frame_image.size()
            framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_movie_tab_height
            shouldusethisheight = current_movie_tab_height
            shouldusethiswidth = framesizeScaledWidth
            self.ui.preview_image.setMaximumHeight(shouldusethisheight)
            self.ui.preview_image.setMaximumWidth(shouldusethiswidth)
            anImage = self.VideoImageContainer.getImageFromPath(imagePath)
            total_number_of_frames_generated = int(self.deforumationnamedpipes.readValue("total_generated_images"))
            if self.shouldExitLiveView:
                break
            #print("Current frame is:" + str(current_frame))
            #print("Total number of frames generated is:" + str(total_number_of_frames_generated))
            #if total_number_of_frames_generated < self.total_number_of_frames_generated:
            #    print("We are ")
            if anImage != None:
                self.ui.preview_image.setPixmap(anImage)
                if self.detachedPreviewWindow != None:
                    self.dettachedPreviewImage.setPixmap(anImage)
                self.total_number_of_frames_generated = total_number_of_frames_generated
                self.DeforumationTotalRecall.setCurrentTotalRecallFrame(self.total_number_of_frames_generated)
                if self.shouldExitLiveView:
                    break
                #print("Setting max value on slider to:" + str(self.total_number_of_frames_generated))
                self.VideoImageContainer.set_current_image_path_from_mediator()
                self.total_number_of_audiovideo_frames = self.AudioWaveContainer.currentTotalAudioVideoFrames()
                if self.total_number_of_audiovideo_frames < self.total_number_of_frames_generated:
                    self.ui.movie_slider.setMaximum(int(self.total_number_of_frames_generated/self.VideoImageContainer.getPreviewCompression()))
                else:
                    self.ui.movie_slider.setMaximum(int(self.total_number_of_audiovideo_frames / self.VideoImageContainer.getPreviewCompression()))
                # Do graphical stuff in a thread-safe way
                if not self.skipLiveValues:
                    QMetaObject.invokeMethod(self, "setLiveValues_from_thread", Qt.QueuedConnection)
                else:
                    self.skipLiveValues = False
                #Values needed have to be read from mediator here, because if done inside the invoked method it will interupt the rendering of the GUI (GUI will lag)
                panValues = self.deforumationnamedpipes.readValue(["syrup_steps_pan_x", "syrup_steps_pan_y", "translation_x", "translation_y"])
                rotationValues = self.deforumationnamedpipes.readValue(["syrup_steps_rotate_x", "syrup_steps_rotate_y", "rotation_x", "rotation_y"])
                zoomValues = self.deforumationnamedpipes.readValue(["syrup_steps_pan_z", "translation_z"])
                tiltValues = self.deforumationnamedpipes.readValue(["syrup_steps_rotate_z", "rotation_z"])
                promptMorphMotionValues = self.deforumationnamedpipes.readValue("syrup_steps_prompt_morph_motions")
                #print("promptMotionValues:" + str(promptMorphMotionValues))
                QMetaObject.invokeMethod(self, "adjustSyrupMotionProgressBar_from_thread", Qt.QueuedConnection, Q_ARG("QVariantList", panValues), Q_ARG("QVariantList", rotationValues), Q_ARG("QVariantList", zoomValues), Q_ARG("QVariantList", tiltValues), Q_ARG("QVariantList", promptMorphMotionValues))
                QMetaObject.invokeMethod(self, "update_movie_strip", Qt.QueuedConnection)
        print("Live view has been terminated")
        QMetaObject.invokeMethod(self, "close_down", Qt.QueuedConnection)

    @Slot()
    def updateAudioPlayerLine(self):
        self.AudioWaveContainer.updateAudioPlayerLine()
    @Slot()
    def showAudioWave(self):
        self.AudioWaveContainer.showAudioWave(shouldUpdateAll=True)
    @Slot()
    def setStyleSheet_to_active_safe(self):
        self.Deforumation_Joystick.currentBindingButton.setStyleSheet(u"QPushButton {\n    background-color: rgb(150, 0, 0); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
    @Slot()
    def setStyleSheet_to_normal_safe(self):
        self.Deforumation_Joystick.previousBindingButton.setStyleSheet(u"QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
        #print("Kalle")
        #identifier.setStyleSheet(styleString)
    @Slot()
    def close_down(self):
        self.close()
    @Slot() # This function is called in a thread safe way from the video_image_container. It starts the video player with the currently stitched video
    def show_media_player(self):
        #print("Starting video player")
        caller = self.VideoImageContainer
        video_size = QSize(caller.image_width, caller.image_height)
        caller.player = Deforumation_Video_Player(self, caller, video_size)
        video_path = "out.mp4"
        if not os.path.exists(video_path):
            print(f"Error: Video file not found at {video_path}")
        else:
            caller.player.load_video("out.mp4")
        self.restoreFFMPEGpreviewWindowPosition(caller.player)
        caller.player.show()
        if self.deforumationVideoPlayerIsOnTop:
            self.makeDeforumationVideoPlayerOnTop(True)
        caller.player.play_video()

    @Slot(list)
    def handler_prompt_morph(self, args):
        print("Should change prompt:" + str(args[0]) + " to:" + str(args[1]))
        self.DeforumationPrompts.changePromptWeightByBindName(args[0], args[1])

    @Slot(list, str)
    def handler(self, args, value):
        self.should_use_deforumation_game_mode = self.DeforumationMotions.should_use_deforumation_game_mode
        if args[0] == "Sampler_Steps":
            self.ui.step_slider.setValue(int(value))
        elif args[0] == "CFG_Scale":
            self.ui.cfg_slider.setValue(int(value))
        elif args[0] == "Strength":
            self.ui.strength_slider.setValue(int(round(float(value),2)*100))
        elif args[0] == "Cadence":
            self.ui.cadence_slider.setValue(int(value))
        elif args[0] == "Noise_Multiplier":
            self.ui.noise_slider.setValue(int(round(float(value),2)*100))

        elif args[0] == "Zoom":
            self.ui.pan_z_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.pan_z_value, float(value))
            self.deforumationnamedpipes.writeValue("translation_z", float(value))
            #self.ui.motion_zoom_slider.setValue(int(float(value) * 100))
        elif args[0] == "Tilt":
            self.ui.rotate_z_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.rotate_z_value, float(value))
            self.deforumationnamedpipes.writeValue("rotation_z", float(value))
        elif args[0] == "Pan_X":
            self.ui.pan_x_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.pan_x_value, float(value))
            self.deforumationnamedpipes.writeValue("translation_x", float(value))
        elif args[0] == "Pan_Y":
            self.ui.pan_y_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.pan_y_value, float(value))
            self.deforumationnamedpipes.writeValue("translation_y", float(value))
        elif args[0] == "Rot_H":
            self.ui.rotate_x_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.rotate_x_value, float(value))
            self.deforumationnamedpipes.writeValue("rotation_y", float(value))
        elif args[0] == "Rot_V":
            self.ui.rotate_y_value.setText(str('%.2f' % float(value)))
            self.DeforumationMotions.propagateAllComponents(self.ui.rotate_y_value, float(value))
            self.deforumationnamedpipes.writeValue("rotation_x", float(value))
        elif args[0] == "Pan_L" or args[0] == "Pan_R":
            if not self.should_use_deforumation_game_mode:
                # Send a faked event to the button
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_pan_x_touch_base:
                    self.controller_pan_x_touch_base = False
                    if args[0] == "Pan_L":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_pan_button_left, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_pan_button_right, mouse_event)
                elif round(float(value),2) == 0:
                    self.controller_pan_x_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_pan_button_left, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_pan_button_right, mouse_event)
            else:
                if args[0] == "Pan_L":
                    value = -abs(float(value) * float(self.ui.motion_pan_granularity.text()))
                else:
                    value = abs(float(value) * float(self.ui.motion_pan_granularity.text()))
                self.ui.pan_x_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.pan_x_value, float(value))
                self.deforumationnamedpipes.writeValue("translation_x", float(value))
        elif args[0] == "Pan_U" or args[0] == "Pan_D":
            if not self.should_use_deforumation_game_mode:
                # Send a faked event to the button
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_pan_y_touch_base:
                    self.controller_pan_y_touch_base = False
                    if args[0] == "Pan_U":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_pan_button_up, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_pan_button_down, mouse_event)
                elif round(float(value), 2) == 0:
                    self.controller_pan_y_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_pan_button_up, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_pan_button_down, mouse_event)
            else:
                if args[0] == "Pan_D":
                    value = -abs(float(value) * float(self.ui.motion_pan_granularity.text()))
                else:
                    value = abs(float(value) * float(self.ui.motion_pan_granularity.text()))
                self.ui.pan_y_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.pan_y_value, float(value))
                self.deforumationnamedpipes.writeValue("translation_y", float(value))
        elif args[0] == "Rot_H_L" or args[0] == "Rot_H_R":
            if not self.should_use_deforumation_game_mode:
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_rot_h_touch_base:
                    self.controller_rot_h_touch_base = False
                    if args[0] == "Rot_H_L":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_rotate_button_left, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_rotate_button_right, mouse_event)
                elif round(float(value), 2) == 0:
                    self.controller_rot_h_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_rotate_button_left, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_rotate_button_right, mouse_event)
            else:
                if args[0] == "Rot_H_L":
                    value = -abs(float(value) * float(self.ui.motion_rotate_granularity.text()))
                else:
                    value = abs(float(value) * float(self.ui.motion_rotate_granularity.text()))
                self.ui.rotate_x_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.rotate_x_value, float(value))
                self.deforumationnamedpipes.writeValue("rotation_y", float(value))
        elif args[0] == "Rot_V_U" or args[0] == "Rot_V_D":
            if not self.should_use_deforumation_game_mode:
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_rot_v_touch_base:
                    self.controller_rot_v_touch_base = False
                    if args[0] == "Rot_V_U":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_rotate_button_up, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_rotate_button_down, mouse_event)
                elif round(float(value), 2) == 0:
                    self.controller_rot_v_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_rotate_button_up, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_rotate_button_down, mouse_event)
            else:
                if args[0] == "Rot_V_D":
                    value = -abs(float(value) * float(self.ui.motion_rotate_granularity.text()))
                else:
                    value = abs(float(value) * float(self.ui.motion_rotate_granularity.text()))
                self.ui.rotate_y_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.rotate_y_value, float(value))
                self.deforumationnamedpipes.writeValue("rotation_x", float(value))
        elif args[0] == "Zoom_F" or args[0] == "Zoom_B":
            if not self.should_use_deforumation_game_mode:
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_zoom_touch_base:
                    self.controller_zoom_touch_base = False

                    if args[0] == "Zoom_F":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_zoom_button_forwards, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_zoom_button_backwards, mouse_event)
                elif round(float(value), 2) == 0:
                    self.controller_zoom_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_zoom_button_forwards, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_zoom_button_backwards, mouse_event)
            else:
                if args[0] == "Zoom_F":
                    value = abs(float(value) * float(self.ui.motion_zoom_granularity_special.text()))
                else:
                    value = -abs(float(value) * float(self.ui.motion_zoom_granularity_special.text()))
                self.ui.pan_z_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.pan_z_value, float(value))
                self.deforumationnamedpipes.writeValue("translation_z", float(value))
        elif args[0] == "Tilt_CW" or args[0] == "Tilt_CC":
            if not self.should_use_deforumation_game_mode:
                button_pos = QPointF(100.0, 100.0)
                if abs(round(float(value),2)) > 0.7 and self.controller_tilt_touch_base:
                    self.controller_tilt_touch_base = False
                    if args[0] == "Tilt_CW":
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_tilt_button_left, mouse_event)
                    else:
                        mouse_event = QMouseEvent(QEvent.MouseButtonRelease, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                        QCoreApplication.postEvent(self.ui.motion_tilt_button_right, mouse_event)
                elif round(float(value), 2) == 0:
                    self.controller_tilt_touch_base = True
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_tilt_button_left, mouse_event)
                    mouse_event = QMouseEvent(QEvent.Leave, button_pos, button_pos, Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
                    QCoreApplication.postEvent(self.ui.motion_tilt_button_right, mouse_event)
            else:
                if args[0] == "Tilt_CW":
                    value = -abs(float(value) * float(self.ui.motion_tilt_granularity.text()))
                else:
                    value = abs(float(value) * float(self.ui.motion_tilt_granularity.text()))
                self.ui.rotate_z_value.setText(str('%.2f' % float(value)))
                self.DeforumationMotions.propagateAllComponents(self.ui.rotate_z_value, float(value))
                self.deforumationnamedpipes.writeValue("rotation_z", float(value))

    def load_language_file(self):
        file_name = self.deforumation_settings.getGuiConfigValue('language_file')
        if file_name != None:
                self.deforumation_settings.openLanguageConfig(file=file_name)
                self.lp = self.deforumation_settings.getLanguageConfiguaration()
                self.deforumationwidgets.extractLabelWidgetsAndChangeToConfig(self, self.ui.centralwidget, self.lp)
        # Write to config so that language file is used on next session
        #only_file_name = QFileInfo(file_name).fileName()
        #self.deforumation_settings.writeDeforumationGuiValuesToConfig("language_file", "./languages/" + only_file_name)

    @Slot(list, list, list, list, list)
    def adjustSyrupMotionProgressBar_from_thread(self, panValues, rotationValues, zoomValues, tiltValues,promptMorphMotionValues):
        self.DeforumationMotions.adjustSyrupMotionProgressBarPan(panValues)
        self.DeforumationMotions.adjustSyrupRotationProgressBarPan(rotationValues)
        self.DeforumationMotions.adjustSyrupMotionProgressBarZoom(zoomValues)
        self.DeforumationMotions.adjustSyrupTiltProgressBarPan(tiltValues)
        self.DeforumationPrompts.adjustSyrupPromptMorphProgressBars(promptMorphMotionValues)

    @Slot()
    def setLiveValues_from_thread(self, totalRecallFrame=-1):
        self.deforumation_live_values.setLiveValues(totalRecallFrame)

    @Slot()
    def update_movie_strip(self, forceupdate=False):

        start_at = self.ui.movie_slider.value()
        videoCompressionRate = self.VideoImageContainer.getPreviewCompression()
        #print("Starting at:" + str(start_at))
        #self.setMovieSlidePosition(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
        #self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
        '''print("Number of images shown:" + str(self.currentlyShownMovieFrames*videoCompressionRate))
        print("self.currentlyShownMovieFrames:" + str(self.currentlyShownMovieFrames))
        print("start_at" + str(start_at*videoCompressionRate))
        print("videoCompressionRate" + str(videoCompressionRate))
        print("Middle frame is:" + str(start_at*videoCompressionRate + int(self.currentlyShownMovieFrames*videoCompressionRate/2)))
        print("Last frame is:" + str(start_at * videoCompressionRate + int(self.currentlyShownMovieFrames * videoCompressionRate)))'''
        #if
        for kk in range(0, self.currentlyShownMovieFrames):
            if self.VideoImageContainer.getImage(kk).getpath() == None or (start_at + kk) >= self.total_number_of_frames_generated or forceupdate == True:
                #print("None Path at image:"+str(kk))
                self.VideoImageContainer.getImageGridContainer(kk).parentWidget().close()
                self.VideoImageContainer.getImageGridContainer(kk).parentWidget().deleteLater()
                self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(kk).parentWidget())
                self.VideoImageContainer.getImage(kk).parentWidget().deleteLater()
                #print("None Path at image:"+str(kk))
                self.VideoImageContainer.getImageGridContainer(kk).parentWidget().close()
                self.VideoImageContainer.getImageGridContainer(kk).parentWidget().deleteLater()
                self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(kk).parentWidget())
                self.VideoImageContainer.getImage(kk).parentWidget().deleteLater()

                self.VideoImageContainer.addImage(kk, click_callback=self.clicked_image, clicked_image_menue=self.clicked_image_menue, image_path_number=start_at + kk, total_number_of_frames_generated=self.total_number_of_frames_generated)
                self.movie_frame = QFrame(self.ui.movie_clip)
                self.movie_frame.setObjectName(f"movie_frame_{kk}")
                self.movie_frame.setFrameShape(QFrame.StyledPanel)
                self.movie_frame.setFrameShadow(QFrame.Raised)
                self.VideoImageContainer.addImageGridContainer(kk, self.movie_frame)
                self.ui.movie_tab_grid_layout.addWidget(self.movie_frame, 0, kk, 1, 1)
                self.VideoImageContainer.getImage(kk).show()
            else:
                pass
        # Now show the appropriate audio wave for visible frames with specific FPS
        showAudioFromFrame = self.ui.movie_slider.value()
        currentFPS = float(self.ui.replay_fps_input_box.text())
        self.AudioWaveContainer.showAudioWave(showAudioFromFrame, self.currentlyShownMovieFrames, currentFPS)

                #print(str(kk)+":" + str(self.VideoImageContainer.getImage(kk).getpath()))
        # If any of the currently shown movie frames was clicked, paint the red frame around it
        #for kk in range(0, self.currentlyShownMovieFrames):
        self.VideoImageContainer.preserveSpecialPurposeFrameLooks(0)
        if self.VideoImageContainer.auto_scroll:
            last_frame_visible = start_at * videoCompressionRate + int(self.currentlyShownMovieFrames * videoCompressionRate)
            if self.total_number_of_frames_generated >= last_frame_visible:
                print("Last frame reached")
                self.setMovieSlidePosition(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)
                self.setMovieSliderFrameNumber(self.ui.movie_slider_frame_number, self.total_number_of_frames_generated)

    def setPositionMovieFrame(self, item, imagenumber):
        #print("Size of currentlyShownMovieFrames:" + str(self.currentlyShownMovieFrames))
        #print("Slider:" + str(item.objectName()))
        # Remove all olod frames
        if item.objectName() == "movie_slider":
            #print("Slider wants to start at:" + str(item.value()))
            #print("But it currently starts at:" + str(self.currentSliderPosition))
            #print("Object name:" + str(item.objectName()))
            slider_jump_window = item.value() - self.currentSliderPosition
            if slider_jump_window > self.currentlyShownMovieFrames:
                #print("Jump to great. So need to update all images")
                slider_jump_window = self.currentlyShownMovieFrames
            if item.value() > self.currentSliderPosition:
                for delIndex in range(0, self.currentlyShownMovieFrames-slider_jump_window):
                    #print("Getting image:" + str(delIndex+slider_jump_window))
                    self.VideoImageContainer.getImage(delIndex).setpathnumber(self.VideoImageContainer.getImage(delIndex + slider_jump_window).getpathnumber())
                    self.VideoImageContainer.getImage(delIndex).setpixmap(self.VideoImageContainer.getImage(delIndex+slider_jump_window).getpixmap(False)) #False))
                    #self.VideoImageContainer.getImage(delIndex).setpixmap(self.VideoImageContainer.getImage(delIndex + slider_jump_window).getpixmap(False))
                    self.VideoImageContainer.getImage(delIndex).setpath(self.VideoImageContainer.getImage(delIndex+slider_jump_window).getpath())
                    self.VideoImageContainer.getImage(delIndex).setObjectName(self.VideoImageContainer.getImage(delIndex+slider_jump_window).objectName())
                for delIndex in range(self.currentlyShownMovieFrames - slider_jump_window, self.currentlyShownMovieFrames):
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().close()
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().deleteLater()
                    self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(delIndex).parentWidget())
                    self.VideoImageContainer.getImage(delIndex).parentWidget().deleteLater()
                for kk in range(self.currentlyShownMovieFrames - slider_jump_window, self.currentlyShownMovieFrames):
                    # sliderandindex = kk + self.ui.movie_slider.value()
                    self.VideoImageContainer.addImage(kk, click_callback=self.clicked_image, clicked_image_menue=self.clicked_image_menue, image_path_number=imagenumber + kk, total_number_of_frames_generated=self.total_number_of_frames_generated)
                    self.movie_frame = QFrame(self.ui.movie_clip)
                    self.movie_frame.setObjectName(f"movie_frame_{kk}")
                    self.movie_frame.setFrameShape(QFrame.StyledPanel)
                    self.movie_frame.setFrameShadow(QFrame.Raised)
                    self.VideoImageContainer.addImageGridContainer(kk, self.movie_frame)
                    self.ui.movie_tab_grid_layout.addWidget(self.movie_frame, 0, kk, 1, 1)
                    self.VideoImageContainer.getImage(kk).show()
            elif item.value() < self.currentSliderPosition:
                slider_jump_window = - slider_jump_window
                if slider_jump_window > self.currentlyShownMovieFrames:
                    #print("Jump to great. So need to update all images")
                    slider_jump_window = self.currentlyShownMovieFrames
                for delIndex in range(self.currentlyShownMovieFrames - 1, slider_jump_window - 1, -1):
                    self.VideoImageContainer.getImage(delIndex).setpathnumber(self.VideoImageContainer.getImage(delIndex - slider_jump_window).getpathnumber())
                    self.VideoImageContainer.getImage(delIndex).setpixmap(self.VideoImageContainer.getImage(delIndex - slider_jump_window).getpixmap(False))
                    self.VideoImageContainer.getImage(delIndex).setpath(self.VideoImageContainer.getImage(delIndex - slider_jump_window).getpath())
                    self.VideoImageContainer.getImage(delIndex).setObjectName(self.VideoImageContainer.getImage(delIndex-slider_jump_window).objectName())
                for delIndex in range(0, slider_jump_window):
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().close()
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().deleteLater()
                    self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(delIndex).parentWidget())
                    self.VideoImageContainer.getImage(delIndex).parentWidget().deleteLater()
                for kk in range(0, slider_jump_window):
                    # sliderandindex = kk + self.ui.movie_slider.value()
                    self.VideoImageContainer.addImage(kk, click_callback=self.clicked_image, clicked_image_menue=self.clicked_image_menue, image_path_number=imagenumber + kk, total_number_of_frames_generated=self.total_number_of_frames_generated)
                    self.movie_frame = QFrame(self.ui.movie_clip)
                    self.movie_frame.setObjectName(f"movie_frame_{kk}")
                    self.movie_frame.setFrameShape(QFrame.StyledPanel)
                    self.movie_frame.setFrameShadow(QFrame.Raised)
                    self.VideoImageContainer.addImageGridContainer(kk, self.movie_frame)
                    self.ui.movie_tab_grid_layout.addWidget(self.movie_frame, 0, kk, 1, 1)
                    self.VideoImageContainer.getImage(kk).show()
            if self.detachedPreviewWindow != None:
                self.dettachedPreviewImage.setPixmap(self.VideoImageContainer.getImage(0).getpixmap(False))

            #If any of the currently shown movie frames was clicked, paint the red frame around it
            self.VideoImageContainer.preserveSpecialPurposeFrameLooks(0)
            #currentFrameParameters = self.DeforumationTotalRecall.getOriginalFrameParameters(imagenumber)

            # Now show the appropriate audio wave for visible frames with specific FPS
            showAudioFromFrame = self.ui.movie_slider.value()
            currentFPS = float(self.ui.replay_fps_input_box.text())
            self.AudioWaveContainer.showAudioWave(showAudioFromFrame, self.currentlyShownMovieFrames, currentFPS)

            videoCompressionRate = self.VideoImageContainer.getPreviewCompression()
            '''print("Number of images shown:" + str(self.currentlyShownMovieFrames * videoCompressionRate))
            print("self.currentlyShownMovieFrames:" + str(self.currentlyShownMovieFrames))
            print("start_at" + str(showAudioFromFrame* videoCompressionRate))
            print("videoCompressionRate" + str(videoCompressionRate))
            print("Middle frame is:" + str(showAudioFromFrame*videoCompressionRate + int(self.currentlyShownMovieFrames * videoCompressionRate / 2)))
            print("Last frame is:" + str(showAudioFromFrame*videoCompressionRate + int(self.currentlyShownMovieFrames * videoCompressionRate)))'''

    def refreshPreviewSliderWindow(self):
        for delIndex in range(0, self.currentlyShownMovieFrames):
            self.VideoImageContainer.getImage(delIndex).setpixmap(self.VideoImageContainer.getImage(delIndex).getpixmap(False))
            self.VideoImageContainer.getImage(delIndex).setpath(self.VideoImageContainer.getImage(delIndex).getpath())
            self.VideoImageContainer.getImage(delIndex).setpathnumber(self.VideoImageContainer.getImage(delIndex).getpathnumber())
            self.VideoImageContainer.getImage(delIndex).setObjectName(self.VideoImageContainer.getImage(delIndex).objectName())
        for delIndex in range(0, self.currentlyShownMovieFrames):
            self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().close()
            self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().deleteLater()
            self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(delIndex).parentWidget())
            self.VideoImageContainer.getImage(delIndex).parentWidget().deleteLater()
        for kk in range(0, self.currentlyShownMovieFrames):
            sliderandindex = kk + self.ui.movie_slider.value()
            self.VideoImageContainer.addImage(kk, click_callback=self.clicked_image, clicked_image_menue=self.clicked_image_menue, image_path_number=sliderandindex, total_number_of_frames_generated=self.total_number_of_frames_generated)
            self.movie_frame = QFrame(self.ui.movie_clip)
            self.movie_frame.setObjectName(f"movie_frame_{kk}")
            self.movie_frame.setFrameShape(QFrame.StyledPanel)
            self.movie_frame.setFrameShadow(QFrame.Raised)
            self.VideoImageContainer.addImageGridContainer(kk, self.movie_frame)
            self.ui.movie_tab_grid_layout.addWidget(self.movie_frame, 0, kk, 1, 1)
            self.VideoImageContainer.getImage(kk).show()

            self.VideoImageContainer.preserveSpecialPurposeFrameLooks(0)

        # Now show the appropriate audio wave for visible frames with specific FPS
        showAudioFromFrame = self.ui.movie_slider.value()
        currentFPS = int(self.ui.replay_fps_input_box.text())
        self.AudioWaveContainer.showAudioWave(showAudioFromFrame, self.currentlyShownMovieFrames, currentFPS)

    def createAcontextMenu(self, event, menuOptions, triggerEvent, identifier):
        context_menu = QMenu(self)
        action = []
        index = 0
        for option in menuOptions:
            action.append(context_menu.addAction(option))
            action[index].triggered.connect(lambda chk=False, item=option: triggerEvent(item, identifier))
            index += 1
        context_menu.popup(event.globalPosition().toPoint())

    def clicked_image_menue(self, event, identifier):
        if event.button().name == "RightButton":
            self.createAcontextMenu(event, ["Set current image & Copy it's original values", "Set current image", "Copy this image's original values to Deforumation", "Get this image's prompt", "Get active prompt", "Mark FFMPEG Preview, IN", "Mark FFMPEG Preview, OUT", "Clear FFMPEG Preview"], self.on_action_popup_preview_image_triggered, identifier)

    def on_action_popup_preview_image_triggered(self, action_string, identifier):
        if action_string == "Set current image":
            #self.DeforumationMotions.setComponetValuesThroughTotalRecall(self.DeforumationTotalRecall.getCurrentTotalRecallFrame())
            self.total_number_of_frames_generated = identifier.pathnumber
            self.refreshPreviewSliderWindow()
            self.DeforumationMotions.haltAllSyrupMotions()
            self.deforumationnamedpipes.writeValue("should_resume", 1)
            self.deforumationnamedpipes.writeValue("start_frame", int(self.total_number_of_frames_generated))
            self.skipLiveValues = True
        elif action_string == "Set current image & Copy it's original values":
            self.DeforumationMotions.setComponetValuesThroughTotalRecall(self.DeforumationTotalRecall.getOriginalFrameParameters(identifier.pathnumber))
            self.total_number_of_frames_generated = identifier.pathnumber
            self.refreshPreviewSliderWindow()
            self.DeforumationMotions.haltAllSyrupMotions()
            self.deforumationnamedpipes.writeValue("should_resume", 1)
            self.deforumationnamedpipes.writeValue("start_frame", int(self.total_number_of_frames_generated))
        elif action_string == "Get this image's prompt":
            self.DeforumationPrompts.setCurrentPromptsThroughTotalRecall(identifier.pathnumber)
        elif action_string == "Copy this image's original values to Deforumation":
            self.DeforumationMotions.setComponetValuesThroughTotalRecall(self.DeforumationTotalRecall.getOriginalFrameParameters(identifier.pathnumber))
            self.DeforumationMotions.haltAllSyrupMotions()
        elif action_string == "Get active prompt":
            self.DeforumationPrompts.setCurrentPrompts()
        elif action_string == "Mark FFMPEG Preview, IN":
            self.ui.replay_from_input_box.setText(str(identifier.pathnumber))
            self.VideoImageContainer.setFFmpegIN(self.ui.replay_from_input_box)
        elif action_string == "Mark FFMPEG Preview, OUT":
            self.ui.replay_to_input_box.setText(str(identifier.pathnumber))
            self.VideoImageContainer.setFFmpegOUT(self.ui.replay_to_input_box)
        elif action_string == "Clear FFMPEG Preview":
            self.ui.replay_from_input_box.setText("")
            self.ui.replay_to_input_box.setText("")
            self.VideoImageContainer.setFFmpegIN(self.ui.replay_from_input_box)
            self.VideoImageContainer.setFFmpegOUT(self.ui.replay_to_input_box)


    @Slot(object)
    def clicked_image(self, identifier):
        self.setWindowTitle(self.window_title + " - Image:" + str(identifier.getpathnumber()))
        self.VideoImageContainer.setCurrentlySelectedImage(identifier.getpathnumber())
        self.VideoImageContainer.makeClickedImageSelected(identifier)

    def closeDettachedPreviewWindow(self, event):
        event.accept()

    def resizeDettachedPreviewWindow(self, event):
        current_preview_dettached_window_size = event.size()
        frameSize = self.VideoImageContainer.getImage(0).getpixmap().size()
        framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_preview_dettached_window_size.height()
        shouldusethisheight = int(current_preview_dettached_window_size.height()) # int(frameSize.height() / 4)
        shouldusethiswidth = int(framesizeScaledWidth)  # in

        self.detachedPreviewWindow.resize(QSize(shouldusethiswidth,shouldusethisheight))
        event.accept()

    def promt_params_frame_resizeEvent(self, event):
        verticalFrame_prompt_width = self.ui.right_prompt_tab_frame.width()
        #print("promt_params_frame_resizeEvent:" + str(verticalFrame_prompt_width))
        #self.table.setColumnWidth(1, int(verticalFrame_prompt_width/2-110))
        #self.table.setColumnWidth(3, int(verticalFrame_prompt_width/2-110))
        self.DeforumationPrompts.resizeEvent_morph_frames(verticalFrame_prompt_width)

    def preview_tab_resizeEvent(self, event):
        current_preview_tab_height = self.ui.preview_screen.height()
        #print("movie_clip.width:" + str(current_preview_tab_width) + " movie_clip.height:" + str(current_preview_tab_height))

        if current_preview_tab_height == 0:
            if self.detachedPreviewWindow == None:
                self.detachedPreviewWindow = QMainWindow()
                self.detachedPreviewWindow.setWindowTitle("Preview")
                self.dettachedPreviewImage = QLabel()
                image = self.VideoImageContainer.getImage(0).getpixmap(False)
                self.dettachedPreviewImage.setMinimumSize(QSize(64,64))
                self.dettachedPreviewImage.setScaledContents(True)
                self.dettachedPreviewImage.setPixmap(image)
                self.detachedPreviewWindow.setCentralWidget(self.dettachedPreviewImage)
                self.detachedPreviewWindow.resize(QSize(image.size().width(), image.size().height()))
                self.detachedPreviewWindow.closeEvent = self.closeDettachedPreviewWindow
                self.detachedPreviewWindow.resizeEvent = self.resizeDettachedPreviewWindow
                self.restoreDetachedPreviewWindow()
                self.detachedPreviewWindow.show()
                if self.deforumationPreviewWindowIsOnTop:
                    self.makeDeforumationPreviewWindowOnTop(True)
        else:
            if self.detachedPreviewWindow != None:
                self.detachedPreviewWindow.close()
                self.detachedPreviewWindow = None


        frame_image = self.ui.preview_image.pixmap()
        frameSize = frame_image.size()
        #print("frameSize.width:" + str(frameSize.width()) + " frameSize.height:" + str(frameSize.height()))
        if frameSize.width() != 0 and frameSize.height() !=0:
            framesizeScaledWidth = (frameSize.width() / frameSize.height()) * current_preview_tab_height
            shouldusethisheight = current_preview_tab_height  # int(frameSize.height() / 4)
            shouldusethiswidth = framesizeScaledWidth  # int(frameSize.width() / 2)
            self.ui.preview_image.setMaximumHeight(shouldusethisheight)
            self.ui.preview_image.setMaximumWidth(shouldusethiswidth)

        # Save the new window sizes for the settings file

    def saveFFMPEGpreviewWindowPosition(self, ffmpeg_preview_window):
        if ffmpeg_preview_window != None:
            self.p["Ffmpeg_Preview_Window_ScreenSizeWidth"] = ffmpeg_preview_window.width()
            self.p["Ffmpeg_Preview_Window_ScreenSizeHeight"] = ffmpeg_preview_window.height()
            self.p["Ffmpeg_Preview_Window_ScreenPosX"] = ffmpeg_preview_window.pos().x()
            self.p["Ffmpeg_Preview_Window_ScreenPosY"] = ffmpeg_preview_window.pos().y()
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.p) #writeToDefaultConfig()
    def restoreFFMPEGpreviewWindowPosition(self, ffmpeg_preview_window):
        if ffmpeg_preview_window != None:
            if "Ffmpeg_Preview_Window_ScreenSizeWidth" in self.p:
                ffmpeg_preview_window.resize(self.p["Ffmpeg_Preview_Window_ScreenSizeWidth"], self.p["Ffmpeg_Preview_Window_ScreenSizeHeight"])
            if "Ffmpeg_Preview_Window_ScreenPosX" in self.p:
                ffmpeg_preview_window.move(self.p["Ffmpeg_Preview_Window_ScreenPosX"], self.p["Ffmpeg_Preview_Window_ScreenPosY"])
    def saveComponentPosition(self, configFile=None):
        componentContainer = self.deforumationwidgets.getComponentContainer()
        self.cc = self.deforumation_settings.getGuiConfig() #getComponentConfiguaration()
        for component_name in componentContainer:
            #print("component_name:" + str(component_name))
            component = componentContainer[component_name]
            #print("Saving position to key:" + str(component.objectName()))
            self.cc[component.objectName()] = [component.pos().x(), component.pos().y(), component.parent().objectName()]
        if configFile != None:
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.cc, configFile=configFile)
        else:
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.cc) #writeToDefaultComponentConfig(self.cc)

    @Slot()
    def removeAllComponentsFromGui(self):
        widgetContainer = self.deforumationwidgets.getWidgetContainer()
        cc = self.deforumation_settings.getGuiConfig().copy()
        for component_name in cc:
            if component_name in widgetContainer:
                if type(cc[component_name]) == list:
                    if len(cc[component_name]) == 3:
                        if self.DeforumationMotions.isComponentAduplicated(component_name):
                            component = widgetContainer[component_name]
                            self.deforumationwidgets.removeWidgetAndItsChildren(component.widget)
                            self.deforumationwidgets.removeComponentFromContainer(component.widget)
                            self.deforumation_settings.deleteGuiConfigKey(component_name)

    @Slot()
    def restoreFromConfigFile(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Load UI Config File", "", "All (*.json)")
        if file_name != "" and file_name != None:
            self.deforumation_settings.loadGuiConfigIntoParameters(file_name)
            self.restoreComponentPosition(False)
            self.restoreScreenPosition()

    @Slot()
    def restoreComponentPosition(self, shouldLoadFromConfigFile=True):
        try:
            widgetContainer = self.deforumationwidgets.getWidgetContainer()
            if shouldLoadFromConfigFile:
                self.deforumation_settings.loadGuiConfigIntoParameters()
            self.cc = self.deforumation_settings.getGuiConfig()
            for component_name in self.cc:
                if component_name in widgetContainer:
                    if type(self.cc[component_name]) == list:
                        if len(self.cc[component_name]) == 3:
                            component = widgetContainer[component_name]
                            component.widget.move(self.cc[component_name][0], self.cc[component_name][1])
                            if self.cc[component_name][2] in widgetContainer:
                                parent = widgetContainer[self.cc[component_name][2]]
                                component.widget.setParent(parent.widget)
                elif self.DeforumationMotions.isComponentAduplicated(component_name):
                        original_component_name = self.DeforumationMotions.getOriginalComponentNameFromName(component_name)
                        if original_component_name in widgetContainer:
                            component = widgetContainer[original_component_name]
                            parent = widgetContainer[self.cc[component_name][2]]
                            pos = QPoint(self.cc[component_name][0], self.cc[component_name][1])
                            self.createDuplicateWidget(component.widget, pos, parent.widget, component_name)
            self.enumerateAllWidgetsInAllWindows()
        except Exception as e:
            if self.is_verbose:
                print("Couldn't find configuration key:" + str(e))
    def setCurrentTabPosition(self):
        tabIndex = self.deforumation_settings.getGuiConfigValue("current_tab_index")
        if tabIndex == None:
            tabIndex = 0
        #print("Current tab index:" + str(tabIndex))
        self.ui.deforumation_tabWidget.setCurrentIndex(tabIndex)
        self.ui.deforumation_tabWidget.update()
    def saveScreenPosition(self, configFile = None):
        self.p = self.deforumation_settings.getGuiConfig()
        #Save the position and size of detached tabs
        dti = self.deftabwidg.detachedTabsIndexer
        dtw = self.deftabwidg.detachedTabsWindows

        numberOfTabs = self.ui.deforumation_tabWidget.count()
        for i in range(0, numberOfTabs):
            tabname = self.ui.deforumation_tabWidget.widget(i).objectName()
            #tabname = self.ui.deforumation_tabWidget.tabName(i)
            self.p["Tab_Detached_" + tabname] = False
        for dtab in dti:
            #print("Tab " + str(dtab) + "(" + str(dti[dtab]) + ")")
            self.p["Tab_Detached_" + dtab] = True
            #print("Tabwindow has size:" + str(dtw[dtab].size()))
            #print("Tabwindow has position:" + str(dtw[dtab].pos()))
            self.p["Tab_Detached_Pos_X_" + dtab] = dtw[dtab].pos().x()
            self.p["Tab_Detached_Pos_Y_" + dtab] = dtw[dtab].pos().y()
            self.p["Tab_Detached_Width_" + dtab] = dtw[dtab].width()
            self.p["Tab_Detached_Height_" + dtab] = dtw[dtab].height()

        self.p["Main_ScreenSizeWidth"] = self.width()
        self.p["Main_ScreenSizeHeight"] = self.height()
        self.p["Main_ScreenPosX"] = self.pos().x()
        self.p["Main_ScreenPosY"] = self.pos().y()
        self.p["Movie_Tab_ScreenSizeWidth"] = self.ui.Movie_Tab.width()
        self.p["Movie_Tab_ScreenSizeHeight"] = self.ui.Movie_Tab.height()
        self.p["Preview_Tab_ScreenSizeWidth"] = self.ui.preview_screen.width()
        self.p["Preview_Tab_ScreenSizeHeight"] = self.ui.preview_screen.height()
        self.p["Tab_Tabs_ScreenSizeWidth"] = self.ui.Tab_Tabs.width()
        self.p["Tab_Tabs_ScreenSizeHeight"] = self.ui.Tab_Tabs.height()
        sizes = self.ui.splitter.sizes()
        self.p["Left_Splitter"] = [sizes[0], sizes[1], sizes[2], sizes[3]]
        sizes = self.ui.splitter_2.sizes()
        self.p["Right_Splitter"] = [sizes[0], sizes[1]]
        sizes = self.ui.splitter_3.sizes()
        self.p["Middle_Splitter"] = [sizes[0], sizes[1]]
        sizes = self.ui.splitter_4.sizes()
        self.p["LeftLeft_Splitter"] = [sizes[0], sizes[1]]

        sizes = self.ui.prompt_splitter.sizes()
        self.p["Prompt_Tab_Splitter"] = [sizes[0], sizes[1]]

        sizes = self.ui.prompt_morph_splitter.sizes()
        self.p["Prompt_Morph_Splitter"] = [sizes[0], sizes[1]]

        self.p["Slider_Tab_ScreenSizeWidth"] = self.ui.Slider_Tab.width()
        self.p["Slider_Tab_ScreenSizeHeight"] = self.ui.Slider_Tab.height()
        if self.detachedPreviewWindow != None:
            self.p["Preview_Detached_Window_ScreenSizeWidth"] = self.detachedPreviewWindow.width()
            self.p["Preview_Detached_Window_ScreenSizeHeight"] = self.detachedPreviewWindow.height()
            self.p["Preview_Detached_Window_ScreenPosX"] = self.detachedPreviewWindow.pos().x()
            self.p["Preview_Detached_Window_ScreenPosY"] = self.detachedPreviewWindow.pos().y()
        if configFile != None:
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.p, configFile=configFile)
        else:
            self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.p)

    def restoreDetachedPreviewWindow(self):
        self.p = self.deforumation_settings.getGuiConfig()
        if self.detachedPreviewWindow != None:
            if "Preview_Detached_Window_ScreenSizeWidth" in self.p and "Preview_Detached_Window_ScreenSizeHeight" in self.p:
                self.detachedPreviewWindow.resize(self.p["Preview_Detached_Window_ScreenSizeWidth"], self.p["Preview_Detached_Window_ScreenSizeHeight"])
            if "Preview_Detached_Window_ScreenPosX" in self.p:
                self.detachedPreviewWindow.move(self.p["Preview_Detached_Window_ScreenPosX"], self.p["Preview_Detached_Window_ScreenPosY"])
    @Slot()
    def restoreScreenPosition(self):
        try:
            self.p = self.deforumation_settings.getGuiConfig()
            dtw = self.deftabwidg.detachedTabsWindows
            self.resize(self.p["Main_ScreenSizeWidth"], self.p["Main_ScreenSizeHeight"])
            if "Main_ScreenPosX" in self.p:
                self.move(self.p["Main_ScreenPosX"], self.p["Main_ScreenPosY"])
            mss = self.p["Main_ScreenSizeHeight"]
            pts = self.p["Preview_Tab_ScreenSizeHeight"]
            mts = self.p["Movie_Tab_ScreenSizeHeight"]
            tts = self.p["Tab_Tabs_ScreenSizeHeight"]
            self.ui.Preview_Tab.resize(self.p["Preview_Tab_ScreenSizeWidth"], self.p["Preview_Tab_ScreenSizeHeight"])
            self.ui.Movie_Tab.resize(self.p["Movie_Tab_ScreenSizeWidth"], self.p["Movie_Tab_ScreenSizeHeight"])
            self.ui.Tab_Tabs.resize(self.p["Tab_Tabs_ScreenSizeWidth"], self.p["Tab_Tabs_ScreenSizeHeight"])
            self.ui.Slider_Tab.resize(self.p["Slider_Tab_ScreenSizeWidth"], self.p["Slider_Tab_ScreenSizeHeight"])
            #Splitter of the Left frames
            sizes = self.ui.splitter.sizes()
            stored_sizes = self.p["Left_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            sizes[2] = stored_sizes[2]
            sizes[3] = stored_sizes[3]
            self.ui.splitter.setSizes(sizes)

            #Splitter of the Right frames
            sizes = self.ui.splitter_2.sizes()
            stored_sizes = self.p["Right_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            self.ui.splitter_2.setSizes(sizes)

            #Splitter between right and left frames
            sizes = self.ui.splitter_3.sizes()
            stored_sizes = self.p["Middle_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            self.ui.splitter_3.setSizes(sizes)

            #Splitter of left frames
            sizes = self.ui.splitter_3.sizes()
            stored_sizes = self.p["LeftLeft_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            self.ui.splitter_4.setSizes(sizes)


            sizes = self.ui.prompt_splitter.sizes()
            stored_sizes = self.p["Prompt_Tab_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            self.ui.prompt_splitter.setSizes(sizes)

            sizes = self.ui.prompt_morph_splitter.sizes()
            stored_sizes = self.p["Prompt_Morph_Splitter"]
            sizes[0] = stored_sizes[0]
            sizes[1] = stored_sizes[1]
            self.ui.prompt_morph_splitter.setSizes(sizes)


            if self.detachedPreviewWindow != None:
                self.detachedPreviewWindow.resize(self.p["Preview_Detached_Window_ScreenSizeWidth"], self.p["Preview_Detached_Window_ScreenSizeHeight"])
                if "Preview_Detached_Window_ScreenPosX" in self.p:
                    self.detachedPreviewWindow.move(self.p["Preview_Detached_Window_ScreenPosX"], self.p["Preview_Detached_Window_ScreenPosY"])

            #restore detached tabs
            numberOfTabs = self.ui.deforumation_tabWidget.count()
            for child in self.ui.deforumation_tabWidget.children():
                if isinstance(child, QStackedWidget):
                    stacked_widget = child
                    break

            self.restoreAlreadyOpenedTabs()

            for child in stacked_widget.children():
                if isinstance(child, QWidget):
                    tabname = child.objectName()
                    if "Tab_Detached_"+tabname in self.p:
                        if self.p["Tab_Detached_" + tabname] == True:
                            page = self.ui.deforumation_tabWidget.findChild(QWidget, tabname)
                            index = self.ui.deforumation_tabWidget.indexOf(page)
                            #print("Detaching: " + tabname + " with index " + str(index))
                            self.deftabwidg.detachTab(index, self.ui.deforumation_tabWidget)
                            dtw[tabname].move(self.p["Tab_Detached_Pos_X_" + tabname], self.p["Tab_Detached_Pos_Y_" + tabname])
                            dtw[tabname].resize(self.p["Tab_Detached_Width_" + tabname], self.p["Tab_Detached_Height_" + tabname])
            dtw_copy = dtw.copy()
            for child in dtw_copy:
                tabname = child
                if "Tab_Detached_" + tabname in self.p:
                    if self.p["Tab_Detached_" + tabname] == False:
                            dtw[tabname].close()



            #self.enumerateAllWidgetsInAllWindows()
        except Exception as e:
            if self.is_verbose:
                print("Couldn't find configuration key:" + str(e))
    def restoreAlreadyOpenedTabs(self, specific_tab=None):
        self.p = self.deforumation_settings.getGuiConfig()
        if specific_tab != None:
            if "Tab_Detached_" + specific_tab in self.p:
                if self.p["Tab_Detached_" + specific_tab] == True:
                    window = self.deftabwidg.detachedTabsWindows[specific_tab]
                    window.move(self.p["Tab_Detached_Pos_X_" + specific_tab], self.p["Tab_Detached_Pos_Y_" + specific_tab])
                    window.resize(self.p["Tab_Detached_Width_" + specific_tab], self.p["Tab_Detached_Height_" + specific_tab])
        else:
            for dtabWindows in self.deftabwidg.detachedTabsWindows:
                window = self.deftabwidg.detachedTabsWindows[dtabWindows]
                tabname = dtabWindows
                if "Tab_Detached_" + tabname in self.p:
                    if self.p["Tab_Detached_" + tabname] == True:
                        window.move(self.p["Tab_Detached_Pos_X_" + tabname], self.p["Tab_Detached_Pos_Y_" + tabname])
                        window.resize(self.p["Tab_Detached_Width_" + tabname], self.p["Tab_Detached_Height_" + tabname])

    def movie_tab_resizeEvent(self, event):
        current_movie_tab_width = self.ui.movie_clip.width()
        current_movie_tab_height = self.ui.movie_clip.height()
        if self.current_movie_tab_width != current_movie_tab_width or self.current_movie_tab_height != current_movie_tab_height:
            self.current_movie_tab_width = current_movie_tab_width
            self.current_movie_tab_height = current_movie_tab_height
            frame_image = self.VideoImageContainer.getImage(0) #QPixmap(imagePath)
            frameSize = frame_image.size()
            #print("Image has size:" + str(frameSize))
            current_image_width = frame_image.image_width
            current_image_height = frame_image.image_height
            framesizeScaledHeight = current_movie_tab_height
            framesizeScaledWidth =  (current_image_width / current_image_height) * current_movie_tab_height #(frameSize.width() / frameSize.height()) * current_movie_tab_height
            shouldusethisheight = framesizeScaledHeight #int(frameSize.height() / 4)
            shouldusethiswidth = framesizeScaledWidth #int(frameSize.width() / 2)
            self.ui.movie_clip.setMinimumWidth(100)
            shouldusethismany = math.ceil(self.current_movie_tab_width / shouldusethiswidth) - 1
            #print("That means that we should use this many frames:" + str(shouldusethismany))
            if shouldusethismany > self.currentlyShownMovieFrames:
                extraFrames = shouldusethismany - self.currentlyShownMovieFrames

                #print(" Now showing frames:" + str(self.currentlyShownMovieFrames + extraFrames))
                for kk in range(self.currentlyShownMovieFrames, self.currentlyShownMovieFrames + extraFrames):
                    self.VideoImageContainer.addImage(kk, click_callback=self.clicked_image, clicked_image_menue=self.clicked_image_menue, image_path_number=kk + self.ui.movie_slider.value(), total_number_of_frames_generated=self.total_number_of_frames_generated)
                    self.movie_frame = QFrame(self.ui.movie_clip)
                    #self.movie_frame_number = QFrame(self.ui.movie_clip_frame_number)
                    self.movie_frame.setObjectName(f"movie_frame_{kk}")
                    self.movie_frame.setFrameShape(QFrame.StyledPanel)
                    self.movie_frame.setFrameShadow(QFrame.Raised)
                    self.VideoImageContainer.addImageGridContainer(kk, self.movie_frame)
                    self.ui.movie_tab_grid_layout.addWidget(self.movie_frame, 0, kk, 1, 1)
                    self.VideoImageContainer.getImage(kk).show()

            elif shouldusethismany < self.currentlyShownMovieFrames:
                for delIndex in range(self.currentlyShownMovieFrames -1, shouldusethismany -1, -1):
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().close()
                    self.VideoImageContainer.getImageGridContainer(delIndex).parentWidget().deleteLater()
                    self.ui.movie_tab_grid_layout.removeWidget(self.VideoImageContainer.getImage(delIndex).parentWidget())
                    self.VideoImageContainer.getImage(delIndex).parentWidget().deleteLater()

                    self.VideoImageContainer.removeImageGridContainer(delIndex)
                    self.VideoImageContainer.removeImage(delIndex)


            '''if shouldusethismany != self.currentlyShownMovieFrames:
                #self.ui.movie_clip_frame_number.setMinimumWidth(24+shouldusethismany*shouldusethiswidth)
                #for kk in range(0, self.currentlyShownMovieFrames):
                #self.ui.movie_clip_frame_number.clear()
                self.frameLabelString = QLabel()
                self.frameLabelString.setText("1")
                self.frameLabelString.setMinimumWidth(shouldusethiswidth)
                self.frameLabelString.setMaximumWidth(shouldusethiswidth)
                for kk in range(0, shouldusethismany):
                    self.ui.movie_clip_frame_number_grid.addWidget(self.frameLabelString, 0, kk, 1, 1)'''


            self.currentlyShownMovieFrames = shouldusethismany
            self.VideoImageContainer.preserveSpecialPurposeFrameLooks(0)

            #Now show the appropriate audio wave for visible frames with specific FPS
            showAudioFromFrame = self.ui.movie_slider.value()
            currentFPS = int(self.ui.replay_fps_input_box.text())
            self.AudioWaveContainer.showAudioWave(showAudioFromFrame, shouldusethismany, currentFPS)

        # Save the new window sizes for the settings file
        QMainWindow.resizeEvent(self, event)

    def createDuplicateWidget(self, item, pos, parent, component_name = None):
        self.newItem = self.deforumationwidgets.duplicate_widget(item, parent)
        if component_name != None:
            self.newItem.setObjectName(component_name)
        #self.newItem.setParent(parent)
        self.newItem.move(pos)
        self.newItem.show()
        self.enumerateAllWidgetsInAllWindows()
        #self.deforumationwidgets.enumerateWidgets(self, self.ui.centralwidget)
    @Slot(bool, str)
    def printItem(self, item, popMenue):
        gp = popMenue.parentWidget().mapToGlobal(QPoint(0, 0))
        realPos = popMenue.mapFromGlobal(gp) * -1
        if realPos.y() < 0:
            realPos.setY(0)
        if realPos.x() < 0:
            realPos.setX(0)
        if type(item) == QPushButton:
            self.newItem = self.deforumationwidgets.duplicate_widget(item)
            #print("New widget is:" + str(self.newItem))
            #print("Parent widget is:" + str(popMenue.parentWidget()))
            self.newItem.setParent(popMenue.parentWidget())
            self.newItem.move(realPos)
            self.newItem.show()
            popMenue.close()
            self.enumerateAllWidgetsInAllWindows()
        elif type(item) == QFrame or type(item) == QScrollArea or type(item) == QWidget:
            self.newItem = self.deforumationwidgets.duplicate_widget(item)
            #print("New widget is:" + str(self.newItem))
            #print("Parent widget is:" + str(popMenue.parentWidget()))
            self.newItem.setParent(popMenue.parentWidget())
            self.newItem.move(realPos)
            self.newItem.show()
            popMenue.close()
            self.deforumation_settings.addGuiConfigKey(self.newItem.objectName(), [self.newItem.pos().x(), self.newItem.pos().y(), self.newItem.parent().objectName()])
            #self.cc[component.objectName()] = [component.pos().x(), component.pos().y(), component.parent().objectName()]
            self.enumerateAllWidgetsInAllWindows()
        elif type(item) == QSlider or type(item) == QComboBox:
            self.newItem = self.deforumationwidgets.duplicate_widget(item)
            #print("New widget is:" + str(self.newItem))
            #print("Parent widget is:" + str(popMenue.parentWidget()))
            self.newItem.setParent(popMenue.parentWidget())
            self.newItem.move(realPos)
            self.newItem.show()
            popMenue.close()
            self.enumerateAllWidgetsInAllWindows()
    def enumerateAllWidgetsInAllWindows(self):
        self.deforumationwidgets.enumerateWidgets(self, self.ui.centralwidget)
        for dtabWindows in self.deftabwidg.detachedTabsWindows:
            window = self.deftabwidg.detachedTabsWindows[dtabWindows]
            self.deforumationwidgets.enumerateWidgets(self, window.centralWidget())

    def saveAndWriteScreenPositionToOtherConfigFile(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Save UI Layout to Config File", "", "Config File(*.json)")
        if file_name != "" and file_name != None:
            self.saveScreenPosition(file_name)
            self.saveComponentPosition(file_name)

    def saveAndWriteScreenPositionToConfigFile(self):
        self.saveScreenPosition()
        self.saveComponentPosition()
        #self.deforumation_settings.writeToDefaultConfig()


    def pressed_return(self):
        handleEventReturnPressed(self)

    #This function receives all the events from a slider

    def slider_release_event(self, item):
        print("Slider was released: " + str(item))
    def value_changed_slider(self, item):
        handleEventValueChanged(self, item)
    #This function handles all the events signaled by widgets/components (except signals when values change, omitted by sliders). See function value_changed_slider, above for that
    def eventFilter(self, object, event):
        global ShouldRestoreOriginalDeforumationGui
        global ShouldOnlyRestartDeforumationGui

        if object == self:
            if event.type() == QEvent.KeyPress:
                if event.key() == Qt.Key_Shift:
                    self.AudioWaveContainer.setSpecialKey("Shift", True)
                elif event.key() == Qt.Key_Control:
                    self.AudioWaveContainer.setSpecialKey("Control", True)
                elif event.key() == Qt.Key_Alt:
                    self.AudioWaveContainer.setSpecialKey("Alt", True)
                elif event.key() == Qt.Key_Delete:
                    self.AudioWaveContainer.setSpecialKey("Delete", True)
                elif event.key() == Qt.Key_A:
                    self.AudioWaveContainer.setSpecialKey("a_key", True)
                elif event.key() == Qt.Key_C:
                    self.AudioWaveContainer.setSpecialKey("c_key", True)
                elif event.key() == Qt.Key_V:
                    self.AudioWaveContainer.setSpecialKey("v_key", True)
                elif event.key() == Qt.Key_Space:
                    self.AudioWaveContainer.togglePlayAudio()
                elif event.key() == Qt.Key_Return:
                    self.AudioWaveContainer.togglePlayAudioRememberStartPosition()

            if event.type() == QEvent.KeyRelease:
                if event.key() == Qt.Key_Delete or event.key() == Qt.Key_Backspace:
                    self.Deforumation_Joystick.abort_joystick_event(1337)
                elif event.key() == Qt.Key_Escape:
                    #print("No changes made, aborting joystick binding")
                    self.Deforumation_Joystick.abort_joystick_event(1338)
                elif event.key() == Qt.Key_Shift:
                    self.AudioWaveContainer.setSpecialKey("Shift", False)
                    #print("Releasing shift")
                elif event.key() == Qt.Key_Control:
                    self.AudioWaveContainer.setSpecialKey("Control", False)
                    #print("Releasing control")
                elif event.key() == Qt.Key_Alt:
                    self.AudioWaveContainer.setSpecialKey("Alt", False)
                    #print("Releasing Alt")




        #Handle all events (done in helpers/events.py)
        handledStatus = handleEvent(self, object, event)

        #Some special values that need to be set in the main deforumation gui
        ShouldRestoreOriginalDeforumationGui = self.ShouldRestoreOriginalDeforumationGui
        ShouldOnlyRestartDeforumationGui = self.ShouldOnlyRestartDeforumationGui

        return handledStatus

    def makeDeforumationMainWindowOnTop(self, shouldBeOnTop):
        self.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
        self.setVisible(False)  # Hide and then show to apply the change
        self.show()
        self.deforumationMainWindowIsOnTop = shouldBeOnTop

    def makeDeforumationPreviewWindowOnTop(self, shouldBeOnTop):
        if self.detachedPreviewWindow != None:
            self.detachedPreviewWindow.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.detachedPreviewWindow.setVisible(False)  # Hide and then show to apply the change
            self.detachedPreviewWindow.show()
            self.deforumationPreviewWindowIsOnTop = shouldBeOnTop

    def makeDeforumationDetachedTabsOnTop(self, shouldBeOnTop):
        tabWindowDict = self.deftabwidg.detachedTabsWindows.copy()
        for dtabWindows in tabWindowDict:
            self.deftabwidg.detachedTabsWindows[dtabWindows].setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.deftabwidg.detachedTabsWindows[dtabWindows].setVisible(False)  # Hide and then show to apply the change
            self.deftabwidg.detachedTabsWindows[dtabWindows].show()
            self.deforumationDetachedTabsAreOnTop = shouldBeOnTop
    def makeDeforumationVideoPlayerOnTop(self, shouldBeOnTop):
        if  self.VideoImageContainer.player != None:
            self.VideoImageContainer.player.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.VideoImageContainer.player.setVisible(False)  # Hide and then show to apply the change
            self.VideoImageContainer.player.show()
            self.deforumationVideoPlayerIsOnTop = shouldBeOnTop

    def makeAllWindowsOnTop(self, shouldBeOnTop):
        self.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
        self.setVisible(False)  # Hide and then show to apply the change
        self.show()

        if self.detachedPreviewWindow != None:
            self.detachedPreviewWindow.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.detachedPreviewWindow.setVisible(False)  # Hide and then show to apply the change
            self.detachedPreviewWindow.show()

        tabWindowDict = self.deftabwidg.detachedTabsWindows.copy()
        for dtabWindows in tabWindowDict:
            self.deftabwidg.detachedTabsWindows[dtabWindows].setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.deftabwidg.detachedTabsWindows[dtabWindows].setVisible(False)  # Hide and then show to apply the change
            self.deftabwidg.detachedTabsWindows[dtabWindows].show()

        if  self.VideoImageContainer.player != None:
            self.VideoImageContainer.player.setWindowFlag(Qt.WindowStaysOnTopHint, shouldBeOnTop)
            self.VideoImageContainer.player.setVisible(False)  # Hide and then show to apply the change
            self.VideoImageContainer.player.show()

        self.deforumationMainWindowIsOnTop = shouldBeOnTop
        self.deforumationPreviewWindowIsOnTop = shouldBeOnTop
        self.deforumationDetachedTabsAreOnTop = shouldBeOnTop
        self.deforumationVideoPlayerIsOnTop = shouldBeOnTop

    def propagateAllCheckboxes(self, sender, checkbox_name):
        for checkboxwidgets in self.deforumationwidgets.getWidgetContainer():
            if checkboxwidgets.startswith(checkbox_name) and not checkboxwidgets == sender.objectName():
                self.deforumationwidgets.getWidgetContainer()[checkboxwidgets].widget.setChecked(not sender.isChecked())

    def mouseMoveEventWidgetButton(self, event, widget):
        #print("I'm in move mode")
        pos = event.scenePosition().toPoint()#event.windowPos().toPoint()
        modulusX = 8
        modulusY = 8
        if widget:
            if event.buttons() & Qt.LeftButton:
                realPos = pos - self.first_click_pos + self.realPos
                x = realPos.x()
                y = realPos.y()
                y = y - y % modulusY
                x = x - x % modulusX
                realPos.setX(x)
                realPos.setY(y)
                widget.move(realPos) # - self.ui.cookie_button.rect().center())

    def setMovieSlidePosition(self, item, imageNumber, specialAudioNumber=None):
        videoCompressionRate = self.VideoImageContainer.getPreviewCompression()
        sliderNumber = int((imageNumber - imageNumber % videoCompressionRate) / videoCompressionRate)
        if videoCompressionRate != 1:
            pass
        if specialAudioNumber == None:
            self.setPositionMovieFrame(item, imageNumber)
        else:
            self.setPositionMovieFrame(item, specialAudioNumber)
        if not item.objectName() == ("movie_slider"):
            for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
                if sliderwidgets.startswith("movie_slider"):
                    if type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                        if specialAudioNumber == None:
                            self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sliderNumber) #imageNumber)
                        else:
                            self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(specialAudioNumber)
    def setMovieSliderFrameNumber(self, item, imageNumber):
        self.ui.movie_slider_frame_number.setText(str(imageNumber))
        for slidertextwidgets in self.deforumationwidgets.getWidgetContainer():
            if slidertextwidgets.startswith("movie_slider_frame_number"):
                if type(self.deforumationwidgets.getWidgetContainer()[slidertextwidgets].widget) == QLineEdit:
                    self.deforumationwidgets.getWidgetContainer()[slidertextwidgets].widget.setText(str(imageNumber))#*self.VideoImageContainer.preview_compression_rate))


    def mousePressEventMorphPromptLabelStandard(self, event, action, popMenu):
        promptWindow = None
        if popMenu == self.popMenu_prompt1:
            promptWindow = self.ui.prompt1
        elif popMenu == self.popMenu_prompt2:
            promptWindow = self.ui.prompt2
        elif popMenu == self.popMenu_negative1:
            promptWindow = self.ui.negative_prompt
        if promptWindow != None:
            if action == "Cut":
                promptWindow.cut()
            elif action == "Copy":
                promptWindow.copy()
            elif action == "Paste":
                promptWindow.paste()
        popMenu.close()
    def mousePressEventMorphPromptLabel(self, event, item, popMenu):
        redColor = QColor(255, 0, 0)
        whiteColor = QColor(255, 255, 255)
        greenColor = QColor(0, 255, 0)
        promptWindow = None
        if popMenu == self.popMenu_prompt1:
            promptWindow = self.ui.prompt1
        elif popMenu == self.popMenu_prompt2:
            promptWindow = self.ui.prompt2
        elif popMenu == self.popMenu_negative1:
            promptWindow = self.ui.negative_prompt
        if promptWindow != None:
            if item.morph_prompt_enabled == 1:
                promptWindow.setTextColor(whiteColor)
            else:
                promptWindow.setTextColor(redColor)
            promptWindow.insertPlainText("{{" + item.morph_prompt_binding.text() + "}}")
            promptWindow.setTextColor(greenColor)
        popMenu.close()



class ParameterContainer():
    # Values in the eyes of Deforum
    deforum_translation_x = 0
    deforum_translation_y = 0
    deforum_translation_z = 0
    deforum_rotation_x = 0
    deforum_rotation_y = 0
    deforum_rotation_z = 0
    deforum_fov = 70
    deforum_strength = 0.65
    deforum_cfg = 6
    deforum_steps = 25
    deforum_cadence = 2
    deforum_perlin_octaves = 4
    deforum_perlin_persistence = 0.5
    deforum_noise_multiplier = 1.0
    # Run/Steps
    steps = 25
    # Keyframes/Strength
    strength_value = 0.65
    # Keyframes/CFG
    cfg_scale = 6
    # Keyframes/3D/Motion
    rotation_x = 0.0
    rotation_y = 0.0
    rotation_z = 0.0
    translation_x = 0.0
    translation_y = 0.0
    translation_z = 0.0
    should_use_deforumation_prompt_scheduling = 1
    Prompt_Positive = "EMPTY"
    Prompt_Negative = "EMPTY"
    positive_prompt_weight_1 = 1.0
    positive_prompt_weight_2 = 1.0
    positive_prompt_1 = ""
    positive_prompt_2 = ""
    negative_prompt_1 = ""
    frame_outdir = ""
    resume_timestring = ""
    seed_value = -1
    did_seed_change = 0
    # Keyframes/Field Of View/FOV schedule
    fov = 70.0
    cadence = 2
    should_use_optical_flow = 1
    cadence_flow_factor = 1
    generation_flow_factor = 1
    cn_weight = []
    cn_stepstart = []
    cn_stepend = []
    cn_lowt = []
    cn_hight = []
    cn_udcn = []
    for i in range(5):
        cn_weight.append(1.0)
        cn_stepstart.append(0.0)
        cn_stepend.append(1.0)
        cn_lowt.append(0)
        cn_hight.append(255)
        cn_udcn.append(0)
    parseq_keys = 0
    use_parseq = 0
    parseq_manifest = ""
    parseq_strength = 0
    parseq_movements = 0
    parseq_prompt = 0

    noise_multiplier = 1.05
    perlin_octaves = 4
    perlin_persistence = 0.5
    start_zero_pan_motion_x = 0
    start_zero_pan_motion_y = 0
    start_zero_pan_motion_z = 0
    start_zero_rotate_motion_x = 0
    start_zero_rotate_motion_y = 0
    start_zero_rotate_motion_z = 0

def get_local_ip():
    # Create a dummy socket
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        # Connect the socket to a remote server on port 80 (http port)
        # We use '8.8.8.8' here as it's the Google Public DNS, and it's unlikely to be down
        s.connect(("8.8.8.8", 80))
        # Get the local IP address the socket is bound to
        return s.getsockname()[0]

if __name__ == "__main__":

    patreons = "Onebit, Chris Barnes, 鑫涛 李, Mintercraft Media, Mizar, 红军 陆, Eddie Wong, Thomas DeColita, Dmitry, Dmitry,\n"
    " Милена Куприна, Jarkabob French, 雨 刘, kimraven, Itzevil, Apollo R.E.D., Michael, Dustin johnsen,\n"
    "wildpusa, ein5tv, eku Zhombi, Davy Smith, Anup prabhakar, Baptiste Perrin, virusvjvisuals, make shimis,\n"
    "Jags, Wrenn Bunker-Koesters, esfera, cheng bei, le000dv, Justin Weiss, Sergiy Dovgal, Pistons&Volts,\n"
    "Pixery Bilgi"
    print("\n\nSpecial thank you to our patreons and contributers:")
    print("--------------------------------------")
    try:
        print(patreons)
    except Exception as e:
        try:
            print(patreons.encode())
        except:
            pass
    print("---------------------------------------------------\n")
    arga = sys.argv[0]
    if len(sys.argv) > 1:
        argb = sys.argv[1].split(' ')
        args = []
        args.append(arga)
        for n in argb:
            args.append(n)
        sys.argv = args
    local_ip = get_local_ip()
    restart = True
    parser = argparse.ArgumentParser(description='DeforumationQT arguments.')
    parser.add_argument('--deforumation_address', default='127.0.0.1', help='Deforumation will listen for external connections (0.0.0.0:<port>)')
    parser.add_argument('--deforumation_port', default='8767', help='Deforumation will use this port for lisening')
    parser.add_argument('--mediator_address', default='127.0.0.1', help='Deforumation will use this address to connect to the mediator')
    parser.add_argument('--mediator_port', default='8766', help='Deforumation will use this port to connect to the mediator')
    parser.add_argument('--use_named_pipes', action='store_true', help='Deforumation will use named pipes instead of websocket')
    parser.add_argument('--use_osc', action='store_true', help='Deforumation will use named pipes instead of websocket')
    parser.add_argument('--osc_port', default='5005', help='Deforumation will use this port for incoming OSC')
    #These are here just so that the .bat file can be used
    """parser.add_argument('--mediator_deforumation_address', default='localhost', help='The mediator will listen on this address for deforumation traffic')
    parser.add_argument('--mediator_deforumation_port', default='8766', help='The mediator will use this port for lisening for deforumation traffic')
    parser.add_argument('--mediator_deforum_address', default='localhost', help='The mediator will listen on this address for deforum traffic')
    parser.add_argument('--mediator_deforum_port', default='8765', help='The mediator will use this port for lisening for deforum traffic')"""
    args = parser.parse_args()
    #args = parser.parse_args()

    if sys.platform.startswith('win'):
        isWindows = True
    else:
        isWindows = False
    if args.use_named_pipes:
        if isWindows:
            import win32pipe, win32file, pywintypes
            shouldUseNamedPipes = True
            print("Starting DeforumationQT with Named Pipes communication")
        else:
            shouldUseNamedPipes = False
            print("Named Pipes communication is only supported on Windows OS... exiting..")
            exit(0)
    else:
        shouldUseNamedPipes = False
        if args.deforumation_address != 'localhost' and args.deforumation_address != '127.0.0.1':
            print("Starting DeforumationQT's liveView server with non local WebSocket communication, listening on " + args.deforumation_address + ":" + args.deforumation_port)
            deforumation_self_address = get_local_ip()
        else:
            print("Starting DeforumationQT's liveView server, using local WebSocket communication, listening on " + args.deforumation_address + ":" + args.deforumation_port)
            deforumation_self_address = args.deforumation_address
        if args.mediator_address != 'localhost':
            print("Connecting to the Mediator's server using " + args.mediator_address + ":" + args.mediator_port)

        deforumation_address = args.deforumation_address
        deforumation_port = args.deforumation_port
        mediator_address = args.mediator_address
        mediator_port = args.mediator_port
    osc_port = args.osc_port
    should_use_osc = args.use_osc
    if should_use_osc:
        #print("Starting DeforumationQT with local OSC support on UDP port 5005")
        from helpers.osc import Deforumation_OSC

    while restart:
        app = QApplication.instance()
        if app == None:
            app = QApplication(sys.argv)
        widget = MainWindow()
        widget.show()
        widget.setCurrentTabPosition()
        widget.resize(QSize(widget.size().width() + 1, widget.size().height()))
        # Set window params:
        widget.restoreScreenPosition()
        widget.restoreComponentPosition()

        #widget.resize()
        app.exec()
        del app
        restart = False
        if ShouldOnlyRestartDeforumationGui:
            restart = True
            ShouldOnlyRestartDeforumationGui = False
        elif ShouldRestoreOriginalDeforumationGui:
            #print("And here we delete config files and restart")
            if os.path.exists("./config/DeforumationGUIconfig.json"):
                os.remove("./config/DeforumationGUIconfig.json")
            #if os.path.exists("./config/DeforumationReceiveConfig.json"):
            #    os.remove("./config/DeforumationReceiveConfig.json")
            #if os.path.exists("./config/DeforumationSendConfig.json"):
            #    os.remove("./config/DeforumationSendConfig.json")
            restart = True
            ShouldRestoreOriginalDeforumationGui = False
    sys.exit()
