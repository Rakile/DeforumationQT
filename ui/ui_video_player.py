# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_player.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QMainWindow,
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(847, 578)
        MainWindow.setStyleSheet(u"/*ElegantDark Style Sheet for QT Applications\n"
"Author: Jaime A. Quiroga P.\n"
"Company: GTRONICK\n"
"Last updated: 17/04/2018\n"
"Available at: https://github.com/GTRONICK/QSS/blob/master/ElegantDark.qss\n"
"*/\n"
"QMainWindow {\n"
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
""
                        "  color: rgb(255, 255, 255);\n"
"  padding: 2px;\n"
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(77, 77, 77, 255), stop:1 rgba(97, 97, 97, 255));\n"
"}\n"
"QPushButton:hover{\n"
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
"  background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0, stop:0 rgba(107, 107, 107, 255), stop:1 rgba(157, 157, 157"
                        ", 255));\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"  border-style: outset;\n"
"  border-width: 2px;\n"
"  border-top-color: qlineargradient(spread:pad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(62, 62, 62, 255));\n"
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
""
                        "  background:rgb(100, 100, 100);\n"
"  selection-background-color: rgb(187, 187, 187);\n"
"  selection-color: rgb(60, 63, 65);\n"
"}\n"
"QLabel {\n"
"  color:rgb(255,255,255); \n"
"}\n"
"QProgressBar {\n"
"  text-align: center;\n"
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
""
                        "  padding-right:8px;\n"
"  padding-top:2px;\n"
"  padding-bottom:3px;\n"
"  background:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 255), stop:1 rgba(93, 103, 113, 255));\n"
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
"    border-c"
                        "olor: rgb(77,77,77);\n"
"    background-color:rgb(101,101,101);\n"
"    border-style: solid;\n"
"    border-width: 1px;\n"
"      border-radius: 6px;\n"
"}\n"
"\n"
"QSplitter{\n"
"    border-color: rgb(77,77,77);\n"
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
"  border-top-color: qlineargradient(spread:p"
                        "ad, x1:0.5, y1:0.6, x2:0.5, y2:0.4, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
"  border-right-color: qlineargradient(spread:pad, x1:0.4, y1:0.5, x2:0.6, y2:0.5, stop:0 rgba(115, 115, 115, 255), stop:1 rgba(95, 92, 93, 255));\n"
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
"  border-color: rgb(87, 97, 106);"
                        "\n"
