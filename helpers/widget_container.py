import enum
import math
import sys

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, QEvent, SIGNAL, Slot, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, QTextDocument, QAbstractTextDocumentLayout,
                           QTextFrame, QAction, QMouseEvent)
from PySide6.QtWidgets import (QApplication, QFrame, QDateEdit, QGridLayout, QStackedLayout, QBoxLayout, QHBoxLayout,
                               QVBoxLayout, QLabel, QSlider, QLayout, QMainWindow, QMenuBar, QPushButton, QSizePolicy, QStatusBar,
                               QTabWidget, QTextEdit, QWidget, QDial, QMenu, QScrollArea, QWidgetAction, QLineEdit, QCheckBox, QProgressBar, QComboBox, QTableView, QRadioButton)
from PySide6 import QtGui, QtCore

class widgetContainerClass():

    def __init__(self, parent=None):
        self.widget = None
        self.MousePressEvent = None
        self.MouseMoveEvent = None
        self.MouseReleaseEvent = None
        self.kukenstar = None
        self.icon = None
        self.isConnected = False
        self.hasBeenProcessed = False
        self.original_widget_name = "Empty"
        self.component_pos = None
        self.component_parent = None
        self.isActivated = False
    def SetValues(self, object):
        self.widget = object
        self.original_widget_name = object.objectName()
        self.kukenstar = object.mousePressEvent
        self.MousePressEvent = object.mousePressEvent
        self.MouseMoveEvent = object.mouseMoveEvent
        self.MouseReleaseEvent = object.mouseReleaseEvent
        if type(object) == QPushButton:
            self.icon = object.icon()

