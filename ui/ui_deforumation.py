# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'deforumation.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QProgressBar,
    QPushButton, QRadioButton, QScrollArea, QSizePolicy,
    QSlider, QSpacerItem, QSplitter, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1925, 1058)
        MainWindow.setMinimumSize(QSize(512, 249))
        MainWindow.setLayoutDirection(Qt.LeftToRight)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"  background-color:rgb(66,66,66);\n"
"\n"
"  border-radius: 10px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"  background-color:rgb(42, 42, 42);\n"
"  color: rgb(0, 255, 0);\n"
"}\n"
"QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hov"
                        "er{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255),"
                        " stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"QLineEdit {\n"
"  border-width: 1px; border-radius: 4px;\n"
"  border-color: rgb(58, 58, 58);\n"
"  border-style: inset;\n"
"  padding: 0 8px;\n"
"  color: rgb(255, 255, 255);\n"
"  background:rgb(100, 100, 100);\n"
"  selection-background-color: rgb(187, 187, 187);\n"
"  selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLabel {\n"
"  color:rgb(255,255,255); \n"
"}\n"
"QProgressBar {\n"
"  text-"
                        "align: center;\n"
"  color: rgb(240, 240, 240);\n"
"  border-width: 1px; \n"
"  border-radius: 3px;\n"
"  border-color: rgb(58, 58, 58);\n"
"  border-style: inset;\n"
"  background-color:rgb(77,77,77);\n"
"}\n"
"QProgressBar::chunk {\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"  border-radius: 5px;\n"
"}\n"
"QMenuBar {\n"
"  background:rgb(82, 82, 82);\n"
"}\n"
"QMenuBar::item {\n"
"  color:rgb(223,219,210);\n"
"  spacing: 3px;\n"
"  padding: 1px 4px;\n"
"  background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"  background:rgb(115, 115, 115);\n"
"}\n"
"QMenu::item:selected {\n"
"  color:rgb(255,255,255);\n"
"  border-width:2px;\n"
"  border-style:solid;\n"
"  padding-left:18px;\n"
"  padding-right:8px;\n"
"  padding-top:2px;\n"
"  padding-bottom:3px;\n"
"  background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));"
                        "\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"}\n"
"QMenu::item {\n"
"  color:rgb(223,219,210);\n"
"  background-color:rgb(78,78,78);\n"
"  padding-left:20px;\n"
"  padding-top:4px;\n"
"  padding-bottom:4px;\n"
"  padding-right:10px;\n"
"}\n"
"QMenu{\n"
"  background-color:rgb(78,78,78);\n"
"}\n"
"\n"
"QScrollArea{\n"
"    border-color: rgb(77,77,77);\n"
"    background-color:rgb(101,101,101);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"\n"
"QSplitter{\n"
"    border-color: rgb(77,77,77"
                        ");\n"
"    background-color:rgb(101,101,101);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QTabWidget {\n"
"  color:rgb(0,0,0);\n"
"  background-color:rgb(247,246,246);\n"
"}\n"
"QTabWidget::pane {\n"
"    border-color: rgb(77,77,77);\n"
"    background-color:rgb(101,101,101);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"\n"
"}\n"
"QTabBar::tab {\n"
"  padding:2px;\n"
"  color:rgb(250,250,250);\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"  border-style: solid;\n"
"  border-width: 2px;\n"
"    border-top-right-radius:4px;\n"
"    border-top-left-radius:4px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 11"
                        "5, 255), stop:1 rgba(95, 92, 93, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"  border-bottom-color: rgb(101,101,101);\n"
"}\n"
"QTabBar::tab:selected, QTabBar::tab:last:selected, QTabBar::tab:hover {\n"
"    background-color:rgb(101,101,101);\n"
"    margin-left: 0px;\n"
"    margin-right: 1px;\n"
"}\n"
"QTabBar::tab:!selected {\n"
"      margin-top: 1px;\n"
"    margin-right: 1px;\n"
"}\n"
"QCheckBox {\n"
"  color:rgb(223,219,210);\n"
"  padding: 2px;\n"
"}\n"
"QCheckBox:hover {\n"
"  border-radius:4px;\n"
"  border-style:solid;\n"
"  padding-left: 1px;\n"
"  padding-right: 1px;\n"
"  padding-bottom: 1px;\n"
"  padding-top: 1px;\n"
"  border-width:1px;\n"
"  border-color: rgb(87, 97, 106);\n"
"  background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  border-radius:4"
                        "px;\n"
"  border-style:solid;\n"
"  border-width:1px;\n"
"  border-color: rgb(180,180,180);\n"
"    background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
"}\n"
"QCheckBox::indicator:unchecked {\n"
"  border-radius:4px;\n"
"  border-style:solid;\n"
"  border-width:1px;\n"
"  border-color: rgb(87, 97, 106);\n"
"    background-color:rgb(255,255,255);\n"
"}\n"
"QStatusBar {\n"
"  color:rgb(240,240,240);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setStyleSheet(u"border-radius: 0px;")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.splitter_3 = QSplitter(self.centralwidget)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setStyleSheet(u"background-color: rgb(66,66,66); border: 0px solid rgb(128,128,128); border-radius: 20px;")
        self.splitter_3.setLineWidth(1)
        self.splitter_3.setOrientation(Qt.Horizontal)
        self.LeftLeft_Frame = QFrame(self.splitter_3)
        self.LeftLeft_Frame.setObjectName(u"LeftLeft_Frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.LeftLeft_Frame.sizePolicy().hasHeightForWidth())
        self.LeftLeft_Frame.setSizePolicy(sizePolicy1)
        self.LeftLeft_Frame.setMinimumSize(QSize(300, 0))
        self.LeftLeft_Frame.setMaximumSize(QSize(250, 16777215))
        self.LeftLeft_Frame.setStyleSheet(u"")
        self.LeftLeft_Frame.setFrameShape(QFrame.StyledPanel)
        self.LeftLeft_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_99 = QGridLayout(self.LeftLeft_Frame)
        self.gridLayout_99.setObjectName(u"gridLayout_99")
        self.gridLayout_99.setContentsMargins(2, 5, 0, 0)
        self.splitter_4 = QSplitter(self.LeftLeft_Frame)
        self.splitter_4.setObjectName(u"splitter_4")
        sizePolicy1.setHeightForWidth(self.splitter_4.sizePolicy().hasHeightForWidth())
        self.splitter_4.setSizePolicy(sizePolicy1)
        self.splitter_4.setStyleSheet(u"border: 0px;")
        self.splitter_4.setOrientation(Qt.Vertical)
        self.splitter_4.setHandleWidth(6)
        self.Slider_Left_Tab = QFrame(self.splitter_4)
        self.Slider_Left_Tab.setObjectName(u"Slider_Left_Tab")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(3)
        sizePolicy2.setHeightForWidth(self.Slider_Left_Tab.sizePolicy().hasHeightForWidth())
        self.Slider_Left_Tab.setSizePolicy(sizePolicy2)
        self.Slider_Left_Tab.setMinimumSize(QSize(0, 0))
        self.Slider_Left_Tab.setStyleSheet(u"")
        self.Slider_Left_Tab.setFrameShape(QFrame.StyledPanel)
        self.Slider_Left_Tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.Slider_Left_Tab)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.temp_tab_frame = QFrame(self.Slider_Left_Tab)
        self.temp_tab_frame.setObjectName(u"temp_tab_frame")
        self.temp_tab_frame.setMinimumSize(QSize(0, 0))
        self.temp_tab_frame.setMaximumSize(QSize(300, 16777215))
        self.temp_tab_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"    border-radius: 10px;\n"
"    padding: 1px; /* To prevent the content from touching the border */\n"
"}\n"
"\n"
"QSlider\n"
"{\n"
"	background-color: rgb(108,108,118);\n"
"}")
        self.temp_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.temp_tab_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_11 = QGridLayout(self.temp_tab_frame)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(10, 10, 10, 10)
        self.SuperTEmp_ParameterLabel = QLabel(self.temp_tab_frame)
        self.SuperTEmp_ParameterLabel.setObjectName(u"SuperTEmp_ParameterLabel")
        sizePolicy1.setHeightForWidth(self.SuperTEmp_ParameterLabel.sizePolicy().hasHeightForWidth())
        self.SuperTEmp_ParameterLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.SuperTEmp_ParameterLabel.setFont(font)
        self.SuperTEmp_ParameterLabel.setMouseTracking(True)
        self.SuperTEmp_ParameterLabel.setTabletTracking(True)
        self.SuperTEmp_ParameterLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 10px;\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.SuperTEmp_ParameterLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_11.addWidget(self.SuperTEmp_ParameterLabel, 0, 0, 1, 1)

        self.scrollArea_Left_slider_frame = QScrollArea(self.temp_tab_frame)
        self.scrollArea_Left_slider_frame.setObjectName(u"scrollArea_Left_slider_frame")
        sizePolicy.setHeightForWidth(self.scrollArea_Left_slider_frame.sizePolicy().hasHeightForWidth())
        self.scrollArea_Left_slider_frame.setSizePolicy(sizePolicy)
        self.scrollArea_Left_slider_frame.setMinimumSize(QSize(0, 0))
        self.scrollArea_Left_slider_frame.setStyleSheet(u"QScrollArea {\n"
"    border: 0px solid #333; /* Adjust the color and size as needed */\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrol"
                        "lBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_Left_slider_frame.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_Left_slider_frame.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSlidersLeft = QWidget()
        self.scrollAreaWidgetContentsSlidersLeft.setObjectName(u"scrollAreaWidgetContentsSlidersLeft")
        self.scrollAreaWidgetContentsSlidersLeft.setGeometry(QRect(0, 0, 270, 361))
        self.scrollAreaWidgetContentsSlidersLeft.setMinimumSize(QSize(0, 330))
        self.scrollAreaWidgetContentsSlidersLeft.setStyleSheet(u"")
        self.verticalLayout_13 = QVBoxLayout(self.scrollAreaWidgetContentsSlidersLeft)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.Seed_frame_poppable = QFrame(self.scrollAreaWidgetContentsSlidersLeft)
        self.Seed_frame_poppable.setObjectName(u"Seed_frame_poppable")
        self.Seed_frame_poppable.setTabletTracking(True)
        self.Seed_frame_poppable.setStyleSheet(u"QWidget{\n"
"border: 0px solid rgb(128,128,128);\n"
"}\n"
"QFrame{\n"
"Qbackground-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Seed_frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.Seed_frame_poppable.setFrameShadow(QFrame.Raised)
        self.iter_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.iter_RadioButton.setObjectName(u"iter_RadioButton")
        self.iter_RadioButton.setGeometry(QRect(14, 30, 171, 20))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(108, 108, 118, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 128))
        brush2.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush2)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush2)
#endif
        self.iter_RadioButton.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.iter_RadioButton.setFont(font1)
        self.iter_RadioButton.setStyleSheet(u"/*QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; \n"
"    background-color: rgb(108,108,118);\n"
"    border: 0px solid #bbb; \n"
"    border-radius: 4px; \n"
"} */\n"
"\n"
"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}\n"
"\n"
"/*background-color: rgb(108,10"
                        "8,118);\n"
"color: white; \n"
"border: 0px solid rgb(40, 40, 40); \n"
"border-radius: 5px;\n"
"padding: 1px; /* \n"
"")
        self.iter_RadioButton.setCheckable(True)
        self.iter_RadioButton.setChecked(True)
        self.fixed_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.fixed_RadioButton.setObjectName(u"fixed_RadioButton")
        self.fixed_RadioButton.setGeometry(QRect(14, 94, 95, 20))
        self.fixed_RadioButton.setFont(font1)
        self.fixed_RadioButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}")
        self.IterSeed_Inputbox = QLineEdit(self.Seed_frame_poppable)
        self.IterSeed_Inputbox.setObjectName(u"IterSeed_Inputbox")
        self.IterSeed_Inputbox.setGeometry(QRect(16, 58, 113, 22))
        self.IterSeed_Inputbox.setMaximumSize(QSize(16777215, 16777215))
        font2 = QFont()
        font2.setPointSize(12)
        self.IterSeed_Inputbox.setFont(font2)
        self.IterSeed_Inputbox.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.fixedSeed_Inputbox = QLineEdit(self.Seed_frame_poppable)
        self.fixedSeed_Inputbox.setObjectName(u"fixedSeed_Inputbox")
        self.fixedSeed_Inputbox.setGeometry(QRect(16, 120, 209, 22))
        self.fixedSeed_Inputbox.setMaximumSize(QSize(16777215, 16777215))
        self.fixedSeed_Inputbox.setFont(font2)
        self.fixedSeed_Inputbox.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.random_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.random_RadioButton.setObjectName(u"random_RadioButton")
        self.random_RadioButton.setGeometry(QRect(14, 160, 95, 20))
        self.random_RadioButton.setFont(font1)
        self.random_RadioButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}")
        self.IterSeed_N_Inputbox = QLineEdit(self.Seed_frame_poppable)
        self.IterSeed_N_Inputbox.setObjectName(u"IterSeed_N_Inputbox")
        self.IterSeed_N_Inputbox.setGeometry(QRect(208, 56, 41, 22))
        self.IterSeed_N_Inputbox.setMaximumSize(QSize(16777215, 16777215))
        self.IterSeed_N_Inputbox.setFont(font2)
        self.IterSeed_N_Inputbox.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.seed_iter_n = QLabel(self.Seed_frame_poppable)
        self.seed_iter_n.setObjectName(u"seed_iter_n")
        self.seed_iter_n.setGeometry(QRect(130, 56, 73, 21))
        font3 = QFont()
        font3.setPointSize(10)
        font3.setBold(True)
        self.seed_iter_n.setFont(font3)
        self.seed_iter_n.setStyleSheet(u"")
        self.ladder_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.ladder_RadioButton.setObjectName(u"ladder_RadioButton")
        self.ladder_RadioButton.setGeometry(QRect(14, 198, 105, 20))
        self.ladder_RadioButton.setFont(font1)
        self.ladder_RadioButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}")
        self.line_a = QFrame(self.Seed_frame_poppable)
        self.line_a.setObjectName(u"line_a")
        self.line_a.setGeometry(QRect(12, 86, 250, 3))
        self.line_a.setStyleSheet(u"QFrame {\n"
"    border: 2px solid rgb(42, 42, 42); /* Adjust the color to fit your UI theme */\n"
"    background-color: black; /* Optional: adjust the background color */\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px; /* Optional: adds rounded corners if you prefer */\n"
"}")
        self.line_a.setLineWidth(2)
        self.line_a.setFrameShape(QFrame.HLine)
        self.line_a.setFrameShadow(QFrame.Sunken)
        self.line_b = QFrame(self.Seed_frame_poppable)
        self.line_b.setObjectName(u"line_b")
        self.line_b.setGeometry(QRect(12, 152, 250, 3))
        self.line_b.setStyleSheet(u"QFrame {\n"
"    border: 2px solid rgb(42, 42, 42); /* Adjust the color to fit your UI theme */\n"
"    background-color: black; /* Optional: adjust the background color */\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px; /* Optional: adds rounded corners if you prefer */\n"
"}")
        self.line_b.setFrameShadow(QFrame.Raised)
        self.line_b.setLineWidth(2)
        self.line_b.setFrameShape(QFrame.HLine)
        self.line_c = QFrame(self.Seed_frame_poppable)
        self.line_c.setObjectName(u"line_c")
        self.line_c.setGeometry(QRect(12, 188, 250, 3))
        self.line_c.setStyleSheet(u"QFrame {\n"
"    border: 2px solid rgb(42, 42, 42); /* Adjust the color to fit your UI theme */\n"
"    background-color: black; /* Optional: adjust the background color */\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px; /* Optional: adds rounded corners if you prefer */\n"
"}")
        self.line_c.setFrameShadow(QFrame.Raised)
        self.line_c.setLineWidth(2)
        self.line_c.setFrameShape(QFrame.HLine)
        self.alternate_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.alternate_RadioButton.setObjectName(u"alternate_RadioButton")
        self.alternate_RadioButton.setGeometry(QRect(14, 234, 105, 20))
        self.alternate_RadioButton.setFont(font1)
        self.alternate_RadioButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}")
        self.line_d = QFrame(self.Seed_frame_poppable)
        self.line_d.setObjectName(u"line_d")
        self.line_d.setGeometry(QRect(12, 224, 250, 3))
        self.line_d.setStyleSheet(u"QFrame {\n"
"    border: 2px solid rgb(42, 42, 42); /* Adjust the color to fit your UI theme */\n"
"    background-color: black; /* Optional: adjust the background color */\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px; /* Optional: adds rounded corners if you prefer */\n"
"}")
        self.line_d.setFrameShadow(QFrame.Raised)
        self.line_d.setLineWidth(2)
        self.line_d.setFrameShape(QFrame.HLine)
        self.update_seed_button = QPushButton(self.Seed_frame_poppable)
        self.update_seed_button.setObjectName(u"update_seed_button")
        self.update_seed_button.setGeometry(QRect(10, 297, 233, 33))
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(1)
        sizePolicy3.setVerticalStretch(80)
        sizePolicy3.setHeightForWidth(self.update_seed_button.sizePolicy().hasHeightForWidth())
        self.update_seed_button.setSizePolicy(sizePolicy3)
        self.update_seed_button.setMinimumSize(QSize(60, 32))
        self.update_seed_button.setMaximumSize(QSize(16777215, 43))
        self.update_seed_button.setFont(font1)
        self.update_seed_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border-style: solid; /* Defines the style of the border */\n"
"    border-width: 2px; /* Width of the border */\n"
"    border-color: rgba(255, 255, 255, 0.5); /* Border color with some transparency */\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"")
        self.update_seed_iter_n_button = QPushButton(self.Seed_frame_poppable)
        self.update_seed_iter_n_button.setObjectName(u"update_seed_iter_n_button")
        self.update_seed_iter_n_button.setGeometry(QRect(145, 29, 105, 24))
        sizePolicy3.setHeightForWidth(self.update_seed_iter_n_button.sizePolicy().hasHeightForWidth())
        self.update_seed_iter_n_button.setSizePolicy(sizePolicy3)
        self.update_seed_iter_n_button.setMinimumSize(QSize(44, 24))
        self.update_seed_iter_n_button.setMaximumSize(QSize(16777215, 39))
        self.update_seed_iter_n_button.setFont(font3)
        self.update_seed_iter_n_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border-style: solid; /* Defines the style of the border */\n"
"    border-width: 2px; /* Width of the border */\n"
"    border-color: rgba(255, 255, 255, 0.5); /* Border color with some transparency */\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 2px 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"")
        self.scheduled_RadioButton = QRadioButton(self.Seed_frame_poppable)
        self.scheduled_RadioButton.setObjectName(u"scheduled_RadioButton")
        self.scheduled_RadioButton.setGeometry(QRect(14, 268, 105, 25))
        self.scheduled_RadioButton.setFont(font1)
        self.scheduled_RadioButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 5px;\n"
"    padding: 2px 2px;\n"
"    color: white; /* Text color */\n"
"    background-color: rgb(108,108,118); /* General background color */\n"
"    border: 0px solid #bbb; /* Border color and width */\n"
"    border-radius: 0px; /* Rounded corners */\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    border-radius: 9px; /* Round indicator */\n"
"border: 2px solid #bbb; /* Border color and width */\n"
"    width: 15px; /* Adjust size as needed */\n"
"    height: 15px; /* Adjust size as needed */\n"
"}\n"
"\n"
"QRadioButton::indicator:unchecked {\n"
"    background-color: rgb(42, 42, 42); /* Dark grey for off state */\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background-color: #00ff00; /* Green for on state */\n"
"}")
        self.line_f = QFrame(self.Seed_frame_poppable)
        self.line_f.setObjectName(u"line_f")
        self.line_f.setGeometry(QRect(12, 260, 250, 3))
        self.line_f.setStyleSheet(u"QFrame {\n"
"    border: 2px solid rgb(42, 42, 42); /* Adjust the color to fit your UI theme */\n"
"    background-color: black; /* Optional: adjust the background color */\n"
"    border-style: inset;\n"
"    border-width: 2px;\n"
"    border-radius: 2px; /* Optional: adds rounded corners if you prefer */\n"
"}")
        self.line_f.setFrameShadow(QFrame.Raised)
        self.line_f.setLineWidth(2)
        self.line_f.setFrameShape(QFrame.HLine)

        self.verticalLayout_13.addWidget(self.Seed_frame_poppable)

        self.scrollArea_Left_slider_frame.setWidget(self.scrollAreaWidgetContentsSlidersLeft)

        self.gridLayout_11.addWidget(self.scrollArea_Left_slider_frame, 2, 0, 1, 1)


        self.verticalLayout_11.addWidget(self.temp_tab_frame)

        self.splitter_4.addWidget(self.Slider_Left_Tab)
        self.OtherLeft_Tab = QFrame(self.splitter_4)
        self.OtherLeft_Tab.setObjectName(u"OtherLeft_Tab")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(4)
        sizePolicy4.setHeightForWidth(self.OtherLeft_Tab.sizePolicy().hasHeightForWidth())
        self.OtherLeft_Tab.setSizePolicy(sizePolicy4)
        self.OtherLeft_Tab.setMinimumSize(QSize(0, 0))
        self.OtherLeft_Tab.setStyleSheet(u"border: 0px")
        self.OtherLeft_Tab.setFrameShape(QFrame.StyledPanel)
        self.OtherLeft_Tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.OtherLeft_Tab)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.live_value_tab_left_frame = QFrame(self.OtherLeft_Tab)
        self.live_value_tab_left_frame.setObjectName(u"live_value_tab_left_frame")
        self.live_value_tab_left_frame.setMaximumSize(QSize(300, 16777215))
        self.live_value_tab_left_frame.setStyleSheet(u"\n"
"    background-color: rgb(108, 108, 118);\n"
"    border: 2px solid rgb(40, 40, 40); /* Refined shadow effect */\n"
"    border-radius: 10px; /* Smooth rounded corners */\n"
"")
        self.live_value_tab_left_frame.setFrameShape(QFrame.StyledPanel)
        self.live_value_tab_left_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.live_value_tab_left_frame)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(10, 10, 10, 10)
        self.Temp_ValuesLabel = QLabel(self.live_value_tab_left_frame)
        self.Temp_ValuesLabel.setObjectName(u"Temp_ValuesLabel")
        self.Temp_ValuesLabel.setFont(font)
        self.Temp_ValuesLabel.setMouseTracking(True)
        self.Temp_ValuesLabel.setTabletTracking(True)
        self.Temp_ValuesLabel.setStyleSheet(u"QLabel{\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"border: 2px solid rgb(32, 32, 32);\n"
"border-radius: 10px;\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.Temp_ValuesLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_13.addWidget(self.Temp_ValuesLabel, 0, 0, 1, 1)

        self.scrollArea_left_values = QScrollArea(self.live_value_tab_left_frame)
        self.scrollArea_left_values.setObjectName(u"scrollArea_left_values")
        self.scrollArea_left_values.setMinimumSize(QSize(0, 0))
        self.scrollArea_left_values.setStyleSheet(u"QScrollArea {\n"
"    border: 0px solid #333; /* Adjust the color and size as needed */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrollBar::add-page:vertical {\n"
"    backgr"
                        "ound: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_left_values.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_left_values.setWidgetResizable(True)
        self.scrollAreaLeftWidgetValues = QWidget()
        self.scrollAreaLeftWidgetValues.setObjectName(u"scrollAreaLeftWidgetValues")
        self.scrollAreaLeftWidgetValues.setGeometry(QRect(0, 0, 274, 488))
        sizePolicy1.setHeightForWidth(self.scrollAreaLeftWidgetValues.sizePolicy().hasHeightForWidth())
        self.scrollAreaLeftWidgetValues.setSizePolicy(sizePolicy1)
        self.scrollAreaLeftWidgetValues.setMinimumSize(QSize(0, 390))
        self.scrollAreaLeftWidgetValues.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaLeftWidgetValues)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.scrollAreaLeftWidgetValues)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"QWidget{\n"
"border: 0px solid rgb(128,128,128);\n"
"}\n"
"QFrame{\n"
"Qbackground-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_5.addWidget(self.frame_6)

        self.scrollArea_left_values.setWidget(self.scrollAreaLeftWidgetValues)

        self.gridLayout_13.addWidget(self.scrollArea_left_values, 2, 0, 1, 1)


        self.verticalLayout_14.addWidget(self.live_value_tab_left_frame)

        self.splitter_4.addWidget(self.OtherLeft_Tab)

        self.gridLayout_99.addWidget(self.splitter_4, 0, 0, 1, 1)

        self.splitter_3.addWidget(self.LeftLeft_Frame)
        self.Left_Frame = QFrame(self.splitter_3)
        self.Left_Frame.setObjectName(u"Left_Frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(3)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.Left_Frame.sizePolicy().hasHeightForWidth())
        self.Left_Frame.setSizePolicy(sizePolicy5)
        self.Left_Frame.setStyleSheet(u"")
        self.Left_Frame.setFrameShape(QFrame.StyledPanel)
        self.Left_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_16 = QGridLayout(self.Left_Frame)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 5, 0, 0)
        self.Deforumation_Main = QFrame(self.Left_Frame)
        self.Deforumation_Main.setObjectName(u"Deforumation_Main")
        self.Deforumation_Main.setFrameShape(QFrame.StyledPanel)
        self.Deforumation_Main.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.Deforumation_Main)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.Deforumation_Main)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setMinimumSize(QSize(0, 0))
        self.splitter.setStyleSheet(u"background-color: rgb(66,66,66); border: 0px solid rgb(128,128,128); border-radius: 0px;")
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setHandleWidth(6)
        self.Preview_Tab = QWidget(self.splitter)
        self.Preview_Tab.setObjectName(u"Preview_Tab")
        sizePolicy4.setHeightForWidth(self.Preview_Tab.sizePolicy().hasHeightForWidth())
        self.Preview_Tab.setSizePolicy(sizePolicy4)
        self.Preview_Tab.setMinimumSize(QSize(0, 1))
        self.Preview_Tab.setSizeIncrement(QSize(0, 0))
        self.Preview_Tab.setBaseSize(QSize(0, 0))
        self.Preview_Tab.setAutoFillBackground(False)
        self.Preview_Tab.setStyleSheet(u"/*background-color: rgb(108,108,118); border: 0px solid rgb(128,128,128); border-radius: 10px;*/\n"
"\n"
"background-color: rgb(108,108,118);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.gridLayout_6 = QGridLayout(self.Preview_Tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 9)
        self.gridLayout_preview_screen = QGridLayout()
        self.gridLayout_preview_screen.setObjectName(u"gridLayout_preview_screen")
        self.preview_screen = QWidget(self.Preview_Tab)
        self.preview_screen.setObjectName(u"preview_screen")
        sizePolicy1.setHeightForWidth(self.preview_screen.sizePolicy().hasHeightForWidth())
        self.preview_screen.setSizePolicy(sizePolicy1)
        self.preview_screen.setStyleSheet(u"border: 0")
        self.gridLayout_14 = QGridLayout(self.preview_screen)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.preview_image = QLabel(self.preview_screen)
        self.preview_image.setObjectName(u"preview_image")
        sizePolicy1.setHeightForWidth(self.preview_image.sizePolicy().hasHeightForWidth())
        self.preview_image.setSizePolicy(sizePolicy1)
        self.preview_image.setMaximumSize(QSize(16777215, 16777215))
        self.preview_image.setStyleSheet(u"\n"
"    border: 10px groove rgb(22,22,22);\n"
"    border-radius: 5px;\n"
"    ")
        self.preview_image.setScaledContents(True)

        self.gridLayout_14.addWidget(self.preview_image, 0, 0, 1, 1)


        self.gridLayout_preview_screen.addWidget(self.preview_screen, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_preview_screen, 0, 0, 1, 1)

        self.splitter.addWidget(self.Preview_Tab)
        self.Movie_Tab = QWidget(self.splitter)
        self.Movie_Tab.setObjectName(u"Movie_Tab")
        sizePolicy1.setHeightForWidth(self.Movie_Tab.sizePolicy().hasHeightForWidth())
        self.Movie_Tab.setSizePolicy(sizePolicy1)
        self.Movie_Tab.setMinimumSize(QSize(0, 200))
        self.Movie_Tab.setMaximumSize(QSize(16777215, 280))
        self.Movie_Tab.setSizeIncrement(QSize(0, 0))
        self.Movie_Tab.setBaseSize(QSize(0, 0))
        self.Movie_Tab.setAutoFillBackground(False)
        self.Movie_Tab.setStyleSheet(u"background-color: rgb(108,108,118);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.gridLayout_8 = QGridLayout(self.Movie_Tab)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(10, 10, 10, 10)
        self.Movie_Slider_Frame_poppable = QFrame(self.Movie_Tab)
        self.Movie_Slider_Frame_poppable.setObjectName(u"Movie_Slider_Frame_poppable")
        self.Movie_Slider_Frame_poppable.setTabletTracking(True)
        self.Movie_Slider_Frame_poppable.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Movie_Slider_Frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.Movie_Slider_Frame_poppable.setFrameShadow(QFrame.Raised)
        self.gridLayout_12 = QGridLayout(self.Movie_Slider_Frame_poppable)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setHorizontalSpacing(9)
        self.gridLayout_12.setVerticalSpacing(0)
        self.gridLayout_12.setContentsMargins(5, 0, 5, 0)
        self.movie_slider_frame_number = QLineEdit(self.Movie_Slider_Frame_poppable)
        self.movie_slider_frame_number.setObjectName(u"movie_slider_frame_number")
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.movie_slider_frame_number.sizePolicy().hasHeightForWidth())
        self.movie_slider_frame_number.setSizePolicy(sizePolicy6)
        self.movie_slider_frame_number.setMinimumSize(QSize(0, 0))
        self.movie_slider_frame_number.setMaximumSize(QSize(60, 16777215))
        self.movie_slider_frame_number.setSizeIncrement(QSize(0, 0))
        self.movie_slider_frame_number.setBaseSize(QSize(0, 0))
        self.movie_slider_frame_number.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.movie_slider_frame_number.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.gridLayout_12.addWidget(self.movie_slider_frame_number, 1, 1, 1, 1)

        self.movie_slider = QSlider(self.Movie_Slider_Frame_poppable)
        self.movie_slider.setObjectName(u"movie_slider")
        sizePolicy6.setHeightForWidth(self.movie_slider.sizePolicy().hasHeightForWidth())
        self.movie_slider.setSizePolicy(sizePolicy6)
        self.movie_slider.setMinimumSize(QSize(0, 28))
        self.movie_slider.setStyleSheet(u"QSlider{\n"
"border:0;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/movie_groove_long.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 31px; /* The height of your image */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - "
                        "adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}")
        self.movie_slider.setMinimum(0)
        self.movie_slider.setMaximum(100)
        self.movie_slider.setOrientation(Qt.Horizontal)
        self.movie_slider.setTickPosition(QSlider.NoTicks)
        self.movie_slider.setTickInterval(10)

        self.gridLayout_12.addWidget(self.movie_slider, 1, 0, 1, 1)


        self.gridLayout_8.addWidget(self.Movie_Slider_Frame_poppable, 2, 0, 1, 1)

        self.Preview_Frame = QFrame(self.Movie_Tab)
        self.Preview_Frame.setObjectName(u"Preview_Frame")
        self.Preview_Frame.setMinimumSize(QSize(0, 44))
        self.Preview_Frame.setStyleSheet(u"QFrame\n"
"{\n"
"border: 0px\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Preview_Frame.setFrameShape(QFrame.StyledPanel)
        self.Preview_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_15 = QGridLayout(self.Preview_Frame)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setVerticalSpacing(0)
        self.gridLayout_15.setContentsMargins(5, 0, 7, 0)
        self.open_Deforum_folder_frame_poppable = QFrame(self.Preview_Frame)
        self.open_Deforum_folder_frame_poppable.setObjectName(u"open_Deforum_folder_frame_poppable")
        self.open_Deforum_folder_frame_poppable.setMinimumSize(QSize(36, 30))
        self.open_Deforum_folder_frame_poppable.setTabletTracking(True)
        self.open_Deforum_folder_frame_poppable.setStyleSheet(u"border:0")
        self.open_Deforum_folder_frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.open_Deforum_folder_frame_poppable.setFrameShadow(QFrame.Raised)
        self.open_Deforum_folder = QPushButton(self.open_Deforum_folder_frame_poppable)
        self.open_Deforum_folder.setObjectName(u"open_Deforum_folder")
        self.open_Deforum_folder.setEnabled(True)
        self.open_Deforum_folder.setGeometry(QRect(0, 0, 40, 32))
        sizePolicy7 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.open_Deforum_folder.sizePolicy().hasHeightForWidth())
        self.open_Deforum_folder.setSizePolicy(sizePolicy7)
        self.open_Deforum_folder.setMinimumSize(QSize(40, 32))
        self.open_Deforum_folder.setBaseSize(QSize(0, 0))
        self.open_Deforum_folder.setFocusPolicy(Qt.StrongFocus)
        self.open_Deforum_folder.setToolTipDuration(-1)
        self.open_Deforum_folder.setAutoFillBackground(False)
        self.open_Deforum_folder.setStyleSheet(u"QPushButton {\n"
"    /* Normal state */\n"
"    background-image: url(images/Folder_off.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 0px;\n"
"    min-width: 38px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Hovered state */\n"
"    background-image: url(images/Folder_hover.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    min-width: 38px;\n"
"    min-height: 30px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed state */\n"
"    background-image: url(images/Folder_active.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    min-width: 38px;\n"
"    min-height: 30px;\n"
"}")
        self.open_Deforum_folder.setIconSize(QSize(36, 30))

        self.gridLayout_15.addWidget(self.open_Deforum_folder_frame_poppable, 0, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_4, 0, 2, 1, 1)

        self.CRF_Compression_Frame_poppable = QFrame(self.Preview_Frame)
        self.CRF_Compression_Frame_poppable.setObjectName(u"CRF_Compression_Frame_poppable")
        self.CRF_Compression_Frame_poppable.setMinimumSize(QSize(211, 0))
        self.CRF_Compression_Frame_poppable.setTabletTracking(True)
        self.CRF_Compression_Frame_poppable.setStyleSheet(u"border: 0px")
        self.CRF_Compression_Frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.CRF_Compression_Frame_poppable.setFrameShadow(QFrame.Raised)
        self.crf_input_box = QLineEdit(self.CRF_Compression_Frame_poppable)
        self.crf_input_box.setObjectName(u"crf_input_box")
        self.crf_input_box.setGeometry(QRect(160, 8, 40, 24))
        self.crf_input_box.setMaximumSize(QSize(40, 16777215))
        self.crf_input_box.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.crf_label = QLabel(self.CRF_Compression_Frame_poppable)
        self.crf_label.setObjectName(u"crf_label")
        self.crf_label.setGeometry(QRect(5, 3, 153, 35))
        font4 = QFont()
        font4.setBold(True)
        self.crf_label.setFont(font4)

        self.gridLayout_15.addWidget(self.CRF_Compression_Frame_poppable, 0, 9, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_3, 0, 6, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_5, 0, 8, 1, 1)

        self.Preview_Play_Buttons_poppable = QFrame(self.Preview_Frame)
        self.Preview_Play_Buttons_poppable.setObjectName(u"Preview_Play_Buttons_poppable")
        self.Preview_Play_Buttons_poppable.setMinimumSize(QSize(260, 44))
        self.Preview_Play_Buttons_poppable.setTabletTracking(True)
        self.Preview_Play_Buttons_poppable.setStyleSheet(u"border: 0px")
        self.Preview_Play_Buttons_poppable.setFrameShape(QFrame.StyledPanel)
        self.Preview_Play_Buttons_poppable.setFrameShadow(QFrame.Raised)
        self.goto_end_button = QPushButton(self.Preview_Play_Buttons_poppable)
        self.goto_end_button.setObjectName(u"goto_end_button")
        self.goto_end_button.setGeometry(QRect(152, 6, 52, 34))
        sizePolicy7.setHeightForWidth(self.goto_end_button.sizePolicy().hasHeightForWidth())
        self.goto_end_button.setSizePolicy(sizePolicy7)
        self.goto_end_button.setMinimumSize(QSize(52, 34))
        self.goto_end_button.setMaximumSize(QSize(52, 34))
        self.goto_end_button.setTabletTracking(False)
        self.goto_end_button.setStyleSheet(u"border : 0")
        icon = QIcon()
        icon.addFile(u"images/goto_end_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u"images/goto_end_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon.addFile(u"images/goto_end_active.png", QSize(), QIcon.Active, QIcon.On)
        self.goto_end_button.setIcon(icon)
        self.goto_end_button.setIconSize(QSize(52, 34))
        self.play_button = QPushButton(self.Preview_Play_Buttons_poppable)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(112, 6, 37, 33))
        sizePolicy7.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy7)
        self.play_button.setMinimumSize(QSize(37, 33))
        self.play_button.setMaximumSize(QSize(37, 33))
        self.play_button.setTabletTracking(False)
        self.play_button.setStyleSheet(u"border : 0")
        icon1 = QIcon()
        icon1.addFile(u"images/play_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon1.addFile(u"images/play_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon1.addFile(u"images/play_active.png", QSize(), QIcon.Active, QIcon.On)
        self.play_button.setIcon(icon1)
        self.play_button.setIconSize(QSize(37, 35))
        self.stop_button = QPushButton(self.Preview_Play_Buttons_poppable)
        self.stop_button.setObjectName(u"stop_button")
        self.stop_button.setGeometry(QRect(72, 6, 34, 33))
        sizePolicy7.setHeightForWidth(self.stop_button.sizePolicy().hasHeightForWidth())
        self.stop_button.setSizePolicy(sizePolicy7)
        self.stop_button.setMinimumSize(QSize(34, 33))
        self.stop_button.setMaximumSize(QSize(34, 33))
        self.stop_button.setTabletTracking(False)
        self.stop_button.setStyleSheet(u"border : 0")
        icon2 = QIcon()
        icon2.addFile(u"images/paus_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon2.addFile(u"images/paus_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon2.addFile(u"images/paus_active.png", QSize(), QIcon.Active, QIcon.On)
        self.stop_button.setIcon(icon2)
        self.stop_button.setIconSize(QSize(34, 33))
        self.goto_start_button = QPushButton(self.Preview_Play_Buttons_poppable)
        self.goto_start_button.setObjectName(u"goto_start_button")
        self.goto_start_button.setGeometry(QRect(8, 6, 52, 34))
        sizePolicy7.setHeightForWidth(self.goto_start_button.sizePolicy().hasHeightForWidth())
        self.goto_start_button.setSizePolicy(sizePolicy7)
        self.goto_start_button.setMinimumSize(QSize(52, 34))
        self.goto_start_button.setMaximumSize(QSize(52, 34))
        self.goto_start_button.setTabletTracking(False)
        self.goto_start_button.setStyleSheet(u"border : 0")
        icon3 = QIcon()
        icon3.addFile(u"images/goto_start_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u"images/goto_start_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon3.addFile(u"images/goto_start_active.png", QSize(), QIcon.Active, QIcon.On)
        self.goto_start_button.setIcon(icon3)
        self.goto_start_button.setIconSize(QSize(52, 34))
        self.loop_button = QPushButton(self.Preview_Play_Buttons_poppable)
        self.loop_button.setObjectName(u"loop_button")
        self.loop_button.setGeometry(QRect(212, 2, 46, 44))
        sizePolicy7.setHeightForWidth(self.loop_button.sizePolicy().hasHeightForWidth())
        self.loop_button.setSizePolicy(sizePolicy7)
        self.loop_button.setMinimumSize(QSize(46, 44))
        self.loop_button.setMaximumSize(QSize(46, 44))
        self.loop_button.setTabletTracking(False)
        self.loop_button.setStyleSheet(u"border : 0")
        icon4 = QIcon()
        icon4.addFile(u"images/loop_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u"images/loop_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon4.addFile(u"images/loop_active.png", QSize(), QIcon.Active, QIcon.On)
        self.loop_button.setIcon(icon4)
        self.loop_button.setIconSize(QSize(41, 38))

        self.gridLayout_15.addWidget(self.Preview_Play_Buttons_poppable, 0, 5, 1, 1)

        self.preview_compression_slider = QSlider(self.Preview_Frame)
        self.preview_compression_slider.setObjectName(u"preview_compression_slider")
        self.preview_compression_slider.setMinimumSize(QSize(200, 0))
        self.preview_compression_slider.setStyleSheet(u"QSlider{\n"
"border:0;\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 31px; /* The height of your image */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust "
                        "as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}")
        self.preview_compression_slider.setMinimum(1)
        self.preview_compression_slider.setMaximum(80)
        self.preview_compression_slider.setOrientation(Qt.Horizontal)
        self.preview_compression_slider.setTickPosition(QSlider.TicksBelow)
        self.preview_compression_slider.setTickInterval(2)

        self.gridLayout_15.addWidget(self.preview_compression_slider, 0, 10, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_15.addItem(self.horizontalSpacer_7, 0, 4, 1, 1)

        self.Play_Preview_From_To_Frame_poppable = QFrame(self.Preview_Frame)
        self.Play_Preview_From_To_Frame_poppable.setObjectName(u"Play_Preview_From_To_Frame_poppable")
        self.Play_Preview_From_To_Frame_poppable.setMinimumSize(QSize(450, 0))
        self.Play_Preview_From_To_Frame_poppable.setTabletTracking(True)
        self.Play_Preview_From_To_Frame_poppable.setStyleSheet(u"border: 0px")
        self.Play_Preview_From_To_Frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.Play_Preview_From_To_Frame_poppable.setFrameShadow(QFrame.Raised)
        self.replay_fps_input_box = QLineEdit(self.Play_Preview_From_To_Frame_poppable)
        self.replay_fps_input_box.setObjectName(u"replay_fps_input_box")
        self.replay_fps_input_box.setGeometry(QRect(392, 8, 40, 24))
        self.replay_fps_input_box.setMaximumSize(QSize(40, 16777215))
        self.replay_fps_input_box.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.fps_label = QLabel(self.Play_Preview_From_To_Frame_poppable)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setGeometry(QRect(342, 3, 44, 35))
        self.fps_label.setFont(font4)
        self.from_framelabel = QLabel(self.Play_Preview_From_To_Frame_poppable)
        self.from_framelabel.setObjectName(u"from_framelabel")
        self.from_framelabel.setGeometry(QRect(106, 2, 79, 35))
        self.from_framelabel.setFont(font4)
        self.play_preview = QPushButton(self.Play_Preview_From_To_Frame_poppable)
        self.play_preview.setObjectName(u"play_preview")
        self.play_preview.setGeometry(QRect(0, 6, 97, 28))
        sizePolicy7.setHeightForWidth(self.play_preview.sizePolicy().hasHeightForWidth())
        self.play_preview.setSizePolicy(sizePolicy7)
        self.play_preview.setMinimumSize(QSize(45, 26))
        self.play_preview.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.to_frame_label = QLabel(self.Play_Preview_From_To_Frame_poppable)
        self.to_frame_label.setObjectName(u"to_frame_label")
        self.to_frame_label.setGeometry(QRect(233, 3, 63, 35))
        self.to_frame_label.setFont(font4)
        self.replay_to_input_box = QLineEdit(self.Play_Preview_From_To_Frame_poppable)
        self.replay_to_input_box.setObjectName(u"replay_to_input_box")
        self.replay_to_input_box.setGeometry(QRect(302, 8, 40, 24))
        self.replay_to_input_box.setMaximumSize(QSize(40, 16777215))
        self.replay_to_input_box.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.replay_from_input_box = QLineEdit(self.Play_Preview_From_To_Frame_poppable)
        self.replay_from_input_box.setObjectName(u"replay_from_input_box")
        self.replay_from_input_box.setGeometry(QRect(187, 8, 40, 24))
        self.replay_from_input_box.setMaximumSize(QSize(40, 16777215))
        self.replay_from_input_box.setStyleSheet(u"QLineEdit {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")

        self.gridLayout_15.addWidget(self.Play_Preview_From_To_Frame_poppable, 0, 7, 1, 1)


        self.gridLayout_8.addWidget(self.Preview_Frame, 4, 0, 1, 1)

        self.gridLayout_movie_clip = QGridLayout()
        self.gridLayout_movie_clip.setObjectName(u"gridLayout_movie_clip")
        self.movie_clip = QWidget(self.Movie_Tab)
        self.movie_clip.setObjectName(u"movie_clip")
        self.movie_clip.setMinimumSize(QSize(0, 64))
        self.movie_clip.setStyleSheet(u"background-color: rgb(0,0,0); border-radius: 1px; color: white;")
        self.movie_tab_grid_layout = QGridLayout(self.movie_clip)
        self.movie_tab_grid_layout.setSpacing(0)
        self.movie_tab_grid_layout.setObjectName(u"movie_tab_grid_layout")
        self.movie_tab_grid_layout.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_movie_clip.addWidget(self.movie_clip, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_movie_clip, 0, 0, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 5, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer_6, 1, 0, 1, 1)

        self.splitter.addWidget(self.Movie_Tab)
        self.Tab_Tabs = QWidget(self.splitter)
        self.Tab_Tabs.setObjectName(u"Tab_Tabs")
        sizePolicy1.setHeightForWidth(self.Tab_Tabs.sizePolicy().hasHeightForWidth())
        self.Tab_Tabs.setSizePolicy(sizePolicy1)
        self.Tab_Tabs.setMinimumSize(QSize(0, 250))
        self.Tab_Tabs.setSizeIncrement(QSize(0, 0))
        self.Tab_Tabs.setBaseSize(QSize(0, 0))
        self.Tab_Tabs.setAutoFillBackground(False)
        self.Tab_Tabs.setStyleSheet(u"background-color: rgb(108,108,118);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 0px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.gridLayout_81 = QGridLayout(self.Tab_Tabs)
        self.gridLayout_81.setObjectName(u"gridLayout_81")
        self.gridLayout_81.setContentsMargins(5, 4, 2, 5)
        self.tabWidget_frame = QFrame(self.Tab_Tabs)
        self.tabWidget_frame.setObjectName(u"tabWidget_frame")
        self.tabWidget_frame.setStyleSheet(u"background-color: rgb(108,108,118); border: 0px solid rgb(128,128,128); border-radius: 10px;")
        self.tabWidget_frame.setFrameShape(QFrame.StyledPanel)
        self.tabWidget_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.tabWidget_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(-1, 0, 8, -1)
        self.deforumation_tabWidget = QTabWidget(self.tabWidget_frame)
        self.deforumation_tabWidget.setObjectName(u"deforumation_tabWidget")
        sizePolicy1.setHeightForWidth(self.deforumation_tabWidget.sizePolicy().hasHeightForWidth())
        self.deforumation_tabWidget.setSizePolicy(sizePolicy1)
        self.deforumation_tabWidget.setMinimumSize(QSize(0, 16))
        font5 = QFont()
        font5.setPointSize(7)
        font5.setBold(True)
        font5.setItalic(False)
        font5.setUnderline(False)
        font5.setKerning(True)
        self.deforumation_tabWidget.setFont(font5)
        self.deforumation_tabWidget.setAutoFillBackground(False)
        self.deforumation_tabWidget.setStyleSheet(u"QTabWidget::pane { /* The tab widget frame */\n"
"    border: none;\n"
"    background-color: rgb(82, 82, 82); /* Dark grey background */\n"
"    border-radius: 10px; /* Rounded corners */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;  /* Removes the line at the base of the tabs */\n"
"}\n"
"\n"
"QTabBar::tab { /* Style for the tabs */\n"
"    background: rgb(64, 64, 64); /* Slightly lighter grey for tabs */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners for tabs */\n"
"    padding: 5px; /* Padding around text */\n"
"    color: white; /* Text color */\n"
"    margin-right: 5px; /* Small space between tabs */\n"
"    min-width: 50px; /* Minimum width of the tab */\n"
"    max-width: 100px; /* Maximum width of the tab */\n"
"    height: 25px; /* Height of the tab */\n"
"    font-size: 14px; /* Text size for the tabs */\n"
"    font-weight: bold; /* Makes the text bold */\n"
"}\n"
"\n"
"QTabBar::tab:hover { /* Style for hovering over a tab */\n"
"    background: rgb(96, 96, 96); /*"
                        " Even lighter grey for hover effect */\n"
"}\n"
"\n"
"QTabBar::tab:selected { /* Style for the selected tab */\n"
"    background: rgb(128, 128, 128); /* Light grey for the active tab */\n"
"}\n"
"")
        self.deforumation_tabWidget.setTabShape(QTabWidget.Rounded)
        self.deforumation_tabWidget.setIconSize(QSize(16, 16))
        self.deforumation_tabWidget.setMovable(True)
        self.deforumation_tabWidget.setTabBarAutoHide(False)
        self.Prompt_Tab = QWidget()
        self.Prompt_Tab.setObjectName(u"Prompt_Tab")
        self.Prompt_Tab.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout_3 = QHBoxLayout(self.Prompt_Tab)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.Prompt_Frame = QFrame(self.Prompt_Tab)
        self.Prompt_Frame.setObjectName(u"Prompt_Frame")
        self.Prompt_Frame.setStyleSheet(u"background-color: rgb(66,66,66); border: 2px solid rgb(40,40,40);  solid rgb(128,128,128); border-radius: 10px;")
        self.Prompt_Frame.setFrameShape(QFrame.NoFrame)
        self.Prompt_Frame.setFrameShadow(QFrame.Plain)
        self.Prompt_Frame.setLineWidth(0)
        self.horizontalLayout_6 = QHBoxLayout(self.Prompt_Frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 6, 8, 6)
        self.prompt_splitter = QSplitter(self.Prompt_Frame)
        self.prompt_splitter.setObjectName(u"prompt_splitter")
        self.prompt_splitter.setStyleSheet(u"background-color: rgb(66,66,66); border: 0px solid rgb(128,128,128); border-radius: 10px;")
        self.prompt_splitter.setMidLineWidth(0)
        self.prompt_splitter.setOrientation(Qt.Horizontal)
        self.prompt_splitter.setHandleWidth(6)
        self.left_prompt_tab_frame = QFrame(self.prompt_splitter)
        self.left_prompt_tab_frame.setObjectName(u"left_prompt_tab_frame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy8.setHorizontalStretch(12)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.left_prompt_tab_frame.sizePolicy().hasHeightForWidth())
        self.left_prompt_tab_frame.setSizePolicy(sizePolicy8)
        self.left_prompt_tab_frame.setMinimumSize(QSize(0, 0))
        self.left_prompt_tab_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 0px  1px ;  /* To prevent the content from touching the border */\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }\n"
"QTextEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 2px solid rgb(128,128,128);\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QScrollArea {\n"
"    border: 0px;\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners"
                        " for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrollBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.left_prompt_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.left_prompt_tab_frame.setFrameShadow(QFrame.Raised)
        self.left_prompt_tab_frame.setLineWidth(0)
        self.verticalLayout_12 = QVBoxLayout(self.left_prompt_tab_frame)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(9, 0, 9, 10)
        self.Prompt_1_Frame = QFrame(self.left_prompt_tab_frame)
        self.Prompt_1_Frame.setObjectName(u"Prompt_1_Frame")
        sizePolicy9 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy9.setHorizontalStretch(1)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.Prompt_1_Frame.sizePolicy().hasHeightForWidth())
        self.Prompt_1_Frame.setSizePolicy(sizePolicy9)
        self.Prompt_1_Frame.setMinimumSize(QSize(200, 21))
        self.Prompt_1_Frame.setMaximumSize(QSize(500, 17))
        self.Prompt_1_Frame.setTabletTracking(True)
        self.Prompt_1_Frame.setStyleSheet(u"border: 0px solid rgb(40, 40, 40);")
        self.Prompt_1_Frame.setFrameShape(QFrame.StyledPanel)
        self.Prompt_1_Frame.setFrameShadow(QFrame.Raised)
        self.label_Positive_Prompt1 = QLabel(self.Prompt_1_Frame)
        self.label_Positive_Prompt1.setObjectName(u"label_Positive_Prompt1")
        self.label_Positive_Prompt1.setGeometry(QRect(0, -8, 241, 38))
        sizePolicy7.setHeightForWidth(self.label_Positive_Prompt1.sizePolicy().hasHeightForWidth())
        self.label_Positive_Prompt1.setSizePolicy(sizePolicy7)
        self.label_Positive_Prompt1.setMinimumSize(QSize(0, 30))
        font6 = QFont()
        font6.setFamilies([u"Courier"])
        font6.setPointSize(15)
        font6.setBold(True)
        self.label_Positive_Prompt1.setFont(font6)
        self.label_Positive_Prompt1.setStyleSheet(u"border:0")
        self.label_Positive_Prompt1.setMargin(2)

        self.verticalLayout_12.addWidget(self.Prompt_1_Frame)

        self.prompt1 = QTextEdit(self.left_prompt_tab_frame)
        self.prompt1.setObjectName(u"prompt1")
        sizePolicy10 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(2)
        sizePolicy10.setHeightForWidth(self.prompt1.sizePolicy().hasHeightForWidth())
        self.prompt1.setSizePolicy(sizePolicy10)
        self.prompt1.setMinimumSize(QSize(0, 1))
        self.prompt1.setMaximumSize(QSize(16777215, 16777215))
        self.prompt1.setSizeIncrement(QSize(0, 0))
        self.prompt1.setAutoFillBackground(False)
        self.prompt1.setStyleSheet(u"QTextEdit QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QTextEdit QScrollBar::sub-line:vertical,\n"
"QTextEdit QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::sub-page:vertical,\n"
"QTextEdit QScrollBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.prompt1.setAcceptRichText(False)

        self.verticalLayout_12.addWidget(self.prompt1)

        self.Prompt_2_Frame = QFrame(self.left_prompt_tab_frame)
        self.Prompt_2_Frame.setObjectName(u"Prompt_2_Frame")
        sizePolicy7.setHeightForWidth(self.Prompt_2_Frame.sizePolicy().hasHeightForWidth())
        self.Prompt_2_Frame.setSizePolicy(sizePolicy7)
        self.Prompt_2_Frame.setMinimumSize(QSize(200, 30))
        self.Prompt_2_Frame.setMaximumSize(QSize(500, 16777215))
        self.Prompt_2_Frame.setStyleSheet(u"border: 0px solid rgb(40, 40, 40);")
        self.Prompt_2_Frame.setFrameShape(QFrame.StyledPanel)
        self.Prompt_2_Frame.setFrameShadow(QFrame.Raised)
        self.label_Positive_Prompt2 = QLabel(self.Prompt_2_Frame)
        self.label_Positive_Prompt2.setObjectName(u"label_Positive_Prompt2")
        self.label_Positive_Prompt2.setGeometry(QRect(0, -2, 241, 38))
        sizePolicy7.setHeightForWidth(self.label_Positive_Prompt2.sizePolicy().hasHeightForWidth())
        self.label_Positive_Prompt2.setSizePolicy(sizePolicy7)
        self.label_Positive_Prompt2.setFont(font6)

        self.verticalLayout_12.addWidget(self.Prompt_2_Frame)

        self.prompt2 = QTextEdit(self.left_prompt_tab_frame)
        self.prompt2.setObjectName(u"prompt2")
        sizePolicy10.setHeightForWidth(self.prompt2.sizePolicy().hasHeightForWidth())
        self.prompt2.setSizePolicy(sizePolicy10)
        self.prompt2.setMinimumSize(QSize(0, 1))
        self.prompt2.setMaximumSize(QSize(16777215, 16777215))
        self.prompt2.setStyleSheet(u"QTextEdit QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QTextEdit QScrollBar::sub-line:vertical,\n"
"QTextEdit QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::sub-page:vertical,\n"
"QTextEdit QScrollBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.prompt2.setAcceptRichText(False)

        self.verticalLayout_12.addWidget(self.prompt2)

        self.Prompt_3_Frame = QFrame(self.left_prompt_tab_frame)
        self.Prompt_3_Frame.setObjectName(u"Prompt_3_Frame")
        sizePolicy7.setHeightForWidth(self.Prompt_3_Frame.sizePolicy().hasHeightForWidth())
        self.Prompt_3_Frame.setSizePolicy(sizePolicy7)
        self.Prompt_3_Frame.setMinimumSize(QSize(200, 30))
        self.Prompt_3_Frame.setMaximumSize(QSize(500, 16777215))
        self.Prompt_3_Frame.setStyleSheet(u"border: 0px solid rgb(40, 40, 40);")
        self.Prompt_3_Frame.setFrameShape(QFrame.StyledPanel)
        self.Prompt_3_Frame.setFrameShadow(QFrame.Raised)
        self.label_Negative_Prompt = QLabel(self.Prompt_3_Frame)
        self.label_Negative_Prompt.setObjectName(u"label_Negative_Prompt")
        self.label_Negative_Prompt.setGeometry(QRect(0, -2, 204, 38))
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Ignored)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.label_Negative_Prompt.sizePolicy().hasHeightForWidth())
        self.label_Negative_Prompt.setSizePolicy(sizePolicy11)
        self.label_Negative_Prompt.setMinimumSize(QSize(0, 20))
        self.label_Negative_Prompt.setFont(font6)

        self.verticalLayout_12.addWidget(self.Prompt_3_Frame)

        self.negative_prompt = QTextEdit(self.left_prompt_tab_frame)
        self.negative_prompt.setObjectName(u"negative_prompt")
        sizePolicy10.setHeightForWidth(self.negative_prompt.sizePolicy().hasHeightForWidth())
        self.negative_prompt.setSizePolicy(sizePolicy10)
        self.negative_prompt.setMinimumSize(QSize(0, 1))
        self.negative_prompt.setMaximumSize(QSize(16777215, 16777215))
        self.negative_prompt.setStyleSheet(u"QTextEdit QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QTextEdit QScrollBar::sub-line:vertical,\n"
"QTextEdit QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QTextEdit QScrollBar::sub-page:vertical,\n"
"QTextEdit QScrollBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.negative_prompt.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.negative_prompt.setAcceptRichText(False)

        self.verticalLayout_12.addWidget(self.negative_prompt)

        self.prompt_splitter.addWidget(self.left_prompt_tab_frame)
        self.right_prompt_tab_frame = QFrame(self.prompt_splitter)
        self.right_prompt_tab_frame.setObjectName(u"right_prompt_tab_frame")
        sizePolicy12 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy12.setHorizontalStretch(2)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.right_prompt_tab_frame.sizePolicy().hasHeightForWidth())
        self.right_prompt_tab_frame.setSizePolicy(sizePolicy12)
        self.right_prompt_tab_frame.setMinimumSize(QSize(665, 0))
        self.right_prompt_tab_frame.setStyleSheet(u"\n"
"QFrame{\n"
"border: 0px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border: 0px solid rgb(128,128,128); border-radius: 10px;\n"
"padding: 0px; /* To prevent the content from touching the border */\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }\n"
"QTextEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 2px solid rgb(128,128,128);\n"
"border-radius: 5px;\n"
"}")
        self.right_prompt_tab_frame.setLineWidth(0)
        self.right_prompt_tab_frame.setMidLineWidth(0)
        self.verticalLayout_20 = QVBoxLayout(self.right_prompt_tab_frame)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.prompt_morph_splitter = QSplitter(self.right_prompt_tab_frame)
        self.prompt_morph_splitter.setObjectName(u"prompt_morph_splitter")
        sizePolicy1.setHeightForWidth(self.prompt_morph_splitter.sizePolicy().hasHeightForWidth())
        self.prompt_morph_splitter.setSizePolicy(sizePolicy1)
        self.prompt_morph_splitter.setAutoFillBackground(False)
        self.prompt_morph_splitter.setFrameShape(QFrame.NoFrame)
        self.prompt_morph_splitter.setFrameShadow(QFrame.Raised)
        self.prompt_morph_splitter.setLineWidth(0)
        self.prompt_morph_splitter.setMidLineWidth(0)
        self.prompt_morph_splitter.setOrientation(Qt.Vertical)
        self.prompt_morph_splitter.setOpaqueResize(True)
        self.prompt_morph_splitter.setHandleWidth(0)
        self.prompt_morph_splitter.setChildrenCollapsible(True)
        self.middle_morph_frame = QFrame(self.prompt_morph_splitter)
        self.middle_morph_frame.setObjectName(u"middle_morph_frame")
        self.middle_morph_frame.setStyleSheet(u"border:0")
        self.middle_morph_frame.setFrameShape(QFrame.StyledPanel)
        self.middle_morph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.middle_morph_frame)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.Prompt_Morph_Key_Binding_Frame = QFrame(self.middle_morph_frame)
        self.Prompt_Morph_Key_Binding_Frame.setObjectName(u"Prompt_Morph_Key_Binding_Frame")
        sizePolicy1.setHeightForWidth(self.Prompt_Morph_Key_Binding_Frame.sizePolicy().hasHeightForWidth())
        self.Prompt_Morph_Key_Binding_Frame.setSizePolicy(sizePolicy1)
        self.Prompt_Morph_Key_Binding_Frame.setTabletTracking(False)
        self.Prompt_Morph_Key_Binding_Frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 0px  1px ;  /* To prevent the content from touching the border */\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }\n"
"QCheckBox{\n"
"border: 0px;\n"
"background-color: transparent;\n"
"}\n"
"QLabel{\n"
"padding: 0px; /* To prevent the content from touching the border */\n"
"border: 0px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border:0;\n"
"}")
        self.verticalLayout_29 = QVBoxLayout(self.Prompt_Morph_Key_Binding_Frame)
        self.verticalLayout_29.setSpacing(4)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(8, 8, 8, 5)
        self.frame_5 = QFrame(self.Prompt_Morph_Key_Binding_Frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 38))
        self.frame_5.setMaximumSize(QSize(16777215, 38))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 0px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px  1px ;  /* To prevent the content from touching the border */\n"
"}\n"
"QLabel{\n"
"padding: 0px; /* To prevent the content from touching the border */\n"
"border: 0px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.prompt_morphing_label = QLabel(self.frame_5)
        self.prompt_morphing_label.setObjectName(u"prompt_morphing_label")
        sizePolicy1.setHeightForWidth(self.prompt_morphing_label.sizePolicy().hasHeightForWidth())
        self.prompt_morphing_label.setSizePolicy(sizePolicy1)
        self.prompt_morphing_label.setMinimumSize(QSize(0, 34))
        self.prompt_morphing_label.setMaximumSize(QSize(16777215, 34))
        font7 = QFont()
        font7.setPointSize(15)
        font7.setBold(True)
        self.prompt_morphing_label.setFont(font7)
        self.prompt_morphing_label.setStyleSheet(u"")
        self.prompt_morphing_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.horizontalLayout_5.addWidget(self.prompt_morphing_label)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_8)

        self.save_morph_data = QPushButton(self.frame_5)
        self.save_morph_data.setObjectName(u"save_morph_data")
        self.save_morph_data.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.save_morph_data.sizePolicy().hasHeightForWidth())
        self.save_morph_data.setSizePolicy(sizePolicy1)
        self.save_morph_data.setMinimumSize(QSize(34, 38))
        self.save_morph_data.setSizeIncrement(QSize(6, 0))
        self.save_morph_data.setBaseSize(QSize(0, 0))
        self.save_morph_data.setFocusPolicy(Qt.StrongFocus)
        self.save_morph_data.setToolTipDuration(-1)
        self.save_morph_data.setAutoFillBackground(False)
        self.save_morph_data.setStyleSheet(u"QPushButton {\n"
"    /* Normal state */\n"
"    background-image: url(images/save_to_file_off.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"	border:0;\n"
"    border-radius: 0px;\n"
"    min-width: 32px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Hovered state */\n"
"    background-image: url(images/save_to_file_hover.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"	border:0;\n"
"    min-width: 32px;\n"
"    min-height: 36px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed state */\n"
"    background-image: url(images/save_to_file_active.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"	border:0;\n"
"    min-width: 32px;\n"
"    min-height: 36px;\n"
"}")
        self.save_morph_data.setIconSize(QSize(28, 20))

        self.horizontalLayout_5.addWidget(self.save_morph_data)

        self.save_current_ui_label_4 = QLabel(self.frame_5)
        self.save_current_ui_label_4.setObjectName(u"save_current_ui_label_4")
        self.save_current_ui_label_4.setMinimumSize(QSize(93, 35))
        self.save_current_ui_label_4.setStyleSheet(u"border: none;")
        self.save_current_ui_label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.save_current_ui_label_4.setWordWrap(True)

        self.horizontalLayout_5.addWidget(self.save_current_ui_label_4)


        self.verticalLayout_29.addWidget(self.frame_5)

        self.prompt_update_frame = QFrame(self.Prompt_Morph_Key_Binding_Frame)
        self.prompt_update_frame.setObjectName(u"prompt_update_frame")
        sizePolicy6.setHeightForWidth(self.prompt_update_frame.sizePolicy().hasHeightForWidth())
        self.prompt_update_frame.setSizePolicy(sizePolicy6)
        self.prompt_update_frame.setMinimumSize(QSize(0, 39))
        self.prompt_update_frame.setMaximumSize(QSize(16777215, 39))
        self.prompt_update_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border:0\n"
"}")
        self.prompt_update_frame.setFrameShape(QFrame.StyledPanel)
        self.prompt_update_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.prompt_update_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.use_deforumation_prompt_scheduling_checkbox = QCheckBox(self.prompt_update_frame)
        self.use_deforumation_prompt_scheduling_checkbox.setObjectName(u"use_deforumation_prompt_scheduling_checkbox")
        self.use_deforumation_prompt_scheduling_checkbox.setEnabled(True)
        sizePolicy13 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.use_deforumation_prompt_scheduling_checkbox.sizePolicy().hasHeightForWidth())
        self.use_deforumation_prompt_scheduling_checkbox.setSizePolicy(sizePolicy13)
        self.use_deforumation_prompt_scheduling_checkbox.setMinimumSize(QSize(0, 0))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        self.use_deforumation_prompt_scheduling_checkbox.setFont(font8)
        self.use_deforumation_prompt_scheduling_checkbox.setStyleSheet(u"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.use_deforumation_prompt_scheduling_checkbox.setIconSize(QSize(54, 29))
        self.use_deforumation_prompt_scheduling_checkbox.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.use_deforumation_prompt_scheduling_checkbox)

        self.horizontalSpacer = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.save_positive_prompt_style = QPushButton(self.prompt_update_frame)
        self.save_positive_prompt_style.setObjectName(u"save_positive_prompt_style")
        sizePolicy3.setHeightForWidth(self.save_positive_prompt_style.sizePolicy().hasHeightForWidth())
        self.save_positive_prompt_style.setSizePolicy(sizePolicy3)
        self.save_positive_prompt_style.setMinimumSize(QSize(60, 32))
        self.save_positive_prompt_style.setMaximumSize(QSize(16777215, 43))
        self.save_positive_prompt_style.setFont(font1)
        self.save_positive_prompt_style.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border-style: solid; /* Defines the style of the border */\n"
"    border-width: 2px; /* Width of the border */\n"
"    border-color: rgba(255, 255, 255, 0.5); /* Border color with some transparency */\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"    min-width: 32px;\n"
"	max-height:31px;\n"
"}\n"
"")

        self.horizontalLayout_4.addWidget(self.save_positive_prompt_style)


        self.verticalLayout_29.addWidget(self.prompt_update_frame)

        self.AddPromptMorp_Button = QPushButton(self.Prompt_Morph_Key_Binding_Frame)
        self.AddPromptMorp_Button.setObjectName(u"AddPromptMorp_Button")
        sizePolicy1.setHeightForWidth(self.AddPromptMorp_Button.sizePolicy().hasHeightForWidth())
        self.AddPromptMorp_Button.setSizePolicy(sizePolicy1)
        self.AddPromptMorp_Button.setMinimumSize(QSize(0, 27))
        self.AddPromptMorp_Button.setMaximumSize(QSize(16777215, 27))
        self.AddPromptMorp_Button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border-style: solid; /* Defines the style of the border */\n"
"    border-width: 1px; /* Width of the border */\n"
"    border-color: rgba(255, 255, 255, 0.5); /* Border color with some transparency */\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"\n"
"}\n"
"")

        self.verticalLayout_29.addWidget(self.AddPromptMorp_Button)

        self.frame_3 = QFrame(self.Prompt_Morph_Key_Binding_Frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 34))
        self.frame_3.setMaximumSize(QSize(16777215, 34))
        self.frame_3.setStyleSheet(u"QFrame{\n"
"border: 2px;\n"
"}\n"
"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.syrup_prompt_morph_label = QLabel(self.frame_3)
        self.syrup_prompt_morph_label.setObjectName(u"syrup_prompt_morph_label")
        self.syrup_prompt_morph_label.setStyleSheet(u"border-radius: 10px;")

        self.horizontalLayout_8.addWidget(self.syrup_prompt_morph_label)

        self.horizontalSpacer_9 = QSpacerItem(10, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)

        self.syrup_prompt_morph_slider = QSlider(self.frame_3)
        self.syrup_prompt_morph_slider.setObjectName(u"syrup_prompt_morph_slider")
        sizePolicy14 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy14.setHorizontalStretch(5)
        sizePolicy14.setVerticalStretch(0)
        sizePolicy14.setHeightForWidth(self.syrup_prompt_morph_slider.sizePolicy().hasHeightForWidth())
        self.syrup_prompt_morph_slider.setSizePolicy(sizePolicy14)
        self.syrup_prompt_morph_slider.setMinimumSize(QSize(0, 33))
        self.syrup_prompt_morph_slider.setMaximumSize(QSize(16777215, 32))
        self.syrup_prompt_morph_slider.setStyleSheet(u"QSlider{\n"
"background-color: transparent; /* Ensures background is transparent */\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230_m.png) ; /* Adjust slicing and stretch as needed */\n"
"    border: none;\n"
"    height: 29px; /* The height of your image */\n"
"\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width o"
                        "f the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
" border: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
" border: none;\n"
"}\n"
"")
        self.syrup_prompt_morph_slider.setMinimum(0)
        self.syrup_prompt_morph_slider.setMaximum(100)
        self.syrup_prompt_morph_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_8.addWidget(self.syrup_prompt_morph_slider)

        self.syrup_prompt_morph_value = QLineEdit(self.frame_3)
        self.syrup_prompt_morph_value.setObjectName(u"syrup_prompt_morph_value")
        self.syrup_prompt_morph_value.setMinimumSize(QSize(0, 33))
        self.syrup_prompt_morph_value.setMaximumSize(QSize(40, 33))
        self.syrup_prompt_morph_value.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"}")

        self.horizontalLayout_8.addWidget(self.syrup_prompt_morph_value)


        self.verticalLayout_29.addWidget(self.frame_3)

        self.scrollArea_Prompt_Morph_bindings = QScrollArea(self.Prompt_Morph_Key_Binding_Frame)
        self.scrollArea_Prompt_Morph_bindings.setObjectName(u"scrollArea_Prompt_Morph_bindings")
        sizePolicy15 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.scrollArea_Prompt_Morph_bindings.sizePolicy().hasHeightForWidth())
        self.scrollArea_Prompt_Morph_bindings.setSizePolicy(sizePolicy15)
        self.scrollArea_Prompt_Morph_bindings.setMinimumSize(QSize(0, 0))
        self.scrollArea_Prompt_Morph_bindings.setTabletTracking(False)
        self.scrollArea_Prompt_Morph_bindings.setStyleSheet(u"QScrollArea {\n"
"    border: 0px;\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrollBar::add-page:vertical {\n"
"    background: none; \n"
""
                        "border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_Prompt_Morph_bindings.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_Prompt_Morph_bindings.setWidgetResizable(True)
        self.scrollAreaWidgetContentsPromptMorph = QWidget()
        self.scrollAreaWidgetContentsPromptMorph.setObjectName(u"scrollAreaWidgetContentsPromptMorph")
        self.scrollAreaWidgetContentsPromptMorph.setGeometry(QRect(0, 0, 641, 0))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContentsPromptMorph.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsPromptMorph.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContentsPromptMorph.setMinimumSize(QSize(520, 0))
        self.scrollAreaWidgetContentsPromptMorph.setMaximumSize(QSize(16777215, 0))
        self.scrollAreaWidgetContentsPromptMorph.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 0px  0px ;  /* To prevent the content from touching the border */\n"
"}\n"
"QWidget{\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"")
        self.gridLayout_28 = QGridLayout(self.scrollAreaWidgetContentsPromptMorph)
        self.gridLayout_28.setSpacing(0)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.scrollAreaWidgetContentsPromptMorph)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 0))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 0))
        self.horizontalWidget.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border-style: solid; /* Defines the style of the border */\n"
"    border-width: 2px; /* Width of the border */\n"
"    border-color: rgba(255, 255, 255, 0.5); /* Border color with some transparency */\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"}\n"
"QFrame {\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
" padding: 0px; /* To prevent the content from touching the border */\n"
"}\n"
"")
        self.gridLayout_29 = QGridLayout(self.horizontalWidget)
        self.gridLayout_29.setSpacing(0)
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.gridLayout_29.setContentsMargins(0, 0, 0, 0)

        self.gridLayout_28.addWidget(self.horizontalWidget, 0, 0, 2, 1)

        self.scrollArea_Prompt_Morph_bindings.setWidget(self.scrollAreaWidgetContentsPromptMorph)

        self.verticalLayout_29.addWidget(self.scrollArea_Prompt_Morph_bindings)


        self.verticalLayout_28.addWidget(self.Prompt_Morph_Key_Binding_Frame)

        self.prompt_morph_splitter.addWidget(self.middle_morph_frame)
        self.lower_morph_frame = QFrame(self.prompt_morph_splitter)
        self.lower_morph_frame.setObjectName(u"lower_morph_frame")
        self.lower_morph_frame.setMinimumSize(QSize(0, 78))
        self.lower_morph_frame.setMaximumSize(QSize(16777215, 78))
        self.lower_morph_frame.setStyleSheet(u"border:0")
        self.lower_morph_frame.setFrameShape(QFrame.StyledPanel)
        self.lower_morph_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.lower_morph_frame)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 8, 0, 0)
        self.lower_right_prompt_frame = QFrame(self.lower_morph_frame)
        self.lower_right_prompt_frame.setObjectName(u"lower_right_prompt_frame")
        sizePolicy1.setHeightForWidth(self.lower_right_prompt_frame.sizePolicy().hasHeightForWidth())
        self.lower_right_prompt_frame.setSizePolicy(sizePolicy1)
        self.lower_right_prompt_frame.setMinimumSize(QSize(0, 70))
        self.lower_right_prompt_frame.setMaximumSize(QSize(16777215, 70))
        self.lower_right_prompt_frame.setStyleSheet(u"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }\n"
"QCheckBox{\n"
"border: 0px;\n"
"background-color: transparent;\n"
"}\n"
"QFrame {\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
" padding: 1px; /* To prevent the content from touching the border */\n"
"}")
        self.lower_right_prompt_frame.setFrameShape(QFrame.StyledPanel)
        self.lower_right_prompt_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.lower_right_prompt_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 1, -1, 1)
        self.frame_2 = QFrame(self.lower_right_prompt_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(298, 58))
        self.frame_2.setMaximumSize(QSize(290, 16777215))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"background-color: rgb(108,108,118);\n"
"border: 0px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 0px;\n"
" padding: 0px; /* To prevent the content from touching the border */\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.add_prompt_after_checkbox = QCheckBox(self.frame_2)
        self.add_prompt_after_checkbox.setObjectName(u"add_prompt_after_checkbox")
        self.add_prompt_after_checkbox.setEnabled(True)
        self.add_prompt_after_checkbox.setGeometry(QRect(0, 27, 289, 28))
        sizePolicy1.setHeightForWidth(self.add_prompt_after_checkbox.sizePolicy().hasHeightForWidth())
        self.add_prompt_after_checkbox.setSizePolicy(sizePolicy1)
        self.add_prompt_after_checkbox.setMinimumSize(QSize(0, 0))
        self.add_prompt_after_checkbox.setMaximumSize(QSize(16777215, 40))
        self.add_prompt_after_checkbox.setFont(font3)
        self.add_prompt_after_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.add_prompt_after_checkbox.setIconSize(QSize(54, 29))
        self.add_prompt_after_checkbox.setCheckable(True)
        self.add_prompt_before_checkbox = QCheckBox(self.frame_2)
        self.add_prompt_before_checkbox.setObjectName(u"add_prompt_before_checkbox")
        self.add_prompt_before_checkbox.setEnabled(True)
        self.add_prompt_before_checkbox.setGeometry(QRect(0, 4, 297, 28))
        sizePolicy1.setHeightForWidth(self.add_prompt_before_checkbox.sizePolicy().hasHeightForWidth())
        self.add_prompt_before_checkbox.setSizePolicy(sizePolicy1)
        self.add_prompt_before_checkbox.setMinimumSize(QSize(0, 0))
        self.add_prompt_before_checkbox.setMaximumSize(QSize(16777215, 40))
        self.add_prompt_before_checkbox.setFont(font3)
        self.add_prompt_before_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"border: none; /* No border for the checkbox */\n"
"}")
        self.add_prompt_before_checkbox.setIconSize(QSize(54, 29))
        self.add_prompt_before_checkbox.setCheckable(True)

        self.horizontalLayout_7.addWidget(self.frame_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)

        self.load_morph_data = QPushButton(self.lower_right_prompt_frame)
        self.load_morph_data.setObjectName(u"load_morph_data")
        self.load_morph_data.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.load_morph_data.sizePolicy().hasHeightForWidth())
        self.load_morph_data.setSizePolicy(sizePolicy7)
        self.load_morph_data.setMinimumSize(QSize(30, 25))
        self.load_morph_data.setBaseSize(QSize(0, 0))
        self.load_morph_data.setFocusPolicy(Qt.StrongFocus)
        self.load_morph_data.setToolTipDuration(-1)
        self.load_morph_data.setAutoFillBackground(False)
        self.load_morph_data.setStyleSheet(u"QPushButton {\n"
"    /* Normal state */\n"
"    background-image: url(images/Folder_off.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border-radius: 0px;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Hovered state */\n"
"    background-image: url(images/Folder_hover.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    min-width:28px;\n"
"    min-height: 23px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed state */\n"
"    background-image: url(images/Folder_active.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    min-width: 28px;\n"
"    min-height: 23px;\n"
"}\n"
"QPushButton{\n"
"background-color: transparent;\n"
"border:0;\n"
"}")
        self.load_morph_data.setIconSize(QSize(28, 20))

        self.horizontalLayout_7.addWidget(self.load_morph_data)

        self.save_current_ui_label_5 = QLabel(self.lower_right_prompt_frame)
        self.save_current_ui_label_5.setObjectName(u"save_current_ui_label_5")
        self.save_current_ui_label_5.setMinimumSize(QSize(0, 30))
        self.save_current_ui_label_5.setStyleSheet(u"border: none;")
        self.save_current_ui_label_5.setAlignment(Qt.AlignCenter)
        self.save_current_ui_label_5.setWordWrap(True)

        self.horizontalLayout_7.addWidget(self.save_current_ui_label_5)


        self.verticalLayout_30.addWidget(self.lower_right_prompt_frame)

        self.prompt_morph_splitter.addWidget(self.lower_morph_frame)

        self.verticalLayout_20.addWidget(self.prompt_morph_splitter)

        self.prompt_splitter.addWidget(self.right_prompt_tab_frame)

        self.horizontalLayout_6.addWidget(self.prompt_splitter)


        self.horizontalLayout_3.addWidget(self.Prompt_Frame)

        self.deforumation_tabWidget.addTab(self.Prompt_Tab, "")
        self.Movement_Tab = QWidget()
        self.Movement_Tab.setObjectName(u"Movement_Tab")
        sizePolicy1.setHeightForWidth(self.Movement_Tab.sizePolicy().hasHeightForWidth())
        self.Movement_Tab.setSizePolicy(sizePolicy1)
        self.Movement_Tab.setMinimumSize(QSize(0, 0))
        self.Movement_Tab.setMaximumSize(QSize(16777207, 16777215))
        self.Movement_Tab.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.Motion_Panning_Component_poppable = QFrame(self.Movement_Tab)
        self.Motion_Panning_Component_poppable.setObjectName(u"Motion_Panning_Component_poppable")
        self.Motion_Panning_Component_poppable.setGeometry(QRect(8, 8, 300, 430))
        self.Motion_Panning_Component_poppable.setTabletTracking(True)
        self.Motion_Panning_Component_poppable.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80); /* Fallback color */\n"
"    border: 2px solid rgb(22, 22, 22);\n"
"    border-radius: 5px;\n"
"\n"
"    background-position: center bottom; /* Centers horizontally and positions one third from the bottom */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"    height: 350px; /* Adjusted to your QFrame's height */\n"
"    width: 300px; /* Adjusted to your QFrame's width */\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Motion_Panning_Component_poppable.setFrameShape(QFrame.StyledPanel)
        self.Motion_Panning_Component_poppable.setFrameShadow(QFrame.Raised)
        self.motion_pan_button_left = QPushButton(self.Motion_Panning_Component_poppable)
        self.motion_pan_button_left.setObjectName(u"motion_pan_button_left")
        self.motion_pan_button_left.setGeometry(QRect(54, 294, 33, 37))
        sizePolicy7.setHeightForWidth(self.motion_pan_button_left.sizePolicy().hasHeightForWidth())
        self.motion_pan_button_left.setSizePolicy(sizePolicy7)
        self.motion_pan_button_left.setMinimumSize(QSize(33, 37))
        self.motion_pan_button_left.setMaximumSize(QSize(33, 34))
        self.motion_pan_button_left.setTabletTracking(True)
        self.motion_pan_button_left.setStyleSheet(u"border : 0")
        icon5 = QIcon()
        icon5.addFile(u"images/left_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon5.addFile(u"images/left_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon5.addFile(u"images/left_active.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_pan_button_left.setIcon(icon5)
        self.motion_pan_button_left.setIconSize(QSize(33, 37))
        self.motion_pan_button_down = QPushButton(self.Motion_Panning_Component_poppable)
        self.motion_pan_button_down.setObjectName(u"motion_pan_button_down")
        self.motion_pan_button_down.setGeometry(QRect(134, 378, 37, 33))
        sizePolicy7.setHeightForWidth(self.motion_pan_button_down.sizePolicy().hasHeightForWidth())
        self.motion_pan_button_down.setSizePolicy(sizePolicy7)
        self.motion_pan_button_down.setMinimumSize(QSize(37, 33))
        self.motion_pan_button_down.setMaximumSize(QSize(37, 33))
        self.motion_pan_button_down.setTabletTracking(True)
        self.motion_pan_button_down.setStyleSheet(u"border : 0")
        icon6 = QIcon()
        icon6.addFile(u"images/down_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon6.addFile(u"images/down_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon6.addFile(u"images/down_active.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_pan_button_down.setIcon(icon6)
        self.motion_pan_button_down.setIconSize(QSize(37, 33))
        self.motion_pan_button_up = QPushButton(self.Motion_Panning_Component_poppable)
        self.motion_pan_button_up.setObjectName(u"motion_pan_button_up")
        self.motion_pan_button_up.setGeometry(QRect(132, 216, 37, 33))
        sizePolicy7.setHeightForWidth(self.motion_pan_button_up.sizePolicy().hasHeightForWidth())
        self.motion_pan_button_up.setSizePolicy(sizePolicy7)
        self.motion_pan_button_up.setMinimumSize(QSize(37, 33))
        self.motion_pan_button_up.setMaximumSize(QSize(37, 33))
        font9 = QFont()
        font9.setKerning(True)
        font9.setStyleStrategy(QFont.PreferAntialias)
        self.motion_pan_button_up.setFont(font9)
        self.motion_pan_button_up.setTabletTracking(True)
        self.motion_pan_button_up.setStyleSheet(u"QPushButton {\n"
"    border: 0; /* Removes the default border */\n"
"    background-repeat: no-repeat;\n"
"    background-position: center;\n"
"   \n"
"}\n"
"\n"
"")
        icon7 = QIcon()
        icon7.addFile(u"images/upp_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon7.addFile(u"images/upp_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon7.addFile(u"images/upp_off.png", QSize(), QIcon.Disabled, QIcon.Off)
        icon7.addFile(u"images/upp_off.png", QSize(), QIcon.Disabled, QIcon.On)
        icon7.addFile(u"images/upp_active.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_pan_button_up.setIcon(icon7)
        self.motion_pan_button_up.setIconSize(QSize(53, 33))
        self.motion_pan_button_right = QPushButton(self.Motion_Panning_Component_poppable)
        self.motion_pan_button_right.setObjectName(u"motion_pan_button_right")
        self.motion_pan_button_right.setGeometry(QRect(216, 294, 33, 37))
        sizePolicy7.setHeightForWidth(self.motion_pan_button_right.sizePolicy().hasHeightForWidth())
        self.motion_pan_button_right.setSizePolicy(sizePolicy7)
        self.motion_pan_button_right.setMinimumSize(QSize(33, 37))
        self.motion_pan_button_right.setMaximumSize(QSize(33, 37))
        self.motion_pan_button_right.setTabletTracking(True)
        self.motion_pan_button_right.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u"images/right_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon8.addFile(u"images/right_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon8.addFile(u"images/right_active.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_pan_button_right.setIcon(icon8)
        self.motion_pan_button_right.setIconSize(QSize(33, 37))
        self.motion_pan_granularity = QLineEdit(self.Motion_Panning_Component_poppable)
        self.motion_pan_granularity.setObjectName(u"motion_pan_granularity")
        self.motion_pan_granularity.setGeometry(QRect(14, 236, 49, 22))
        self.motion_pan_granularity.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.panning_preset_label = QLabel(self.Motion_Panning_Component_poppable)
        self.panning_preset_label.setObjectName(u"panning_preset_label")
        self.panning_preset_label.setGeometry(QRect(10, 218, 105, 16))
        self.panning_preset_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.syrup_pan_motion_slider = QSlider(self.Motion_Panning_Component_poppable)
        self.syrup_pan_motion_slider.setObjectName(u"syrup_pan_motion_slider")
        self.syrup_pan_motion_slider.setGeometry(QRect(38, 108, 225, 34))
        self.syrup_pan_motion_slider.setStyleSheet(u"\n"
"/*QSlider {\n"
"    border: 2px solid #1B1D1F;\n"
"    border-radius: 15px;\n"
"}*/\n"
"\n"
"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::hand"
                        "le:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background:"
                        " none;\n"
"}\n"
" ")
        self.syrup_pan_motion_slider.setMaximum(100)
        self.syrup_pan_motion_slider.setOrientation(Qt.Horizontal)
        self.syrup_pan_motion_slider.setTickPosition(QSlider.TicksAbove)
        self.syrup_pan_motion_slider.setTickInterval(10)
        self.smooth_motion_steps_pan_label = QLabel(self.Motion_Panning_Component_poppable)
        self.smooth_motion_steps_pan_label.setObjectName(u"smooth_motion_steps_pan_label")
        self.smooth_motion_steps_pan_label.setGeometry(QRect(12, 78, 185, 25))
        self.smooth_motion_steps_pan_label.setFont(font3)
        self.smooth_motion_steps_pan_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.smooth_motion_steps_pan_label.setAlignment(Qt.AlignCenter)
        self.syrup_pan_motion_slider_frame_number = QLineEdit(self.Motion_Panning_Component_poppable)
        self.syrup_pan_motion_slider_frame_number.setObjectName(u"syrup_pan_motion_slider_frame_number")
        self.syrup_pan_motion_slider_frame_number.setGeometry(QRect(206, 82, 41, 22))
        self.syrup_pan_motion_slider_frame_number.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.pan_x_value = QLabel(self.Motion_Panning_Component_poppable)
        self.pan_x_value.setObjectName(u"pan_x_value")
        self.pan_x_value.setGeometry(QRect(6, 294, 32, 17))
        self.pan_x_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.pan_y_value = QLabel(self.Motion_Panning_Component_poppable)
        self.pan_y_value.setObjectName(u"pan_y_value")
        self.pan_y_value.setGeometry(QRect(116, 178, 33, 17))
        self.pan_y_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.motion_syrup_progressbar_x = QProgressBar(self.Motion_Panning_Component_poppable)
        self.motion_syrup_progressbar_x.setObjectName(u"motion_syrup_progressbar_x")
        self.motion_syrup_progressbar_x.setGeometry(QRect(34, 34, 125, 16))
        self.motion_syrup_progressbar_x.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}")
        self.motion_syrup_progressbar_x.setValue(100)
        self.motion_syrup_progressbar_x.setTextVisible(True)
        self.motion_syrup_progressbar_y = QProgressBar(self.Motion_Panning_Component_poppable)
        self.motion_syrup_progressbar_y.setObjectName(u"motion_syrup_progressbar_y")
        self.motion_syrup_progressbar_y.setGeometry(QRect(34, 58, 125, 16))
        self.motion_syrup_progressbar_y.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}")
        self.motion_syrup_progressbar_y.setValue(100)
        self.motion_syrup_progressbar_y.setTextVisible(True)
        self.syrup_x_label = QLabel(self.Motion_Panning_Component_poppable)
        self.syrup_x_label.setObjectName(u"syrup_x_label")
        self.syrup_x_label.setGeometry(QRect(10, 34, 16, 16))
        self.syrup_y_label = QLabel(self.Motion_Panning_Component_poppable)
        self.syrup_y_label.setObjectName(u"syrup_y_label")
        self.syrup_y_label.setGeometry(QRect(10, 58, 16, 16))
        self.exponential_pan_motion = QCheckBox(self.Motion_Panning_Component_poppable)
        self.exponential_pan_motion.setObjectName(u"exponential_pan_motion")
        self.exponential_pan_motion.setGeometry(QRect(10, 148, 281, 20))
        self.exponential_pan_motion.setLayoutDirection(Qt.RightToLeft)
        self.exponential_pan_motion.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.exponential_pan_motion.setIconSize(QSize(20, 20))
        self.exponential_pan_motion.setCheckable(True)
        self.pan_x_value_progress = QLabel(self.Motion_Panning_Component_poppable)
        self.pan_x_value_progress.setObjectName(u"pan_x_value_progress")
        self.pan_x_value_progress.setGeometry(QRect(6, 316, 32, 17))
        self.pan_x_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.pan_y_value_progress = QLabel(self.Motion_Panning_Component_poppable)
        self.pan_y_value_progress.setObjectName(u"pan_y_value_progress")
        self.pan_y_value_progress.setGeometry(QRect(152, 178, 33, 17))
        self.pan_y_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.Motion_Panning_Label = QLabel(self.Motion_Panning_Component_poppable)
        self.Motion_Panning_Label.setObjectName(u"Motion_Panning_Label")
        self.Motion_Panning_Label.setGeometry(QRect(68, 6, 167, 16))
        self.Motion_Panning_Label.setFont(font1)
        self.Motion_Panning_Label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.Motion_Panning_Label.setAlignment(Qt.AlignCenter)
        self.syrup_pan_curve_type = QComboBox(self.Motion_Panning_Component_poppable)
        self.syrup_pan_curve_type.addItem("")
        self.syrup_pan_curve_type.addItem("")
        self.syrup_pan_curve_type.addItem("")
        self.syrup_pan_curve_type.addItem("")
        self.syrup_pan_curve_type.addItem("")
        self.syrup_pan_curve_type.setObjectName(u"syrup_pan_curve_type")
        self.syrup_pan_curve_type.setGeometry(QRect(162, 56, 120, 19))
        self.syrup_pan_curve_type.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 5px;\n"
"color: rgb(0, 255, 0);\n"
"}\n"
"QFrame {\n"
"    background-color: rgb(70, 70, 70); /* Fallback color */\n"
"        color: rgb(0, 255, 0);\n"
"    \n"
"\n"
"}")
        self.pan_middle_button = QPushButton(self.Motion_Panning_Component_poppable)
        self.pan_middle_button.setObjectName(u"pan_middle_button")
        self.pan_middle_button.setGeometry(QRect(126, 286, 51, 51))
        self.pan_middle_button.setStyleSheet(u"border : 0")
        icon9 = QIcon()
        icon9.addFile(u"images/middle_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon9.addFile(u"images/middle_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon9.addFile(u"images/middle_active.png", QSize(), QIcon.Active, QIcon.On)
        self.pan_middle_button.setIcon(icon9)
        self.pan_middle_button.setIconSize(QSize(51, 51))
        self.Panning_Component = QLabel(self.Motion_Panning_Component_poppable)
        self.Panning_Component.setObjectName(u"Panning_Component")
        self.Panning_Component.setGeometry(QRect(40, 200, 222, 222))
        self.Panning_Component.setStyleSheet(u"  border: none;")
        self.Panning_Component.setPixmap(QPixmap(u"images/Panning_cross_embossed.png"))
        self.Panning_Component.setIndent(0)
        self.smooth_motion_curve_pan_label = QLabel(self.Motion_Panning_Component_poppable)
        self.smooth_motion_curve_pan_label.setObjectName(u"smooth_motion_curve_pan_label")
        self.smooth_motion_curve_pan_label.setGeometry(QRect(160, 30, 137, 16))
        self.smooth_motion_curve_pan_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.Motion_panning_checkbox = QCheckBox(self.Motion_Panning_Component_poppable)
        self.Motion_panning_checkbox.setObjectName(u"Motion_panning_checkbox")
        self.Motion_panning_checkbox.setGeometry(QRect(256, 6, 33, 20))
        sizePolicy1.setHeightForWidth(self.Motion_panning_checkbox.sizePolicy().hasHeightForWidth())
        self.Motion_panning_checkbox.setSizePolicy(sizePolicy1)
        self.Motion_panning_checkbox.setBaseSize(QSize(0, 0))
        self.Motion_panning_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.Motion_panning_checkbox.setIconSize(QSize(33, 20))
        self.Panning_Component.raise_()
        self.motion_pan_button_left.raise_()
        self.motion_pan_button_down.raise_()
        self.motion_pan_button_up.raise_()
        self.motion_pan_button_right.raise_()
        self.motion_pan_granularity.raise_()
        self.panning_preset_label.raise_()
        self.syrup_pan_motion_slider.raise_()
        self.smooth_motion_steps_pan_label.raise_()
        self.syrup_pan_motion_slider_frame_number.raise_()
        self.pan_x_value.raise_()
        self.pan_y_value.raise_()
        self.motion_syrup_progressbar_x.raise_()
        self.motion_syrup_progressbar_y.raise_()
        self.syrup_x_label.raise_()
        self.syrup_y_label.raise_()
        self.exponential_pan_motion.raise_()
        self.pan_x_value_progress.raise_()
        self.pan_y_value_progress.raise_()
        self.Motion_Panning_Label.raise_()
        self.syrup_pan_curve_type.raise_()
        self.pan_middle_button.raise_()
        self.smooth_motion_curve_pan_label.raise_()
        self.Motion_panning_checkbox.raise_()
        self.Motion_Rotation_Component_poppable = QFrame(self.Movement_Tab)
        self.Motion_Rotation_Component_poppable.setObjectName(u"Motion_Rotation_Component_poppable")
        self.Motion_Rotation_Component_poppable.setGeometry(QRect(314, 8, 300, 430))
        self.Motion_Rotation_Component_poppable.setTabletTracking(True)
        self.Motion_Rotation_Component_poppable.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80); /* Fallback color */\n"
"    border: 2px solid rgb(22, 22, 22);\n"
"    border-radius: 5px;\n"
"\n"
"    background-position: center bottom; /* Centers horizontally and positions one third from the bottom */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"    height: 350px; /* Adjusted to your QFrame's height */\n"
"    width: 300px; /* Adjusted to your QFrame's width */\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.Motion_Rotation_Component_poppable.setFrameShape(QFrame.StyledPanel)
        self.Motion_Rotation_Component_poppable.setFrameShadow(QFrame.Raised)
        self.motion_rotate_button_left = QPushButton(self.Motion_Rotation_Component_poppable)
        self.motion_rotate_button_left.setObjectName(u"motion_rotate_button_left")
        self.motion_rotate_button_left.setGeometry(QRect(54, 294, 33, 37))
        sizePolicy7.setHeightForWidth(self.motion_rotate_button_left.sizePolicy().hasHeightForWidth())
        self.motion_rotate_button_left.setSizePolicy(sizePolicy7)
        self.motion_rotate_button_left.setMinimumSize(QSize(33, 37))
        self.motion_rotate_button_left.setMaximumSize(QSize(33, 37))
        self.motion_rotate_button_left.setTabletTracking(True)
        self.motion_rotate_button_left.setStyleSheet(u"border : 0")
        self.motion_rotate_button_left.setIcon(icon5)
        self.motion_rotate_button_left.setIconSize(QSize(33, 37))
        self.motion_rotate_button_down = QPushButton(self.Motion_Rotation_Component_poppable)
        self.motion_rotate_button_down.setObjectName(u"motion_rotate_button_down")
        self.motion_rotate_button_down.setGeometry(QRect(134, 378, 37, 33))
        sizePolicy7.setHeightForWidth(self.motion_rotate_button_down.sizePolicy().hasHeightForWidth())
        self.motion_rotate_button_down.setSizePolicy(sizePolicy7)
        self.motion_rotate_button_down.setMinimumSize(QSize(37, 33))
        self.motion_rotate_button_down.setMaximumSize(QSize(37, 33))
        self.motion_rotate_button_down.setTabletTracking(True)
        self.motion_rotate_button_down.setStyleSheet(u"border : 0")
        self.motion_rotate_button_down.setIcon(icon6)
        self.motion_rotate_button_down.setIconSize(QSize(37, 33))
        self.motion_rotate_button_up = QPushButton(self.Motion_Rotation_Component_poppable)
        self.motion_rotate_button_up.setObjectName(u"motion_rotate_button_up")
        self.motion_rotate_button_up.setGeometry(QRect(132, 216, 37, 33))
        sizePolicy7.setHeightForWidth(self.motion_rotate_button_up.sizePolicy().hasHeightForWidth())
        self.motion_rotate_button_up.setSizePolicy(sizePolicy7)
        self.motion_rotate_button_up.setMinimumSize(QSize(37, 33))
        self.motion_rotate_button_up.setMaximumSize(QSize(37, 33))
        self.motion_rotate_button_up.setTabletTracking(True)
        self.motion_rotate_button_up.setStyleSheet(u"border : 0")
        icon10 = QIcon()
        icon10.addFile(u"images/upp_off.png", QSize(), QIcon.Normal, QIcon.Off)
        icon10.addFile(u"images/upp_hover.png", QSize(), QIcon.Normal, QIcon.On)
        icon10.addFile(u"images/upp_active.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_rotate_button_up.setIcon(icon10)
        self.motion_rotate_button_up.setIconSize(QSize(37, 33))
        self.motion_rotate_button_right = QPushButton(self.Motion_Rotation_Component_poppable)
        self.motion_rotate_button_right.setObjectName(u"motion_rotate_button_right")
        self.motion_rotate_button_right.setGeometry(QRect(216, 294, 33, 37))
        sizePolicy7.setHeightForWidth(self.motion_rotate_button_right.sizePolicy().hasHeightForWidth())
        self.motion_rotate_button_right.setSizePolicy(sizePolicy7)
        self.motion_rotate_button_right.setMinimumSize(QSize(33, 37))
        self.motion_rotate_button_right.setMaximumSize(QSize(33, 37))
        self.motion_rotate_button_right.setTabletTracking(True)
        self.motion_rotate_button_right.setStyleSheet(u"")
        self.motion_rotate_button_right.setIcon(icon8)
        self.motion_rotate_button_right.setIconSize(QSize(33, 37))
        self.motion_rotate_granularity = QLineEdit(self.Motion_Rotation_Component_poppable)
        self.motion_rotate_granularity.setObjectName(u"motion_rotate_granularity")
        self.motion_rotate_granularity.setGeometry(QRect(14, 236, 49, 22))
        self.motion_rotate_granularity.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.rot_preset_label = QLabel(self.Motion_Rotation_Component_poppable)
        self.rot_preset_label.setObjectName(u"rot_preset_label")
        self.rot_preset_label.setGeometry(QRect(10, 218, 105, 16))
        self.rot_preset_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.syrup_rotate_motion_slider = QSlider(self.Motion_Rotation_Component_poppable)
        self.syrup_rotate_motion_slider.setObjectName(u"syrup_rotate_motion_slider")
        self.syrup_rotate_motion_slider.setGeometry(QRect(38, 108, 225, 34))
        self.syrup_rotate_motion_slider.setStyleSheet(u"\n"
"/*QSlider {\n"
"    border: 2px solid #1B1D1F;\n"
"    border-radius: 15px;\n"
"}*/\n"
"\n"
"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::hand"
                        "le:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background:"
                        " none;\n"
"}\n"
" ")
        self.syrup_rotate_motion_slider.setMaximum(100)
        self.syrup_rotate_motion_slider.setOrientation(Qt.Horizontal)
        self.syrup_rotate_motion_slider.setTickPosition(QSlider.TicksAbove)
        self.syrup_rotate_motion_slider.setTickInterval(10)
        self.smooth_motion_curve_rot_label = QLabel(self.Motion_Rotation_Component_poppable)
        self.smooth_motion_curve_rot_label.setObjectName(u"smooth_motion_curve_rot_label")
        self.smooth_motion_curve_rot_label.setGeometry(QRect(160, 30, 137, 16))
        self.smooth_motion_curve_rot_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.syrup_rotate_motion_slider_frame_number = QLineEdit(self.Motion_Rotation_Component_poppable)
        self.syrup_rotate_motion_slider_frame_number.setObjectName(u"syrup_rotate_motion_slider_frame_number")
        self.syrup_rotate_motion_slider_frame_number.setGeometry(QRect(206, 82, 41, 22))
        self.syrup_rotate_motion_slider_frame_number.setMaximumSize(QSize(16777214, 16777215))
        self.syrup_rotate_motion_slider_frame_number.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.rotate_x_value = QLabel(self.Motion_Rotation_Component_poppable)
        self.rotate_x_value.setObjectName(u"rotate_x_value")
        self.rotate_x_value.setGeometry(QRect(6, 294, 32, 17))
        self.rotate_x_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.rotate_y_value = QLabel(self.Motion_Rotation_Component_poppable)
        self.rotate_y_value.setObjectName(u"rotate_y_value")
        self.rotate_y_value.setGeometry(QRect(116, 178, 33, 17))
        self.rotate_y_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.motion_syrup_progressbar_rx = QProgressBar(self.Motion_Rotation_Component_poppable)
        self.motion_syrup_progressbar_rx.setObjectName(u"motion_syrup_progressbar_rx")
        self.motion_syrup_progressbar_rx.setGeometry(QRect(34, 34, 125, 16))
        self.motion_syrup_progressbar_rx.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}")
        self.motion_syrup_progressbar_rx.setValue(100)
        self.motion_syrup_progressbar_rx.setTextVisible(True)
        self.motion_syrup_progressbar_ry = QProgressBar(self.Motion_Rotation_Component_poppable)
        self.motion_syrup_progressbar_ry.setObjectName(u"motion_syrup_progressbar_ry")
        self.motion_syrup_progressbar_ry.setGeometry(QRect(34, 58, 125, 16))
        self.motion_syrup_progressbar_ry.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}")
        self.motion_syrup_progressbar_ry.setValue(100)
        self.motion_syrup_progressbar_ry.setTextVisible(True)
        self.syrup_xr_label = QLabel(self.Motion_Rotation_Component_poppable)
        self.syrup_xr_label.setObjectName(u"syrup_xr_label")
        self.syrup_xr_label.setGeometry(QRect(6, 34, 25, 16))
        self.syrup_ry_label = QLabel(self.Motion_Rotation_Component_poppable)
        self.syrup_ry_label.setObjectName(u"syrup_ry_label")
        self.syrup_ry_label.setGeometry(QRect(6, 58, 25, 16))
        self.exponential_rotate_motion = QCheckBox(self.Motion_Rotation_Component_poppable)
        self.exponential_rotate_motion.setObjectName(u"exponential_rotate_motion")
        self.exponential_rotate_motion.setGeometry(QRect(10, 148, 281, 20))
        self.exponential_rotate_motion.setLayoutDirection(Qt.RightToLeft)
        self.exponential_rotate_motion.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.rotate_x_value_progress = QLabel(self.Motion_Rotation_Component_poppable)
        self.rotate_x_value_progress.setObjectName(u"rotate_x_value_progress")
        self.rotate_x_value_progress.setGeometry(QRect(6, 316, 32, 17))
        self.rotate_x_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.rotate_y_value_progress = QLabel(self.Motion_Rotation_Component_poppable)
        self.rotate_y_value_progress.setObjectName(u"rotate_y_value_progress")
        self.rotate_y_value_progress.setGeometry(QRect(152, 178, 33, 17))
        self.rotate_y_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.Motion_Rotation_Label = QLabel(self.Motion_Rotation_Component_poppable)
        self.Motion_Rotation_Label.setObjectName(u"Motion_Rotation_Label")
        self.Motion_Rotation_Label.setGeometry(QRect(64, 6, 163, 16))
        self.Motion_Rotation_Label.setFont(font1)
        self.Motion_Rotation_Label.setTabletTracking(False)
        self.Motion_Rotation_Label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.syrup_rotation_curve_type = QComboBox(self.Motion_Rotation_Component_poppable)
        self.syrup_rotation_curve_type.addItem("")
        self.syrup_rotation_curve_type.addItem("")
        self.syrup_rotation_curve_type.addItem("")
        self.syrup_rotation_curve_type.addItem("")
        self.syrup_rotation_curve_type.addItem("")
        self.syrup_rotation_curve_type.setObjectName(u"syrup_rotation_curve_type")
        self.syrup_rotation_curve_type.setGeometry(QRect(162, 56, 120, 19))
        self.syrup_rotation_curve_type.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 5px;\n"
"color: rgb(0, 255, 0);\n"
"}\n"
"QFrame {\n"
"    background-color: rgb(70, 70, 70); /* Fallback color */\n"
"        color: rgb(0, 255, 0);\n"
"    \n"
"\n"
"}")
        self.rotate_middle_button = QPushButton(self.Motion_Rotation_Component_poppable)
        self.rotate_middle_button.setObjectName(u"rotate_middle_button")
        self.rotate_middle_button.setGeometry(QRect(126, 286, 51, 51))
        self.rotate_middle_button.setStyleSheet(u"border : 0")
        self.rotate_middle_button.setIcon(icon9)
        self.rotate_middle_button.setIconSize(QSize(51, 51))
        self.smooth_motion_steps_rotation_label = QLabel(self.Motion_Rotation_Component_poppable)
        self.smooth_motion_steps_rotation_label.setObjectName(u"smooth_motion_steps_rotation_label")
        self.smooth_motion_steps_rotation_label.setGeometry(QRect(6, 79, 193, 25))
        self.smooth_motion_steps_rotation_label.setFont(font3)
        self.smooth_motion_steps_rotation_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.smooth_motion_steps_rotation_label.setAlignment(Qt.AlignCenter)
        self.Rotation_Component = QLabel(self.Motion_Rotation_Component_poppable)
        self.Rotation_Component.setObjectName(u"Rotation_Component")
        self.Rotation_Component.setGeometry(QRect(40, 200, 222, 222))
        self.Rotation_Component.setStyleSheet(u"  border: none;")
        self.Rotation_Component.setPixmap(QPixmap(u"images/Panning_cross_embossed.png"))
        self.Rotation_Component.setIndent(0)
        self.Motion_rotation_checkbox = QCheckBox(self.Motion_Rotation_Component_poppable)
        self.Motion_rotation_checkbox.setObjectName(u"Motion_rotation_checkbox")
        self.Motion_rotation_checkbox.setGeometry(QRect(256, 6, 33, 20))
        sizePolicy1.setHeightForWidth(self.Motion_rotation_checkbox.sizePolicy().hasHeightForWidth())
        self.Motion_rotation_checkbox.setSizePolicy(sizePolicy1)
        self.Motion_rotation_checkbox.setBaseSize(QSize(0, 0))
        self.Motion_rotation_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.Motion_rotation_checkbox.setIconSize(QSize(33, 20))
        self.Rotation_Component.raise_()
        self.motion_rotate_button_left.raise_()
        self.motion_rotate_button_down.raise_()
        self.motion_rotate_button_up.raise_()
        self.motion_rotate_button_right.raise_()
        self.motion_rotate_granularity.raise_()
        self.rot_preset_label.raise_()
        self.syrup_rotate_motion_slider.raise_()
        self.smooth_motion_curve_rot_label.raise_()
        self.syrup_rotate_motion_slider_frame_number.raise_()
        self.rotate_x_value.raise_()
        self.rotate_y_value.raise_()
        self.syrup_xr_label.raise_()
        self.syrup_ry_label.raise_()
        self.exponential_rotate_motion.raise_()
        self.rotate_x_value_progress.raise_()
        self.rotate_y_value_progress.raise_()
        self.Motion_Rotation_Label.raise_()
        self.motion_syrup_progressbar_rx.raise_()
        self.motion_syrup_progressbar_ry.raise_()
        self.syrup_rotation_curve_type.raise_()
        self.rotate_middle_button.raise_()
        self.smooth_motion_steps_rotation_label.raise_()
        self.Motion_rotation_checkbox.raise_()
        self.Motion_Tilt_Component_poppable = QFrame(self.Movement_Tab)
        self.Motion_Tilt_Component_poppable.setObjectName(u"Motion_Tilt_Component_poppable")
        self.Motion_Tilt_Component_poppable.setGeometry(QRect(826, 8, 300, 430))
        self.Motion_Tilt_Component_poppable.setTabletTracking(True)
        self.Motion_Tilt_Component_poppable.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80); /* Fallback color */\n"
"    border: 2px solid rgb(22, 22, 22);\n"
"    border-radius: 5px;\n"
"\n"
"    background-position: center bottom; /* Centers horizontally and positions one third from the bottom */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"    height: 350px; /* Adjusted to your QFrame's height */\n"
"    width: 300px; /* Adjusted to your QFrame's width */\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }\n"
"\n"
"\n"
"")
        self.Motion_Tilt_Component_poppable.setFrameShape(QFrame.StyledPanel)
        self.Motion_Tilt_Component_poppable.setFrameShadow(QFrame.Raised)
        self.motion_tilt_granularity = QLineEdit(self.Motion_Tilt_Component_poppable)
        self.motion_tilt_granularity.setObjectName(u"motion_tilt_granularity")
        self.motion_tilt_granularity.setGeometry(QRect(28, 228, 49, 22))
        self.motion_tilt_granularity.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.tilt_preset_label = QLabel(self.Motion_Tilt_Component_poppable)
        self.tilt_preset_label.setObjectName(u"tilt_preset_label")
        self.tilt_preset_label.setGeometry(QRect(23, 208, 75, 16))
        self.tilt_preset_label.setStyleSheet(u"border: 0")
        self.syrup_tilt_motion_slider = QSlider(self.Motion_Tilt_Component_poppable)
        self.syrup_tilt_motion_slider.setObjectName(u"syrup_tilt_motion_slider")
        self.syrup_tilt_motion_slider.setGeometry(QRect(66, 168, 169, 34))
        self.syrup_tilt_motion_slider.setStyleSheet(u"\n"
"/*QSlider {\n"
"    border: 2px solid #1B1D1F;\n"
"    border-radius: 15px;\n"
"}*/\n"
"\n"
"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_130.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 150px; /* Width of the handle - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::hand"
                        "le:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background:"
                        " none;\n"
"}\n"
" ")
        self.syrup_tilt_motion_slider.setMaximum(100)
        self.syrup_tilt_motion_slider.setOrientation(Qt.Horizontal)
        self.syrup_tilt_motion_slider.setTickPosition(QSlider.TicksAbove)
        self.syrup_tilt_motion_slider.setTickInterval(10)
        self.smooth_motion_steps_tilt_label = QLabel(self.Motion_Tilt_Component_poppable)
        self.smooth_motion_steps_tilt_label.setObjectName(u"smooth_motion_steps_tilt_label")
        self.smooth_motion_steps_tilt_label.setGeometry(QRect(36, 134, 159, 25))
        self.smooth_motion_steps_tilt_label.setFont(font3)
        self.smooth_motion_steps_tilt_label.setStyleSheet(u"border: 0")
        self.smooth_motion_steps_tilt_label.setAlignment(Qt.AlignCenter)
        self.syrup_tilt_motion_slider_frame_number = QLineEdit(self.Motion_Tilt_Component_poppable)
        self.syrup_tilt_motion_slider_frame_number.setObjectName(u"syrup_tilt_motion_slider_frame_number")
        self.syrup_tilt_motion_slider_frame_number.setGeometry(QRect(204, 136, 41, 22))
        self.syrup_tilt_motion_slider_frame_number.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.rotate_z_value = QLabel(self.Motion_Tilt_Component_poppable)
        self.rotate_z_value.setObjectName(u"rotate_z_value")
        self.rotate_z_value.setGeometry(QRect(136, 212, 33, 16))
        self.rotate_z_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.motion_syrup_progressbar_rz = QProgressBar(self.Motion_Tilt_Component_poppable)
        self.motion_syrup_progressbar_rz.setObjectName(u"motion_syrup_progressbar_rz")
        self.motion_syrup_progressbar_rz.setGeometry(QRect(72, 34, 153, 16))
        self.motion_syrup_progressbar_rz.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0,\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}")
        self.motion_syrup_progressbar_rz.setValue(100)
        self.motion_syrup_progressbar_rz.setTextVisible(True)
        self.syrup_z_tilt_label = QLabel(self.Motion_Tilt_Component_poppable)
        self.syrup_z_tilt_label.setObjectName(u"syrup_z_tilt_label")
        self.syrup_z_tilt_label.setGeometry(QRect(52, 34, 16, 16))
        self.exponential_tilt_motion = QCheckBox(self.Motion_Tilt_Component_poppable)
        self.exponential_tilt_motion.setObjectName(u"exponential_tilt_motion")
        self.exponential_tilt_motion.setGeometry(QRect(32, 108, 201, 20))
        self.exponential_tilt_motion.setLayoutDirection(Qt.RightToLeft)
        self.exponential_tilt_motion.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 34px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.rotate_z_value_progress = QLabel(self.Motion_Tilt_Component_poppable)
        self.rotate_z_value_progress.setObjectName(u"rotate_z_value_progress")
        self.rotate_z_value_progress.setGeometry(QRect(136, 232, 33, 16))
        self.rotate_z_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.Motion_Tilt_Label = QLabel(self.Motion_Tilt_Component_poppable)
        self.Motion_Tilt_Label.setObjectName(u"Motion_Tilt_Label")
        self.Motion_Tilt_Label.setGeometry(QRect(86, 6, 121, 16))
        self.Motion_Tilt_Label.setFont(font1)
        self.Motion_Tilt_Label.setStyleSheet(u"border: 0")
        self.Motion_Tilt_Label.setAlignment(Qt.AlignCenter)
        self.syrup_tilt_curve_type = QComboBox(self.Motion_Tilt_Component_poppable)
        self.syrup_tilt_curve_type.addItem("")
        self.syrup_tilt_curve_type.addItem("")
        self.syrup_tilt_curve_type.addItem("")
        self.syrup_tilt_curve_type.addItem("")
        self.syrup_tilt_curve_type.addItem("")
        self.syrup_tilt_curve_type.setObjectName(u"syrup_tilt_curve_type")
        self.syrup_tilt_curve_type.setGeometry(QRect(94, 78, 105, 19))
        self.syrup_tilt_curve_type.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 5px;\n"
"color: rgb(0, 255, 0);\n"
"}\n"
"QFrame {\n"
"    background-color: rgb(70, 70, 70); /* Fallback color */\n"
"        color: rgb(0, 255, 0);\n"
"    \n"
"\n"
"}")
        self.Motion_tilt_checkbox = QCheckBox(self.Motion_Tilt_Component_poppable)
        self.Motion_tilt_checkbox.setObjectName(u"Motion_tilt_checkbox")
        self.Motion_tilt_checkbox.setGeometry(QRect(256, 6, 33, 20))
        sizePolicy1.setHeightForWidth(self.Motion_tilt_checkbox.sizePolicy().hasHeightForWidth())
        self.Motion_tilt_checkbox.setSizePolicy(sizePolicy1)
        self.Motion_tilt_checkbox.setBaseSize(QSize(0, 0))
        self.Motion_tilt_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.Motion_tilt_checkbox.setIconSize(QSize(33, 20))
        self.smooth_motion_curve_tilt_label = QLabel(self.Motion_Tilt_Component_poppable)
        self.smooth_motion_curve_tilt_label.setObjectName(u"smooth_motion_curve_tilt_label")
        self.smooth_motion_curve_tilt_label.setGeometry(QRect(94, 52, 129, 20))
        self.smooth_motion_curve_tilt_label.setStyleSheet(u"border: 0")
        self.Tilt_Component = QLabel(self.Motion_Tilt_Component_poppable)
        self.Tilt_Component.setObjectName(u"Tilt_Component")
        self.Tilt_Component.setGeometry(QRect(68, 254, 169, 161))
        self.Tilt_Component.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.Tilt_Component.setPixmap(QPixmap(u"images/tilt_circle.png"))
        self.Tilt_Component.setAlignment(Qt.AlignCenter)
        self.motion_tilt_button_left = QPushButton(self.Motion_Tilt_Component_poppable)
        self.motion_tilt_button_left.setObjectName(u"motion_tilt_button_left")
        self.motion_tilt_button_left.setGeometry(QRect(78, 258, 75, 79))
        sizePolicy7.setHeightForWidth(self.motion_tilt_button_left.sizePolicy().hasHeightForWidth())
        self.motion_tilt_button_left.setSizePolicy(sizePolicy7)
        self.motion_tilt_button_left.setMinimumSize(QSize(75, 79))
        self.motion_tilt_button_left.setMaximumSize(QSize(7579, 71))
        self.motion_tilt_button_left.setTabletTracking(True)
        self.motion_tilt_button_left.setStyleSheet(u"border : 0")
        icon11 = QIcon()
        icon11.addFile(u"images/tilt_left.png", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u"images/tilt_left_press.png", QSize(), QIcon.Normal, QIcon.On)
        self.motion_tilt_button_left.setIcon(icon11)
        self.motion_tilt_button_left.setIconSize(QSize(75, 79))
        self.motion_tilt_button_right = QPushButton(self.Motion_Tilt_Component_poppable)
        self.motion_tilt_button_right.setObjectName(u"motion_tilt_button_right")
        self.motion_tilt_button_right.setGeometry(QRect(152, 258, 76, 79))
        sizePolicy7.setHeightForWidth(self.motion_tilt_button_right.sizePolicy().hasHeightForWidth())
        self.motion_tilt_button_right.setSizePolicy(sizePolicy7)
        self.motion_tilt_button_right.setMinimumSize(QSize(76, 79))
        self.motion_tilt_button_right.setMaximumSize(QSize(76, 79))
        self.motion_tilt_button_right.setTabletTracking(True)
        self.motion_tilt_button_right.setStyleSheet(u"border : 0")
        icon12 = QIcon()
        icon12.addFile(u"images/tilt_right.png", QSize(), QIcon.Normal, QIcon.Off)
        icon12.addFile(u"images/tilt_right_press.png", QSize(), QIcon.Normal, QIcon.On)
        icon12.addFile(u"images/tilt_right_press.png", QSize(), QIcon.Active, QIcon.On)
        self.motion_tilt_button_right.setIcon(icon12)
        self.motion_tilt_button_right.setIconSize(QSize(76, 79))
        self.tilt_middle_button = QPushButton(self.Motion_Tilt_Component_poppable)
        self.tilt_middle_button.setObjectName(u"tilt_middle_button")
        self.tilt_middle_button.setGeometry(QRect(126, 308, 51, 51))
        self.tilt_middle_button.setStyleSheet(u"border : 0")
        self.tilt_middle_button.setIcon(icon9)
        self.tilt_middle_button.setIconSize(QSize(51, 51))
        self.Motion_Fov_Component_poppable = QFrame(self.Movement_Tab)
        self.Motion_Fov_Component_poppable.setObjectName(u"Motion_Fov_Component_poppable")
        self.Motion_Fov_Component_poppable.setGeometry(QRect(1132, 6, 160, 430))
        self.Motion_Fov_Component_poppable.setTabletTracking(True)
        self.Motion_Fov_Component_poppable.setStyleSheet(u"QFrame{\n"
"background-color: rgb(80, 80, 80); /* Fallback color */    \n"
"border: 2px solid rgb(22, 22, 22);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.Motion_Fov_Component_poppable.setFrameShape(QFrame.StyledPanel)
        self.Motion_Fov_Component_poppable.setFrameShadow(QFrame.Raised)
        self.motion_fov_slider = QSlider(self.Motion_Fov_Component_poppable)
        self.motion_fov_slider.setObjectName(u"motion_fov_slider")
        self.motion_fov_slider.setGeometry(QRect(68, 100, 34, 235))
        self.motion_fov_slider.setStyleSheet(u"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-image: url(images/groove_230_vertical.png); /* Adjust slicing and stretch as needed */\n"
"    width: 29px; /* The width of your image */\n"
"    height: 225px; /* Height of the groove - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image"
                        " when hovering */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.motion_fov_slider.setMinimum(20)
        self.motion_fov_slider.setMaximum(120)
        self.motion_fov_slider.setValue(70)
        self.motion_fov_slider.setOrientation(Qt.Vertical)
        self.motion_fov_slider.setTickPosition(QSlider.TicksAbove)
        self.motion_fov_slider.setTickInterval(10)
        self.max_fov = QLabel(self.Motion_Fov_Component_poppable)
        self.max_fov.setObjectName(u"max_fov")
        self.max_fov.setGeometry(QRect(70, 80, 33, 16))
        self.max_fov.setStyleSheet(u"border: 0")
        self.min_fov = QLabel(self.Motion_Fov_Component_poppable)
        self.min_fov.setObjectName(u"min_fov")
        self.min_fov.setGeometry(QRect(76, 340, 25, 16))
        self.min_fov.setStyleSheet(u"border: 0")
        self.Motion_Fov = QLabel(self.Motion_Fov_Component_poppable)
        self.Motion_Fov.setObjectName(u"Motion_Fov")
        self.Motion_Fov.setGeometry(QRect(10, 6, 97, 16))
        self.Motion_Fov.setFont(font3)
        self.Motion_Fov.setStyleSheet(u"border: 0")
        self.Motion_Fov.setAlignment(Qt.AlignCenter)
        self.fov_value = QLabel(self.Motion_Fov_Component_poppable)
        self.fov_value.setObjectName(u"fov_value")
        self.fov_value.setGeometry(QRect(40, 210, 27, 16))
        self.fov_value.setStyleSheet(u"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.Motion_fow_checkbox = QCheckBox(self.Motion_Fov_Component_poppable)
        self.Motion_fow_checkbox.setObjectName(u"Motion_fow_checkbox")
        self.Motion_fow_checkbox.setGeometry(QRect(116, 6, 33, 20))
        sizePolicy1.setHeightForWidth(self.Motion_fow_checkbox.sizePolicy().hasHeightForWidth())
        self.Motion_fow_checkbox.setSizePolicy(sizePolicy1)
        self.Motion_fow_checkbox.setBaseSize(QSize(0, 0))
        self.Motion_fow_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.Motion_fow_checkbox.setIconSize(QSize(33, 20))
        self.Motion_Zoom_Component_poppable = QFrame(self.Movement_Tab)
        self.Motion_Zoom_Component_poppable.setObjectName(u"Motion_Zoom_Component_poppable")
        self.Motion_Zoom_Component_poppable.setGeometry(QRect(620, 8, 200, 430))
        self.Motion_Zoom_Component_poppable.setTabletTracking(True)
        self.Motion_Zoom_Component_poppable.setStyleSheet(u"QFrame {\n"
"    background-color: rgb(80, 80, 80); /* Fallback color */\n"
"    border: 2px solid rgb(22, 22, 22);\n"
"    border-radius: 5px;\n"
"\n"
"    background-position: center bottom; /* Centers horizontally and positions one third from the bottom */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"    height: 350px; /* Adjusted to your QFrame's height */\n"
"    width: 300px; /* Adjusted to your QFrame's width */\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.Motion_Zoom_Component_poppable.setFrameShape(QFrame.StyledPanel)
        self.Motion_Zoom_Component_poppable.setFrameShadow(QFrame.Raised)
        self.motion_zoom_slider = QSlider(self.Motion_Zoom_Component_poppable)
        self.motion_zoom_slider.setObjectName(u"motion_zoom_slider")
        self.motion_zoom_slider.setGeometry(QRect(42, 126, 34, 190))
        self.motion_zoom_slider.setStyleSheet(u"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-image: url(images/groove_230_vertical.png); /* Adjust slicing and stretch as needed */\n"
"    width: 29px; /* The width of your image */\n"
"    height: 180px; /* Height of the groove - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image"
                        " when hovering */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.motion_zoom_slider.setMinimum(-100)
        self.motion_zoom_slider.setMaximum(100)
        self.motion_zoom_slider.setOrientation(Qt.Vertical)
        self.motion_zoom_slider.setTickPosition(QSlider.TicksAbove)
        self.motion_zoom_slider.setTickInterval(10)
        self.motion_zoom_granularity = QSlider(self.Motion_Zoom_Component_poppable)
        self.motion_zoom_granularity.setObjectName(u"motion_zoom_granularity")
        self.motion_zoom_granularity.setGeometry(QRect(26, 362, 151, 34))
        self.motion_zoom_granularity.setStyleSheet(u"\n"
"/*QSlider {\n"
"    border: 2px solid #1B1D1F;\n"
"    border-radius: 15px;\n"
"}*/\n"
"\n"
"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_130.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 140px; /* Width of the handle - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::hand"
                        "le:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background:"
                        " none;\n"
"}\n"
" ")
        self.motion_zoom_granularity.setMinimum(1)
        self.motion_zoom_granularity.setMaximum(10)
        self.motion_zoom_granularity.setPageStep(1)
        self.motion_zoom_granularity.setOrientation(Qt.Horizontal)
        self.motion_zoom_granularity.setTickPosition(QSlider.TicksBelow)
        self.motion_zoom_granularity.setTickInterval(1)
        self.max_zoom = QLabel(self.Motion_Zoom_Component_poppable)
        self.max_zoom.setObjectName(u"max_zoom")
        self.max_zoom.setGeometry(QRect(44, 106, 31, 16))
        self.max_zoom.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.min_zoom = QLabel(self.Motion_Zoom_Component_poppable)
        self.min_zoom.setObjectName(u"min_zoom")
        self.min_zoom.setGeometry(QRect(40, 320, 37, 16))
        self.min_zoom.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.Motion_Zoom_Label = QLabel(self.Motion_Zoom_Component_poppable)
        self.Motion_Zoom_Label.setObjectName(u"Motion_Zoom_Label")
        self.Motion_Zoom_Label.setGeometry(QRect(8, 6, 133, 16))
        self.Motion_Zoom_Label.setFont(font1)
        self.Motion_Zoom_Label.setStyleSheet(u"border: 0")
        self.Motion_Zoom_Label.setAlignment(Qt.AlignCenter)
        self.syrup_zoom_motion_slider_frame_number = QLineEdit(self.Motion_Zoom_Component_poppable)
        self.syrup_zoom_motion_slider_frame_number.setObjectName(u"syrup_zoom_motion_slider_frame_number")
        self.syrup_zoom_motion_slider_frame_number.setGeometry(QRect(152, 78, 41, 22))
        self.syrup_zoom_motion_slider_frame_number.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.smooth_motion_curve_zoom_label = QLabel(self.Motion_Zoom_Component_poppable)
        self.smooth_motion_curve_zoom_label.setObjectName(u"smooth_motion_curve_zoom_label")
        self.smooth_motion_curve_zoom_label.setGeometry(QRect(36, 30, 145, 20))
        self.smooth_motion_curve_zoom_label.setStyleSheet(u"border: 0")
        self.syrup_zoom_motion_slider = QSlider(self.Motion_Zoom_Component_poppable)
        self.syrup_zoom_motion_slider.setObjectName(u"syrup_zoom_motion_slider")
        self.syrup_zoom_motion_slider.setGeometry(QRect(99, 105, 34, 230))
        self.syrup_zoom_motion_slider.setStyleSheet(u"QSlider {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 15px;\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-image: url(images/groove_230_vertical.png); /* Adjust slicing and stretch as needed */\n"
"    width: 29px; /* The width of your image */\n"
"    height: 225px; /* Height of the groove - adjust as needed */\n"
"    border: none; /* Ensures no border */\n"
"}\n"
"\n"
"QSlider::handle:vertical {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:hover {\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image"
                        " when hovering */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:vertical:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"    background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: 0 -2px; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::add-page:vertical {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:vertical {\n"
"    background: none;\n"
"}\n"
"")
        self.syrup_zoom_motion_slider.setMinimum(0)
        self.syrup_zoom_motion_slider.setMaximum(100)
        self.syrup_zoom_motion_slider.setOrientation(Qt.Vertical)
        self.syrup_zoom_motion_slider.setTickPosition(QSlider.TicksAbove)
        self.syrup_zoom_motion_slider.setTickInterval(10)
        self.pan_z_value = QLabel(self.Motion_Zoom_Component_poppable)
        self.pan_z_value.setObjectName(u"pan_z_value")
        self.pan_z_value.setGeometry(QRect(6, 206, 32, 16))
        self.pan_z_value.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.pan_z_value_progress = QLabel(self.Motion_Zoom_Component_poppable)
        self.pan_z_value_progress.setObjectName(u"pan_z_value_progress")
        self.pan_z_value_progress.setGeometry(QRect(6, 226, 32, 16))
        self.pan_z_value_progress.setStyleSheet(u"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"color: rgb(0, 255, 0);\n"
"border-radius: 4px;\n"
"padding: 1px; /* To prevent the content from touching the border */")
        self.motion_syrup_progressbar_z = QProgressBar(self.Motion_Zoom_Component_poppable)
        self.motion_syrup_progressbar_z.setObjectName(u"motion_syrup_progressbar_z")
        self.motion_syrup_progressbar_z.setGeometry(QRect(138, 130, 39, 181))
        font10 = QFont()
        font10.setPointSize(9)
        font10.setBold(True)
        self.motion_syrup_progressbar_z.setFont(font10)
        self.motion_syrup_progressbar_z.setLayoutDirection(Qt.LeftToRight)
        self.motion_syrup_progressbar_z.setStyleSheet(u"QProgressBar {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 2px;\n"
"    background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, /* Vertical gradient */\n"
"                                 stop: 0 #00ff00,   /* Green at the start */\n"
"                                 stop: 0.8 #ffff00, /* Yellow in the middle */\n"
"                                 stop: 1 #ff0000 ); /* Red at the end */\n"
"}\n"
"QProgressBar[orientation=\"vertical\"] {\n"
"    text-align: center;\n"
"    color: rgb(0, 0, 0);\n"
"    border-width: 2px;\n"
"    border-radius: 2px;\n"
"    border-color: rgb(58, 58, 58);\n"
"    border-style: inset;\n"
"    background-color: rgb(77, 77, 77);\n"
"}")
        self.motion_syrup_progressbar_z.setValue(100)
        self.motion_syrup_progressbar_z.setTextVisible(True)
        self.motion_syrup_progressbar_z.setOrientation(Qt.Vertical)
        self.syrup_zoom_label = QLabel(self.Motion_Zoom_Component_poppable)
        self.syrup_zoom_label.setObjectName(u"syrup_zoom_label")
        self.syrup_zoom_label.setGeometry(QRect(148, 110, 16, 16))
        self.syrup_zoom_label.setStyleSheet(u"background: none;\n"
"border: 1px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"    border-radius: 4px;\n"
"    padding: 1px; /* To prevent the content from touching the border */")
        self.syrup_zoom_curve_type = QComboBox(self.Motion_Zoom_Component_poppable)
        self.syrup_zoom_curve_type.addItem("")
        self.syrup_zoom_curve_type.addItem("")
        self.syrup_zoom_curve_type.addItem("")
        self.syrup_zoom_curve_type.addItem("")
        self.syrup_zoom_curve_type.addItem("")
        self.syrup_zoom_curve_type.setObjectName(u"syrup_zoom_curve_type")
        self.syrup_zoom_curve_type.setGeometry(QRect(36, 56, 120, 19))
        self.syrup_zoom_curve_type.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 5px;\n"
"color: rgb(0, 255, 0);\n"
"}\n"
"QFrame {\n"
"    background-color: rgb(70, 70, 70); /* Fallback color */\n"
"        color: rgb(0, 255, 0);\n"
"    \n"
"\n"
"}")
        self.zoom_preset_label = QLabel(self.Motion_Zoom_Component_poppable)
        self.zoom_preset_label.setObjectName(u"zoom_preset_label")
        self.zoom_preset_label.setGeometry(QRect(62, 340, 89, 16))
        self.zoom_preset_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.Motion_zoom_checkbox = QCheckBox(self.Motion_Zoom_Component_poppable)
        self.Motion_zoom_checkbox.setObjectName(u"Motion_zoom_checkbox")
        self.Motion_zoom_checkbox.setGeometry(QRect(156, 6, 33, 20))
        sizePolicy1.setHeightForWidth(self.Motion_zoom_checkbox.sizePolicy().hasHeightForWidth())
        self.Motion_zoom_checkbox.setSizePolicy(sizePolicy1)
        self.Motion_zoom_checkbox.setBaseSize(QSize(0, 0))
        self.Motion_zoom_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(80, 80, 80); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbo"
                        "x */\n"
"}\n"
"")
        self.Motion_zoom_checkbox.setIconSize(QSize(33, 20))
        self.smooth_motion_steps_zoom_label = QLabel(self.Motion_Zoom_Component_poppable)
        self.smooth_motion_steps_zoom_label.setObjectName(u"smooth_motion_steps_zoom_label")
        self.smooth_motion_steps_zoom_label.setGeometry(QRect(8, 78, 145, 20))
        self.smooth_motion_steps_zoom_label.setFont(font3)
        self.smooth_motion_steps_zoom_label.setStyleSheet(u"border: 0")
        self.smooth_motion_steps_zoom_label.setAlignment(Qt.AlignCenter)
        self.motion_zoom_granularity_special = QLineEdit(self.Motion_Zoom_Component_poppable)
        self.motion_zoom_granularity_special.setObjectName(u"motion_zoom_granularity_special")
        self.motion_zoom_granularity_special.setGeometry(QRect(132, 400, 49, 22))
        self.motion_zoom_granularity_special.setStyleSheet(u"QLineEdit{\n"
"background-color:rgb(42, 42, 42);\n"
"color: rgb(0, 255, 0);\n"
"border: 1px solid rgb(128,128,128);\n"
"border-radius: 2px;\n"
"}")
        self.zoom_preset_special_label = QLabel(self.Motion_Zoom_Component_poppable)
        self.zoom_preset_special_label.setObjectName(u"zoom_preset_special_label")
        self.zoom_preset_special_label.setGeometry(QRect(16, 402, 107, 16))
        self.zoom_preset_special_label.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.motion_zoom_button_forwards = QPushButton(self.Motion_Zoom_Component_poppable)
        self.motion_zoom_button_forwards.setObjectName(u"motion_zoom_button_forwards")
        self.motion_zoom_button_forwards.setGeometry(QRect(78, 208, 16, 16))
        sizePolicy7.setHeightForWidth(self.motion_zoom_button_forwards.sizePolicy().hasHeightForWidth())
        self.motion_zoom_button_forwards.setSizePolicy(sizePolicy7)
        self.motion_zoom_button_forwards.setMinimumSize(QSize(16, 16))
        self.motion_zoom_button_forwards.setMaximumSize(QSize(16, 16))
        self.motion_zoom_button_forwards.setTabletTracking(True)
        self.motion_zoom_button_forwards.setStyleSheet(u"border : 0;background: none;")
        self.motion_zoom_button_forwards.setIcon(icon10)
        self.motion_zoom_button_forwards.setIconSize(QSize(16, 16))
        self.motion_zoom_button_backwards = QPushButton(self.Motion_Zoom_Component_poppable)
        self.motion_zoom_button_backwards.setObjectName(u"motion_zoom_button_backwards")
        self.motion_zoom_button_backwards.setGeometry(QRect(78, 224, 16, 16))
        sizePolicy7.setHeightForWidth(self.motion_zoom_button_backwards.sizePolicy().hasHeightForWidth())
        self.motion_zoom_button_backwards.setSizePolicy(sizePolicy7)
        self.motion_zoom_button_backwards.setMinimumSize(QSize(16, 16))
        self.motion_zoom_button_backwards.setMaximumSize(QSize(16, 16))
        self.motion_zoom_button_backwards.setTabletTracking(True)
        self.motion_zoom_button_backwards.setStyleSheet(u"border : 0;background: none;")
        self.motion_zoom_button_backwards.setIcon(icon6)
        self.motion_zoom_button_backwards.setIconSize(QSize(16, 16))
        self.deforumation_tabWidget.addTab(self.Movement_Tab, "")
        self.Settings_Tab = QWidget()
        self.Settings_Tab.setObjectName(u"Settings_Tab")
        self.Settings_Tab.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.Settings_Tab.sizePolicy().hasHeightForWidth())
        self.Settings_Tab.setSizePolicy(sizePolicy1)
        self.Settings_Tab.setMinimumSize(QSize(0, 0))
        self.Settings_Tab.setAutoFillBackground(False)
        self.Settings_Tab.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.user_interface = QFrame(self.Settings_Tab)
        self.user_interface.setObjectName(u"user_interface")
        self.user_interface.setGeometry(QRect(8, 8, 437, 433))
        sizePolicy.setHeightForWidth(self.user_interface.sizePolicy().hasHeightForWidth())
        self.user_interface.setSizePolicy(sizePolicy)
        self.user_interface.setTabletTracking(True)
        self.user_interface.setStyleSheet(u"    border-radius: 5px;")
        self.user_interface.setFrameShape(QFrame.StyledPanel)
        self.user_interface.setFrameShadow(QFrame.Raised)
        self.user_interface_settings_label = QLabel(self.user_interface)
        self.user_interface_settings_label.setObjectName(u"user_interface_settings_label")
        self.user_interface_settings_label.setGeometry(QRect(8, 4, 409, 35))
        font11 = QFont()
        font11.setPointSize(14)
        font11.setBold(True)
        self.user_interface_settings_label.setFont(font11)
        self.user_interface_settings_label.setStyleSheet(u"   border: none;")
        self.Save_Settings = QPushButton(self.user_interface)
        self.Save_Settings.setObjectName(u"Save_Settings")
        self.Save_Settings.setGeometry(QRect(11, 42, 177, 30))
        self.Save_Settings.setTabletTracking(False)
        self.Save_Settings.setStyleSheet(u"/*QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(11"
                        "0, 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  "
                        "border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}*/\n"
"\n"
"/*  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
""
                        "  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));*/\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.Restore_Settings = QPushButton(self.user_interface)
        self.Restore_Settings.setObjectName(u"Restore_Settings")
        self.Restore_Settings.setGeometry(QRect(11, 80, 177, 30))
        self.Restore_Settings.setStyleSheet(u"/*QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(11"
                        "0, 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  "
                        "border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}\n"
"*/\n"
"/*  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
""
                        "  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));*/\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.enablemovements_button = QPushButton(self.user_interface)
        self.enablemovements_button.setObjectName(u"enablemovements_button")
        self.enablemovements_button.setGeometry(QRect(11, 338, 177, 30))
        self.enablemovements_button.setAutoFillBackground(False)
        self.enablemovements_button.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.enablemovements_button.setAutoDefault(False)
        self.enablemovements_button.setFlat(False)
        self.dissablemovements_button = QPushButton(self.user_interface)
        self.dissablemovements_button.setObjectName(u"dissablemovements_button")
        self.dissablemovements_button.setGeometry(QRect(11, 374, 177, 30))
        self.dissablemovements_button.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.save_current_ui_label = QLabel(self.user_interface)
        self.save_current_ui_label.setObjectName(u"save_current_ui_label")
        self.save_current_ui_label.setGeometry(QRect(201, 40, 225, 33))
        self.save_current_ui_label.setStyleSheet(u"border: none;")
        self.save_current_ui_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.save_current_ui_label.setWordWrap(True)
        self.restore_current_ui_label = QLabel(self.user_interface)
        self.restore_current_ui_label.setObjectName(u"restore_current_ui_label")
        self.restore_current_ui_label.setGeometry(QRect(201, 80, 233, 33))
        self.restore_current_ui_label.setStyleSheet(u"border: none;")
        self.restore_current_ui_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.restore_current_ui_label.setWordWrap(True)
        self.user_interface_cust_label = QLabel(self.user_interface)
        self.user_interface_cust_label.setObjectName(u"user_interface_cust_label")
        self.user_interface_cust_label.setGeometry(QRect(8, 278, 417, 35))
        self.user_interface_cust_label.setFont(font11)
        self.user_interface_cust_label.setStyleSheet(u"   border: none;")
        self.enable_movement_label = QLabel(self.user_interface)
        self.enable_movement_label.setObjectName(u"enable_movement_label")
        self.enable_movement_label.setGeometry(QRect(201, 334, 233, 41))
        self.enable_movement_label.setStyleSheet(u"border: none;")
        self.enable_movement_label.setWordWrap(True)
        self.dissable_movement_label = QLabel(self.user_interface)
        self.dissable_movement_label.setObjectName(u"dissable_movement_label")
        self.dissable_movement_label.setGeometry(QRect(201, 372, 233, 35))
        self.dissable_movement_label.setStyleSheet(u"border: none;")
        self.dissable_movement_label.setWordWrap(True)
        self.revert_ui_to_original_label = QLabel(self.user_interface)
        self.revert_ui_to_original_label.setObjectName(u"revert_ui_to_original_label")
        self.revert_ui_to_original_label.setGeometry(QRect(200, 232, 233, 33))
        self.revert_ui_to_original_label.setStyleSheet(u"border: none;")
        self.revert_ui_to_original_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.revert_ui_to_original_label.setWordWrap(True)
        self.revert_UI_to_original = QPushButton(self.user_interface)
        self.revert_UI_to_original.setObjectName(u"revert_UI_to_original")
        self.revert_UI_to_original.setGeometry(QRect(10, 232, 177, 30))
        self.revert_UI_to_original.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: red; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.save_current_ui_label_2 = QLabel(self.user_interface)
        self.save_current_ui_label_2.setObjectName(u"save_current_ui_label_2")
        self.save_current_ui_label_2.setGeometry(QRect(200, 128, 217, 33))
        self.save_current_ui_label_2.setStyleSheet(u"border: none;")
        self.save_current_ui_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.save_current_ui_label_2.setWordWrap(True)
        self.Save_Settings_To_File = QPushButton(self.user_interface)
        self.Save_Settings_To_File.setObjectName(u"Save_Settings_To_File")
        self.Save_Settings_To_File.setGeometry(QRect(10, 130, 177, 30))
        self.Save_Settings_To_File.setTabletTracking(False)
        self.Save_Settings_To_File.setStyleSheet(u"/*QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(11"
                        "0, 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  "
                        "border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}*/\n"
"\n"
"/*  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
""
                        "  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));*/\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.save_current_ui_label_3 = QLabel(self.user_interface)
        self.save_current_ui_label_3.setObjectName(u"save_current_ui_label_3")
        self.save_current_ui_label_3.setGeometry(QRect(200, 175, 217, 33))
        self.save_current_ui_label_3.setStyleSheet(u"border: none;")
        self.save_current_ui_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.save_current_ui_label_3.setWordWrap(True)
        self.Load_Settings_From_File = QPushButton(self.user_interface)
        self.Load_Settings_From_File.setObjectName(u"Load_Settings_From_File")
        self.Load_Settings_From_File.setGeometry(QRect(10, 177, 177, 30))
        self.Load_Settings_From_File.setTabletTracking(False)
        self.Load_Settings_From_File.setStyleSheet(u"/*QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(11"
                        "0, 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  "
                        "border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}*/\n"
"\n"
"/*  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
""
                        "  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));*/\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.line_user_interface_middle = QFrame(self.user_interface)
        self.line_user_interface_middle.setObjectName(u"line_user_interface_middle")
        self.line_user_interface_middle.setGeometry(QRect(12, 120, 410, 1))
        self.line_user_interface_middle.setFrameShape(QFrame.HLine)
        self.line_user_interface_middle.setFrameShadow(QFrame.Sunken)
        self.line_user_interface_bottom = QFrame(self.user_interface)
        self.line_user_interface_bottom.setObjectName(u"line_user_interface_bottom")
        self.line_user_interface_bottom.setGeometry(QRect(12, 219, 410, 1))
        self.line_user_interface_bottom.setFrameShape(QFrame.HLine)
        self.line_user_interface_bottom.setFrameShadow(QFrame.Sunken)
        self.line_user_interface_middle.raise_()
        self.user_interface_settings_label.raise_()
        self.Save_Settings.raise_()
        self.Restore_Settings.raise_()
        self.enablemovements_button.raise_()
        self.dissablemovements_button.raise_()
        self.save_current_ui_label.raise_()
        self.restore_current_ui_label.raise_()
        self.user_interface_cust_label.raise_()
        self.enable_movement_label.raise_()
        self.dissable_movement_label.raise_()
        self.revert_ui_to_original_label.raise_()
        self.revert_UI_to_original.raise_()
        self.save_current_ui_label_2.raise_()
        self.Save_Settings_To_File.raise_()
        self.save_current_ui_label_3.raise_()
        self.Load_Settings_From_File.raise_()
        self.line_user_interface_bottom.raise_()
        self.language_setting = QFrame(self.Settings_Tab)
        self.language_setting.setObjectName(u"language_setting")
        self.language_setting.setGeometry(QRect(448, 8, 384, 215))
        self.language_setting.setTabletTracking(True)
        self.language_setting.setStyleSheet(u"    border-radius: 5px;")
        self.language_setting.setFrameShape(QFrame.StyledPanel)
        self.language_setting.setFrameShadow(QFrame.Raised)
        self.Create_Language_Config = QPushButton(self.language_setting)
        self.Create_Language_Config.setObjectName(u"Create_Language_Config")
        self.Create_Language_Config.setGeometry(QRect(17, 44, 273, 30))
        self.Create_Language_Config.setTabletTracking(False)
        self.Create_Language_Config.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.Load_Language_Config = QPushButton(self.language_setting)
        self.Load_Language_Config.setObjectName(u"Load_Language_Config")
        self.Load_Language_Config.setGeometry(QRect(17, 96, 273, 30))
        self.Load_Language_Config.setTabletTracking(False)
        self.Load_Language_Config.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.language_setting_label = QLabel(self.language_setting)
        self.language_setting_label.setObjectName(u"language_setting_label")
        self.language_setting_label.setGeometry(QRect(8, 4, 361, 35))
        self.language_setting_label.setFont(font11)
        self.language_setting_label.setStyleSheet(u"   border: none;")
        self.Restore_To_Language = QPushButton(self.language_setting)
        self.Restore_To_Language.setObjectName(u"Restore_To_Language")
        self.Restore_To_Language.setGeometry(QRect(16, 144, 273, 30))
        self.Restore_To_Language.setTabletTracking(False)
        self.Restore_To_Language.setStyleSheet(u"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")
        self.ffmpeg_setting = QFrame(self.Settings_Tab)
        self.ffmpeg_setting.setObjectName(u"ffmpeg_setting")
        self.ffmpeg_setting.setGeometry(QRect(448, 226, 384, 215))
        self.ffmpeg_setting.setTabletTracking(True)
        self.ffmpeg_setting.setStyleSheet(u"    border-radius: 5px;")
        self.ffmpeg_setting.setFrameShape(QFrame.StyledPanel)
        self.ffmpeg_setting.setFrameShadow(QFrame.Raised)
        self.ffmpeg_howto_more_label = QLabel(self.ffmpeg_setting)
        self.ffmpeg_howto_more_label.setObjectName(u"ffmpeg_howto_more_label")
        self.ffmpeg_howto_more_label.setGeometry(QRect(8, 72, 369, 41))
        self.ffmpeg_howto_more_label.setStyleSheet(u"   border: none;")
        self.ffmpeg_howto_more_label.setWordWrap(True)
        self.ffmpeg_title_label = QLabel(self.ffmpeg_setting)
        self.ffmpeg_title_label.setObjectName(u"ffmpeg_title_label")
        self.ffmpeg_title_label.setGeometry(QRect(6, 2, 369, 35))
        self.ffmpeg_title_label.setFont(font11)
        self.ffmpeg_title_label.setStyleSheet(u"   border: none;")
        self.ffmpeg_how_to_label = QLabel(self.ffmpeg_setting)
        self.ffmpeg_how_to_label.setObjectName(u"ffmpeg_how_to_label")
        self.ffmpeg_how_to_label.setGeometry(QRect(8, 32, 369, 41))
        self.ffmpeg_how_to_label.setStyleSheet(u"   border: none;")
        self.ffmpeg_how_to_label.setWordWrap(True)
        self.ffmpeg_settings_frame = QFrame(self.ffmpeg_setting)
        self.ffmpeg_settings_frame.setObjectName(u"ffmpeg_settings_frame")
        self.ffmpeg_settings_frame.setGeometry(QRect(4, 128, 377, 57))
        self.ffmpeg_settings_frame.setStyleSheet(u"background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 3px")
        self.ffmpeg_settings_frame.setFrameShape(QFrame.StyledPanel)
        self.ffmpeg_settings_frame.setFrameShadow(QFrame.Raised)
        self.pathToFFMPEG_value = QLineEdit(self.ffmpeg_settings_frame)
        self.pathToFFMPEG_value.setObjectName(u"pathToFFMPEG_value")
        self.pathToFFMPEG_value.setGeometry(QRect(112, 5, 185, 22))
        self.pathToFFMPEG_value.setStyleSheet(u"background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;")
        self.pathffmpeg_label = QLabel(self.ffmpeg_settings_frame)
        self.pathffmpeg_label.setObjectName(u"pathffmpeg_label")
        self.pathffmpeg_label.setGeometry(QRect(4, 8, 105, 16))
        self.pathffmpeg_label.setStyleSheet(u"border:0")
        self.pathaudiofile_label = QLabel(self.ffmpeg_settings_frame)
        self.pathaudiofile_label.setObjectName(u"pathaudiofile_label")
        self.pathaudiofile_label.setGeometry(QRect(4, 31, 105, 16))
        self.pathaudiofile_label.setStyleSheet(u"border:0")
        self.pathToAudioFile_value = QLineEdit(self.ffmpeg_settings_frame)
        self.pathToAudioFile_value.setObjectName(u"pathToAudioFile_value")
        self.pathToAudioFile_value.setGeometry(QRect(112, 29, 185, 22))
        self.pathToAudioFile_value.setStyleSheet(u"background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;")
        self.browse_audio_file = QPushButton(self.ffmpeg_settings_frame)
        self.browse_audio_file.setObjectName(u"browse_audio_file")
        self.browse_audio_file.setGeometry(QRect(302, 31, 65, 17))
        self.browse_audio_file.setTabletTracking(False)
        self.browse_audio_file.setStyleSheet(u"QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110,"
                        " 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  bo"
                        "rder-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}")
        self.browse_ffmpeg_file = QPushButton(self.ffmpeg_settings_frame)
        self.browse_ffmpeg_file.setObjectName(u"browse_ffmpeg_file")
        self.browse_ffmpeg_file.setGeometry(QRect(302, 8, 65, 17))
        self.browse_ffmpeg_file.setTabletTracking(False)
        self.browse_ffmpeg_file.setStyleSheet(u"QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110,"
                        " 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  bo"
                        "rder-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}")
        self.controller_settings = QFrame(self.Settings_Tab)
        self.controller_settings.setObjectName(u"controller_settings")
        self.controller_settings.setGeometry(QRect(835, 8, 345, 433))
        self.controller_settings.setStyleSheet(u"    border-radius: 5px;")
        self.controller_settings.setFrameShape(QFrame.StyledPanel)
        self.controller_settings.setFrameShadow(QFrame.Raised)
        self.joystick_combo_box = QComboBox(self.controller_settings)
        self.joystick_combo_box.addItem("")
        self.joystick_combo_box.setObjectName(u"joystick_combo_box")
        self.joystick_combo_box.setGeometry(QRect(13, 112, 249, 19))
        self.joystick_combo_box.setStyleSheet(u"QComboBox\n"
"{\n"
"border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 5px;\n"
"color: rgb(0, 255, 0);\n"
"text-align: center;\n"
"}\n"
"QFrame {\n"
"    background-color: rgb(70, 70, 70); /* Fallback color */\n"
"    color: rgb(0, 255, 0);\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Joystic_Key_Bindings_Frame = QFrame(self.controller_settings)
        self.Joystic_Key_Bindings_Frame.setObjectName(u"Joystic_Key_Bindings_Frame")
        self.Joystic_Key_Bindings_Frame.setGeometry(QRect(8, 195, 321, 233))
        self.Joystic_Key_Bindings_Frame.setStyleSheet(u"border:0")
        self.Joystic_Key_Bindings_Frame.setFrameShape(QFrame.StyledPanel)
        self.Joystic_Key_Bindings_Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.Joystic_Key_Bindings_Frame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_joystick_key_bindings = QScrollArea(self.Joystic_Key_Bindings_Frame)
        self.scrollArea_joystick_key_bindings.setObjectName(u"scrollArea_joystick_key_bindings")
        sizePolicy1.setHeightForWidth(self.scrollArea_joystick_key_bindings.sizePolicy().hasHeightForWidth())
        self.scrollArea_joystick_key_bindings.setSizePolicy(sizePolicy1)
        self.scrollArea_joystick_key_bindings.setMinimumSize(QSize(0, 0))
        self.scrollArea_joystick_key_bindings.setStyleSheet(u"QScrollArea {\n"
"    border: 0px;\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrollBar::add-page:vertical {\n"
"    background: none; \n"
""
                        "border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_joystick_key_bindings.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_joystick_key_bindings.setWidgetResizable(True)
        self.scrollAreaWidgetContentsJoystickBindings = QWidget()
        self.scrollAreaWidgetContentsJoystickBindings.setObjectName(u"scrollAreaWidgetContentsJoystickBindings")
        self.scrollAreaWidgetContentsJoystickBindings.setGeometry(QRect(0, 0, 302, 340))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContentsJoystickBindings.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsJoystickBindings.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContentsJoystickBindings.setMinimumSize(QSize(0, 340))
        self.scrollAreaWidgetContentsJoystickBindings.setStyleSheet(u"border:0")
        self.verticalLayout_10 = QVBoxLayout(self.scrollAreaWidgetContentsJoystickBindings)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_joystic_bindings = QFrame(self.scrollAreaWidgetContentsJoystickBindings)
        self.frame_joystic_bindings.setObjectName(u"frame_joystic_bindings")
        self.frame_joystic_bindings.setMinimumSize(QSize(0, 0))
        self.frame_joystic_bindings.setAutoFillBackground(False)
        self.frame_joystic_bindings.setStyleSheet(u"background-color: rgb(108,108,118); border: 0px solid rgb(128,128,128); border-radius: 0px;")
        self.frame_joystic_bindings.setFrameShape(QFrame.StyledPanel)
        self.frame_joystic_bindings.setFrameShadow(QFrame.Raised)
        self.joystic_key_bindings_frame_poppable = QFrame(self.frame_joystic_bindings)
        self.joystic_key_bindings_frame_poppable.setObjectName(u"joystic_key_bindings_frame_poppable")
        self.joystic_key_bindings_frame_poppable.setGeometry(QRect(0, 0, 305, 513))
        self.joystic_key_bindings_frame_poppable.setTabletTracking(True)
        self.joystic_key_bindings_frame_poppable.setStyleSheet(u"border:0")
        self.joystic_key_bindings_frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.joystic_key_bindings_frame_poppable.setFrameShadow(QFrame.Raised)
        self.joystic_bindings_row = QWidget(self.joystic_key_bindings_frame_poppable)
        self.joystic_bindings_row.setObjectName(u"joystic_bindings_row")
        self.joystic_bindings_row.setGeometry(QRect(5, 0, 137, 345))
        sizePolicy15.setHeightForWidth(self.joystic_bindings_row.sizePolicy().hasHeightForWidth())
        self.joystic_bindings_row.setSizePolicy(sizePolicy15)
        self.joystic_bindings_row.setStyleSheet(u"")
        self.verticalLayoutWidget_4 = QWidget(self.joystic_bindings_row)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(0, 4, 137, 337))
        self.verticalLayout_JoystickBinding_Key_Name = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_JoystickBinding_Key_Name.setSpacing(4)
        self.verticalLayout_JoystickBinding_Key_Name.setObjectName(u"verticalLayout_JoystickBinding_Key_Name")
        self.verticalLayout_JoystickBinding_Key_Name.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_JoystickBinding_Key_Name.setContentsMargins(0, 0, 0, 0)
        self.joystick_panning_left_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_panning_left_label.setObjectName(u"joystick_panning_left_label")
        sizePolicy16 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.joystick_panning_left_label.sizePolicy().hasHeightForWidth())
        self.joystick_panning_left_label.setSizePolicy(sizePolicy16)
        self.joystick_panning_left_label.setMinimumSize(QSize(0, 0))
        font12 = QFont()
        font12.setPointSize(9)
        self.joystick_panning_left_label.setFont(font12)
        self.joystick_panning_left_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_panning_left_label)

        self.joystick_panning_right_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_panning_right_label.setObjectName(u"joystick_panning_right_label")
        sizePolicy16.setHeightForWidth(self.joystick_panning_right_label.sizePolicy().hasHeightForWidth())
        self.joystick_panning_right_label.setSizePolicy(sizePolicy16)
        self.joystick_panning_right_label.setMinimumSize(QSize(0, 0))
        self.joystick_panning_right_label.setFont(font12)
        self.joystick_panning_right_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_panning_right_label)

        self.joystick_panning_up_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_panning_up_label.setObjectName(u"joystick_panning_up_label")
        sizePolicy16.setHeightForWidth(self.joystick_panning_up_label.sizePolicy().hasHeightForWidth())
        self.joystick_panning_up_label.setSizePolicy(sizePolicy16)
        self.joystick_panning_up_label.setMinimumSize(QSize(0, 0))
        self.joystick_panning_up_label.setFont(font12)
        self.joystick_panning_up_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_panning_up_label)

        self.joystick_panning_down_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_panning_down_label.setObjectName(u"joystick_panning_down_label")
        sizePolicy16.setHeightForWidth(self.joystick_panning_down_label.sizePolicy().hasHeightForWidth())
        self.joystick_panning_down_label.setSizePolicy(sizePolicy16)
        self.joystick_panning_down_label.setMinimumSize(QSize(0, 0))
        self.joystick_panning_down_label.setFont(font12)
        self.joystick_panning_down_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_panning_down_label)

        self.joystick_rotate_h_left_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_rotate_h_left_label.setObjectName(u"joystick_rotate_h_left_label")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_h_left_label.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_h_left_label.setSizePolicy(sizePolicy16)
        self.joystick_rotate_h_left_label.setMinimumSize(QSize(0, 0))
        self.joystick_rotate_h_left_label.setFont(font12)
        self.joystick_rotate_h_left_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_rotate_h_left_label)

        self.joystick_rotate_h_right_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_rotate_h_right_label.setObjectName(u"joystick_rotate_h_right_label")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_h_right_label.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_h_right_label.setSizePolicy(sizePolicy16)
        self.joystick_rotate_h_right_label.setMinimumSize(QSize(0, 0))
        self.joystick_rotate_h_right_label.setFont(font12)
        self.joystick_rotate_h_right_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_rotate_h_right_label)

        self.joystick_rotate_v_up_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_rotate_v_up_label.setObjectName(u"joystick_rotate_v_up_label")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_v_up_label.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_v_up_label.setSizePolicy(sizePolicy16)
        self.joystick_rotate_v_up_label.setMinimumSize(QSize(0, 0))
        self.joystick_rotate_v_up_label.setFont(font12)
        self.joystick_rotate_v_up_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_rotate_v_up_label)

        self.joystick_rotate_v_down_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_rotate_v_down_label.setObjectName(u"joystick_rotate_v_down_label")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_v_down_label.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_v_down_label.setSizePolicy(sizePolicy16)
        self.joystick_rotate_v_down_label.setMinimumSize(QSize(0, 0))
        self.joystick_rotate_v_down_label.setFont(font12)
        self.joystick_rotate_v_down_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_rotate_v_down_label)

        self.joystick_zoom_forwards_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_zoom_forwards_label.setObjectName(u"joystick_zoom_forwards_label")
        sizePolicy16.setHeightForWidth(self.joystick_zoom_forwards_label.sizePolicy().hasHeightForWidth())
        self.joystick_zoom_forwards_label.setSizePolicy(sizePolicy16)
        self.joystick_zoom_forwards_label.setMinimumSize(QSize(0, 0))
        self.joystick_zoom_forwards_label.setFont(font12)
        self.joystick_zoom_forwards_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_zoom_forwards_label)

        self.joystick_zoom_backwards_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_zoom_backwards_label.setObjectName(u"joystick_zoom_backwards_label")
        sizePolicy16.setHeightForWidth(self.joystick_zoom_backwards_label.sizePolicy().hasHeightForWidth())
        self.joystick_zoom_backwards_label.setSizePolicy(sizePolicy16)
        self.joystick_zoom_backwards_label.setMinimumSize(QSize(0, 0))
        self.joystick_zoom_backwards_label.setFont(font12)
        self.joystick_zoom_backwards_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_zoom_backwards_label)

        self.joystick_tilt_cw_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_tilt_cw_label.setObjectName(u"joystick_tilt_cw_label")
        sizePolicy16.setHeightForWidth(self.joystick_tilt_cw_label.sizePolicy().hasHeightForWidth())
        self.joystick_tilt_cw_label.setSizePolicy(sizePolicy16)
        self.joystick_tilt_cw_label.setMinimumSize(QSize(0, 0))
        self.joystick_tilt_cw_label.setFont(font12)
        self.joystick_tilt_cw_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_tilt_cw_label)

        self.joystick_tilt_cc_label = QLabel(self.verticalLayoutWidget_4)
        self.joystick_tilt_cc_label.setObjectName(u"joystick_tilt_cc_label")
        sizePolicy16.setHeightForWidth(self.joystick_tilt_cc_label.sizePolicy().hasHeightForWidth())
        self.joystick_tilt_cc_label.setSizePolicy(sizePolicy16)
        self.joystick_tilt_cc_label.setMinimumSize(QSize(0, 0))
        self.joystick_tilt_cc_label.setFont(font12)
        self.joystick_tilt_cc_label.setStyleSheet(u"background-color: rgb(64, 64, 64);\n"
"padding: 4px; /* To prevent the content from touching the border */\n"
" border-radius: 3px;")

        self.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joystick_tilt_cc_label)

        self.joystic_value_bindings_row = QWidget(self.joystic_key_bindings_frame_poppable)
        self.joystic_value_bindings_row.setObjectName(u"joystic_value_bindings_row")
        self.joystic_value_bindings_row.setGeometry(QRect(144, 0, 161, 345))
        self.joystic_value_bindings_row.setStyleSheet(u"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.verticalLayoutWidget_5 = QWidget(self.joystic_value_bindings_row)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(0, 4, 153, 337))
        self.verticalLayout_JoystickBinding_Key_Value = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_JoystickBinding_Key_Value.setSpacing(4)
        self.verticalLayout_JoystickBinding_Key_Value.setObjectName(u"verticalLayout_JoystickBinding_Key_Value")
        self.verticalLayout_JoystickBinding_Key_Value.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout_JoystickBinding_Key_Value.setContentsMargins(0, 0, 0, 0)
        self.joystick_panning_left_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_panning_left_binding_button.setObjectName(u"joystick_panning_left_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_panning_left_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_panning_left_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_panning_left_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_panning_left_binding_button)

        self.joystick_panning_right_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_panning_right_binding_button.setObjectName(u"joystick_panning_right_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_panning_right_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_panning_right_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_panning_right_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_panning_right_binding_button)

        self.joystick_panning_up_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_panning_up_binding_button.setObjectName(u"joystick_panning_up_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_panning_up_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_panning_up_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_panning_up_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_panning_up_binding_button)

        self.joystick_panning_down_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_panning_down_binding_button.setObjectName(u"joystick_panning_down_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_panning_down_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_panning_down_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_panning_down_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_panning_down_binding_button)

        self.joystick_rotate_h_left_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_rotate_h_left_binding_button.setObjectName(u"joystick_rotate_h_left_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_h_left_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_h_left_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_rotate_h_left_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_rotate_h_left_binding_button)

        self.joystick_rotate_h_right_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_rotate_h_right_binding_button.setObjectName(u"joystick_rotate_h_right_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_h_right_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_h_right_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_rotate_h_right_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_rotate_h_right_binding_button)

        self.joystick_rotate_v_up_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_rotate_v_up_binding_button.setObjectName(u"joystick_rotate_v_up_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_v_up_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_v_up_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_rotate_v_up_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_rotate_v_up_binding_button)

        self.joystick_rotate_v_down_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_rotate_v_down_binding_button.setObjectName(u"joystick_rotate_v_down_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_rotate_v_down_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_rotate_v_down_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_rotate_v_down_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_rotate_v_down_binding_button)

        self.joystick_zoom_forwards_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_zoom_forwards_binding_button.setObjectName(u"joystick_zoom_forwards_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_zoom_forwards_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_zoom_forwards_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_zoom_forwards_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_zoom_forwards_binding_button)

        self.joystick_zoom_backwards_binding_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_zoom_backwards_binding_button.setObjectName(u"joystick_zoom_backwards_binding_button")
        sizePolicy16.setHeightForWidth(self.joystick_zoom_backwards_binding_button.sizePolicy().hasHeightForWidth())
        self.joystick_zoom_backwards_binding_button.setSizePolicy(sizePolicy16)
        self.joystick_zoom_backwards_binding_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_zoom_backwards_binding_button)

        self.joystick_tilt_cw_bind_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_tilt_cw_bind_button.setObjectName(u"joystick_tilt_cw_bind_button")
        sizePolicy16.setHeightForWidth(self.joystick_tilt_cw_bind_button.sizePolicy().hasHeightForWidth())
        self.joystick_tilt_cw_bind_button.setSizePolicy(sizePolicy16)
        self.joystick_tilt_cw_bind_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_tilt_cw_bind_button)

        self.joystick_tilt_cc_bind_button = QPushButton(self.verticalLayoutWidget_5)
        self.joystick_tilt_cc_bind_button.setObjectName(u"joystick_tilt_cc_bind_button")
        sizePolicy16.setHeightForWidth(self.joystick_tilt_cc_bind_button.sizePolicy().hasHeightForWidth())
        self.joystick_tilt_cc_bind_button.setSizePolicy(sizePolicy16)
        self.joystick_tilt_cc_bind_button.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 3px; /* Consistent with the tab's rounded corners */\n"
"    padding: 4px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"")

        self.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joystick_tilt_cc_bind_button)


        self.verticalLayout_10.addWidget(self.frame_joystic_bindings)

        self.scrollArea_joystick_key_bindings.setWidget(self.scrollAreaWidgetContentsJoystickBindings)

        self.verticalLayout_9.addWidget(self.scrollArea_joystick_key_bindings)

        self.motion_control_params_label = QLabel(self.controller_settings)
        self.motion_control_params_label.setObjectName(u"motion_control_params_label")
        self.motion_control_params_label.setGeometry(QRect(16, 171, 135, 24))
        sizePolicy16.setHeightForWidth(self.motion_control_params_label.sizePolicy().hasHeightForWidth())
        self.motion_control_params_label.setSizePolicy(sizePolicy16)
        self.motion_control_params_label.setMinimumSize(QSize(0, 0))
        self.motion_control_params_label.setFont(font12)
        self.motion_control_params_label.setStyleSheet(u"border: none;")
        self.motion_control_bindings_label = QLabel(self.controller_settings)
        self.motion_control_bindings_label.setObjectName(u"motion_control_bindings_label")
        self.motion_control_bindings_label.setGeometry(QRect(156, 171, 135, 24))
        sizePolicy16.setHeightForWidth(self.motion_control_bindings_label.sizePolicy().hasHeightForWidth())
        self.motion_control_bindings_label.setSizePolicy(sizePolicy16)
        self.motion_control_bindings_label.setMinimumSize(QSize(0, 0))
        self.motion_control_bindings_label.setFont(font12)
        self.motion_control_bindings_label.setStyleSheet(u"border: none;")
        self.controller_setting_label = QLabel(self.controller_settings)
        self.controller_setting_label.setObjectName(u"controller_setting_label")
        self.controller_setting_label.setGeometry(QRect(8, 8, 313, 35))
        self.controller_setting_label.setFont(font11)
        self.controller_setting_label.setStyleSheet(u"   border: none;")
        self.controller_how_to = QLabel(self.controller_settings)
        self.controller_how_to.setObjectName(u"controller_how_to")
        self.controller_how_to.setGeometry(QRect(13, 40, 313, 65))
        self.controller_how_to.setStyleSheet(u"   border: none;")
        self.controller_how_to.setWordWrap(True)
        self.refresh_controller_list = QPushButton(self.controller_settings)
        self.refresh_controller_list.setObjectName(u"refresh_controller_list")
        self.refresh_controller_list.setGeometry(QRect(264, 112, 64, 19))
        self.refresh_controller_list.setTabletTracking(False)
        self.refresh_controller_list.setStyleSheet(u"QPushButton{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110,"
                        " 110, 110, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(180, 180, 180, 255), stop:1 rgba(110, 110, 110, 255));\n"
"  border-bottom-color: rgb(115, 115, 115);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157, 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  bo"
                        "rder-left-color: qlineargradient(spread:pad, x1:0.6, y1:0.5, x2:0.4, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
"  border-bottom-color: rgb(58, 58, 58);\n"
"  border-bottom-width: 1px;\n"
"  border-style: solid;\n"
"  color: rgb(0, 0, 0);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(57, 57, 57, 255), stop:1 rgba(77, 77, 77, 255));\n"
"}")
        self.frame = QFrame(self.controller_settings)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(13, 136, 201, 25))
        self.frame.setStyleSheet(u"QFrame{\n"
"border-radius: 5px;\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.mode_work_label = QLabel(self.frame)
        self.mode_work_label.setObjectName(u"mode_work_label")
        self.mode_work_label.setGeometry(QRect(120, 4, 73, 17))
        self.mode_work_label.setStyleSheet(u"border: none;")
        self.mode_work_label.setWordWrap(True)
        self.controller_mode_checkbox = QCheckBox(self.frame)
        self.controller_mode_checkbox.setObjectName(u"controller_mode_checkbox")
        self.controller_mode_checkbox.setGeometry(QRect(83, 6, 38, 16))
        sizePolicy1.setHeightForWidth(self.controller_mode_checkbox.sizePolicy().hasHeightForWidth())
        self.controller_mode_checkbox.setSizePolicy(sizePolicy1)
        self.controller_mode_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.controller_mode_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(102, 102, 102); /* Fallback color */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 34px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small_green.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for th"
                        "e checkbox */\n"
"}\n"
"")
        self.mode_game_label = QLabel(self.frame)
        self.mode_game_label.setObjectName(u"mode_game_label")
        self.mode_game_label.setGeometry(QRect(6, 4, 73, 17))
        self.mode_game_label.setStyleSheet(u"border: none;")
        self.mode_game_label.setWordWrap(True)
        self.deforumation_tabWidget.addTab(self.Settings_Tab, "")
        self.ControlNet_tab = QWidget()
        self.ControlNet_tab.setObjectName(u"ControlNet_tab")
        self.ControlNet_tab.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.tabWidget_CN = QTabWidget(self.ControlNet_tab)
        self.tabWidget_CN.setObjectName(u"tabWidget_CN")
        self.tabWidget_CN.setGeometry(QRect(4, 6, 803, 240))
        self.tabWidget_CN.setMaximumSize(QSize(16777215, 240))
        self.tabWidget_CN.setStyleSheet(u"\n"
"\n"
"border: 0px solid rgb(82, 82, 82); /* Simulated shadow using border */\n"
"border-radius: 5px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QTabWidget::pane { /* The tab widget frame */\n"
"    border: none;\n"
"    background-color: rgb(82, 82, 82); /* Dark grey background */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"}\n"
"\n"
"QTabBar {\n"
"    qproperty-drawBase: 0;  /* Removes the line at the base of the tabs */\n"
"}\n"
"\n"
"QTabBar::tab { /* Style for the tabs */\n"
"    background: rgb(64, 64, 64); /* Slightly lighter grey for tabs */\n"
"    border: none;\n"
"    border-radius: 5px; /* Rounded corners for tabs */\n"
"    padding: 0px; /* Padding around text */\n"
"    color: white; /* Text color */\n"
"    margin-right: 5px; /* Small space between tabs */\n"
"    min-width: 50px; /* Minimum width of the tab */\n"
"    max-width: 100px; /* Maximum width of the tab */\n"
"    height: 25px; /* Height of the tab */\n"
"    font-size: 14px; /* Text "
                        "size for the tabs */\n"
"    font-weight: bold; /* Makes the text bold */\n"
"}\n"
"\n"
"QTabBar::tab:hover { /* Style for hovering over a tab */\n"
"    background: rgb(96, 96, 96); /* Even lighter grey for hover effect */\n"
"}\n"
"\n"
"QTabBar::tab:selected { /* Style for the selected tab */\n"
"    background: rgb(128, 128, 128); /* Light grey for the active tab */\n"
"}\n"
"")
        self.tabWidget_CN.setIconSize(QSize(40, 20))
        self.tab_CN01 = QWidget()
        self.tab_CN01.setObjectName(u"tab_CN01")
        self.tab_CN01.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.CN_1_weight_poppable = QFrame(self.tab_CN01)
        self.CN_1_weight_poppable.setObjectName(u"CN_1_weight_poppable")
        self.CN_1_weight_poppable.setGeometry(QRect(8, 8, 257, 87))
        self.CN_1_weight_poppable.setMouseTracking(False)
        self.CN_1_weight_poppable.setTabletTracking(True)
        self.CN_1_weight_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_1_weight_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_1_weight_poppable.setFrameShadow(QFrame.Raised)
        self.CN_1_weight_slider = QSlider(self.CN_1_weight_poppable)
        self.CN_1_weight_slider.setObjectName(u"CN_1_weight_slider")
        self.CN_1_weight_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_1_weight_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_1_weight_slider.setMaximum(200)
        self.CN_1_weight_slider.setPageStep(2)
        self.CN_1_weight_slider.setValue(100)
        self.CN_1_weight_slider.setOrientation(Qt.Horizontal)
        self.CN_1_weight_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_1_weight_slider.setTickInterval(4)
        self.label_cnet15 = QLabel(self.CN_1_weight_poppable)
        self.label_cnet15.setObjectName(u"label_cnet15")
        self.label_cnet15.setGeometry(QRect(10, 8, 121, 25))
        self.label_cnet15.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_1_weight_slider_value = QLabel(self.CN_1_weight_poppable)
        self.CN_1_weight_slider_value.setObjectName(u"CN_1_weight_slider_value")
        self.CN_1_weight_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_1_weight_slider_value.setFont(font1)
        self.CN_1_weight_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_1_weight_slider_value.setIndent(0)
        self.CN_1_start_control_step_poppable = QFrame(self.tab_CN01)
        self.CN_1_start_control_step_poppable.setObjectName(u"CN_1_start_control_step_poppable")
        self.CN_1_start_control_step_poppable.setGeometry(QRect(270, 8, 257, 87))
        self.CN_1_start_control_step_poppable.setMouseTracking(False)
        self.CN_1_start_control_step_poppable.setTabletTracking(True)
        self.CN_1_start_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_1_start_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_1_start_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_1_starting_control_step_slider = QSlider(self.CN_1_start_control_step_poppable)
        self.CN_1_starting_control_step_slider.setObjectName(u"CN_1_starting_control_step_slider")
        self.CN_1_starting_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_1_starting_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_1_starting_control_step_slider.setMaximum(100)
        self.CN_1_starting_control_step_slider.setPageStep(2)
        self.CN_1_starting_control_step_slider.setValue(0)
        self.CN_1_starting_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_1_starting_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_1_starting_control_step_slider.setTickInterval(4)
        self.label_cnet14 = QLabel(self.CN_1_start_control_step_poppable)
        self.label_cnet14.setObjectName(u"label_cnet14")
        self.label_cnet14.setGeometry(QRect(10, 8, 155, 25))
        self.label_cnet14.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_1_starting_control_step_slider_value = QLabel(self.CN_1_start_control_step_poppable)
        self.CN_1_starting_control_step_slider_value.setObjectName(u"CN_1_starting_control_step_slider_value")
        self.CN_1_starting_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_1_starting_control_step_slider_value.setFont(font1)
        self.CN_1_starting_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_1_starting_control_step_slider_value.setIndent(0)
        self.CN_1_end_control_step_poppable = QFrame(self.tab_CN01)
        self.CN_1_end_control_step_poppable.setObjectName(u"CN_1_end_control_step_poppable")
        self.CN_1_end_control_step_poppable.setGeometry(QRect(532, 8, 257, 87))
        self.CN_1_end_control_step_poppable.setMouseTracking(False)
        self.CN_1_end_control_step_poppable.setTabletTracking(True)
        self.CN_1_end_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_1_end_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_1_end_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_1_ending_control_step_slider = QSlider(self.CN_1_end_control_step_poppable)
        self.CN_1_ending_control_step_slider.setObjectName(u"CN_1_ending_control_step_slider")
        self.CN_1_ending_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_1_ending_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_1_ending_control_step_slider.setMaximum(100)
        self.CN_1_ending_control_step_slider.setPageStep(2)
        self.CN_1_ending_control_step_slider.setValue(100)
        self.CN_1_ending_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_1_ending_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_1_ending_control_step_slider.setTickInterval(4)
        self.label_cnet11 = QLabel(self.CN_1_end_control_step_poppable)
        self.label_cnet11.setObjectName(u"label_cnet11")
        self.label_cnet11.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet11.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_1_ending_control_step_slider_value = QLabel(self.CN_1_end_control_step_poppable)
        self.CN_1_ending_control_step_slider_value.setObjectName(u"CN_1_ending_control_step_slider_value")
        self.CN_1_ending_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_1_ending_control_step_slider_value.setFont(font1)
        self.CN_1_ending_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_1_ending_control_step_slider_value.setIndent(0)
        self.CN_1_low_threshold_poppable = QFrame(self.tab_CN01)
        self.CN_1_low_threshold_poppable.setObjectName(u"CN_1_low_threshold_poppable")
        self.CN_1_low_threshold_poppable.setGeometry(QRect(8, 100, 257, 87))
        self.CN_1_low_threshold_poppable.setMouseTracking(False)
        self.CN_1_low_threshold_poppable.setTabletTracking(True)
        self.CN_1_low_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_1_low_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_1_low_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_1_low_threshold_slider = QSlider(self.CN_1_low_threshold_poppable)
        self.CN_1_low_threshold_slider.setObjectName(u"CN_1_low_threshold_slider")
        self.CN_1_low_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_1_low_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_1_low_threshold_slider.setMaximum(255)
        self.CN_1_low_threshold_slider.setPageStep(2)
        self.CN_1_low_threshold_slider.setValue(100)
        self.CN_1_low_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_1_low_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_1_low_threshold_slider.setTickInterval(4)
        self.label_cnet13 = QLabel(self.CN_1_low_threshold_poppable)
        self.label_cnet13.setObjectName(u"label_cnet13")
        self.label_cnet13.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet13.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_1_low_threshold_slider_value = QLabel(self.CN_1_low_threshold_poppable)
        self.CN_1_low_threshold_slider_value.setObjectName(u"CN_1_low_threshold_slider_value")
        self.CN_1_low_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_1_low_threshold_slider_value.setFont(font1)
        self.CN_1_low_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_1_low_threshold_slider_value.setIndent(0)
        self.CN_1_high_threshold_poppable = QFrame(self.tab_CN01)
        self.CN_1_high_threshold_poppable.setObjectName(u"CN_1_high_threshold_poppable")
        self.CN_1_high_threshold_poppable.setGeometry(QRect(270, 100, 257, 87))
        self.CN_1_high_threshold_poppable.setMouseTracking(False)
        self.CN_1_high_threshold_poppable.setTabletTracking(True)
        self.CN_1_high_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_1_high_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_1_high_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_1_high_threshold_slider = QSlider(self.CN_1_high_threshold_poppable)
        self.CN_1_high_threshold_slider.setObjectName(u"CN_1_high_threshold_slider")
        self.CN_1_high_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_1_high_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_1_high_threshold_slider.setMaximum(255)
        self.CN_1_high_threshold_slider.setPageStep(2)
        self.CN_1_high_threshold_slider.setValue(200)
        self.CN_1_high_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_1_high_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_1_high_threshold_slider.setTickInterval(4)
        self.label_cnet12 = QLabel(self.CN_1_high_threshold_poppable)
        self.label_cnet12.setObjectName(u"label_cnet12")
        self.label_cnet12.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet12.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_1_high_threshold_slider_value = QLabel(self.CN_1_high_threshold_poppable)
        self.CN_1_high_threshold_slider_value.setObjectName(u"CN_1_high_threshold_slider_value")
        self.CN_1_high_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_1_high_threshold_slider_value.setFont(font1)
        self.CN_1_high_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_1_high_threshold_slider_value.setIndent(0)
        self.tabWidget_CN.addTab(self.tab_CN01, "")
        self.tab_CN02 = QWidget()
        self.tab_CN02.setObjectName(u"tab_CN02")
        self.tab_CN02.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.CN_2_high_threshold_poppable = QFrame(self.tab_CN02)
        self.CN_2_high_threshold_poppable.setObjectName(u"CN_2_high_threshold_poppable")
        self.CN_2_high_threshold_poppable.setGeometry(QRect(270, 100, 257, 87))
        self.CN_2_high_threshold_poppable.setTabletTracking(True)
        self.CN_2_high_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_2_high_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_2_high_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_2_high_threshold_slider = QSlider(self.CN_2_high_threshold_poppable)
        self.CN_2_high_threshold_slider.setObjectName(u"CN_2_high_threshold_slider")
        self.CN_2_high_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_2_high_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_2_high_threshold_slider.setMaximum(255)
        self.CN_2_high_threshold_slider.setPageStep(2)
        self.CN_2_high_threshold_slider.setValue(200)
        self.CN_2_high_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_2_high_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_2_high_threshold_slider.setTickInterval(4)
        self.label_cnet22 = QLabel(self.CN_2_high_threshold_poppable)
        self.label_cnet22.setObjectName(u"label_cnet22")
        self.label_cnet22.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet22.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_2_high_threshold_slider_value = QLabel(self.CN_2_high_threshold_poppable)
        self.CN_2_high_threshold_slider_value.setObjectName(u"CN_2_high_threshold_slider_value")
        self.CN_2_high_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_2_high_threshold_slider_value.setFont(font1)
        self.CN_2_high_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_2_high_threshold_slider_value.setIndent(0)
        self.CN_2_weight_poppable = QFrame(self.tab_CN02)
        self.CN_2_weight_poppable.setObjectName(u"CN_2_weight_poppable")
        self.CN_2_weight_poppable.setGeometry(QRect(8, 8, 257, 87))
        self.CN_2_weight_poppable.setTabletTracking(True)
        self.CN_2_weight_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_2_weight_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_2_weight_poppable.setFrameShadow(QFrame.Raised)
        self.CN_2_weight_slider = QSlider(self.CN_2_weight_poppable)
        self.CN_2_weight_slider.setObjectName(u"CN_2_weight_slider")
        self.CN_2_weight_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_2_weight_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_2_weight_slider.setMaximum(200)
        self.CN_2_weight_slider.setPageStep(2)
        self.CN_2_weight_slider.setValue(100)
        self.CN_2_weight_slider.setOrientation(Qt.Horizontal)
        self.CN_2_weight_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_2_weight_slider.setTickInterval(4)
        self.label_cnet25 = QLabel(self.CN_2_weight_poppable)
        self.label_cnet25.setObjectName(u"label_cnet25")
        self.label_cnet25.setGeometry(QRect(10, 8, 121, 25))
        self.label_cnet25.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_2_weight_slider_value = QLabel(self.CN_2_weight_poppable)
        self.CN_2_weight_slider_value.setObjectName(u"CN_2_weight_slider_value")
        self.CN_2_weight_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_2_weight_slider_value.setFont(font1)
        self.CN_2_weight_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_2_weight_slider_value.setIndent(0)
        self.CN_2_end_control_step_poppable = QFrame(self.tab_CN02)
        self.CN_2_end_control_step_poppable.setObjectName(u"CN_2_end_control_step_poppable")
        self.CN_2_end_control_step_poppable.setGeometry(QRect(532, 8, 257, 87))
        self.CN_2_end_control_step_poppable.setTabletTracking(True)
        self.CN_2_end_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_2_end_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_2_end_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_2_ending_control_step_slider = QSlider(self.CN_2_end_control_step_poppable)
        self.CN_2_ending_control_step_slider.setObjectName(u"CN_2_ending_control_step_slider")
        self.CN_2_ending_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_2_ending_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_2_ending_control_step_slider.setMaximum(100)
        self.CN_2_ending_control_step_slider.setPageStep(2)
        self.CN_2_ending_control_step_slider.setValue(100)
        self.CN_2_ending_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_2_ending_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_2_ending_control_step_slider.setTickInterval(4)
        self.label_cnet21 = QLabel(self.CN_2_end_control_step_poppable)
        self.label_cnet21.setObjectName(u"label_cnet21")
        self.label_cnet21.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet21.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_2_ending_control_step_slider_value = QLabel(self.CN_2_end_control_step_poppable)
        self.CN_2_ending_control_step_slider_value.setObjectName(u"CN_2_ending_control_step_slider_value")
        self.CN_2_ending_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_2_ending_control_step_slider_value.setFont(font1)
        self.CN_2_ending_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_2_ending_control_step_slider_value.setIndent(0)
        self.CN_2_start_control_step_poppable = QFrame(self.tab_CN02)
        self.CN_2_start_control_step_poppable.setObjectName(u"CN_2_start_control_step_poppable")
        self.CN_2_start_control_step_poppable.setGeometry(QRect(270, 8, 257, 87))
        self.CN_2_start_control_step_poppable.setTabletTracking(True)
        self.CN_2_start_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_2_start_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_2_start_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_2_starting_control_step_slider = QSlider(self.CN_2_start_control_step_poppable)
        self.CN_2_starting_control_step_slider.setObjectName(u"CN_2_starting_control_step_slider")
        self.CN_2_starting_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_2_starting_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_2_starting_control_step_slider.setMaximum(100)
        self.CN_2_starting_control_step_slider.setPageStep(2)
        self.CN_2_starting_control_step_slider.setValue(0)
        self.CN_2_starting_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_2_starting_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_2_starting_control_step_slider.setTickInterval(4)
        self.label_cnet24 = QLabel(self.CN_2_start_control_step_poppable)
        self.label_cnet24.setObjectName(u"label_cnet24")
        self.label_cnet24.setGeometry(QRect(10, 8, 155, 25))
        self.label_cnet24.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_2_starting_control_step_slider_value = QLabel(self.CN_2_start_control_step_poppable)
        self.CN_2_starting_control_step_slider_value.setObjectName(u"CN_2_starting_control_step_slider_value")
        self.CN_2_starting_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_2_starting_control_step_slider_value.setFont(font1)
        self.CN_2_starting_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_2_starting_control_step_slider_value.setIndent(0)
        self.CN_2_low_threshold_poppable = QFrame(self.tab_CN02)
        self.CN_2_low_threshold_poppable.setObjectName(u"CN_2_low_threshold_poppable")
        self.CN_2_low_threshold_poppable.setGeometry(QRect(8, 100, 257, 87))
        self.CN_2_low_threshold_poppable.setTabletTracking(True)
        self.CN_2_low_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_2_low_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_2_low_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_2_low_threshold_slider = QSlider(self.CN_2_low_threshold_poppable)
        self.CN_2_low_threshold_slider.setObjectName(u"CN_2_low_threshold_slider")
        self.CN_2_low_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_2_low_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_2_low_threshold_slider.setMaximum(255)
        self.CN_2_low_threshold_slider.setPageStep(2)
        self.CN_2_low_threshold_slider.setValue(100)
        self.CN_2_low_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_2_low_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_2_low_threshold_slider.setTickInterval(4)
        self.label_cnet23 = QLabel(self.CN_2_low_threshold_poppable)
        self.label_cnet23.setObjectName(u"label_cnet23")
        self.label_cnet23.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet23.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_2_low_threshold_slider_value = QLabel(self.CN_2_low_threshold_poppable)
        self.CN_2_low_threshold_slider_value.setObjectName(u"CN_2_low_threshold_slider_value")
        self.CN_2_low_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_2_low_threshold_slider_value.setFont(font1)
        self.CN_2_low_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_2_low_threshold_slider_value.setIndent(0)
        self.tabWidget_CN.addTab(self.tab_CN02, "")
        self.tab_CN03 = QWidget()
        self.tab_CN03.setObjectName(u"tab_CN03")
        self.tab_CN03.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.CN_3_high_threshold_poppable = QFrame(self.tab_CN03)
        self.CN_3_high_threshold_poppable.setObjectName(u"CN_3_high_threshold_poppable")
        self.CN_3_high_threshold_poppable.setGeometry(QRect(270, 100, 257, 87))
        self.CN_3_high_threshold_poppable.setTabletTracking(True)
        self.CN_3_high_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_3_high_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_3_high_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_3_high_threshold_slider = QSlider(self.CN_3_high_threshold_poppable)
        self.CN_3_high_threshold_slider.setObjectName(u"CN_3_high_threshold_slider")
        self.CN_3_high_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_3_high_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_3_high_threshold_slider.setMaximum(255)
        self.CN_3_high_threshold_slider.setPageStep(2)
        self.CN_3_high_threshold_slider.setValue(200)
        self.CN_3_high_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_3_high_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_3_high_threshold_slider.setTickInterval(4)
        self.label_cnet32 = QLabel(self.CN_3_high_threshold_poppable)
        self.label_cnet32.setObjectName(u"label_cnet32")
        self.label_cnet32.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet32.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_3_high_threshold_slider_value = QLabel(self.CN_3_high_threshold_poppable)
        self.CN_3_high_threshold_slider_value.setObjectName(u"CN_3_high_threshold_slider_value")
        self.CN_3_high_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_3_high_threshold_slider_value.setFont(font1)
        self.CN_3_high_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_3_high_threshold_slider_value.setIndent(0)
        self.CN_3_weight_poppable = QFrame(self.tab_CN03)
        self.CN_3_weight_poppable.setObjectName(u"CN_3_weight_poppable")
        self.CN_3_weight_poppable.setGeometry(QRect(8, 8, 257, 87))
        self.CN_3_weight_poppable.setTabletTracking(True)
        self.CN_3_weight_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_3_weight_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_3_weight_poppable.setFrameShadow(QFrame.Raised)
        self.CN_3_weight_slider = QSlider(self.CN_3_weight_poppable)
        self.CN_3_weight_slider.setObjectName(u"CN_3_weight_slider")
        self.CN_3_weight_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_3_weight_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_3_weight_slider.setMaximum(200)
        self.CN_3_weight_slider.setPageStep(2)
        self.CN_3_weight_slider.setValue(100)
        self.CN_3_weight_slider.setOrientation(Qt.Horizontal)
        self.CN_3_weight_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_3_weight_slider.setTickInterval(4)
        self.label_cnet35 = QLabel(self.CN_3_weight_poppable)
        self.label_cnet35.setObjectName(u"label_cnet35")
        self.label_cnet35.setGeometry(QRect(10, 8, 121, 25))
        self.label_cnet35.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_3_weight_slider_value = QLabel(self.CN_3_weight_poppable)
        self.CN_3_weight_slider_value.setObjectName(u"CN_3_weight_slider_value")
        self.CN_3_weight_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_3_weight_slider_value.setFont(font1)
        self.CN_3_weight_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_3_weight_slider_value.setIndent(0)
        self.CN_3_end_control_step_poppable = QFrame(self.tab_CN03)
        self.CN_3_end_control_step_poppable.setObjectName(u"CN_3_end_control_step_poppable")
        self.CN_3_end_control_step_poppable.setGeometry(QRect(532, 8, 257, 87))
        self.CN_3_end_control_step_poppable.setTabletTracking(True)
        self.CN_3_end_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_3_end_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_3_end_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_3_ending_control_step_slider = QSlider(self.CN_3_end_control_step_poppable)
        self.CN_3_ending_control_step_slider.setObjectName(u"CN_3_ending_control_step_slider")
        self.CN_3_ending_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_3_ending_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_3_ending_control_step_slider.setMaximum(100)
        self.CN_3_ending_control_step_slider.setPageStep(2)
        self.CN_3_ending_control_step_slider.setValue(100)
        self.CN_3_ending_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_3_ending_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_3_ending_control_step_slider.setTickInterval(4)
        self.label_cnet31 = QLabel(self.CN_3_end_control_step_poppable)
        self.label_cnet31.setObjectName(u"label_cnet31")
        self.label_cnet31.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet31.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_3_ending_control_step_slider_value = QLabel(self.CN_3_end_control_step_poppable)
        self.CN_3_ending_control_step_slider_value.setObjectName(u"CN_3_ending_control_step_slider_value")
        self.CN_3_ending_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_3_ending_control_step_slider_value.setFont(font1)
        self.CN_3_ending_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_3_ending_control_step_slider_value.setIndent(0)
        self.CN_3_start_control_step_poppable = QFrame(self.tab_CN03)
        self.CN_3_start_control_step_poppable.setObjectName(u"CN_3_start_control_step_poppable")
        self.CN_3_start_control_step_poppable.setGeometry(QRect(270, 8, 257, 87))
        self.CN_3_start_control_step_poppable.setTabletTracking(True)
        self.CN_3_start_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_3_start_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_3_start_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_3_starting_control_step_slider = QSlider(self.CN_3_start_control_step_poppable)
        self.CN_3_starting_control_step_slider.setObjectName(u"CN_3_starting_control_step_slider")
        self.CN_3_starting_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_3_starting_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_3_starting_control_step_slider.setMaximum(100)
        self.CN_3_starting_control_step_slider.setPageStep(2)
        self.CN_3_starting_control_step_slider.setValue(0)
        self.CN_3_starting_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_3_starting_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_3_starting_control_step_slider.setTickInterval(4)
        self.label_cnet34 = QLabel(self.CN_3_start_control_step_poppable)
        self.label_cnet34.setObjectName(u"label_cnet34")
        self.label_cnet34.setGeometry(QRect(10, 8, 155, 25))
        self.label_cnet34.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_3_starting_control_step_slider_value = QLabel(self.CN_3_start_control_step_poppable)
        self.CN_3_starting_control_step_slider_value.setObjectName(u"CN_3_starting_control_step_slider_value")
        self.CN_3_starting_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_3_starting_control_step_slider_value.setFont(font1)
        self.CN_3_starting_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_3_starting_control_step_slider_value.setIndent(0)
        self.CN_3_low_threshold_poppable = QFrame(self.tab_CN03)
        self.CN_3_low_threshold_poppable.setObjectName(u"CN_3_low_threshold_poppable")
        self.CN_3_low_threshold_poppable.setGeometry(QRect(8, 100, 257, 87))
        self.CN_3_low_threshold_poppable.setTabletTracking(True)
        self.CN_3_low_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_3_low_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_3_low_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_3_low_threshold_slider = QSlider(self.CN_3_low_threshold_poppable)
        self.CN_3_low_threshold_slider.setObjectName(u"CN_3_low_threshold_slider")
        self.CN_3_low_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_3_low_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_3_low_threshold_slider.setMaximum(255)
        self.CN_3_low_threshold_slider.setPageStep(2)
        self.CN_3_low_threshold_slider.setValue(100)
        self.CN_3_low_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_3_low_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_3_low_threshold_slider.setTickInterval(4)
        self.label_cnet33 = QLabel(self.CN_3_low_threshold_poppable)
        self.label_cnet33.setObjectName(u"label_cnet33")
        self.label_cnet33.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet33.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_3_low_threshold_slider_value = QLabel(self.CN_3_low_threshold_poppable)
        self.CN_3_low_threshold_slider_value.setObjectName(u"CN_3_low_threshold_slider_value")
        self.CN_3_low_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_3_low_threshold_slider_value.setFont(font1)
        self.CN_3_low_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_3_low_threshold_slider_value.setIndent(0)
        self.tabWidget_CN.addTab(self.tab_CN03, "")
        self.tab_CN04 = QWidget()
        self.tab_CN04.setObjectName(u"tab_CN04")
        self.tab_CN04.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.CN_4_high_threshold_poppable = QFrame(self.tab_CN04)
        self.CN_4_high_threshold_poppable.setObjectName(u"CN_4_high_threshold_poppable")
        self.CN_4_high_threshold_poppable.setGeometry(QRect(270, 100, 257, 87))
        self.CN_4_high_threshold_poppable.setTabletTracking(True)
        self.CN_4_high_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_4_high_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_4_high_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_4_high_threshold_slider = QSlider(self.CN_4_high_threshold_poppable)
        self.CN_4_high_threshold_slider.setObjectName(u"CN_4_high_threshold_slider")
        self.CN_4_high_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_4_high_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_4_high_threshold_slider.setMaximum(255)
        self.CN_4_high_threshold_slider.setPageStep(2)
        self.CN_4_high_threshold_slider.setValue(200)
        self.CN_4_high_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_4_high_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_4_high_threshold_slider.setTickInterval(4)
        self.label_cnet42 = QLabel(self.CN_4_high_threshold_poppable)
        self.label_cnet42.setObjectName(u"label_cnet42")
        self.label_cnet42.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet42.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_4_high_threshold_slider_value = QLabel(self.CN_4_high_threshold_poppable)
        self.CN_4_high_threshold_slider_value.setObjectName(u"CN_4_high_threshold_slider_value")
        self.CN_4_high_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_4_high_threshold_slider_value.setFont(font1)
        self.CN_4_high_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_4_high_threshold_slider_value.setIndent(0)
        self.CN_4_weight_poppable = QFrame(self.tab_CN04)
        self.CN_4_weight_poppable.setObjectName(u"CN_4_weight_poppable")
        self.CN_4_weight_poppable.setGeometry(QRect(8, 8, 257, 87))
        self.CN_4_weight_poppable.setTabletTracking(True)
        self.CN_4_weight_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_4_weight_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_4_weight_poppable.setFrameShadow(QFrame.Raised)
        self.CN_4_weight_slider = QSlider(self.CN_4_weight_poppable)
        self.CN_4_weight_slider.setObjectName(u"CN_4_weight_slider")
        self.CN_4_weight_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_4_weight_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_4_weight_slider.setMaximum(200)
        self.CN_4_weight_slider.setPageStep(2)
        self.CN_4_weight_slider.setValue(100)
        self.CN_4_weight_slider.setOrientation(Qt.Horizontal)
        self.CN_4_weight_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_4_weight_slider.setTickInterval(4)
        self.label_17 = QLabel(self.CN_4_weight_poppable)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(10, 8, 121, 25))
        self.label_17.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_4_weight_slider_value = QLabel(self.CN_4_weight_poppable)
        self.CN_4_weight_slider_value.setObjectName(u"CN_4_weight_slider_value")
        self.CN_4_weight_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_4_weight_slider_value.setFont(font1)
        self.CN_4_weight_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_4_weight_slider_value.setIndent(0)
        self.CN_4_end_control_step_poppable = QFrame(self.tab_CN04)
        self.CN_4_end_control_step_poppable.setObjectName(u"CN_4_end_control_step_poppable")
        self.CN_4_end_control_step_poppable.setGeometry(QRect(532, 8, 257, 87))
        self.CN_4_end_control_step_poppable.setTabletTracking(True)
        self.CN_4_end_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_4_end_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_4_end_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_4_ending_control_step_slider = QSlider(self.CN_4_end_control_step_poppable)
        self.CN_4_ending_control_step_slider.setObjectName(u"CN_4_ending_control_step_slider")
        self.CN_4_ending_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_4_ending_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_4_ending_control_step_slider.setMaximum(100)
        self.CN_4_ending_control_step_slider.setPageStep(2)
        self.CN_4_ending_control_step_slider.setValue(100)
        self.CN_4_ending_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_4_ending_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_4_ending_control_step_slider.setTickInterval(4)
        self.label_cnet41 = QLabel(self.CN_4_end_control_step_poppable)
        self.label_cnet41.setObjectName(u"label_cnet41")
        self.label_cnet41.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet41.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_4_ending_control_step_slider_value = QLabel(self.CN_4_end_control_step_poppable)
        self.CN_4_ending_control_step_slider_value.setObjectName(u"CN_4_ending_control_step_slider_value")
        self.CN_4_ending_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_4_ending_control_step_slider_value.setFont(font1)
        self.CN_4_ending_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_4_ending_control_step_slider_value.setIndent(0)
        self.CN_4_start_control_step_poppable = QFrame(self.tab_CN04)
        self.CN_4_start_control_step_poppable.setObjectName(u"CN_4_start_control_step_poppable")
        self.CN_4_start_control_step_poppable.setGeometry(QRect(270, 8, 257, 87))
        self.CN_4_start_control_step_poppable.setTabletTracking(True)
        self.CN_4_start_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_4_start_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_4_start_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_4_starting_control_step_slider = QSlider(self.CN_4_start_control_step_poppable)
        self.CN_4_starting_control_step_slider.setObjectName(u"CN_4_starting_control_step_slider")
        self.CN_4_starting_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_4_starting_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_4_starting_control_step_slider.setMaximum(100)
        self.CN_4_starting_control_step_slider.setPageStep(2)
        self.CN_4_starting_control_step_slider.setValue(0)
        self.CN_4_starting_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_4_starting_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_4_starting_control_step_slider.setTickInterval(4)
        self.label_cnet44 = QLabel(self.CN_4_start_control_step_poppable)
        self.label_cnet44.setObjectName(u"label_cnet44")
        self.label_cnet44.setGeometry(QRect(10, 8, 155, 25))
        self.label_cnet44.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_4_starting_control_step_slider_value = QLabel(self.CN_4_start_control_step_poppable)
        self.CN_4_starting_control_step_slider_value.setObjectName(u"CN_4_starting_control_step_slider_value")
        self.CN_4_starting_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_4_starting_control_step_slider_value.setFont(font1)
        self.CN_4_starting_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_4_starting_control_step_slider_value.setIndent(0)
        self.CN_4_low_threshold_poppable = QFrame(self.tab_CN04)
        self.CN_4_low_threshold_poppable.setObjectName(u"CN_4_low_threshold_poppable")
        self.CN_4_low_threshold_poppable.setGeometry(QRect(8, 100, 257, 87))
        self.CN_4_low_threshold_poppable.setTabletTracking(True)
        self.CN_4_low_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_4_low_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_4_low_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_4_low_threshold_slider = QSlider(self.CN_4_low_threshold_poppable)
        self.CN_4_low_threshold_slider.setObjectName(u"CN_4_low_threshold_slider")
        self.CN_4_low_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_4_low_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_4_low_threshold_slider.setMaximum(255)
        self.CN_4_low_threshold_slider.setPageStep(2)
        self.CN_4_low_threshold_slider.setValue(100)
        self.CN_4_low_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_4_low_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_4_low_threshold_slider.setTickInterval(4)
        self.label_cnet43 = QLabel(self.CN_4_low_threshold_poppable)
        self.label_cnet43.setObjectName(u"label_cnet43")
        self.label_cnet43.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet43.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_4_low_threshold_slider_value = QLabel(self.CN_4_low_threshold_poppable)
        self.CN_4_low_threshold_slider_value.setObjectName(u"CN_4_low_threshold_slider_value")
        self.CN_4_low_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_4_low_threshold_slider_value.setFont(font1)
        self.CN_4_low_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_4_low_threshold_slider_value.setIndent(0)
        self.tabWidget_CN.addTab(self.tab_CN04, "")
        self.tab_CN05 = QWidget()
        self.tab_CN05.setObjectName(u"tab_CN05")
        self.tab_CN05.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"")
        self.CN_5_high_threshold_poppable = QFrame(self.tab_CN05)
        self.CN_5_high_threshold_poppable.setObjectName(u"CN_5_high_threshold_poppable")
        self.CN_5_high_threshold_poppable.setGeometry(QRect(270, 100, 257, 87))
        self.CN_5_high_threshold_poppable.setTabletTracking(True)
        self.CN_5_high_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_5_high_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_5_high_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_5_high_threshold_slider = QSlider(self.CN_5_high_threshold_poppable)
        self.CN_5_high_threshold_slider.setObjectName(u"CN_5_high_threshold_slider")
        self.CN_5_high_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_5_high_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_5_high_threshold_slider.setMaximum(255)
        self.CN_5_high_threshold_slider.setPageStep(2)
        self.CN_5_high_threshold_slider.setValue(200)
        self.CN_5_high_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_5_high_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_5_high_threshold_slider.setTickInterval(4)
        self.label_cnet52 = QLabel(self.CN_5_high_threshold_poppable)
        self.label_cnet52.setObjectName(u"label_cnet52")
        self.label_cnet52.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet52.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_5_high_threshold_slider_value = QLabel(self.CN_5_high_threshold_poppable)
        self.CN_5_high_threshold_slider_value.setObjectName(u"CN_5_high_threshold_slider_value")
        self.CN_5_high_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_5_high_threshold_slider_value.setFont(font1)
        self.CN_5_high_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_5_high_threshold_slider_value.setIndent(0)
        self.CN_5_weight_poppable = QFrame(self.tab_CN05)
        self.CN_5_weight_poppable.setObjectName(u"CN_5_weight_poppable")
        self.CN_5_weight_poppable.setGeometry(QRect(8, 8, 257, 87))
        self.CN_5_weight_poppable.setTabletTracking(True)
        self.CN_5_weight_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_5_weight_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_5_weight_poppable.setFrameShadow(QFrame.Raised)
        self.CN_5_weight_slider = QSlider(self.CN_5_weight_poppable)
        self.CN_5_weight_slider.setObjectName(u"CN_5_weight_slider")
        self.CN_5_weight_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_5_weight_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_5_weight_slider.setMaximum(200)
        self.CN_5_weight_slider.setPageStep(2)
        self.CN_5_weight_slider.setValue(100)
        self.CN_5_weight_slider.setOrientation(Qt.Horizontal)
        self.CN_5_weight_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_5_weight_slider.setTickInterval(4)
        self.label_cnet55 = QLabel(self.CN_5_weight_poppable)
        self.label_cnet55.setObjectName(u"label_cnet55")
        self.label_cnet55.setGeometry(QRect(10, 8, 121, 25))
        self.label_cnet55.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_5_weight_slider_value = QLabel(self.CN_5_weight_poppable)
        self.CN_5_weight_slider_value.setObjectName(u"CN_5_weight_slider_value")
        self.CN_5_weight_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_5_weight_slider_value.setFont(font1)
        self.CN_5_weight_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_5_weight_slider_value.setIndent(0)
        self.CN_5_end_control_step_poppable = QFrame(self.tab_CN05)
        self.CN_5_end_control_step_poppable.setObjectName(u"CN_5_end_control_step_poppable")
        self.CN_5_end_control_step_poppable.setGeometry(QRect(532, 8, 257, 87))
        self.CN_5_end_control_step_poppable.setTabletTracking(True)
        self.CN_5_end_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_5_end_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_5_end_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_5_ending_control_step_slider = QSlider(self.CN_5_end_control_step_poppable)
        self.CN_5_ending_control_step_slider.setObjectName(u"CN_5_ending_control_step_slider")
        self.CN_5_ending_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_5_ending_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_5_ending_control_step_slider.setMaximum(100)
        self.CN_5_ending_control_step_slider.setPageStep(2)
        self.CN_5_ending_control_step_slider.setValue(100)
        self.CN_5_ending_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_5_ending_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_5_ending_control_step_slider.setTickInterval(4)
        self.label_cnet51 = QLabel(self.CN_5_end_control_step_poppable)
        self.label_cnet51.setObjectName(u"label_cnet51")
        self.label_cnet51.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet51.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_5_ending_control_step_slider_value = QLabel(self.CN_5_end_control_step_poppable)
        self.CN_5_ending_control_step_slider_value.setObjectName(u"CN_5_ending_control_step_slider_value")
        self.CN_5_ending_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_5_ending_control_step_slider_value.setFont(font1)
        self.CN_5_ending_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_5_ending_control_step_slider_value.setIndent(0)
        self.CN_5_start_control_step_poppable = QFrame(self.tab_CN05)
        self.CN_5_start_control_step_poppable.setObjectName(u"CN_5_start_control_step_poppable")
        self.CN_5_start_control_step_poppable.setGeometry(QRect(270, 8, 257, 87))
        self.CN_5_start_control_step_poppable.setTabletTracking(True)
        self.CN_5_start_control_step_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_5_start_control_step_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_5_start_control_step_poppable.setFrameShadow(QFrame.Raised)
        self.CN_5_starting_control_step_slider = QSlider(self.CN_5_start_control_step_poppable)
        self.CN_5_starting_control_step_slider.setObjectName(u"CN_5_starting_control_step_slider")
        self.CN_5_starting_control_step_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_5_starting_control_step_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_5_starting_control_step_slider.setMaximum(100)
        self.CN_5_starting_control_step_slider.setPageStep(2)
        self.CN_5_starting_control_step_slider.setValue(0)
        self.CN_5_starting_control_step_slider.setOrientation(Qt.Horizontal)
        self.CN_5_starting_control_step_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_5_starting_control_step_slider.setTickInterval(4)
        self.label_cnet54 = QLabel(self.CN_5_start_control_step_poppable)
        self.label_cnet54.setObjectName(u"label_cnet54")
        self.label_cnet54.setGeometry(QRect(10, 8, 155, 25))
        self.label_cnet54.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_5_starting_control_step_slider_value = QLabel(self.CN_5_start_control_step_poppable)
        self.CN_5_starting_control_step_slider_value.setObjectName(u"CN_5_starting_control_step_slider_value")
        self.CN_5_starting_control_step_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_5_starting_control_step_slider_value.setFont(font1)
        self.CN_5_starting_control_step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_5_starting_control_step_slider_value.setIndent(0)
        self.CN_5_low_threshold_poppable = QFrame(self.tab_CN05)
        self.CN_5_low_threshold_poppable.setObjectName(u"CN_5_low_threshold_poppable")
        self.CN_5_low_threshold_poppable.setGeometry(QRect(8, 100, 257, 87))
        self.CN_5_low_threshold_poppable.setTabletTracking(True)
        self.CN_5_low_threshold_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_5_low_threshold_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_5_low_threshold_poppable.setFrameShadow(QFrame.Raised)
        self.CN_5_low_threshold_slider = QSlider(self.CN_5_low_threshold_poppable)
        self.CN_5_low_threshold_slider.setObjectName(u"CN_5_low_threshold_slider")
        self.CN_5_low_threshold_slider.setGeometry(QRect(10, 42, 235, 32))
        self.CN_5_low_threshold_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.CN_5_low_threshold_slider.setMaximum(255)
        self.CN_5_low_threshold_slider.setPageStep(2)
        self.CN_5_low_threshold_slider.setValue(100)
        self.CN_5_low_threshold_slider.setOrientation(Qt.Horizontal)
        self.CN_5_low_threshold_slider.setTickPosition(QSlider.TicksBelow)
        self.CN_5_low_threshold_slider.setTickInterval(4)
        self.label_cnet53 = QLabel(self.CN_5_low_threshold_poppable)
        self.label_cnet53.setObjectName(u"label_cnet53")
        self.label_cnet53.setGeometry(QRect(10, 8, 161, 25))
        self.label_cnet53.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.CN_5_low_threshold_slider_value = QLabel(self.CN_5_low_threshold_poppable)
        self.CN_5_low_threshold_slider_value.setObjectName(u"CN_5_low_threshold_slider_value")
        self.CN_5_low_threshold_slider_value.setGeometry(QRect(194, 10, 46, 22))
        self.CN_5_low_threshold_slider_value.setFont(font1)
        self.CN_5_low_threshold_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.CN_5_low_threshold_slider_value.setIndent(0)
        self.tabWidget_CN.addTab(self.tab_CN05, "")
        self.CN_on_off_poppable = QFrame(self.ControlNet_tab)
        self.CN_on_off_poppable.setObjectName(u"CN_on_off_poppable")
        self.CN_on_off_poppable.setGeometry(QRect(14, 250, 518, 59))
        self.CN_on_off_poppable.setMouseTracking(False)
        self.CN_on_off_poppable.setTabletTracking(True)
        self.CN_on_off_poppable.setStyleSheet(u"background-color: rgb(80, 80, 80); /* Fallback color */")
        self.CN_on_off_poppable.setFrameShape(QFrame.StyledPanel)
        self.CN_on_off_poppable.setFrameShadow(QFrame.Raised)
        self.cn_udcn3 = QCheckBox(self.CN_on_off_poppable)
        self.cn_udcn3.setObjectName(u"cn_udcn3")
        self.cn_udcn3.setGeometry(QRect(208, 26, 104, 31))
        sizePolicy1.setHeightForWidth(self.cn_udcn3.sizePolicy().hasHeightForWidth())
        self.cn_udcn3.setSizePolicy(sizePolicy1)
        self.cn_udcn3.setBaseSize(QSize(0, 0))
        self.cn_udcn3.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 96px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.cn_udcn3.setIconSize(QSize(33, 20))
        self.cn_udcn4 = QCheckBox(self.CN_on_off_poppable)
        self.cn_udcn4.setObjectName(u"cn_udcn4")
        self.cn_udcn4.setGeometry(QRect(316, 26, 104, 31))
        sizePolicy1.setHeightForWidth(self.cn_udcn4.sizePolicy().hasHeightForWidth())
        self.cn_udcn4.setSizePolicy(sizePolicy1)
        self.cn_udcn4.setBaseSize(QSize(0, 0))
        self.cn_udcn4.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 96px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.cn_udcn4.setIconSize(QSize(33, 20))
        self.label_cnet2_switch = QLabel(self.CN_on_off_poppable)
        self.label_cnet2_switch.setObjectName(u"label_cnet2_switch")
        self.label_cnet2_switch.setGeometry(QRect(112, 7, 81, 18))
        self.label_cnet2_switch.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.label_cnet2_switch.setAlignment(Qt.AlignCenter)
        self.label_cnet4_switch = QLabel(self.CN_on_off_poppable)
        self.label_cnet4_switch.setObjectName(u"label_cnet4_switch")
        self.label_cnet4_switch.setGeometry(QRect(322, 7, 81, 18))
        self.label_cnet4_switch.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.label_cnet4_switch.setAlignment(Qt.AlignCenter)
        self.label_cnet3_switch = QLabel(self.CN_on_off_poppable)
        self.label_cnet3_switch.setObjectName(u"label_cnet3_switch")
        self.label_cnet3_switch.setGeometry(QRect(216, 7, 81, 18))
        self.label_cnet3_switch.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.label_cnet3_switch.setAlignment(Qt.AlignCenter)
        self.label_cnet1_switch = QLabel(self.CN_on_off_poppable)
        self.label_cnet1_switch.setObjectName(u"label_cnet1_switch")
        self.label_cnet1_switch.setGeometry(QRect(8, 7, 81, 18))
        self.label_cnet1_switch.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.label_cnet1_switch.setAlignment(Qt.AlignCenter)
        self.label_cnet5_switch = QLabel(self.CN_on_off_poppable)
        self.label_cnet5_switch.setObjectName(u"label_cnet5_switch")
        self.label_cnet5_switch.setGeometry(QRect(426, 7, 81, 18))
        self.label_cnet5_switch.setStyleSheet(u"border: 0;\n"
"background: none;")
        self.label_cnet5_switch.setAlignment(Qt.AlignCenter)
        self.cn_udcn5 = QCheckBox(self.CN_on_off_poppable)
        self.cn_udcn5.setObjectName(u"cn_udcn5")
        self.cn_udcn5.setGeometry(QRect(420, 26, 81, 31))
        sizePolicy1.setHeightForWidth(self.cn_udcn5.sizePolicy().hasHeightForWidth())
        self.cn_udcn5.setSizePolicy(sizePolicy1)
        self.cn_udcn5.setBaseSize(QSize(0, 0))
        self.cn_udcn5.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 96px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.cn_udcn5.setIconSize(QSize(33, 20))
        self.cn_udcn2 = QCheckBox(self.CN_on_off_poppable)
        self.cn_udcn2.setObjectName(u"cn_udcn2")
        self.cn_udcn2.setGeometry(QRect(106, 26, 104, 31))
        sizePolicy1.setHeightForWidth(self.cn_udcn2.sizePolicy().hasHeightForWidth())
        self.cn_udcn2.setSizePolicy(sizePolicy1)
        self.cn_udcn2.setBaseSize(QSize(0, 0))
        self.cn_udcn2.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 96px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.cn_udcn2.setIconSize(QSize(33, 20))
        self.cn_udcn1 = QCheckBox(self.CN_on_off_poppable)
        self.cn_udcn1.setObjectName(u"cn_udcn1")
        self.cn_udcn1.setGeometry(QRect(28, 26, 53, 27))
        sizePolicy1.setHeightForWidth(self.cn_udcn1.sizePolicy().hasHeightForWidth())
        self.cn_udcn1.setSizePolicy(sizePolicy1)
        self.cn_udcn1.setBaseSize(QSize(0, 0))
        self.cn_udcn1.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 45px; /* Width of the checkbox */\n"
"    height: 25px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: center; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.cn_udcn1.setIconSize(QSize(33, 20))
        self.deforumation_tabWidget.addTab(self.ControlNet_tab, "")
        self.Misc_Tab_A = QWidget()
        self.Misc_Tab_A.setObjectName(u"Misc_Tab_A")
        self.Misc_Tab_A.setMinimumSize(QSize(0, 0))
        self.Misc_Tab_A.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.morph_slider = QSlider(self.Misc_Tab_A)
        self.morph_slider.setObjectName(u"morph_slider")
        self.morph_slider.setGeometry(QRect(264, 124, 643, 33))
        sizePolicy1.setHeightForWidth(self.morph_slider.sizePolicy().hasHeightForWidth())
        self.morph_slider.setSizePolicy(sizePolicy1)
        self.morph_slider.setMinimumSize(QSize(0, 33))
        self.morph_slider.setMaximumSize(QSize(16777215, 33))
        self.morph_slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px;"
                        " /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
" ")
        self.morph_slider.setMinimum(-100)
        self.morph_slider.setMaximum(100)
        self.morph_slider.setOrientation(Qt.Horizontal)
        self.morphing_text_howto_label = QLabel(self.Misc_Tab_A)
        self.morphing_text_howto_label.setObjectName(u"morphing_text_howto_label")
        self.morphing_text_howto_label.setGeometry(QRect(264, 157, 643, 29))
        sizePolicy1.setHeightForWidth(self.morphing_text_howto_label.sizePolicy().hasHeightForWidth())
        self.morphing_text_howto_label.setSizePolicy(sizePolicy1)
        self.morphing_text_howto_label.setMinimumSize(QSize(0, 22))
        font13 = QFont()
        font13.setPointSize(10)
        self.morphing_text_howto_label.setFont(font13)
        self.morphing_text_howto_label.setStyleSheet(u"")
        self.morphing_text_howto_label.setScaledContents(False)
        self.morphing_text_howto_label.setAlignment(Qt.AlignCenter)
        self.morphing_text_howto_label.setWordWrap(True)
        self.prpmta_to_promptb_label = QLabel(self.Misc_Tab_A)
        self.prpmta_to_promptb_label.setObjectName(u"prpmta_to_promptb_label")
        self.prpmta_to_promptb_label.setGeometry(QRect(264, 96, 643, 28))
        self.prpmta_to_promptb_label.setMinimumSize(QSize(0, 28))
        self.prpmta_to_promptb_label.setMaximumSize(QSize(16777215, 28))
        self.prpmta_to_promptb_label.setFont(font2)
        self.prpmta_to_promptb_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.deforumation_tabWidget.addTab(self.Misc_Tab_A, "")
        self.Misc_Tab_B = QWidget()
        self.Misc_Tab_B.setObjectName(u"Misc_Tab_B")
        self.Misc_Tab_B.setStyleSheet(u"background-color: rgb(102,102,102);\n"
"\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"border-radius: 10px;\n"
"padding: 1px; /* To prevent the content from touching the border */\n"
"\n"
"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 12px; /* Comfortable padding for the button text */\n"
"    color: white; /* White text for contrast */\n"
"    text-align: center;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n"
"\n"
"}\n"
"\n"
"\n"
"")
        self.deforumation_tabWidget.addTab(self.Misc_Tab_B, "")

        self.gridLayout_2.addWidget(self.deforumation_tabWidget, 1, 0, 1, 1)


        self.gridLayout_81.addWidget(self.tabWidget_frame, 0, 0, 1, 1)

        self.splitter.addWidget(self.Tab_Tabs)

        self.gridLayout_4.addWidget(self.splitter, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.Deforumation_Main, 0, 1, 1, 1)

        self.splitter_3.addWidget(self.Left_Frame)
        self.Right_Frame = QFrame(self.splitter_3)
        self.Right_Frame.setObjectName(u"Right_Frame")
        sizePolicy1.setHeightForWidth(self.Right_Frame.sizePolicy().hasHeightForWidth())
        self.Right_Frame.setSizePolicy(sizePolicy1)
        self.Right_Frame.setMinimumSize(QSize(300, 0))
        self.Right_Frame.setMaximumSize(QSize(250, 16777215))
        self.Right_Frame.setStyleSheet(u"")
        self.Right_Frame.setFrameShape(QFrame.StyledPanel)
        self.Right_Frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_17 = QGridLayout(self.Right_Frame)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(2, 5, 5, 0)
        self.stay_on_top_checkbox = QCheckBox(self.Right_Frame)
        self.stay_on_top_checkbox.setObjectName(u"stay_on_top_checkbox")
        sizePolicy16.setHeightForWidth(self.stay_on_top_checkbox.sizePolicy().hasHeightForWidth())
        self.stay_on_top_checkbox.setSizePolicy(sizePolicy16)
        self.stay_on_top_checkbox.setMinimumSize(QSize(0, 40))
        self.stay_on_top_checkbox.setMaximumSize(QSize(300, 16777215))
        self.stay_on_top_checkbox.setFont(font3)
        self.stay_on_top_checkbox.setLayoutDirection(Qt.RightToLeft)
        self.stay_on_top_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"    border-radius: 10px;\n"
"    padding: 1px; /* To prevent the content from touching the border */\n"
"spacing:28px\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 22px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */"
                        "\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.stay_on_top_checkbox.setIconSize(QSize(20, 20))
        self.stay_on_top_checkbox.setCheckable(True)

        self.gridLayout_17.addWidget(self.stay_on_top_checkbox, 0, 0, 1, 1)

        self.right_frame_frame = QFrame(self.Right_Frame)
        self.right_frame_frame.setObjectName(u"right_frame_frame")
        self.right_frame_frame.setStyleSheet(u"border: 0px")
        self.right_frame_frame.setFrameShape(QFrame.StyledPanel)
        self.right_frame_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.right_frame_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.splitter_2 = QSplitter(self.right_frame_frame)
        self.splitter_2.setObjectName(u"splitter_2")
        sizePolicy1.setHeightForWidth(self.splitter_2.sizePolicy().hasHeightForWidth())
        self.splitter_2.setSizePolicy(sizePolicy1)
        self.splitter_2.setStyleSheet(u"border: 0px;")
        self.splitter_2.setOrientation(Qt.Vertical)
        self.splitter_2.setHandleWidth(6)
        self.Slider_Tab = QFrame(self.splitter_2)
        self.Slider_Tab.setObjectName(u"Slider_Tab")
        sizePolicy2.setHeightForWidth(self.Slider_Tab.sizePolicy().hasHeightForWidth())
        self.Slider_Tab.setSizePolicy(sizePolicy2)
        self.Slider_Tab.setMinimumSize(QSize(0, 0))
        self.Slider_Tab.setStyleSheet(u"")
        self.Slider_Tab.setFrameShape(QFrame.StyledPanel)
        self.Slider_Tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.Slider_Tab)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.slider_tab_frame = QFrame(self.Slider_Tab)
        self.slider_tab_frame.setObjectName(u"slider_tab_frame")
        self.slider_tab_frame.setMinimumSize(QSize(0, 0))
        self.slider_tab_frame.setMaximumSize(QSize(300, 16777215))
        self.slider_tab_frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(108,108,118);\n"
"border: 2px solid rgb(40, 40, 40); /* Simulated shadow using border */\n"
"    border-radius: 10px;\n"
"    padding: 1px; /* To prevent the content from touching the border */\n"
"}\n"
"\n"
"QSlider\n"
"{\n"
"	background-color: rgb(108,108,118);\n"
"}")
        self.slider_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.slider_tab_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.slider_tab_frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 10, 10, 10)
        self.Live_ParameterLabel = QLabel(self.slider_tab_frame)
        self.Live_ParameterLabel.setObjectName(u"Live_ParameterLabel")
        sizePolicy1.setHeightForWidth(self.Live_ParameterLabel.sizePolicy().hasHeightForWidth())
        self.Live_ParameterLabel.setSizePolicy(sizePolicy1)
        self.Live_ParameterLabel.setFont(font)
        self.Live_ParameterLabel.setMouseTracking(True)
        self.Live_ParameterLabel.setTabletTracking(True)
        self.Live_ParameterLabel.setStyleSheet(u"QLabel {\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"        border: 2px solid rgb(32, 32, 32);\n"
"    border-radius: 10px;\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.Live_ParameterLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.Live_ParameterLabel, 0, 0, 1, 1)

        self.scrollArea_slider_frame = QScrollArea(self.slider_tab_frame)
        self.scrollArea_slider_frame.setObjectName(u"scrollArea_slider_frame")
        sizePolicy.setHeightForWidth(self.scrollArea_slider_frame.sizePolicy().hasHeightForWidth())
        self.scrollArea_slider_frame.setSizePolicy(sizePolicy)
        self.scrollArea_slider_frame.setMinimumSize(QSize(0, 0))
        self.scrollArea_slider_frame.setStyleSheet(u"QScrollArea {\n"
"    border: 0px solid #333; /* Adjust the color and size as needed */\n"
"background-color: rgb(108,108,118);\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrol"
                        "lBar::add-page:vertical {\n"
"    background: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_slider_frame.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_slider_frame.setWidgetResizable(True)
        self.scrollAreaWidgetContentsSliders = QWidget()
        self.scrollAreaWidgetContentsSliders.setObjectName(u"scrollAreaWidgetContentsSliders")
        self.scrollAreaWidgetContentsSliders.setGeometry(QRect(0, 0, 250, 352))
        self.scrollAreaWidgetContentsSliders.setMinimumSize(QSize(0, 352))
        self.scrollAreaWidgetContentsSliders.setStyleSheet(u"")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContentsSliders)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ubder_slider_frame = QFrame(self.scrollAreaWidgetContentsSliders)
        self.ubder_slider_frame.setObjectName(u"ubder_slider_frame")
        self.ubder_slider_frame.setStyleSheet(u"QWidget{\n"
"border: 0px solid rgb(128,128,128);\n"
"}\n"
"QFrame{\n"
"Qbackground-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px;\n"
" }")
        self.ubder_slider_frame.setFrameShape(QFrame.StyledPanel)
        self.ubder_slider_frame.setFrameShadow(QFrame.Raised)
        self.frame_live_params_poppable = QFrame(self.ubder_slider_frame)
        self.frame_live_params_poppable.setObjectName(u"frame_live_params_poppable")
        self.frame_live_params_poppable.setGeometry(QRect(12, 8, 245, 363))
        sizePolicy1.setHeightForWidth(self.frame_live_params_poppable.sizePolicy().hasHeightForWidth())
        self.frame_live_params_poppable.setSizePolicy(sizePolicy1)
        self.frame_live_params_poppable.setMinimumSize(QSize(0, 0))
        self.frame_live_params_poppable.setTabletTracking(True)
        self.frame_live_params_poppable.setStyleSheet(u"QFrame{\n"
"Qbackground-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}")
        self.frame_live_params_poppable.setFrameShape(QFrame.StyledPanel)
        self.frame_live_params_poppable.setFrameShadow(QFrame.Raised)
        self.live_parameter_frame = QFrame(self.frame_live_params_poppable)
        self.live_parameter_frame.setObjectName(u"live_parameter_frame")
        self.live_parameter_frame.setGeometry(QRect(0, 0, 241, 361))
        self.live_parameter_frame.setTabletTracking(False)
        self.live_parameter_frame.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"background-color: rgb(108, 108, 108); /* Fallback color */\n"
"padding:1;\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 34px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No bord"
                        "er for the checkbox */\n"
"}\n"
"QSlider::groove:horizontal {\n"
"    border-image: url(images/groove_230.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 29px; /* The height of your image */\n"
"    width: 215px; /* Width of the handle - adjust as needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"  background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:hover {\n"
"\n"
"    background-image: url(images/handle_hover.png); /* Change the handle image when hovering */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust a"
                        "s needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -2px 0; /* Optional: Adjust the margin if needed */\n"
"  \n"
"}\n"
"\n"
"QSlider::add-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background: none;\n"
"}\n"
"\n"
"QFrame{\n"
"Qbackground-color: rgb(108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}")
        self.live_parameter_frame.setFrameShape(QFrame.StyledPanel)
        self.live_parameter_frame.setFrameShadow(QFrame.Raised)
        self.Strength_Slider_poppable = QFrame(self.live_parameter_frame)
        self.Strength_Slider_poppable.setObjectName(u"Strength_Slider_poppable")
        self.Strength_Slider_poppable.setGeometry(QRect(8, 144, 225, 65))
        self.Strength_Slider_poppable.setTabletTracking(True)
        self.Strength_Slider_poppable.setStyleSheet(u"")
        self.Strength_Slider_poppable.setFrameShape(QFrame.StyledPanel)
        self.Strength_Slider_poppable.setFrameShadow(QFrame.Raised)
        self.strength_slider = QSlider(self.Strength_Slider_poppable)
        self.strength_slider.setObjectName(u"strength_slider")
        self.strength_slider.setGeometry(QRect(-4, 24, 235, 32))
        self.strength_slider.setStyleSheet(u"")
        self.strength_slider.setMaximum(100)
        self.strength_slider.setPageStep(1)
        self.strength_slider.setValue(68)
        self.strength_slider.setOrientation(Qt.Horizontal)
        self.strength_slider.setTickPosition(QSlider.TicksBelow)
        self.strength_slider.setTickInterval(4)
        self.strength_slider_label = QLabel(self.Strength_Slider_poppable)
        self.strength_slider_label.setObjectName(u"strength_slider_label")
        self.strength_slider_label.setGeometry(QRect(43, 0, 121, 25))
        self.strength_slider_label.setFont(font1)
        self.strength_slider_value = QLabel(self.Strength_Slider_poppable)
        self.strength_slider_value.setObjectName(u"strength_slider_value")
        self.strength_slider_value.setGeometry(QRect(170, 2, 46, 22))
        self.strength_slider_value.setFont(font1)
        self.strength_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.strength_slider_value.setIndent(0)
        self.strength_active_checkbox = QCheckBox(self.Strength_Slider_poppable)
        self.strength_active_checkbox.setObjectName(u"strength_active_checkbox")
        self.strength_active_checkbox.setGeometry(QRect(7, 2, 33, 20))
        self.strength_active_checkbox.setStyleSheet(u"")
        self.Step_Slider_Frame_poppable = QFrame(self.live_parameter_frame)
        self.Step_Slider_Frame_poppable.setObjectName(u"Step_Slider_Frame_poppable")
        self.Step_Slider_Frame_poppable.setGeometry(QRect(8, 2, 225, 65))
        self.Step_Slider_Frame_poppable.setTabletTracking(True)
        self.Step_Slider_Frame_poppable.setStyleSheet(u"")
        self.Step_Slider_Frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.Step_Slider_Frame_poppable.setFrameShadow(QFrame.Raised)
        self.step_slider = QSlider(self.Step_Slider_Frame_poppable)
        self.step_slider.setObjectName(u"step_slider")
        self.step_slider.setGeometry(QRect(-6, 24, 235, 32))
        self.step_slider.setTabletTracking(False)
        self.step_slider.setStyleSheet(u"")
        self.step_slider.setMinimum(1)
        self.step_slider.setMaximum(200)
        self.step_slider.setPageStep(1)
        self.step_slider.setValue(50)
        self.step_slider.setOrientation(Qt.Horizontal)
        self.step_slider.setTickPosition(QSlider.TicksBelow)
        self.step_slider.setTickInterval(8)
        self.step_slider_label = QLabel(self.Step_Slider_Frame_poppable)
        self.step_slider_label.setObjectName(u"step_slider_label")
        self.step_slider_label.setGeometry(QRect(43, 2, 121, 21))
        self.step_slider_label.setFont(font1)
        self.step_slider_label.setStyleSheet(u"")
        self.step_slider_value = QLabel(self.Step_Slider_Frame_poppable)
        self.step_slider_value.setObjectName(u"step_slider_value")
        self.step_slider_value.setGeometry(QRect(170, 2, 46, 22))
        self.step_slider_value.setMinimumSize(QSize(0, 6))
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setKerning(True)
        self.step_slider_value.setFont(font14)
        self.step_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.step_slider_value.setMargin(0)
        self.step_slider_value.setIndent(0)
        self.Noice_Slider_poppable = QFrame(self.live_parameter_frame)
        self.Noice_Slider_poppable.setObjectName(u"Noice_Slider_poppable")
        self.Noice_Slider_poppable.setGeometry(QRect(8, 286, 225, 65))
        self.Noice_Slider_poppable.setTabletTracking(True)
        self.Noice_Slider_poppable.setStyleSheet(u"")
        self.Noice_Slider_poppable.setFrameShape(QFrame.StyledPanel)
        self.Noice_Slider_poppable.setFrameShadow(QFrame.Raised)
        self.noise_slider = QSlider(self.Noice_Slider_poppable)
        self.noise_slider.setObjectName(u"noise_slider")
        self.noise_slider.setGeometry(QRect(-4, 24, 235, 32))
        self.noise_slider.setStyleSheet(u"")
        self.noise_slider.setMinimum(1)
        self.noise_slider.setMaximum(200)
        self.noise_slider.setSingleStep(1)
        self.noise_slider.setPageStep(1)
        self.noise_slider.setValue(3)
        self.noise_slider.setOrientation(Qt.Horizontal)
        self.noise_slider.setTickPosition(QSlider.TicksBelow)
        self.noise_slider.setTickInterval(1)
        self.noise_slider_label = QLabel(self.Noice_Slider_poppable)
        self.noise_slider_label.setObjectName(u"noise_slider_label")
        self.noise_slider_label.setGeometry(QRect(43, 0, 121, 21))
        self.noise_slider_label.setFont(font1)
        self.noise_slider_value = QLabel(self.Noice_Slider_poppable)
        self.noise_slider_value.setObjectName(u"noise_slider_value")
        self.noise_slider_value.setGeometry(QRect(170, 2, 46, 22))
        self.noise_slider_value.setFont(font1)
        self.noise_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.noise_slider_value.setIndent(0)
        self.noise_multiplier_active_checkbox = QCheckBox(self.Noice_Slider_poppable)
        self.noise_multiplier_active_checkbox.setObjectName(u"noise_multiplier_active_checkbox")
        self.noise_multiplier_active_checkbox.setGeometry(QRect(7, 2, 33, 20))
        self.noise_multiplier_active_checkbox.setAutoFillBackground(False)
        self.noise_multiplier_active_checkbox.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"")
        self.noise_multiplier_active_checkbox.setTristate(False)
        self.CFG_Slider_poppable = QFrame(self.live_parameter_frame)
        self.CFG_Slider_poppable.setObjectName(u"CFG_Slider_poppable")
        self.CFG_Slider_poppable.setEnabled(True)
        self.CFG_Slider_poppable.setGeometry(QRect(8, 73, 225, 65))
        self.CFG_Slider_poppable.setTabletTracking(True)
        self.CFG_Slider_poppable.setStyleSheet(u"")
        self.CFG_Slider_poppable.setFrameShape(QFrame.StyledPanel)
        self.CFG_Slider_poppable.setFrameShadow(QFrame.Raised)
        self.cfg_slider = QSlider(self.CFG_Slider_poppable)
        self.cfg_slider.setObjectName(u"cfg_slider")
        self.cfg_slider.setGeometry(QRect(-6, 24, 235, 32))
        self.cfg_slider.setStyleSheet(u"QCheckBox {\n"
"    border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"    width: 54px; /* Width of the checkbox */\n"
"    height: 29px; /* Height of the checkbox */\n"
"    background-color: transparent; /* Ensures background is transparent */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"    background-image: url(images/check_off_small.png); /* Image for unchecked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background-image: url(images/check_on_small.png); /* Image for checked state */\n"
"    background-repeat: no-repeat; /* Prevents the image from repeating */\n"
"background-position: left; /* Left the image */\n"
"border: none; /* No border for the checkbox */\n"
"}\n"
"\n"
"\n"
"QFrame{\n"
"Qbackground-color: rgb("
                        "108,108,118);\n"
"border: 0px solid rgb(128,128,128);\n"
"border-radius: 0px;\n"
"}")
        self.cfg_slider.setMinimum(1)
        self.cfg_slider.setMaximum(30)
        self.cfg_slider.setPageStep(1)
        self.cfg_slider.setValue(3)
        self.cfg_slider.setOrientation(Qt.Horizontal)
        self.cfg_slider.setTickPosition(QSlider.TicksBelow)
        self.cfg_slider.setTickInterval(1)
        self.cfg_slider_label = QLabel(self.CFG_Slider_poppable)
        self.cfg_slider_label.setObjectName(u"cfg_slider_label")
        self.cfg_slider_label.setGeometry(QRect(43, 0, 121, 21))
        self.cfg_slider_label.setFont(font1)
        self.cfg_slider_value = QLabel(self.CFG_Slider_poppable)
        self.cfg_slider_value.setObjectName(u"cfg_slider_value")
        self.cfg_slider_value.setGeometry(QRect(170, 2, 46, 22))
        self.cfg_slider_value.setMinimumSize(QSize(0, 0))
        self.cfg_slider_value.setFont(font1)
        self.cfg_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.cfg_slider_value.setIndent(0)
        self.cfg_active_checkbox = QCheckBox(self.CFG_Slider_poppable)
        self.cfg_active_checkbox.setObjectName(u"cfg_active_checkbox")
        self.cfg_active_checkbox.setGeometry(QRect(7, 2, 33, 20))
        sizePolicy1.setHeightForWidth(self.cfg_active_checkbox.sizePolicy().hasHeightForWidth())
        self.cfg_active_checkbox.setSizePolicy(sizePolicy1)
        self.cfg_active_checkbox.setBaseSize(QSize(0, 0))
        self.cfg_active_checkbox.setStyleSheet(u"")
        self.cfg_active_checkbox.setIconSize(QSize(33, 20))
        self.Cadence_Slider_poppable = QFrame(self.live_parameter_frame)
        self.Cadence_Slider_poppable.setObjectName(u"Cadence_Slider_poppable")
        self.Cadence_Slider_poppable.setGeometry(QRect(8, 215, 225, 65))
        self.Cadence_Slider_poppable.setTabletTracking(True)
        self.Cadence_Slider_poppable.setStyleSheet(u"")
        self.Cadence_Slider_poppable.setFrameShape(QFrame.StyledPanel)
        self.Cadence_Slider_poppable.setFrameShadow(QFrame.Raised)
        self.cadence_slider = QSlider(self.Cadence_Slider_poppable)
        self.cadence_slider.setObjectName(u"cadence_slider")
        self.cadence_slider.setGeometry(QRect(-4, 24, 235, 32))
        self.cadence_slider.setStyleSheet(u"")
        self.cadence_slider.setMinimum(1)
        self.cadence_slider.setMaximum(30)
        self.cadence_slider.setPageStep(1)
        self.cadence_slider.setValue(3)
        self.cadence_slider.setOrientation(Qt.Horizontal)
        self.cadence_slider.setTickPosition(QSlider.TicksBelow)
        self.cadence_slider.setTickInterval(1)
        self.cadence_slider_label = QLabel(self.Cadence_Slider_poppable)
        self.cadence_slider_label.setObjectName(u"cadence_slider_label")
        self.cadence_slider_label.setGeometry(QRect(43, 0, 121, 21))
        self.cadence_slider_label.setFont(font1)
        self.cadence_slider_value = QLabel(self.Cadence_Slider_poppable)
        self.cadence_slider_value.setObjectName(u"cadence_slider_value")
        self.cadence_slider_value.setGeometry(QRect(170, 2, 46, 22))
        self.cadence_slider_value.setFont(font1)
        self.cadence_slider_value.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 2px solid rgb(40,40,40); border-radius: 5px;*/\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.cadence_slider_value.setIndent(0)
        self.cadence_active_checkbox = QCheckBox(self.Cadence_Slider_poppable)
        self.cadence_active_checkbox.setObjectName(u"cadence_active_checkbox")
        self.cadence_active_checkbox.setGeometry(QRect(7, 2, 33, 20))
        self.cadence_active_checkbox.setStyleSheet(u"")

        self.verticalLayout_7.addWidget(self.ubder_slider_frame)

        self.scrollArea_slider_frame.setWidget(self.scrollAreaWidgetContentsSliders)

        self.gridLayout_9.addWidget(self.scrollArea_slider_frame, 2, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.slider_tab_frame)

        self.splitter_2.addWidget(self.Slider_Tab)
        self.LiveValue_Tab = QFrame(self.splitter_2)
        self.LiveValue_Tab.setObjectName(u"LiveValue_Tab")
        sizePolicy4.setHeightForWidth(self.LiveValue_Tab.sizePolicy().hasHeightForWidth())
        self.LiveValue_Tab.setSizePolicy(sizePolicy4)
        self.LiveValue_Tab.setMinimumSize(QSize(0, 0))
        self.LiveValue_Tab.setStyleSheet(u"border: 0px")
        self.LiveValue_Tab.setFrameShape(QFrame.StyledPanel)
        self.LiveValue_Tab.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.LiveValue_Tab)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.live_value_tab_frame = QFrame(self.LiveValue_Tab)
        self.live_value_tab_frame.setObjectName(u"live_value_tab_frame")
        self.live_value_tab_frame.setMaximumSize(QSize(300, 16777215))
        self.live_value_tab_frame.setStyleSheet(u"\n"
"    background-color: rgb(108, 108, 118);\n"
"    border: 2px solid rgb(40, 40, 40); /* Refined shadow effect */\n"
"    border-radius: 10px; /* Smooth rounded corners */\n"
"")
        self.live_value_tab_frame.setFrameShape(QFrame.StyledPanel)
        self.live_value_tab_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_10 = QGridLayout(self.live_value_tab_frame)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(10, 10, 10, 10)
        self.scrollArea_live_values = QScrollArea(self.live_value_tab_frame)
        self.scrollArea_live_values.setObjectName(u"scrollArea_live_values")
        self.scrollArea_live_values.setMinimumSize(QSize(0, 0))
        self.scrollArea_live_values.setStyleSheet(u"QScrollArea {\n"
"    border: 0px solid #333; /* Adjust the color and size as needed */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar:vertical {\n"
"    border: 2px;\n"
"    background: rgb(66,66,66);\n"
"    width: 15px; /* Narrow scrollbar for a sleek look */\n"
"    border-radius: 5px;\n"
"    margin: 0px 0 0px 0;\n"
"    \n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical {\n"
"    background-color: rgb(40,129,232); /* Dark handle */\n"
"    min-height: 20px; /* Minimum handle height */\n"
"    border-radius: 5px; /* Rounded corners for the handle */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::handle:vertical:hover {\n"
"    background-color: rgb(59,165,0); /* Slightly lighter handle on hover */\n"
"}\n"
"\n"
"\n"
"QScrollArea QScrollBar::sub-line:vertical,\n"
"QScrollArea QScrollBar::add-line:vertical {\n"
"    background: none;\n"
"border: none; /* No buttons at the end of the scrollbar */\n"
"}\n"
"\n"
"QScrollArea QScrollBar::sub-page:vertical,\n"
"QScrollArea QScrollBar::add-page:vertical {\n"
"    backgr"
                        "ound: none; \n"
"border: none;/* No background for the scrollable area behind the handle */\n"
"}")
        self.scrollArea_live_values.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_live_values.setWidgetResizable(True)
        self.scrollAreaWidgetContentsLiveValues = QWidget()
        self.scrollAreaWidgetContentsLiveValues.setObjectName(u"scrollAreaWidgetContentsLiveValues")
        self.scrollAreaWidgetContentsLiveValues.setGeometry(QRect(0, 0, 269, 462))
        sizePolicy1.setHeightForWidth(self.scrollAreaWidgetContentsLiveValues.sizePolicy().hasHeightForWidth())
        self.scrollAreaWidgetContentsLiveValues.setSizePolicy(sizePolicy1)
        self.scrollAreaWidgetContentsLiveValues.setMinimumSize(QSize(0, 390))
        self.scrollAreaWidgetContentsLiveValues.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidgetContentsLiveValues)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_live_values = QFrame(self.scrollAreaWidgetContentsLiveValues)
        self.frame_live_values.setObjectName(u"frame_live_values")
        self.frame_live_values.setMinimumSize(QSize(0, 0))
        self.frame_live_values.setAutoFillBackground(False)
        self.frame_live_values.setStyleSheet(u"background-color: rgb(108,108,118); border: 0px solid rgb(128,128,128); border-radius: 0px;")
        self.frame_live_values.setFrameShape(QFrame.StyledPanel)
        self.frame_live_values.setFrameShadow(QFrame.Raised)
        self.live_value_frame_poppable = QFrame(self.frame_live_values)
        self.live_value_frame_poppable.setObjectName(u"live_value_frame_poppable")
        self.live_value_frame_poppable.setGeometry(QRect(16, 8, 255, 377))
        self.live_value_frame_poppable.setTabletTracking(True)
        self.live_value_frame_poppable.setStyleSheet(u"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.live_value_frame_poppable.setFrameShape(QFrame.StyledPanel)
        self.live_value_frame_poppable.setFrameShadow(QFrame.Raised)
        self.live_value_names = QWidget(self.live_value_frame_poppable)
        self.live_value_names.setObjectName(u"live_value_names")
        self.live_value_names.setGeometry(QRect(0, 0, 113, 385))
        self.verticalLayoutWidget = QWidget(self.live_value_names)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 109, 377))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.panning_x_label = QLabel(self.verticalLayoutWidget)
        self.panning_x_label.setObjectName(u"panning_x_label")
        self.panning_x_label.setMinimumSize(QSize(0, 0))
        self.panning_x_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.panning_x_label)

        self.panning_y_label = QLabel(self.verticalLayoutWidget)
        self.panning_y_label.setObjectName(u"panning_y_label")
        self.panning_y_label.setMinimumSize(QSize(0, 0))
        self.panning_y_label.setFont(font2)
        self.panning_y_label.setTextFormat(Qt.AutoText)

        self.verticalLayout_2.addWidget(self.panning_y_label)

        self.rotate_h_label = QLabel(self.verticalLayoutWidget)
        self.rotate_h_label.setObjectName(u"rotate_h_label")
        self.rotate_h_label.setMinimumSize(QSize(0, 0))
        self.rotate_h_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.rotate_h_label)

        self.rotate_v_label = QLabel(self.verticalLayoutWidget)
        self.rotate_v_label.setObjectName(u"rotate_v_label")
        self.rotate_v_label.setMinimumSize(QSize(0, 0))
        self.rotate_v_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.rotate_v_label)

        self.zoom_label = QLabel(self.verticalLayoutWidget)
        self.zoom_label.setObjectName(u"zoom_label")
        self.zoom_label.setMinimumSize(QSize(0, 0))
        self.zoom_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.zoom_label)

        self.tilt_label = QLabel(self.verticalLayoutWidget)
        self.tilt_label.setObjectName(u"tilt_label")
        self.tilt_label.setMinimumSize(QSize(0, 0))
        self.tilt_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.tilt_label)

        self.fov_label = QLabel(self.verticalLayoutWidget)
        self.fov_label.setObjectName(u"fov_label")
        self.fov_label.setMinimumSize(QSize(0, 0))
        self.fov_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.fov_label)

        self.steps_label = QLabel(self.verticalLayoutWidget)
        self.steps_label.setObjectName(u"steps_label")
        self.steps_label.setMinimumSize(QSize(0, 0))
        self.steps_label.setFont(font2)
        self.steps_label.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.steps_label)

        self.strength_label = QLabel(self.verticalLayoutWidget)
        self.strength_label.setObjectName(u"strength_label")
        self.strength_label.setMinimumSize(QSize(0, 0))
        self.strength_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.strength_label)

        self.cfg_label = QLabel(self.verticalLayoutWidget)
        self.cfg_label.setObjectName(u"cfg_label")
        self.cfg_label.setMinimumSize(QSize(0, 0))
        self.cfg_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.cfg_label)

        self.cadence_label = QLabel(self.verticalLayoutWidget)
        self.cadence_label.setObjectName(u"cadence_label")
        self.cadence_label.setMinimumSize(QSize(0, 0))
        self.cadence_label.setFont(font2)

        self.verticalLayout_2.addWidget(self.cadence_label)

        self.noise_multi_label = QLabel(self.verticalLayoutWidget)
        self.noise_multi_label.setObjectName(u"noise_multi_label")
        self.noise_multi_label.setMinimumSize(QSize(0, 0))
        font15 = QFont()
        font15.setFamilies([u"Segoe UI"])
        font15.setPointSize(12)
        self.noise_multi_label.setFont(font15)

        self.verticalLayout_2.addWidget(self.noise_multi_label)

        self.seed_value_label = QLabel(self.verticalLayoutWidget)
        self.seed_value_label.setObjectName(u"seed_value_label")
        self.seed_value_label.setMinimumSize(QSize(0, 0))
        self.seed_value_label.setFont(font15)

        self.verticalLayout_2.addWidget(self.seed_value_label)

        self.live_value_row = QFrame(self.live_value_frame_poppable)
        self.live_value_row.setObjectName(u"live_value_row")
        self.live_value_row.setGeometry(QRect(120, 0, 89, 377))
        self.live_value_row.setStyleSheet(u"/*background-color:rgb(42, 42, 42);color: rgb(0, 255, 0); border: 1px solid rgb(128,128,128); border-radius: 2px;*/\n"
"\n"
"\n"
"\n"
"QLabel {\n"
"    background-color: rgb(42, 42, 42); /* Dark background */\n"
"    color: rgb(0, 255, 0); /* Bright green text */\n"
"    border: 2px solid rgb(40, 40, 40); /* Dark grey border */\n"
"    border-radius: 5px; /* Rounded corners */\n"
"    padding-top: 1px; /* Top padding to push the text down */\n"
"    padding-bottom: 1px; /* Bottom padding for even spacing */\n"
"    padding-left: 1px; /* Left padding */\n"
"    padding-right: 1px; /* Right padding */\n"
"    text-align: center; /* Center the text horizontally */\n"
"}")
        self.live_value_row.setFrameShape(QFrame.StyledPanel)
        self.live_value_row.setFrameShadow(QFrame.Raised)
        self.verticalLayoutWidget_2 = QWidget(self.live_value_row)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(6, 0, 81, 377))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.panning_x_live_value = QLabel(self.verticalLayoutWidget_2)
        self.panning_x_live_value.setObjectName(u"panning_x_live_value")
        self.panning_x_live_value.setMaximumSize(QSize(50, 16777215))
        self.panning_x_live_value.setFont(font2)
        self.panning_x_live_value.setFrameShape(QFrame.NoFrame)
        self.panning_x_live_value.setFrameShadow(QFrame.Plain)
        self.panning_x_live_value.setLineWidth(1)
        self.panning_x_live_value.setScaledContents(False)

        self.verticalLayout_3.addWidget(self.panning_x_live_value)

        self.panning_y_live_value = QLabel(self.verticalLayoutWidget_2)
        self.panning_y_live_value.setObjectName(u"panning_y_live_value")
        self.panning_y_live_value.setMaximumSize(QSize(50, 16777215))
        self.panning_y_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.panning_y_live_value)

        self.rotate_h_live_value = QLabel(self.verticalLayoutWidget_2)
        self.rotate_h_live_value.setObjectName(u"rotate_h_live_value")
        self.rotate_h_live_value.setMaximumSize(QSize(50, 16777215))
        self.rotate_h_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.rotate_h_live_value)

        self.rotate_v_live_value = QLabel(self.verticalLayoutWidget_2)
        self.rotate_v_live_value.setObjectName(u"rotate_v_live_value")
        self.rotate_v_live_value.setMaximumSize(QSize(50, 16777215))
        self.rotate_v_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.rotate_v_live_value)

        self.zoom_live_value = QLabel(self.verticalLayoutWidget_2)
        self.zoom_live_value.setObjectName(u"zoom_live_value")
        self.zoom_live_value.setMaximumSize(QSize(50, 16777215))
        self.zoom_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.zoom_live_value)

        self.tilt_live_value = QLabel(self.verticalLayoutWidget_2)
        self.tilt_live_value.setObjectName(u"tilt_live_value")
        self.tilt_live_value.setMaximumSize(QSize(50, 16777215))
        self.tilt_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.tilt_live_value)

        self.fov_live_value = QLabel(self.verticalLayoutWidget_2)
        self.fov_live_value.setObjectName(u"fov_live_value")
        self.fov_live_value.setMaximumSize(QSize(50, 16777215))
        self.fov_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.fov_live_value)

        self.steps_live_value = QLabel(self.verticalLayoutWidget_2)
        self.steps_live_value.setObjectName(u"steps_live_value")
        self.steps_live_value.setMaximumSize(QSize(50, 16777215))
        self.steps_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.steps_live_value)

        self.strength_live_value = QLabel(self.verticalLayoutWidget_2)
        self.strength_live_value.setObjectName(u"strength_live_value")
        self.strength_live_value.setMaximumSize(QSize(50, 16777215))
        self.strength_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.strength_live_value)

        self.cfg_live_value = QLabel(self.verticalLayoutWidget_2)
        self.cfg_live_value.setObjectName(u"cfg_live_value")
        self.cfg_live_value.setMaximumSize(QSize(50, 16777215))
        self.cfg_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.cfg_live_value)

        self.cadence_live_value = QLabel(self.verticalLayoutWidget_2)
        self.cadence_live_value.setObjectName(u"cadence_live_value")
        self.cadence_live_value.setMaximumSize(QSize(50, 16777215))
        self.cadence_live_value.setFont(font2)

        self.verticalLayout_3.addWidget(self.cadence_live_value)

        self.noise_multiplier_live = QLabel(self.verticalLayoutWidget_2)
        self.noise_multiplier_live.setObjectName(u"noise_multiplier_live")
        self.noise_multiplier_live.setMaximumSize(QSize(50, 16777215))
        self.noise_multiplier_live.setFont(font2)

        self.verticalLayout_3.addWidget(self.noise_multiplier_live)

        self.seed_live_value = QLabel(self.verticalLayoutWidget_2)
        self.seed_live_value.setObjectName(u"seed_live_value")
        self.seed_live_value.setMaximumSize(QSize(90, 16777215))
        self.seed_live_value.setFont(font12)

        self.verticalLayout_3.addWidget(self.seed_live_value)

        self.panx_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.panx_rise_fall_frame.setObjectName(u"panx_rise_fall_frame")
        self.panx_rise_fall_frame.setGeometry(QRect(209, 3, 48, 24))
        self.panx_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.panx_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.panx_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.panx_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.panx_l = QLabel(self.panx_rise_fall_frame)
        self.panx_l.setObjectName(u"panx_l")
        self.panx_l.setGeometry(QRect(1, 1, 24, 24))
        self.panx_l.setStyleSheet(u"")
        self.panx_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.panx_r = QLabel(self.panx_rise_fall_frame)
        self.panx_r.setObjectName(u"panx_r")
        self.panx_r.setGeometry(QRect(24, 1, 24, 24))
        self.panx_r.setStyleSheet(u"")
        self.panx_r.setPixmap(QPixmap(u"images/value_rising_off.png"))
        self.pany_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.pany_rise_fall_frame.setObjectName(u"pany_rise_fall_frame")
        self.pany_rise_fall_frame.setGeometry(QRect(209, 33, 49, 24))
        self.pany_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.pany_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.pany_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.pany_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.pany_l = QLabel(self.pany_rise_fall_frame)
        self.pany_l.setObjectName(u"pany_l")
        self.pany_l.setGeometry(QRect(0, 0, 26, 26))
        self.pany_l.setStyleSheet(u"")
        self.pany_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.pany_r = QLabel(self.pany_rise_fall_frame)
        self.pany_r.setObjectName(u"pany_r")
        self.pany_r.setGeometry(QRect(24, 1, 24, 24))
        self.pany_r.setStyleSheet(u"")
        self.pany_r.setPixmap(QPixmap(u"images/value_rising_off.png"))
        self.roth_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.roth_rise_fall_frame.setObjectName(u"roth_rise_fall_frame")
        self.roth_rise_fall_frame.setGeometry(QRect(209, 62, 48, 24))
        self.roth_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.roth_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.roth_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.roth_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.roth_l = QLabel(self.roth_rise_fall_frame)
        self.roth_l.setObjectName(u"roth_l")
        self.roth_l.setGeometry(QRect(0, 0, 26, 26))
        self.roth_l.setStyleSheet(u"")
        self.roth_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.roth_r = QLabel(self.roth_rise_fall_frame)
        self.roth_r.setObjectName(u"roth_r")
        self.roth_r.setGeometry(QRect(24, 1, 24, 24))
        self.roth_r.setStyleSheet(u"")
        self.roth_r.setPixmap(QPixmap(u"images/value_rising_off.png"))
        self.rotv_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.rotv_rise_fall_frame.setObjectName(u"rotv_rise_fall_frame")
        self.rotv_rise_fall_frame.setGeometry(QRect(209, 91, 48, 26))
        self.rotv_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.rotv_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.rotv_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.rotv_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.rotv_l = QLabel(self.rotv_rise_fall_frame)
        self.rotv_l.setObjectName(u"rotv_l")
        self.rotv_l.setGeometry(QRect(0, 0, 26, 26))
        self.rotv_l.setStyleSheet(u"")
        self.rotv_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.rotv_r = QLabel(self.rotv_rise_fall_frame)
        self.rotv_r.setObjectName(u"rotv_r")
        self.rotv_r.setGeometry(QRect(24, 1, 24, 24))
        self.rotv_r.setStyleSheet(u"")
        self.rotv_r.setPixmap(QPixmap(u"images/value_rising_off.png"))
        self.zoom_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.zoom_rise_fall_frame.setObjectName(u"zoom_rise_fall_frame")
        self.zoom_rise_fall_frame.setGeometry(QRect(209, 120, 48, 24))
        self.zoom_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.zoom_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.zoom_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.zoom_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.zoom_l = QLabel(self.zoom_rise_fall_frame)
        self.zoom_l.setObjectName(u"zoom_l")
        self.zoom_l.setGeometry(QRect(0, 0, 26, 26))
        self.zoom_l.setStyleSheet(u"")
        self.zoom_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.zoom_r = QLabel(self.zoom_rise_fall_frame)
        self.zoom_r.setObjectName(u"zoom_r")
        self.zoom_r.setGeometry(QRect(24, 1, 24, 24))
        self.zoom_r.setStyleSheet(u"")
        self.zoom_r.setPixmap(QPixmap(u"images/value_rising_off.png"))
        self.tilt_rise_fall_frame = QFrame(self.live_value_frame_poppable)
        self.tilt_rise_fall_frame.setObjectName(u"tilt_rise_fall_frame")
        self.tilt_rise_fall_frame.setGeometry(QRect(209, 149, 48, 24))
        self.tilt_rise_fall_frame.setLayoutDirection(Qt.LeftToRight)
        self.tilt_rise_fall_frame.setStyleSheet(u" border-radius: 0px; border:0")
        self.tilt_rise_fall_frame.setFrameShape(QFrame.StyledPanel)
        self.tilt_rise_fall_frame.setFrameShadow(QFrame.Raised)
        self.tilt_l = QLabel(self.tilt_rise_fall_frame)
        self.tilt_l.setObjectName(u"tilt_l")
        self.tilt_l.setGeometry(QRect(0, 0, 26, 26))
        self.tilt_l.setStyleSheet(u"")
        self.tilt_l.setPixmap(QPixmap(u"images/value_declining_off.png"))
        self.tilt_r = QLabel(self.tilt_rise_fall_frame)
        self.tilt_r.setObjectName(u"tilt_r")
        self.tilt_r.setGeometry(QRect(24, 1, 24, 24))
        self.tilt_r.setStyleSheet(u"")
        self.tilt_r.setPixmap(QPixmap(u"images/value_rising_off.png"))

        self.verticalLayout.addWidget(self.frame_live_values)

        self.scrollArea_live_values.setWidget(self.scrollAreaWidgetContentsLiveValues)

        self.gridLayout_10.addWidget(self.scrollArea_live_values, 2, 0, 1, 1)

        self.Live_ValuesLabel = QLabel(self.live_value_tab_frame)
        self.Live_ValuesLabel.setObjectName(u"Live_ValuesLabel")
        self.Live_ValuesLabel.setFont(font)
        self.Live_ValuesLabel.setMouseTracking(True)
        self.Live_ValuesLabel.setTabletTracking(True)
        self.Live_ValuesLabel.setStyleSheet(u"QLabel{\n"
"background-color: rgb(88, 88, 98); /* Fallback color */\n"
"border: 2px solid rgb(32, 32, 32);\n"
"border-radius: 10px;\n"
"}\n"
"QToolTip { \n"
" background-color: black; \n"
"color: white; \n"
" border: black solid 1px\n"
" }")
        self.Live_ValuesLabel.setAlignment(Qt.AlignCenter)

        self.gridLayout_10.addWidget(self.Live_ValuesLabel, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.live_value_tab_frame)

        self.splitter_2.addWidget(self.LiveValue_Tab)

        self.gridLayout_5.addWidget(self.splitter_2, 0, 0, 1, 1)


        self.gridLayout_17.addWidget(self.right_frame_frame, 1, 0, 1, 1)

        self.splitter_3.addWidget(self.Right_Frame)

        self.horizontalLayout.addWidget(self.splitter_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1925, 19))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.setEnabled(True)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.deforumation_tabWidget.setCurrentIndex(0)
        self.syrup_pan_curve_type.setCurrentIndex(0)
        self.enablemovements_button.setDefault(False)
        self.tabWidget_CN.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Deforumation QT v 0.1.5", None))
#if QT_CONFIG(tooltip)
        self.SuperTEmp_ParameterLabel.setToolTip(QCoreApplication.translate("MainWindow", u"This window contains the most common key values that influence the image generation.", None))
#endif // QT_CONFIG(tooltip)
        self.SuperTEmp_ParameterLabel.setText(QCoreApplication.translate("MainWindow", u"Seed Parameters", None))
#if QT_CONFIG(tooltip)
        self.iter_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"The seed value will increment by 1 for each subsequent iteration (depends on iter N)", None))
#endif // QT_CONFIG(tooltip)
        self.iter_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Iteration", None))
        self.fixed_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Fixed", None))
#if QT_CONFIG(tooltip)
        self.IterSeed_Inputbox.setToolTip(QCoreApplication.translate("MainWindow", u"Seed value", None))
#endif // QT_CONFIG(tooltip)
        self.IterSeed_Inputbox.setText(QCoreApplication.translate("MainWindow", u"20", None))
#if QT_CONFIG(tooltip)
        self.fixedSeed_Inputbox.setToolTip(QCoreApplication.translate("MainWindow", u"Fixed Seed value that will be used.", None))
#endif // QT_CONFIG(tooltip)
        self.fixedSeed_Inputbox.setText(QCoreApplication.translate("MainWindow", u"20", None))
#if QT_CONFIG(tooltip)
        self.random_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Will create a random seed for each new iteration.", None))
#endif // QT_CONFIG(tooltip)
        self.random_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Random", None))
#if QT_CONFIG(tooltip)
        self.IterSeed_N_Inputbox.setToolTip(QCoreApplication.translate("MainWindow", u"Iter N value, that decides how many iterations will be skipped before seed increase.", None))
#endif // QT_CONFIG(tooltip)
        self.IterSeed_N_Inputbox.setText(QCoreApplication.translate("MainWindow", u"20", None))
#if QT_CONFIG(tooltip)
        self.seed_iter_n.setToolTip(QCoreApplication.translate("MainWindow", u"Iter N value, that decides how many iterations will be skipped before seed increase.", None))
#endif // QT_CONFIG(tooltip)
        self.seed_iter_n.setText(QCoreApplication.translate("MainWindow", u"Seed iter N", None))
#if QT_CONFIG(tooltip)
        self.ladder_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Ladder when starting with seed value 1: 1,3,2,4,3,5,4,6", None))
#endif // QT_CONFIG(tooltip)
        self.ladder_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Ladder", None))
#if QT_CONFIG(tooltip)
        self.alternate_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Alternates up and down one seed value.. e.g 1,2 1,2 1,2 1,2   etc", None))
#endif // QT_CONFIG(tooltip)
        self.alternate_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Alternate", None))
#if QT_CONFIG(tooltip)
        self.update_seed_button.setToolTip(QCoreApplication.translate("MainWindow", u"Send the seed/seed scheme to the renderer. This has to be pushed after having changed the seed value in Iteration or Fixed.\\n\n"
"If you switch to another seed scheme, the value will also automatically be sent and updated.", None))
#endif // QT_CONFIG(tooltip)
        self.update_seed_button.setText(QCoreApplication.translate("MainWindow", u"Update Seed && iter N", None))
#if QT_CONFIG(tooltip)
        self.update_seed_iter_n_button.setToolTip(QCoreApplication.translate("MainWindow", u"Send the new Itern N value to the renderer. This has to be pushed after having changed the iter N value,", None))
#endif // QT_CONFIG(tooltip)
        self.update_seed_iter_n_button.setText(QCoreApplication.translate("MainWindow", u"Update iter N", None))
#if QT_CONFIG(tooltip)
        self.scheduled_RadioButton.setToolTip(QCoreApplication.translate("MainWindow", u"Uses Deforum seed schedule", None))
#endif // QT_CONFIG(tooltip)
        self.scheduled_RadioButton.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
#if QT_CONFIG(tooltip)
        self.Temp_ValuesLabel.setToolTip(QCoreApplication.translate("MainWindow", u"This window shows the values that Deforum is currently working with. These values can be different from the values that Deforumation is currently using.", None))
#endif // QT_CONFIG(tooltip)
        self.Temp_ValuesLabel.setText(QCoreApplication.translate("MainWindow", u"Empty Space", None))
        self.preview_image.setText("")
#if QT_CONFIG(tooltip)
        self.movie_slider_frame_number.setToolTip(QCoreApplication.translate("MainWindow", u"Tells what frame number is currently in the most left film reel. You can jump directly to a frame by typing it in.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.movie_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Film Reel jogging slider.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.open_Deforum_folder.setToolTip(QCoreApplication.translate("MainWindow", u"This magic button will open the current Deforum output folder, usually something like \"...\\outputs\\img2img-images\\Deforum_timestring\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.open_Deforum_folder.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.open_Deforum_folder.setText("")
#if QT_CONFIG(tooltip)
        self.crf_input_box.setToolTip(QCoreApplication.translate("MainWindow", u"CRF in FFmpeg: Control for video quality and size. Lower values mean better quality, higher values mean smaller file sizes.\n"
"Low value and many frames takes time to compile. A good baseline is 17.", None))
#endif // QT_CONFIG(tooltip)
        self.crf_input_box.setText(QCoreApplication.translate("MainWindow", u"20", None))
#if QT_CONFIG(tooltip)
        self.crf_label.setToolTip(QCoreApplication.translate("MainWindow", u"CRF in FFmpeg: Control for video quality and size. Lower values mean better quality, higher values mean smaller file sizes. Low value and many frames takes time to compile. A good baseline is 17.", None))
#endif // QT_CONFIG(tooltip)
        self.crf_label.setText(QCoreApplication.translate("MainWindow", u"CRF:(compression level)", None))
#if QT_CONFIG(tooltip)
        self.goto_end_button.setToolTip(QCoreApplication.translate("MainWindow", u"Go to last / current frame in Film Reel.", None))
#endif // QT_CONFIG(tooltip)
        self.goto_end_button.setText("")
#if QT_CONFIG(tooltip)
        self.play_button.setToolTip(QCoreApplication.translate("MainWindow", u"Resume Deforum Rendering.", None))
#endif // QT_CONFIG(tooltip)
        self.play_button.setText("")
#if QT_CONFIG(tooltip)
        self.stop_button.setToolTip(QCoreApplication.translate("MainWindow", u"Paus Deforum Rendering.", None))
#endif // QT_CONFIG(tooltip)
        self.stop_button.setText("")
#if QT_CONFIG(tooltip)
        self.goto_start_button.setToolTip(QCoreApplication.translate("MainWindow", u"Go to first frame in Film Reel.", None))
#endif // QT_CONFIG(tooltip)
        self.goto_start_button.setText("")
#if QT_CONFIG(tooltip)
        self.loop_button.setToolTip(QCoreApplication.translate("MainWindow", u"This will put the generation in or out of loop-back. Number of generated images in loop-back mode,\n"
"depends on the current Cadence.", None))
#endif // QT_CONFIG(tooltip)
        self.loop_button.setText("")
#if QT_CONFIG(tooltip)
        self.preview_compression_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Film Reel Granularity Slider: Drag left to \"zoom in\", or drag right to \"zoom out\".", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.replay_fps_input_box.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the playback FPS of the preview animation. This works independently of what FPS you choose in deforum's \"Video Output Settings\".", None))
#endif // QT_CONFIG(tooltip)
        self.replay_fps_input_box.setText(QCoreApplication.translate("MainWindow", u"30", None))
#if QT_CONFIG(tooltip)
        self.fps_label.setToolTip(QCoreApplication.translate("MainWindow", u"Enter the playback FPS of the preview animation. This works independently of what FPS you choose in deforum's \"Video Output Settings\".", None))
#endif // QT_CONFIG(tooltip)
        self.fps_label.setText(QCoreApplication.translate("MainWindow", u"     fps:", None))
#if QT_CONFIG(tooltip)
        self.from_framelabel.setToolTip(QCoreApplication.translate("MainWindow", u"Input starting frame of preview animation. You can also right click Film reel and \"Mark FFMPEG preview, IN\" to set this value.", None))
#endif // QT_CONFIG(tooltip)
        self.from_framelabel.setText(QCoreApplication.translate("MainWindow", u"From Frame:", None))
#if QT_CONFIG(tooltip)
        self.play_preview.setToolTip(QCoreApplication.translate("MainWindow", u"Play Prewiev, This play a preview animation of the frames between IN and OUT marking in film reel. Fps is set in \"fps\"", None))
#endif // QT_CONFIG(tooltip)
        self.play_preview.setText(QCoreApplication.translate("MainWindow", u"Play Preview", None))
#if QT_CONFIG(tooltip)
        self.to_frame_label.setToolTip(QCoreApplication.translate("MainWindow", u"Input ending frame of preview animation. You can also right click Film reel and \"Mark FFMPEG preview, OUT\" to set this value.", None))
#endif // QT_CONFIG(tooltip)
        self.to_frame_label.setText(QCoreApplication.translate("MainWindow", u"To Frame:", None))
#if QT_CONFIG(tooltip)
        self.replay_to_input_box.setToolTip(QCoreApplication.translate("MainWindow", u"Input ending frame of preview animation. You can also right click Film reel and \"Mark FFMPEG preview, OUT\" to set this value.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.replay_from_input_box.setToolTip(QCoreApplication.translate("MainWindow", u"Input starting frame of preview animation. You can also right click Film reel and \"Mark FFMPEG preview, IN\" to set this value.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.movie_clip.setToolTip(QCoreApplication.translate("MainWindow", u"Right click for more options.\n"
"\n"
"\"Set current image and Copy it's original values\": select image to start generating from and also use all that image's original values, such as movement and live parameter values.\n"
"\n"
"\"Set current image\": select image to start generate from.\n"
"\n"
"\"Copy this image`s original value to Deforumation\": this will copy movement values and it`s parameters (CFG, Strength, Cadence, Noise Multiplier) to Deforumation.\n"
"\n"
"\"Get this image's prompt\": Copy the image prompt to Deforumation current prompt.\n"
"\n"
"\"Get active prompt\": Copy the active prompt to Deforumation prompt.\n"
"\n"
"\"Mark FFmpeg preview, IN\": Selects the starting frame of the preview animation.\n"
"\n"
"\"Mark FFmpeg preview, OUT\": Selects the last frame of the preview animation.\n"
"\n"
"\"Clear FFmpeg preview\": Clear all selected frames.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_Positive_Prompt1.setToolTip(QCoreApplication.translate("MainWindow", u"This is the first prompt window (Prompt A). It will be combined (put infront) Prompt B.", None))
#endif // QT_CONFIG(tooltip)
        self.label_Positive_Prompt1.setText(QCoreApplication.translate("MainWindow", u"Positive Prompt A", None))
        self.prompt1.setMarkdown("")
        self.prompt1.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.label_Positive_Prompt2.setToolTip(QCoreApplication.translate("MainWindow", u"This is the second prompt window (Prompt B). It will be combined (put behind) Prompt A.", None))
#endif // QT_CONFIG(tooltip)
        self.label_Positive_Prompt2.setText(QCoreApplication.translate("MainWindow", u"Positive Prompt B", None))
#if QT_CONFIG(tooltip)
        self.label_Negative_Prompt.setToolTip(QCoreApplication.translate("MainWindow", u"This is the negative prompt window. Write stuff that you don't want to show up in your AI generation.", None))
#endif // QT_CONFIG(tooltip)
        self.label_Negative_Prompt.setText(QCoreApplication.translate("MainWindow", u"Negativ Prompt", None))
        self.prompt_morphing_label.setText(QCoreApplication.translate("MainWindow", u"Prompt Morphing", None))
#if QT_CONFIG(tooltip)
        self.save_morph_data.setToolTip(QCoreApplication.translate("MainWindow", u"Save all the current Prompt Morphing Bindings to a file.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.save_morph_data.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.save_morph_data.setText("")
        self.save_current_ui_label_4.setText(QCoreApplication.translate("MainWindow", u"Save Prompt Morphing to file", None))
#if QT_CONFIG(tooltip)
        self.use_deforumation_prompt_scheduling_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Prompt from Deforumation will be used to generate frames if checked. If unchecked (grey) prompt schedulinging,\n"
"from deforum will be used to generate frames. You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.use_deforumation_prompt_scheduling_checkbox.setText(QCoreApplication.translate("MainWindow", u"Use Deforumation Prompts", None))
#if QT_CONFIG(tooltip)
        self.save_positive_prompt_style.setToolTip(QCoreApplication.translate("MainWindow", u"Send positive and negative prompt to the renderer. This has to be pushed after having changed a prompt in order for the change to take effect.", None))
#endif // QT_CONFIG(tooltip)
        self.save_positive_prompt_style.setText(QCoreApplication.translate("MainWindow", u"Update Prompt", None))
#if QT_CONFIG(tooltip)
        self.AddPromptMorp_Button.setToolTip(QCoreApplication.translate("MainWindow", u"This will add a new Promp Morph component", None))
#endif // QT_CONFIG(tooltip)
        self.AddPromptMorp_Button.setText(QCoreApplication.translate("MainWindow", u"Add Prompt Morp Binding", None))
        self.syrup_prompt_morph_label.setText(QCoreApplication.translate("MainWindow", u"Prompt Morph Smooth Motion", None))
#if QT_CONFIG(tooltip)
        self.syrup_prompt_morph_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Gives Prompt A or Prompt B more focus. Left of middle will give Prompt A more focus,\n"
"while right of middle will give Prompt B more focus. In the middle, both prompts have\n"
"the same focus. Right click to reset balance.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.syrup_prompt_morph_value.setToolTip(QCoreApplication.translate("MainWindow", u"Current set \"Smoot motion steps\" shows how many frames the smooth motion will use to reach the end value.\n"
"Lower value equals faster smooth motion. Higher value equals slower smooth motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.add_prompt_after_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked (green), Positive prompt will be placed after active prompt from Deforum prompt scedule.", None))
#endif // QT_CONFIG(tooltip)
        self.add_prompt_after_checkbox.setText(QCoreApplication.translate("MainWindow", u"Add prompt after Deforum prompt", None))
#if QT_CONFIG(tooltip)
        self.add_prompt_before_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked (green), Positive prompt will be placed before active prompt from Deforum prompt scedule.", None))
#endif // QT_CONFIG(tooltip)
        self.add_prompt_before_checkbox.setText(QCoreApplication.translate("MainWindow", u"Add prompt before Deforum prompt", None))
#if QT_CONFIG(tooltip)
        self.load_morph_data.setToolTip(QCoreApplication.translate("MainWindow", u"Load Prompt Morphing Bindings from a file.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.load_morph_data.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.load_morph_data.setText("")
        self.save_current_ui_label_5.setText(QCoreApplication.translate("MainWindow", u"Load Prompt Morphing from disc", None))
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.Prompt_Tab), QCoreApplication.translate("MainWindow", u"Prompts", None))
#if QT_CONFIG(tooltip)
        self.motion_pan_button_left.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Pan towards the Left. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_pan_button_left.setText("")
#if QT_CONFIG(tooltip)
        self.motion_pan_button_down.setToolTip(QCoreApplication.translate("MainWindow", u"Increase downwards Panning. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_pan_button_down.setText("")
#if QT_CONFIG(tooltip)
        self.motion_pan_button_up.setToolTip(QCoreApplication.translate("MainWindow", u"Increase uppwards Panning. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_pan_button_up.setText("")
#if QT_CONFIG(tooltip)
        self.motion_pan_button_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Pan towards the Right. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_pan_button_right.setText("")
#if QT_CONFIG(tooltip)
        self.motion_pan_granularity.setToolTip(QCoreApplication.translate("MainWindow", u"Decides how big each step should be when clicking a motion button. Decimal numbers can be used.", None))
#endif // QT_CONFIG(tooltip)
        self.panning_preset_label.setText(QCoreApplication.translate("MainWindow", u"Panning preset", None))
#if QT_CONFIG(tooltip)
        self.syrup_pan_motion_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slider to set the smoothness of the motion. A lower value means that the motion value that you choose (X or Y panning), will be reached faster.\n"
"A smoothness of 0, will instantly jump to the motion panning value that you chose.A higer value will gradually work towards your choosen motion panning value.", None))
#endif // QT_CONFIG(tooltip)
        self.smooth_motion_steps_pan_label.setText(QCoreApplication.translate("MainWindow", u"Smooth pan steps:", None))
#if QT_CONFIG(tooltip)
        self.syrup_pan_motion_slider_frame_number.setToolTip(QCoreApplication.translate("MainWindow", u"Current set \"Smoot motion steps\" shows how many frames the smooth motion will use to reach the end value.\n"
"Lower value equals faster smooth motion. Higher value equals slower smooth motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pan_x_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_x_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.pan_y_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_y_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_x.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps panning X (Left, Right)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_y.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps panning Y (Upp, Down)", None))
#endif // QT_CONFIG(tooltip)
        self.syrup_x_label.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.syrup_y_label.setText(QCoreApplication.translate("MainWindow", u"Y", None))
#if QT_CONFIG(tooltip)
        self.exponential_pan_motion.setToolTip(QCoreApplication.translate("MainWindow", u"If enabled, any panning value set with the motion buttons, will be the goal values to reach using the (\"Smooth pan steps\") value.\n"
" When disabled, a motion using the same smoothness value and granularity preset (Panning preset), will be kept constant.\n"
"This means that any further motion changes (you pushing a motion button while a motion is already ongoing), will b\n"
" regulated to follow the already ongoing motion curve.", None))
#endif // QT_CONFIG(tooltip)
        self.exponential_pan_motion.setText(QCoreApplication.translate("MainWindow", u"Exponential Panning Motion", None))
#if QT_CONFIG(tooltip)
        self.pan_x_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_x_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.pan_y_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_y_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.Motion_Panning_Label.setText(QCoreApplication.translate("MainWindow", u"MOTION - PANNING", None))
        self.syrup_pan_curve_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.syrup_pan_curve_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Ease", None))
        self.syrup_pan_curve_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Ease-In", None))
        self.syrup_pan_curve_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Ease-Out", None))
        self.syrup_pan_curve_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Ease-In-Out", None))

#if QT_CONFIG(tooltip)
        self.syrup_pan_curve_type.setToolTip(QCoreApplication.translate("MainWindow", u"What \"Smooth motion curve\" to use with \"Smooth motion steps\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pan_middle_button.setToolTip(QCoreApplication.translate("MainWindow", u"Zero all Panning motions.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_middle_button.setText("")
#if QT_CONFIG(tooltip)
        self.Panning_Component.setToolTip(QCoreApplication.translate("MainWindow", u"The motion controller for changing panning motions.", None))
#endif // QT_CONFIG(tooltip)
        self.Panning_Component.setText("")
        self.smooth_motion_curve_pan_label.setText(QCoreApplication.translate("MainWindow", u"Smooth motion curve", None))
#if QT_CONFIG(tooltip)
        self.Motion_panning_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable or disable live panning control. If disabled, the values given in the scheduled Deforum motion will take over.\n"
"You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Motion_panning_checkbox.setStatusTip(QCoreApplication.translate("MainWindow", u"Enable or disable live panning control.", None))
#endif // QT_CONFIG(statustip)
        self.Motion_panning_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.motion_rotate_button_left.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Rotation towards the Left. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_rotate_button_left.setText("")
#if QT_CONFIG(tooltip)
        self.motion_rotate_button_down.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Rotation Downwards. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_rotate_button_down.setText("")
#if QT_CONFIG(tooltip)
        self.motion_rotate_button_up.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Rotation Upwards. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_rotate_button_up.setText("")
#if QT_CONFIG(tooltip)
        self.motion_rotate_button_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Rotation towards the Right. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_rotate_button_right.setText("")
#if QT_CONFIG(tooltip)
        self.motion_rotate_granularity.setToolTip(QCoreApplication.translate("MainWindow", u"Decides how big each step should be when clicking a motion button. Decimal numbers can be used.", None))
#endif // QT_CONFIG(tooltip)
        self.rot_preset_label.setText(QCoreApplication.translate("MainWindow", u"Rotation preset", None))
#if QT_CONFIG(tooltip)
        self.syrup_rotate_motion_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slider to set the smoothness of the motion. A lower value means that the motion value that\n"
"you choose (Rotate Horizontally or Rotate Vertically), will be reached faster.\n"
"A smoothness of 0, will instantly jump to the motion rotation value that you chose.\n"
"A higer value will gradually work towards your choosen motion rotation value.", None))
#endif // QT_CONFIG(tooltip)
        self.smooth_motion_curve_rot_label.setText(QCoreApplication.translate("MainWindow", u"Smooth motion curve", None))
#if QT_CONFIG(tooltip)
        self.syrup_rotate_motion_slider_frame_number.setToolTip(QCoreApplication.translate("MainWindow", u"Current set \"Smoot motion steps\" shows how many frames the smooth motion will use to reach the end value.\n"
"Lower value equals faster smooth motion. Higher value equals slower smooth motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rotate_x_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_x_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.rotate_y_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_y_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_rx.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps rotation vertically (Up, Down)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_ry.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps rotation vertically (Left, Right)", None))
#endif // QT_CONFIG(tooltip)
        self.syrup_xr_label.setText(QCoreApplication.translate("MainWindow", u"RV", None))
        self.syrup_ry_label.setText(QCoreApplication.translate("MainWindow", u"RH", None))
#if QT_CONFIG(tooltip)
        self.exponential_rotate_motion.setToolTip(QCoreApplication.translate("MainWindow", u"If enabled, any rotation value set with the motion buttons, will be the goal values to reach using the (\"Smooth rotation steps\") value.\n"
"When disabled, a motion using the same smoothness value and granularity preset (Rotation preset), will be kept constant.\n"
"This means that any further motion changes (you pushing a motion button while a motion is already ongoing), will be\n"
"regulated to follow the already ongoing motion curve.", None))
#endif // QT_CONFIG(tooltip)
        self.exponential_rotate_motion.setText(QCoreApplication.translate("MainWindow", u"Exponential Rotation Motion", None))
#if QT_CONFIG(tooltip)
        self.rotate_x_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_x_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.rotate_y_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_y_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.Motion_Rotation_Label.setText(QCoreApplication.translate("MainWindow", u"MOTION - ROTATION", None))
        self.syrup_rotation_curve_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.syrup_rotation_curve_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Ease", None))
        self.syrup_rotation_curve_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Ease-In", None))
        self.syrup_rotation_curve_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Ease-Out", None))
        self.syrup_rotation_curve_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Ease-In-Out", None))

#if QT_CONFIG(tooltip)
        self.syrup_rotation_curve_type.setToolTip(QCoreApplication.translate("MainWindow", u"What \"Smooth motion curve\" to use with \"Smooth motion steps\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rotate_middle_button.setToolTip(QCoreApplication.translate("MainWindow", u"Zero all Rotation motions.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_middle_button.setText("")
        self.smooth_motion_steps_rotation_label.setText(QCoreApplication.translate("MainWindow", u"Smooth rotation steps:", None))
#if QT_CONFIG(tooltip)
        self.Rotation_Component.setToolTip(QCoreApplication.translate("MainWindow", u"The motion controller for changing rotational motions.", None))
#endif // QT_CONFIG(tooltip)
        self.Rotation_Component.setText("")
#if QT_CONFIG(tooltip)
        self.Motion_rotation_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable or disable live rotation control. If disabled, the values given in the scheduled Deforum motion will take over.\n"
"You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.Motion_rotation_checkbox.setStatusTip(QCoreApplication.translate("MainWindow", u"Enable or disable live panning control.", None))
#endif // QT_CONFIG(statustip)
        self.Motion_rotation_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.motion_tilt_granularity.setToolTip(QCoreApplication.translate("MainWindow", u"Decides how big each step should be when clicking a motion button. Decimal numbers can be used.", None))
#endif // QT_CONFIG(tooltip)
        self.tilt_preset_label.setText(QCoreApplication.translate("MainWindow", u"Tilt preset", None))
#if QT_CONFIG(tooltip)
        self.syrup_tilt_motion_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slider to set the smoothness of a motion. A lower value means that the motion value that you choose (Tilt), will be reached faster.\n"
"A smoothness of 0, will instantly jump to the motion tilt value that you chose.\n"
"A higer value will gradually work towards your choosen motion tilt value.", None))
#endif // QT_CONFIG(tooltip)
        self.smooth_motion_steps_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Smooth tilt steps:", None))
#if QT_CONFIG(tooltip)
        self.syrup_tilt_motion_slider_frame_number.setToolTip(QCoreApplication.translate("MainWindow", u"Current set \"Smoot motion steps\" shows how many frames the smooth motion will use to reach the end value.\n"
"Lower value equals faster smooth motion. Higher value equals slower smooth motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rotate_z_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_z_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_rz.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps tilt (Clockwise or Counterclockwise)", None))
#endif // QT_CONFIG(tooltip)
        self.syrup_z_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Z", None))
#if QT_CONFIG(tooltip)
        self.exponential_tilt_motion.setToolTip(QCoreApplication.translate("MainWindow", u"If enabled, any tilt value set with the motion buttons, will be the goal values to reach using the (\"Smooth tilt steps\") value.\n"
"When disabled, a motion using the same smoothness value and granularity preset (Tilt preset), will be kept constant.\n"
"This means that any further motion changes (you pushing a motion button while a motion is already ongoing),\n"
"will be regulated to follow the already ongoing motion curve.", None))
#endif // QT_CONFIG(tooltip)
        self.exponential_tilt_motion.setText(QCoreApplication.translate("MainWindow", u"Exponential Tilt Motion", None))
#if QT_CONFIG(tooltip)
        self.rotate_z_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_z_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
        self.Motion_Tilt_Label.setText(QCoreApplication.translate("MainWindow", u"MOTION - TILT", None))
        self.syrup_tilt_curve_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.syrup_tilt_curve_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Ease", None))
        self.syrup_tilt_curve_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Ease-In", None))
        self.syrup_tilt_curve_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Ease-Out", None))
        self.syrup_tilt_curve_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Ease-In-Out", None))

#if QT_CONFIG(tooltip)
        self.syrup_tilt_curve_type.setToolTip(QCoreApplication.translate("MainWindow", u"What \"Smooth motion curve\" to use with \"Smooth motion steps\"", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.Motion_tilt_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable or disable live tilt control. If disabled, the values given in the scheduled Deforum motion will take over.\n"
"You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.Motion_tilt_checkbox.setText("")
        self.smooth_motion_curve_tilt_label.setText(QCoreApplication.translate("MainWindow", u"Smooth tilt curve", None))
#if QT_CONFIG(tooltip)
        self.Tilt_Component.setToolTip(QCoreApplication.translate("MainWindow", u"The motion controller for changing tilt motion.", None))
#endif // QT_CONFIG(tooltip)
        self.Tilt_Component.setText("")
#if QT_CONFIG(tooltip)
        self.motion_tilt_button_left.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Clockwise Tilt motion. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_tilt_button_left.setText("")
#if QT_CONFIG(tooltip)
        self.motion_tilt_button_right.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Counterclockwise Tilt motion. Right-clicking will reset motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_tilt_button_right.setText("")
#if QT_CONFIG(tooltip)
        self.tilt_middle_button.setToolTip(QCoreApplication.translate("MainWindow", u"Zero all Tilt motions.", None))
#endif // QT_CONFIG(tooltip)
        self.tilt_middle_button.setText("")
#if QT_CONFIG(tooltip)
        self.motion_fov_slider.setToolTip(QCoreApplication.translate("MainWindow", u"The motion controller for changing FOV (field of view). Right-clicking will reset motion back to  the normal value (70).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.max_fov.setToolTip(QCoreApplication.translate("MainWindow", u"Maximum FOV value.", None))
#endif // QT_CONFIG(tooltip)
        self.max_fov.setText(QCoreApplication.translate("MainWindow", u"120", None))
#if QT_CONFIG(tooltip)
        self.min_fov.setToolTip(QCoreApplication.translate("MainWindow", u"Minimum FOV value.", None))
#endif // QT_CONFIG(tooltip)
        self.min_fov.setText(QCoreApplication.translate("MainWindow", u"20", None))
        self.Motion_Fov.setText(QCoreApplication.translate("MainWindow", u"MOTION - FOV", None))
#if QT_CONFIG(tooltip)
        self.fov_value.setToolTip(QCoreApplication.translate("MainWindow", u"Normal FOV value.", None))
#endif // QT_CONFIG(tooltip)
        self.fov_value.setText(QCoreApplication.translate("MainWindow", u"70", None))
#if QT_CONFIG(tooltip)
        self.Motion_fow_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable or disable live Fov control. If disabled, the values given in the scheduled Deforum motion will take over.\n"
"You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.Motion_fow_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.motion_zoom_slider.setToolTip(QCoreApplication.translate("MainWindow", u"The motion controller for changing zoom motion. Right-clicking on the controller will reset the motion back to 0.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.motion_zoom_granularity.setToolTip(QCoreApplication.translate("MainWindow", u"Decides the min and max value of the Zoom slider.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.max_zoom.setToolTip(QCoreApplication.translate("MainWindow", u"Maximum zoom value.", None))
#endif // QT_CONFIG(tooltip)
        self.max_zoom.setText(QCoreApplication.translate("MainWindow", u"1.00", None))
#if QT_CONFIG(tooltip)
        self.min_zoom.setToolTip(QCoreApplication.translate("MainWindow", u"Minimum zoom value.", None))
#endif // QT_CONFIG(tooltip)
        self.min_zoom.setText(QCoreApplication.translate("MainWindow", u"-1.00", None))
        self.Motion_Zoom_Label.setText(QCoreApplication.translate("MainWindow", u"MOTION - ZOOM", None))
#if QT_CONFIG(tooltip)
        self.syrup_zoom_motion_slider_frame_number.setToolTip(QCoreApplication.translate("MainWindow", u"Current set \"Smoot motion steps\" shows how many frames the smooth motion will use to reach the end value.\n"
"Lower value equals faster smooth motion. Higher value equals slower smooth motion.", None))
#endif // QT_CONFIG(tooltip)
        self.smooth_motion_curve_zoom_label.setText(QCoreApplication.translate("MainWindow", u"Smooth zoom curve", None))
#if QT_CONFIG(tooltip)
        self.syrup_zoom_motion_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Slider to set the smoothness \"of a motion\". A lower value means that the motion value that you choose (Zoom),\n"
"will be reached faster. A smoothness of 0, will instantly jump to the motion zoom value that you chose.\n"
"A higer value will gradually work towards your choosen motion zoom value.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pan_z_value.setToolTip(QCoreApplication.translate("MainWindow", u"Value to strive towards.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_z_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.pan_z_value_progress.setToolTip(QCoreApplication.translate("MainWindow", u"Current value being used. This value might differ from the goal value.", None))
#endif // QT_CONFIG(tooltip)
        self.pan_z_value_progress.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.motion_syrup_progressbar_z.setToolTip(QCoreApplication.translate("MainWindow", u"Current completion level of set smoot motion steps zoom (Forwards or Backwards)", None))
#endif // QT_CONFIG(tooltip)
        self.syrup_zoom_label.setText(QCoreApplication.translate("MainWindow", u"Z", None))
        self.syrup_zoom_curve_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Linear", None))
        self.syrup_zoom_curve_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Ease", None))
        self.syrup_zoom_curve_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Ease-In", None))
        self.syrup_zoom_curve_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Ease-Out", None))
        self.syrup_zoom_curve_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Ease-In-Out", None))

#if QT_CONFIG(tooltip)
        self.syrup_zoom_curve_type.setToolTip(QCoreApplication.translate("MainWindow", u"What \"Smooth motion curve\" to use with \"Smooth motion steps\"", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_preset_label.setText(QCoreApplication.translate("MainWindow", u"Zoom preset", None))
#if QT_CONFIG(tooltip)
        self.Motion_zoom_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"Enable or disable live zoom control. If disabled, the values given in the scheduled Deforum motion will take over.\n"
"You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.Motion_zoom_checkbox.setText("")
        self.smooth_motion_steps_zoom_label.setText(QCoreApplication.translate("MainWindow", u"Smooth zoom steps:", None))
#if QT_CONFIG(tooltip)
        self.motion_zoom_granularity_special.setToolTip(QCoreApplication.translate("MainWindow", u"Decides how big each step should be when clicking a motion button. Decimal numbers can be used.", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_preset_special_label.setText(QCoreApplication.translate("MainWindow", u"C - Zoom preset", None))
#if QT_CONFIG(tooltip)
        self.motion_zoom_button_forwards.setToolTip(QCoreApplication.translate("MainWindow", u"Increase Zoom value as much as the C - Zoom preset is set to.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_zoom_button_forwards.setText("")
#if QT_CONFIG(tooltip)
        self.motion_zoom_button_backwards.setToolTip(QCoreApplication.translate("MainWindow", u"Decrease Zoom value as much as the C - Zoom preset is set to.", None))
#endif // QT_CONFIG(tooltip)
        self.motion_zoom_button_backwards.setText("")
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.Movement_Tab), QCoreApplication.translate("MainWindow", u"Motion", None))
        self.user_interface_settings_label.setText(QCoreApplication.translate("MainWindow", u"User Interface Settings", None))
        self.Save_Settings.setText(QCoreApplication.translate("MainWindow", u"Save Current UI Settings", None))
        self.Restore_Settings.setText(QCoreApplication.translate("MainWindow", u"Restore UI Settings", None))
        self.enablemovements_button.setText(QCoreApplication.translate("MainWindow", u"Enter UI edit mode", None))
        self.dissablemovements_button.setText(QCoreApplication.translate("MainWindow", u"Exit UI edit mode", None))
        self.save_current_ui_label.setText(QCoreApplication.translate("MainWindow", u"Saves the current Ui Window layout", None))
        self.restore_current_ui_label.setText(QCoreApplication.translate("MainWindow", u"Restores to the current Saved Ui Window layout", None))
        self.user_interface_cust_label.setText(QCoreApplication.translate("MainWindow", u"User interface customization", None))
        self.enable_movement_label.setText(QCoreApplication.translate("MainWindow", u"Enables you to edit the Deforumation UI", None))
        self.dissable_movement_label.setText(QCoreApplication.translate("MainWindow", u"Exits Deforumation UI editing mode", None))
        self.revert_ui_to_original_label.setText(QCoreApplication.translate("MainWindow", u"Reverts to the original Ui layout", None))
        self.revert_UI_to_original.setText(QCoreApplication.translate("MainWindow", u"Revert UI to Original", None))
        self.save_current_ui_label_2.setText(QCoreApplication.translate("MainWindow", u"Saves the current Ui Window layout to a file of your choosing", None))
        self.Save_Settings_To_File.setText(QCoreApplication.translate("MainWindow", u"Save UI Settings To File", None))
        self.save_current_ui_label_3.setText(QCoreApplication.translate("MainWindow", u"Loades a Ui Window layout from a file. This will also set the default layout.", None))
        self.Load_Settings_From_File.setText(QCoreApplication.translate("MainWindow", u"Load UI Settings From File", None))
        self.Create_Language_Config.setText(QCoreApplication.translate("MainWindow", u"Create Language Config", None))
        self.Load_Language_Config.setText(QCoreApplication.translate("MainWindow", u"Load Language Config", None))
        self.language_setting_label.setText(QCoreApplication.translate("MainWindow", u"Language Settings", None))
        self.Restore_To_Language.setText(QCoreApplication.translate("MainWindow", u"Revert Back to English", None))
        self.ffmpeg_howto_more_label.setText(QCoreApplication.translate("MainWindow", u"Set the path to audio file; FFmpeg will use the audio file when\n"
"prewiving the animation", None))
        self.ffmpeg_title_label.setText(QCoreApplication.translate("MainWindow", u"FFmpeg settings", None))
        self.ffmpeg_how_to_label.setText(QCoreApplication.translate("MainWindow", u"Set the path to FFmpeg; not necessary if it is included\n"
" in Windows environments.", None))
        self.pathToFFMPEG_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<Path to ffmpeg executable>", None))
        self.pathffmpeg_label.setText(QCoreApplication.translate("MainWindow", u"Path to FFMPEG :", None))
        self.pathaudiofile_label.setText(QCoreApplication.translate("MainWindow", u"Path to Audio     :", None))
        self.pathToAudioFile_value.setPlaceholderText(QCoreApplication.translate("MainWindow", u"<Path to audio file>", None))
        self.browse_audio_file.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.browse_ffmpeg_file.setText(QCoreApplication.translate("MainWindow", u"Browse", None))
        self.joystick_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"<Choose Controller>", None))

#if QT_CONFIG(tooltip)
        self.joystick_combo_box.setToolTip(QCoreApplication.translate("MainWindow", u"If Deforumation can find any controlers, they will be visible in this menu.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_panning_left_label.setText(QCoreApplication.translate("MainWindow", u"Panning Left", None))
        self.joystick_panning_right_label.setText(QCoreApplication.translate("MainWindow", u"Panning Right", None))
        self.joystick_panning_up_label.setText(QCoreApplication.translate("MainWindow", u"Panning Up", None))
        self.joystick_panning_down_label.setText(QCoreApplication.translate("MainWindow", u"Panning Down", None))
        self.joystick_rotate_h_left_label.setText(QCoreApplication.translate("MainWindow", u"Rotate H Left", None))
        self.joystick_rotate_h_right_label.setText(QCoreApplication.translate("MainWindow", u"Rotate H Right", None))
        self.joystick_rotate_v_up_label.setText(QCoreApplication.translate("MainWindow", u"Rotate V Up", None))
        self.joystick_rotate_v_down_label.setText(QCoreApplication.translate("MainWindow", u"Rotate V Down", None))
        self.joystick_zoom_forwards_label.setText(QCoreApplication.translate("MainWindow", u"Zoom Forwards", None))
        self.joystick_zoom_backwards_label.setText(QCoreApplication.translate("MainWindow", u"Zoom Backwards", None))
        self.joystick_tilt_cw_label.setText(QCoreApplication.translate("MainWindow", u"Tilt Clockwise", None))
        self.joystick_tilt_cc_label.setText(QCoreApplication.translate("MainWindow", u"Tilt Counter-Clockwise", None))
#if QT_CONFIG(tooltip)
        self.joystick_panning_left_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_panning_left_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_panning_right_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_panning_right_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_panning_up_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_panning_up_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_panning_down_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_panning_down_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_rotate_h_left_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_rotate_h_left_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_rotate_h_right_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_rotate_h_right_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_rotate_v_up_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_rotate_v_up_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_rotate_v_down_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_rotate_v_down_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_zoom_forwards_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_zoom_forwards_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_zoom_backwards_binding_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_zoom_backwards_binding_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_tilt_cw_bind_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_tilt_cw_bind_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
#if QT_CONFIG(tooltip)
        self.joystick_tilt_cc_bind_button.setToolTip(QCoreApplication.translate("MainWindow", u"After clicking the button, push a button or use a joystick on your controller to bind it to the specific motion. Pushing Escape will undo a binding. Pushing Delete or Backspace will un-bind.", None))
#endif // QT_CONFIG(tooltip)
        self.joystick_tilt_cc_bind_button.setText(QCoreApplication.translate("MainWindow", u"<Unbound>", None))
        self.motion_control_params_label.setText(QCoreApplication.translate("MainWindow", u"Motion / Parameter", None))
        self.motion_control_bindings_label.setText(QCoreApplication.translate("MainWindow", u"Controler - Bindings", None))
        self.controller_setting_label.setText(QCoreApplication.translate("MainWindow", u"Controller Settings", None))
        self.controller_how_to.setText(QCoreApplication.translate("MainWindow", u"If a controller has been detected, it can be choosen in the drop down box below; After you have chosen a controller, you can push the button next to a Motion Parameter to create a binding.", None))
        self.refresh_controller_list.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
#if QT_CONFIG(tooltip)
        self.frame.setToolTip(QCoreApplication.translate("MainWindow", u"In Game Mode, all motions will always return to 0. In this mode, the Preset-box for each motion decides\n"
"the maximum and minimum value that can be reached from 0 (Smooth steps are ignored).\n"
"In Work Mode, the controller will work the same way as would you manually click a button. This includes\n"
"Smooth steps and each step will follow the granularity preset.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.mode_work_label.setToolTip(QCoreApplication.translate("MainWindow", u"In Game Mode, all motions will always return to 0. In this mode, the Preset-box for each motion decides\n"
"the maximum and minimum value that can be reached from 0 (Smooth steps are ignored).\n"
"In Work Mode, the controller will work the same way as would you manually click a button. This includes\n"
"Smooth steps and each step will follow the granularity preset.", None))
#endif // QT_CONFIG(tooltip)
        self.mode_work_label.setText(QCoreApplication.translate("MainWindow", u"Work Mode", None))
#if QT_CONFIG(tooltip)
        self.controller_mode_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"In Game Mode, all motions will always return to 0. In this mode, the Preset-box for each motion decides\n"
"the maximum and minimum value that can be reached from 0 (Smooth steps are ignored).\n"
"In Work Mode, the controller will work the same way as would you manually click a button. This includes\n"
"Smooth steps and each step will follow the granularity preset.", None))
#endif // QT_CONFIG(tooltip)
        self.controller_mode_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.mode_game_label.setToolTip(QCoreApplication.translate("MainWindow", u"In Game Mode, all motions will always return to 0. In this mode, the Preset-box for each motion decides\n"
"the maximum and minimum value that can be reached from 0 (Smooth steps are ignored).\n"
"In Work Mode, the controller will work the same way as would you manually click a button. This includes\n"
"Smooth steps and each step will follow the granularity preset.", None))
#endif // QT_CONFIG(tooltip)
        self.mode_game_label.setText(QCoreApplication.translate("MainWindow", u"GAME Mode", None))
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.Settings_Tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_cnet15.setText(QCoreApplication.translate("MainWindow", u"CNet 1 Weight", None))
        self.CN_1_weight_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet14.setText(QCoreApplication.translate("MainWindow", u"CNet 1 Starting Control Step", None))
        self.CN_1_starting_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cnet11.setText(QCoreApplication.translate("MainWindow", u"CNet 1 Ending Control Step", None))
        self.CN_1_ending_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet13.setText(QCoreApplication.translate("MainWindow", u"CNet 1 Low Threshold", None))
        self.CN_1_low_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.label_cnet12.setText(QCoreApplication.translate("MainWindow", u"CNet 1 High Threshold", None))
        self.CN_1_high_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.tabWidget_CN.setTabText(self.tabWidget_CN.indexOf(self.tab_CN01), QCoreApplication.translate("MainWindow", u"CN 1", None))
        self.label_cnet22.setText(QCoreApplication.translate("MainWindow", u"CNet 2 High Threshold", None))
        self.CN_2_high_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_cnet25.setText(QCoreApplication.translate("MainWindow", u"CNet 2 Weight", None))
        self.CN_2_weight_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet21.setText(QCoreApplication.translate("MainWindow", u"CNet 2 Ending Control Step", None))
        self.CN_2_ending_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet24.setText(QCoreApplication.translate("MainWindow", u"CNet 2 Starting Control Step", None))
        self.CN_2_starting_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cnet23.setText(QCoreApplication.translate("MainWindow", u"CNet 2 Low Threshold", None))
        self.CN_2_low_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.tabWidget_CN.setTabText(self.tabWidget_CN.indexOf(self.tab_CN02), QCoreApplication.translate("MainWindow", u"CN 2", None))
        self.label_cnet32.setText(QCoreApplication.translate("MainWindow", u"CNet 3 High Threshold", None))
        self.CN_3_high_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_cnet35.setText(QCoreApplication.translate("MainWindow", u"CNet 3 Weight", None))
        self.CN_3_weight_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet31.setText(QCoreApplication.translate("MainWindow", u"CNet 3 Ending Control Step", None))
        self.CN_3_ending_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet34.setText(QCoreApplication.translate("MainWindow", u"CNet 3 Starting Control Step", None))
        self.CN_3_starting_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cnet33.setText(QCoreApplication.translate("MainWindow", u"CNet 3 Low Threshold", None))
        self.CN_3_low_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.tabWidget_CN.setTabText(self.tabWidget_CN.indexOf(self.tab_CN03), QCoreApplication.translate("MainWindow", u"CN 3", None))
        self.label_cnet42.setText(QCoreApplication.translate("MainWindow", u"CNet 4 High Threshold", None))
        self.CN_4_high_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"CNet 4 Weight", None))
        self.CN_4_weight_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet41.setText(QCoreApplication.translate("MainWindow", u"CNet 4 Ending Control Step", None))
        self.CN_4_ending_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet44.setText(QCoreApplication.translate("MainWindow", u"CNet 4 Starting Control Step", None))
        self.CN_4_starting_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cnet43.setText(QCoreApplication.translate("MainWindow", u"CNet 4 Low Threshold", None))
        self.CN_4_low_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.tabWidget_CN.setTabText(self.tabWidget_CN.indexOf(self.tab_CN04), QCoreApplication.translate("MainWindow", u"CN 4", None))
        self.label_cnet52.setText(QCoreApplication.translate("MainWindow", u"CNet 5 High Threshold", None))
        self.CN_5_high_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"200", None))
        self.label_cnet55.setText(QCoreApplication.translate("MainWindow", u"CNet 5 Weight", None))
        self.CN_5_weight_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet51.setText(QCoreApplication.translate("MainWindow", u"CNet 5 Ending Control Step", None))
        self.CN_5_ending_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.0", None))
        self.label_cnet54.setText(QCoreApplication.translate("MainWindow", u"CNet 5 Starting Control Step", None))
        self.CN_5_starting_control_step_slider_value.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_cnet53.setText(QCoreApplication.translate("MainWindow", u"CNet 5 Low Threshold", None))
        self.CN_5_low_threshold_slider_value.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.tabWidget_CN.setTabText(self.tabWidget_CN.indexOf(self.tab_CN05), QCoreApplication.translate("MainWindow", u"CN 5", None))
        self.cn_udcn3.setText("")
        self.cn_udcn4.setText("")
        self.label_cnet2_switch.setText(QCoreApplication.translate("MainWindow", u"CN 2 ON / OFF", None))
        self.label_cnet4_switch.setText(QCoreApplication.translate("MainWindow", u"CN 4 ON / OFF", None))
        self.label_cnet3_switch.setText(QCoreApplication.translate("MainWindow", u"CN 3 ON / OFF", None))
        self.label_cnet1_switch.setText(QCoreApplication.translate("MainWindow", u"CN 1 ON / OFF", None))
        self.label_cnet5_switch.setText(QCoreApplication.translate("MainWindow", u"CN 5 ON / OFF", None))
        self.cn_udcn5.setText("")
        self.cn_udcn2.setText("")
        self.cn_udcn1.setText("")
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.ControlNet_tab), QCoreApplication.translate("MainWindow", u"ControlNet", None))
#if QT_CONFIG(tooltip)
        self.morph_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Gives Prompt A or Prompt B more focus. Left of middle will give Prompt A more focus,\n"
"while right of middle will give Prompt B more focus. In the middle, both prompts have\n"
"the same focus. Right click to reset balance.", None))
#endif // QT_CONFIG(tooltip)
        self.morphing_text_howto_label.setText(QCoreApplication.translate("MainWindow", u"Right click the slider to equal the weight", None))
        self.prpmta_to_promptb_label.setText(QCoreApplication.translate("MainWindow", u"Prompt A - Prompt B", None))
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.Misc_Tab_A), QCoreApplication.translate("MainWindow", u"MiscA", None))
        self.deforumation_tabWidget.setTabText(self.deforumation_tabWidget.indexOf(self.Misc_Tab_B), QCoreApplication.translate("MainWindow", u"MiscB", None))
#if QT_CONFIG(tooltip)
        self.stay_on_top_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"When activated, all Deforumation windows will stay on top of other windows.", None))
#endif // QT_CONFIG(tooltip)
        self.stay_on_top_checkbox.setText(QCoreApplication.translate("MainWindow", u"Deforumation Stay On Top", None))
#if QT_CONFIG(tooltip)
        self.Live_ParameterLabel.setToolTip(QCoreApplication.translate("MainWindow", u"This window contains the most common key values that influence the image generation.", None))
#endif // QT_CONFIG(tooltip)
        self.Live_ParameterLabel.setText(QCoreApplication.translate("MainWindow", u"Live Parameters", None))
#if QT_CONFIG(tooltip)
        self.strength_slider_label.setToolTip(QCoreApplication.translate("MainWindow", u"Strength set amount of presence of previous frame to influence next frame.", None))
#endif // QT_CONFIG(tooltip)
        self.strength_slider_label.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
#if QT_CONFIG(tooltip)
        self.strength_slider_value.setToolTip(QCoreApplication.translate("MainWindow", u"Strength set amount of presence of previous frame to influence next frame.", None))
#endif // QT_CONFIG(tooltip)
        self.strength_slider_value.setText(QCoreApplication.translate("MainWindow", u"0.68", None))
#if QT_CONFIG(tooltip)
        self.strength_active_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, this value will be used, else the Deforum value will be used. You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.strength_active_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.step_slider_label.setToolTip(QCoreApplication.translate("MainWindow", u"How many times to improve the generated image iteratively; higher values take longer; very low values can produce bad results.", None))
#endif // QT_CONFIG(tooltip)
        self.step_slider_label.setText(QCoreApplication.translate("MainWindow", u"Sampler Steps", None))
#if QT_CONFIG(tooltip)
        self.step_slider_value.setToolTip(QCoreApplication.translate("MainWindow", u"How many times to improve the generated image iteratively; higher values take longer; very low values can produce bad results.", None))
#endif // QT_CONFIG(tooltip)
        self.step_slider_value.setText(QCoreApplication.translate("MainWindow", u"50", None))
#if QT_CONFIG(tooltip)
        self.noise_slider_label.setToolTip(QCoreApplication.translate("MainWindow", u"The noise multiplier parameter increases the amount of noise resulting in more detailed images. Default value is 1.05 lower removed details and higher gives more details. Small changes is recomended.", None))
#endif // QT_CONFIG(tooltip)
        self.noise_slider_label.setText(QCoreApplication.translate("MainWindow", u"Noise Multi", None))
#if QT_CONFIG(tooltip)
        self.noise_slider_value.setToolTip(QCoreApplication.translate("MainWindow", u"The noise multiplier parameter increases the amount of noise resulting in more detailed images. Default value is 1.05 lower removed details and higher gives more details. Small changes is recomended.", None))
#endif // QT_CONFIG(tooltip)
        self.noise_slider_value.setText(QCoreApplication.translate("MainWindow", u"1.05", None))
#if QT_CONFIG(tooltip)
        self.noise_multiplier_active_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, this value will be used, else the Deforum value will be used. You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.noise_multiplier_active_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.cfg_slider_label.setToolTip(QCoreApplication.translate("MainWindow", u"How closely the image should conform to the prompt. Lower values produce more creative results. (recommended range 5-15)", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_slider_label.setText(QCoreApplication.translate("MainWindow", u"CFG scale", None))
#if QT_CONFIG(tooltip)
        self.cfg_slider_value.setToolTip(QCoreApplication.translate("MainWindow", u"How closely the image should conform to the prompt. Lower values produce more creative results. (recommended range 5-15)", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_slider_value.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.cfg_active_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, this value will be used, else the Deforum value will be used. You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_active_checkbox.setText("")
#if QT_CONFIG(tooltip)
        self.cadence_slider_label.setToolTip(QCoreApplication.translate("MainWindow", u"Cadence value set how many in-between frames that will not be directly diffused. Low value produces more flickering and longer render time. Higher value produces less flickering and shorter render time. Diffrent settings for diffrent results.", None))
#endif // QT_CONFIG(tooltip)
        self.cadence_slider_label.setText(QCoreApplication.translate("MainWindow", u"Cadence", None))
#if QT_CONFIG(tooltip)
        self.cadence_slider_value.setToolTip(QCoreApplication.translate("MainWindow", u"Cadence value set how many in-between frames that will not be directly diffused. Low value produces more flickering and longer render time. Higher value produces less flickering and shorter render time. Diffrent settings for diffrent results.", None))
#endif // QT_CONFIG(tooltip)
        self.cadence_slider_value.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.cadence_active_checkbox.setToolTip(QCoreApplication.translate("MainWindow", u"If checked, this value will be used, else the Deforum value will be used. You can dynamically switch between the two.", None))
#endif // QT_CONFIG(tooltip)
        self.cadence_active_checkbox.setText("")
        self.panning_x_label.setText(QCoreApplication.translate("MainWindow", u"Panning X", None))
        self.panning_y_label.setText(QCoreApplication.translate("MainWindow", u"Panning Y", None))
        self.rotate_h_label.setText(QCoreApplication.translate("MainWindow", u"Rotate H", None))
        self.rotate_v_label.setText(QCoreApplication.translate("MainWindow", u"Rotate V", None))
        self.zoom_label.setText(QCoreApplication.translate("MainWindow", u"Zoom", None))
        self.tilt_label.setText(QCoreApplication.translate("MainWindow", u"Tilt", None))
        self.fov_label.setText(QCoreApplication.translate("MainWindow", u"FOV", None))
        self.steps_label.setText(QCoreApplication.translate("MainWindow", u"Steps", None))
        self.strength_label.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.cfg_label.setText(QCoreApplication.translate("MainWindow", u"CFG scale", None))
        self.cadence_label.setText(QCoreApplication.translate("MainWindow", u"Cadence", None))
        self.noise_multi_label.setText(QCoreApplication.translate("MainWindow", u"Noise Multi", None))
        self.seed_value_label.setText(QCoreApplication.translate("MainWindow", u"Seed", None))
#if QT_CONFIG(tooltip)
        self.panning_x_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.panning_x_live_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.panning_y_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.panning_y_live_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.rotate_h_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_h_live_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.rotate_v_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.rotate_v_live_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.zoom_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_live_value.setText(QCoreApplication.translate("MainWindow", u"70", None))
#if QT_CONFIG(tooltip)
        self.tilt_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.tilt_live_value.setText(QCoreApplication.translate("MainWindow", u"0.00", None))
#if QT_CONFIG(tooltip)
        self.fov_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.fov_live_value.setText(QCoreApplication.translate("MainWindow", u"70", None))
#if QT_CONFIG(tooltip)
        self.steps_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.steps_live_value.setText(QCoreApplication.translate("MainWindow", u"50", None))
#if QT_CONFIG(tooltip)
        self.strength_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.strength_live_value.setText(QCoreApplication.translate("MainWindow", u"0.68", None))
#if QT_CONFIG(tooltip)
        self.cfg_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.cfg_live_value.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.cadence_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.cadence_live_value.setText(QCoreApplication.translate("MainWindow", u"3", None))
#if QT_CONFIG(tooltip)
        self.noise_multiplier_live.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.noise_multiplier_live.setText(QCoreApplication.translate("MainWindow", u"1.05", None))
#if QT_CONFIG(tooltip)
        self.seed_live_value.setToolTip(QCoreApplication.translate("MainWindow", u"Shows the value for this motion, currently used by Deforum.", None))
#endif // QT_CONFIG(tooltip)
        self.seed_live_value.setText(QCoreApplication.translate("MainWindow", u"-1", None))
#if QT_CONFIG(tooltip)
        self.panx_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.panx_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.panx_l.setText("")
#if QT_CONFIG(tooltip)
        self.panx_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.panx_r.setText("")
#if QT_CONFIG(tooltip)
        self.pany_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.pany_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.pany_l.setText("")
#if QT_CONFIG(tooltip)
        self.pany_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.pany_r.setText("")
#if QT_CONFIG(tooltip)
        self.roth_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.roth_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.roth_l.setText("")
#if QT_CONFIG(tooltip)
        self.roth_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.roth_r.setText("")
#if QT_CONFIG(tooltip)
        self.rotv_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.rotv_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.rotv_l.setText("")
#if QT_CONFIG(tooltip)
        self.rotv_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.rotv_r.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.zoom_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_l.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_r.setText("")
#if QT_CONFIG(tooltip)
        self.tilt_rise_fall_frame.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.tilt_l.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.tilt_l.setText("")
#if QT_CONFIG(tooltip)
        self.tilt_r.setToolTip(QCoreApplication.translate("MainWindow", u"When the left arrow becomes red, it means that the previous value was higher than the current value (values are decreasing).\n"
"When the right arrow becomes green, it means that the previous value was lower than the current value (values are increaing.\n"
"If neither of them are showing any color, the value has not changed, and there is probably no ongoing motion.", None))
#endif // QT_CONFIG(tooltip)
        self.tilt_r.setText("")
#if QT_CONFIG(tooltip)
        self.Live_ValuesLabel.setToolTip(QCoreApplication.translate("MainWindow", u"This window shows the values that Deforum is currently working with. These values can be different from the values that Deforumation is currently using.", None))
#endif // QT_CONFIG(tooltip)
        self.Live_ValuesLabel.setText(QCoreApplication.translate("MainWindow", u"Live Values", None))
    # retranslateUi