"  background-color:qlineargradient(spread:pad, x1:0.5, y1:0.7, x2:0.5, y2:0.3, stop:0 rgba(87, 97, 106, 150), stop:1 rgba(93, 103, 113, 150));\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"  border-radius:4px;\n"
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
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QTabWidget.Triangular)
        MainWindow.setDockNestingEnabled(True)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setObjectName(u"layout")
        self.layout.setContentsMargins(4, 0, 4, 4)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 54))
        self.frame_2.setStyleSheet(u"QFrame {\n"
"    /* Background color */\n"
"    background-color: rgb(88, 88, 98);  /* Light gray background */\n"
"\n"
"    /* Border properties */\n"
"    border-style: solid;\n"
"    border-width: 2px;\n"
"    border-color: #000000; /* Black border */\n"
"\n"
"    /* Rounded corners */\n"
"    border-radius: 10px;\n"
"\n"
"    /* Shadow (optional) */\n"
"    /* Note: This will only work in QWidget subclasses with the 'frame' attribute set */\n"
"\n"
"    /* Size constraints (optional) */\n"
"    min-height: 50px;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.videoWidget = QVideoWidget(self.frame_2)
        self.videoWidget.setObjectName(u"videoWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.videoWidget.sizePolicy().hasHeightForWidth())
        self.videoWidget.setSizePolicy(sizePolicy1)
        self.videoWidget.setStyleSheet(u"    border: 10px groove rgb(22,22,22);\n"
"    border-radius: 10px;")

        self.verticalLayout_3.addWidget(self.videoWidget)


        self.verticalLayout.addWidget(self.frame_2)


        self.layout.addLayout(self.verticalLayout)

        self.horizontalSpacer = QSpacerItem(40, 5, QSizePolicy.Preferred, QSizePolicy.Minimum)

        self.layout.addItem(self.horizontalSpacer)

        self.slider = QSlider(self.centralwidget)
        self.slider.setObjectName(u"slider")
        self.slider.setMinimumSize(QSize(3, 35))
        self.slider.setStyleSheet(u"QSlider::groove:horizontal {\n"
"    border-image: url(images/movie_groove_long.png) ; /* Adjust slicing and stretch as needed */\n"
"    height: 31px; /* The height of your image */\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-image: url(images/handle_off.png); /* The path to your handle image */\n"
"	background-repeat: no-repeat;\n"
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
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin"
                        ": -1px 0; /* Optional: Adjust the margin if needed */\n"
"}\n"
"\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-image: url(images/handle_on.png); /* Change the handle image when pressed */\n"
"background-repeat: no-repeat;\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 32px; /* Width of the handle - adjust as needed */\n"
"    height: 32px; /* Height of the handle - adjust as needed */\n"
"    margin: -1px 0; /* Optional: Adjust the margin if needed */\n"
" 	\n"
"}")
        self.slider.setOrientation(Qt.Horizontal)

        self.layout.addWidget(self.slider)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(671, 0))
        self.frame_3.setMaximumSize(QSize(16777215, 50))
        self.frame_3.setStyleSheet(u"background-color:rgb(66,66,66);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.save_video_to_file = QPushButton(self.frame_3)
        self.save_video_to_file.setObjectName(u"save_video_to_file")
        self.save_video_to_file.setGeometry(QRect(16, 8, 42, 34))
        sizePolicy1.setHeightForWidth(self.save_video_to_file.sizePolicy().hasHeightForWidth())
        self.save_video_to_file.setSizePolicy(sizePolicy1)
        self.save_video_to_file.setMinimumSize(QSize(0, 0))
        self.save_video_to_file.setMaximumSize(QSize(38, 32))
        self.save_video_to_file.setStyleSheet(u"QPushButton {\n"
"    /* Normal state */\n"
"    background-image: url(images/Folder_off.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    /* Hovered state */\n"
"    background-image: url(images/Folder_hover.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    /* Pressed state */\n"
"    background-image: url(images/Folder_active.png);\n"
"    background-position: left top;\n"
"    background-repeat: no-repeat;\n"
"    border: none;\n"
"}")
        self.save_video_to_file.setIconSize(QSize(38, 32))
        self.restore_original_size = QPushButton(self.frame_3)
        self.restore_original_size.setObjectName(u"restore_original_size")
        self.restore_original_size.setGeometry(QRect(435, 8, 225, 35))
        sizePolicy1.setHeightForWidth(self.restore_original_size.sizePolicy().hasHeightForWidth())
        self.restore_original_size.setSizePolicy(sizePolicy1)
        self.restore_original_size.setMinimumSize(QSize(60, 35))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.restore_original_size.setFont(font)
        self.restore_original_size.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n"
"    border: none;\n"
"    border-radius: 5px; /* Consistent with the tab's rounded corners */\n"
"    padding: 6px 2px; /* Comfortable padding for the button text */\n"
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
"")
        self.paus_button = QPushButton(self.frame_3)
        self.paus_button.setObjectName(u"paus_button")
        self.paus_button.setGeometry(QRect(158, 8, 35, 33))
        sizePolicy1.setHeightForWidth(self.paus_button.sizePolicy().hasHeightForWidth())
        self.paus_button.setSizePolicy(sizePolicy1)
        self.paus_button.setMinimumSize(QSize(35, 33))
        self.paus_button.setMaximumSize(QSize(34, 33))
        self.paus_button.setTabletTracking(False)
        self.paus_button.setStyleSheet(u"\n"
"QPushButton {\n"
"   border-image: url(images/paus_off.png); /* Change the handle image when hovering */\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}\n"
"QPushButton:hover {\n"
"   border-image: url(images/paus_hover.png); /* Change the handle image when hovering */\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}\n"
"QPushButton:pressed {\n"
"   border-image: url(images/paus_active.png); /* Change the handle image when hovering */\n"
"    border: none; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}")
        self.paus_button.setIconSize(QSize(34, 33))
        self.play_button = QPushButton(self.frame_3)
        self.play_button.setObjectName(u"play_button")
        self.play_button.setGeometry(QRect(296, 8, 34, 33))
        sizePolicy1.setHeightForWidth(self.play_button.sizePolicy().hasHeightForWidth())
        self.play_button.setSizePolicy(sizePolicy1)
        self.play_button.setMinimumSize(QSize(34, 33))
        self.play_button.setMaximumSize(QSize(35, 33))
        self.play_button.setTabletTracking(False)
        self.play_button.setAutoFillBackground(False)
        self.play_button.setStyleSheet(u"\n"
"QPushButton {\n"
"   border-image: url(images/play_off.png); /* Change the handle image when hovering */\n"
"    border: 0; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}\n"
"QPushButton:hover {\n"
"   border-image: url(images/play_hover.png); /* Change the handle image when hovering */\n"
"    border: 0; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}\n"
"QPushButton:pressed {\n"
"   border-image: url(images/play_active.png); /* Change the handle image when hovering */\n"
"    border: 0; /* Remove the border if you don't need it */\n"
"    width: 34px; /* Width of the handle - adjust as needed */\n"
"    height: 33px; /* Height of the handle - adjust as needed */\n"
"}")
        self.play_button.setIconSize(QSize(34, 33))

        self.horizontalLayout.addWidget(self.frame_3)

        self.horizontalSpacer_3 = QSpacerItem(58, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.layout.addWidget(self.frame)


        self.verticalLayout_2.addLayout(self.layout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.save_video_to_file.setText("")
        self.restore_original_size.setText(QCoreApplication.translate("MainWindow", u"Restore Original Video Size", None))
        self.paus_button.setText("")
        self.play_button.setText("")
    # retranslateUi