class Deforumation_Widgets():

    def __init__(self, parent=None, deforumation_settings=None):
        self.parent = parent
        self.deforumation_settings = deforumation_settings
        self.image_grid_container = {}
        self.widgetContainer = {}
        self.componentContainer = {}
        self.new_widget = None


    def copy_layout(self, layout):
        if layout is None:
            return None

        # Determine the type of the layout and create a new instance
        if isinstance(layout, QVBoxLayout):
            new_layout = QVBoxLayout()
        # Add more layout types here if needed
        else:
            return None

        # Iterate over all items in the layout and add them to the new layout
        for i in range(layout.count()):
            item = layout.itemAt(i)
            if item.widget():
                new_layout.addWidget(self.copy_widget(item.widget()))
            # Add handling for other item types (like spacers) here if needed

        return new_layout

    def copy_properties(self, src, dest):
        # Iterate over all properties using the meta-object system
        #print("Duplicating:" + str(src) + " ... With object name:" + str(src.objectName()))
        for i in range(src.metaObject().propertyCount()):
            meta_property = src.metaObject().property(i)
            nameis = meta_property.name()
            if meta_property.isReadable() and meta_property.isWritable():
                if nameis == "pixmap":
                    if src.pixmap().width() != 0 and src.pixmap().height() != 0:
                        value = src.property(meta_property.name())
                        dest.setProperty(meta_property.name(), value)
                elif nameis == "visible" or nameis == "objectName":
                    #print("Not copying:" + nameis)
                    pass
                else:
                    value = src.property(meta_property.name())
                    if isinstance(value, enum.Enum):
                        value = value.value
                    dest.setProperty(meta_property.name(), value)


        #Hot-fix for displaying Comboboxes correctly
        if type(src) == QComboBox:
            dest.deleteLater()
            dest = QComboBox(dest.parent()) #self.Motion_Zoom_Component_poppable)
            for index in range(src.count()):
                text = src.itemText(index)
                dest.addItem(text)
                #new_combo_box.addItem("")
            dest.setGeometry(src.geometry())
            dest.setLayout(src.layout())

        # Look for a proper name
        index = 1
        while True:
            if not f"{src.objectName()}_{index}" in self.widgetContainer:
                dest.setObjectName(f"{src.objectName()}_{index}")
                break
            index += 1

        if type(src) == QPushButton:
            dest.setIcon(self.widgetContainer[src.objectName()].icon)
        self.widgetContainer[dest.objectName()] = widgetContainerClass()
        self.widgetContainer[dest.objectName()].SetValues(dest)

    def get_signals(self, source):
        cls = source if isinstance(source, type) else type(source)
        signal = type(QtCore.Signal())
        for subcls in cls.mro():
            clsname = f'{subcls.__module__}.{subcls.__name__}'
            for key, value in sorted(vars(subcls).items()):
                if isinstance(value, signal):
                    print(f'{key} [{clsname}]')
    def handle_slider_orientation(self, src, dest):
        # Explicitly copy the orientation of a slider
        dest.setOrientation(src.orientation())

    def duplicate_widget(self, original, parent=None, ):
        # Create a new instance of the widget
        if type(original) == QComboBox:
            new_widget = QComboBox(parent)
            """elif type(original) == QScrollArea or type(original) == QFrame or type(original) == QWidget:
                new_widget = self.#self.copy_widget_with_scroll_area(original)
                # Look for a proper name
                index = 1
                while True:
                    if not f"{original.objectName()}_{index}" in self.widgetContainer:
                        new_widget.setObjectName(f"{original.objectName()}_{index}")
                        break
                    index += 1
        
                return new_widget"""
        else:
            new_widget = type(original)(parent)
        #if type(original) == QComboBox:
        #    new_widget = self.duplicate_combobox(original)
        # Copy relevant properties
        self.copy_properties(original, new_widget)
        piss = new_widget.parent()
        # Check for layout
        #if original.layout():# and isinstance(original.layout(), QWidget):
        #    self.duplicate_layout(original, new_widget)
        #else:
            #if type(original) == QComboBox:
            #    return self.new_widget
            #else:
            # If no layout, duplicate child widgets manually
        for child in original.children():
            if isinstance(child, QWidget):
                new_child = self.duplicate_widget(child, new_widget)
                #new_child.setGeometry(child.geometry())

        return new_widget

    def clone_layout(self, old_layout):
        """
        Clone the given layout and return the clone.
        """
        try:
            layout = type(old_layout)()
        except Exception as e:
            layout = old_layout.layout()
        #QBoxLayout.layout()

        for i in range(old_layout.count()):
            item = old_layout.itemAt(i)
            if item.widget():
                # Create a new instance of the widget
                widget_type = type(item.widget())
                new_widget = widget_type()  # Assumes the widget can be created with no arguments
                layout.addWidget(new_widget)
            elif item.layout():
                # Recursively clone the layout
                layout.addLayout(self.clone_layout(item.layout()))

        return layout

    def duplicate_layout(self, original_widget, new_widget):
        """
        Duplicate the layout of 'original_widget' to 'new_widget'.
        """
        if original_widget.layout() is None:
            return  # Original widget does not have a layout

        new_layout = self.clone_layout(original_widget.layout())
        new_widget.setLayout(new_layout)


    def extractLabelWidgetsAndChangeToConfig(self, parent, aWidget, config):
        for child in aWidget.children():
            self.extractLabelWidgetsAndChangeToConfig(parent, child, config)
            # Check if the child is a widget and has a tooltip
            if isinstance(child, QWidget) and child.toolTip():
                objname = child.objectName()
                if objname + "_tooltip" in config:
                    child.setToolTip(config[objname + "_tooltip"])
            # Check if the child is a widget
            if isinstance(child, QWidget):
                # Attempt to get text if the widget supports it
                text_method = getattr(child, "text", None)
                if callable(text_method):
                    widget_text = text_method()
                    if widget_text:
                        if not child.text().replace(".", "").replace("%", "").replace("-", "").replace(" ", "").isnumeric():
                            objname = child.objectName()
                            if objname in config:
                                child.setText(config[objname])
    def extractLabelWidgetsAndAddToConfig(self, parent, aWidget, config):
        for child in aWidget.children():
            #objname = widget.objectName()
            self.extractLabelWidgetsAndAddToConfig(parent, child, config)
            # Check if the child is a widget and has a tooltip
            if isinstance(child, QWidget) and child.toolTip():
                objname = child.objectName()
                tooltip = child.toolTip()
                config[objname+"_tooltip"] = tooltip
                # Check if the child is a widget
            if isinstance(child, QWidget):
                # Attempt to get text if the widget supports it
                text_method = getattr(child, "text", None)
                if callable(text_method):
                    widget_text = text_method()
                    if widget_text:
                        if not child.text().replace(".", "").replace("%", "").replace("-", "").replace(" ", "").isnumeric():
                            objname = child.objectName()
                            config[objname] = child.text()

    def enumerateWidgets(self, parent, aWidget):
        moveableTypes = [QFrame, QLabel, QPushButton, QLabel, QSlider, QDateEdit, QDial, QLineEdit, QCheckBox, QTextEdit, QProgressBar, QComboBox, QWidget, QTableView, QScrollArea, QRadioButton]
        #for widget in aWidget.children():
        isIterable = False
        while isIterable == False:
            try:
                isIterable = iter(aWidget)
            except TypeError as e:
                aWidget.installEventFilter(parent)
                aWidget = aWidget.children()
        for widget in aWidget:
            objname = widget.objectName()
            if not objname in self.widgetContainer and objname != "":
                if type(widget) in moveableTypes:
                    self.widgetContainer[widget.objectName()] = widgetContainerClass()
                    self.widgetContainer[widget.objectName()].SetValues(widget)
                    if type(widget) == QPushButton and not widget.icon().isNull():
                        widget.setMask(widget.icon().pixmap(widget.iconSize(), QIcon.Normal, QIcon.Off).mask())
                    if type(widget) == QTableView:
                        pass
                    widget.installEventFilter(parent)
                    #print("Installing eventFilter for: " + str(objname))
                    if type(widget) == QPushButton or type(widget) == QCheckBox or type(widget) == QComboBox or type(widget) == QTableView:
                        if self.widgetContainer[objname].isConnected == False:
                            self.widgetContainer[objname].isConnected = True
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    elif type(widget) == QLineEdit:
                        if self.widgetContainer[objname].isConnected == False:
                            widget.returnPressed.connect(parent.pressed_return)
                            self.widgetContainer[objname].isConnected = True
                            self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    elif type(widget) == QSlider:
                        widget.valueChanged.connect(lambda chk=False, item=widget: parent.value_changed_slider(item))
                        #widget.mouseReleaseEvent.connect(lambda chk=False, item=widget: parent.slider_release_event(item))
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    if widget.hasTabletTracking():# and "_poppable" in objname:
                        self.componentContainer[widget.objectName()] = widget
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True
            #This is for duplicated components
            elif objname != "" and not self.widgetContainer[widget.objectName()].hasBeenProcessed:
                if type(widget) in moveableTypes:
                    if type(widget) == QPushButton and not widget.icon().isNull():
                        widget.setMask(widget.icon().pixmap(widget.iconSize(), QIcon.Normal, QIcon.Off).mask())

                    widget.installEventFilter(parent)
                    if type(widget) == QPushButton or type(widget) == QCheckBox or type(widget) == QComboBox or type(widget) == QTableView:
                        if self.widgetContainer[objname].isConnected == False:
                            self.widgetContainer[objname].isConnected = True
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    elif type(widget) == QLineEdit:
                        if self.widgetContainer[objname].isConnected == False:
                            widget.returnPressed.connect(parent.pressed_return)
                            self.widgetContainer[objname].isConnected = True
                            self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    elif type(widget) == QSlider:
                        widget.valueChanged.connect(lambda chk=False, item=widget: parent.value_changed_slider(item))
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True
                    if widget.hasTabletTracking():# and "_poppable" in objname:
                        self.componentContainer[widget.objectName()] = widget
                        self.widgetContainer[widget.objectName()].hasBeenProcessed = True

            self.enumerateWidgets(parent, widget.children())

    def getWidgetContainer(self):
        return self.widgetContainer

    def getComponentContainer(self):
        return self.componentContainer

    #def removeWidgetAndItsChildren(self, parent_widget):
    #    self.removeWidgetChildren(parent_widget)
    def removeWidgetAndItsChildren(self, parent_widget):
        for child in parent_widget.children():
            if child.objectName() in self.widgetContainer:
                #print("Removing from container: " + str(child.objectName()))
                del self.widgetContainer[child.objectName()]
                #if "poppable" in child.objectName(): #If it also is in the component container it should be deleted
                self.removeComponentFromContainer(child)
                self.deforumation_settings.deleteGuiConfigKey(child.objectName())
            if isinstance(child, QWidget):
                self.removeWidgetAndItsChildren(child)
        if parent_widget.objectName() in self.widgetContainer:
            #print("Removing from container: " + str(parent_widget.objectName()))
            del self.widgetContainer[parent_widget.objectName()]
            #if "poppable" in parent_widget.objectName():  # If it also is in the component container it should be deleted
            self.removeComponentFromContainer(parent_widget)
            self.deforumation_settings.deleteGuiConfigKey(parent_widget.objectName())
        #print("Deleting real widget: " + str(parent_widget.objectName()))
        #del parent_widget
        parent_widget.deleteLater()
    def removeComponentFromContainer(self, parent_widget):
        if parent_widget.objectName() in self.componentContainer:
            del self.componentContainer[parent_widget.objectName()]
