from PySide6.QtWidgets import QCheckBox, QLabel, QLineEdit, QSlider, QProgressBar
from helpers.widget_container import Deforumation_Widgets
class Deforumation_Tools():

    def __init__(self, parent=None, deforumationwidgets=None):
        self.parent = parent
        self.deforumationwidgets = deforumationwidgets

    def getOriginalComponentName(self, sender):
        # Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(sender.objectName()):
            if c.isdigit() and sender.objectName()[i-1] == "_":
                digitPosition = i
                break
        if digitPosition == -1:
            original_component_name = sender.objectName()
        else:
            original_component_name = sender.objectName()[:digitPosition - 1]
        return original_component_name

    def getOriginalComponentNameFromName(self, component_name):
        # Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(component_name):
            if c.isdigit():
                digitPosition = i
                break
        if digitPosition == -1:
            original_component_name = component_name
        else:
            original_component_name = component_name[:digitPosition - 1]
        return original_component_name

    def isComponentAduplicated(self, component_name):
        # Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(component_name):
            if c.isdigit():
                digitPosition = i
                break
        if digitPosition == -1:
            return False
        else:
            return True

    def propagateAllComponents(self, sender, value = None, shouldHide = False, onlySetSizes = False):
        original_component_name = self.getOriginalComponentName(sender)
        for component in self.deforumationwidgets.getWidgetContainer():
            if component.startswith(original_component_name) and not component == sender.objectName():
                if len(component) <= len(original_component_name ) +3:
                    if type(sender) == QCheckBox:
                        if value == None:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.setChecked(not sender.isChecked())
                        else:
                            component.setChecked(value)
                    elif type(sender) == QLabel or type(sender) == QLineEdit:
                        if value == -1:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.setText("")
                        else:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.setText(str(sender.text()))
                        if shouldHide:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.hide()
                        else:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.show()
                    elif type(sender) == QSlider:
                        if onlySetSizes == False:
                            self.deforumationwidgets.getWidgetContainer()[component].widget.setValue(sender.value())
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setMaximum(sender.maximum())
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setMinimum(sender.minimum())
                    elif type(sender) == QProgressBar:
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setValue(sender.value())
    def propagateAllCheckboxes(self, sender):
        #Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(sender.objectName()):
            if c.isdigit() and sender.objectName()[i-1] == "_":
                digitPosition = i
                break
        if digitPosition == -1:
            original_checkbox_name = sender.objectName()
        else:
            original_checkbox_name = sender.objectName()[:digitPosition-1]
        for checkboxwidgets in self.deforumationwidgets.getWidgetContainer():
            if checkboxwidgets.startswith(original_checkbox_name) and not checkboxwidgets == sender.objectName():
                self.deforumationwidgets.getWidgetContainer()[checkboxwidgets].widget.setChecked(not sender.isChecked())

    def getWidgetFromContainer(self, component_name):
        widgetContainer = self.deforumationwidgets.getWidgetContainer()
        if component_name in widgetContainer:
            return widgetContainer[component_name].widget
        else:
            return None