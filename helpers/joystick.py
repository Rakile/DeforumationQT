"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import importlib
import math
import queue
import threading
import time

from PySide6.QtCore import Slot, QMetaObject, Q_ARG, QSize, QCoreApplication, QRect, QGenericArgument
from PySide6.QtGui import Qt, QFont
from PySide6.QtWidgets import QComboBox, QLabel, QVBoxLayout, QWidget, QLineEdit, QPushButton, QSizePolicy
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
#import pyjoystick
#from pyjoystick.sdl2 import Key, Joystick, run_event_loop, get_mapping, set_mapping
import inputs
from inputs import get_key

Axis_left = "-Axis 0"
Axis_right = "Axis 0"
Axis_down = "Axis 1"
Axis_up = "-Axis 1"
EVENT_ABB = (
    ('Absolute-ABS_X', 'A0'),
    ('Absolute-ABS_Y', 'A1'),
    ('Absolute-ABS_RX', 'A2'),
    ('Absolute-ABS_RY', 'A3'),

    ('Absolute-ABS_Z', 'A4'),
    ('Absolute-ABS_RZ', 'A5'),
    # D-PAD, aka HAT
    ('Absolute-ABS_HAT0X', 'HX'),
    ('Absolute-ABS_HAT0Y', 'HY'),

    # Face Buttons
    ('Key-BTN_NORTH', 'N'),
    ('Key-BTN_EAST', 'E'),
    ('Key-BTN_SOUTH', 'S'),
    ('Key-BTN_WEST', 'W'),

    # Other buttons
    ('Key-BTN_THUMBL', 'THL'),
    ('Key-BTN_THUMBR', 'THR'),
    ('Key-BTN_TL', 'TL'),
    ('Key-BTN_TR', 'TR'),
    ('Key-BTN_TL2', 'TL2'),
    ('Key-BTN_TR2', 'TR3'),
    ('Key-BTN_MODE', 'M'),
    ('Key-BTN_START', 'ST'),

    # PiHUT SNES style controller buttons
    ('Key-BTN_TRIGGER', 'N'),
    ('Key-BTN_THUMB', 'E'),
    ('Key-BTN_THUMB2', 'S'),
    ('Key-BTN_TOP', 'W'),
    ('Key-BTN_BASE3', 'SL'),
    ('Key-BTN_BASE4', 'ST'),
    ('Key-BTN_TOP2', 'TL'),
    ('Key-BTN_PINKIE', 'TR')
)

BINDINGS = {
    'Pan_L': 'A0_L',
    'Pan_R': 'A0_R',
    'Pan_U': 'A1_U',
    'Pan_D': 'A1_D',
    'Rot_H': 'A2',
    'Rot_V': 'A3',
    'Zoom_B': 'A4',
    'Zoom_F': 'A5',
}

# This is to reduce noise from the PlayStation controllers
# For the Xbox controller, you can set this to 0
MIN_ABS_DIFFERENCE = 5

CHUNK_SIZE = 1024
BUF_MAX_SIZE = CHUNK_SIZE * 10
class binding():
  button_object = None
  bindings_name = None
  controller_code = None

class Deforumation_Joystick():
  def __init__(self, deforumation_settings=None, parent=None, DeforumationMotions=None):
    if deforumation_settings != None:
      self.deforumation_settings = deforumation_settings
    else:
      pass
    self.parent = parent
    self.DeforumationMotions = DeforumationMotions
    #self.shouldRunJoystickManager = False
    self.mngr = None
    self._other = 0
    self.currentJoystick = ""
    self.shouldRunJoystickManager = False
    self.joystic_device = {}
    self.keyboard = None
    self.btn_state = {}
    self.old_btn_state = {}
    self.abs_state = {}
    self.old_abs_state = {}
    self.controller_bindings = {}
    self.abbrevs = dict(EVENT_ABB)
    self.currentJoystickObject = None
    self.notInLimbo = True
    self.currentBindingButton = None
    self.previousBindingButton = None
    self.shouldBind = False
    self.bindings = {}
    for key, value in self.abbrevs.items():
      if key.startswith('Absolute'):
        self.abs_state[value] = 0
        self.old_abs_state[value] = 0
      if key.startswith('Key'):
        self.btn_state[value] = 0
        self.old_btn_state[value] = 0
    self.parent.ui.joystick_combo_box.currentIndexChanged.connect(self.joystic_selection_changed)
    self.get_bindings_from_config()


  def convert_timeval(self, seconds_since_epoch):
    """Convert time into C style timeval."""
    frac, whole = math.modf(seconds_since_epoch)
    microseconds = math.floor(frac * 1000000)
    seconds = math.floor(whole)
    return seconds, microseconds

  def get_bindings_from_config(self):
    control_binding_buttons = {"joystick_panning_left_binding_button":"Pan_L", "joystick_panning_right_binding_button":"Pan_R", "joystick_panning_up_binding_button":"Pan_U", "joystick_panning_down_binding_button":"Pan_D", "joystick_rotate_h_left_binding_button":"Rot_H_L", "joystick_rotate_h_right_binding_button":"Rot_H_R", "joystick_rotate_v_up_binding_button":"Rot_V_U", "joystick_rotate_v_down_binding_button":"Rot_V_D", "joystick_zoom_forwards_binding_button":"Zoom_F", "joystick_zoom_backwards_binding_button":"Zoom_B", "joystick_tilt_cw_bind_button":"Tilt_CW", "joystick_tilt_cc_bind_button":"Tilt_CC"}
    for c_b in control_binding_buttons:
      controller_code = self.deforumation_settings.getGuiConfigValue(c_b)
      if controller_code != -1:
        if not controller_code in self.bindings:
          self.bindings[controller_code] = binding()
          self.bindings[controller_code].bindings_name = control_binding_buttons[c_b]
          self.bindings[controller_code].button_object = getattr(self.parent.ui, c_b) #self.currentBindingButton
          self.bindings[controller_code].button_object.setText(controller_code)

  def __write_to_character_device(self, device, event_list, timeval=None):
    """Emulate the Linux character device on other platforms such as
    Windows."""
    # Remember the position of the stream
    pos = device._character_device.tell()
    # Go to the end of the stream
    device._character_device.seek(0, 2)
    # Write the new data to the end
    for event in event_list:
      device._character_device.write(event)
    # Add a sync marker
    sync = device.create_event_object("Sync", 0, 0, timeval)
    device._character_device.write(sync)
    # Put the stream back to its original position
    device._character_device.seek(pos)
  def free_current_joystick(self):
    timeval = self.convert_timeval(time.time()) # self.currentJoystickObject.__get_timeval()
    if self.currentJoystickObject != None:
      event = self.currentJoystickObject.create_event_object("Misc", 5, 4242, timeval=timeval)
      events = []
      events.append(event)
      self.__write_to_character_device(self.currentJoystickObject, events, timeval)

  def abort_joystick_event(self, eventCode):
    if self.currentJoystickObject != None:
      timeval = self.convert_timeval(time.time())  # self.currentJoystickObject.__get_timeval()
      event = self.currentJoystickObject.create_event_object("Misc", 5, eventCode, timeval=timeval)
      events = []
      events.append(event)
      self.__write_to_character_device(self.currentJoystickObject, events, timeval)


  def joystic_selection_changed(self, index):
    self.currentJoystick = self.parent.ui.joystick_combo_box.currentText()
    print("Changed controller to:" + self.currentJoystick)
    #devices = None #Joystick.get_joysticks()
    if self.currentJoystick in self.joystic_device:
      #print("Found it")
      if self.currentJoystickObject != None:
        self.notInLimbo = False
        self.free_current_joystick()
      self.currentJoystickObject = self.joystic_device[self.currentJoystick]


      """font5 = QFont()
      font5.setPointSize(9)
      currentGeometry = self.parent.ui.verticalLayoutWidget_4.geometry()
      new_height_key_name = currentGeometry.height()
      currentWidth = currentGeometry.width()
      currentGeometry = self.parent.ui.verticalLayoutWidget_5.geometry()
      new_height_key_value = currentGeometry.height()

      sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
      sizePolicy2.setHorizontalStretch(0)
      sizePolicy2.setVerticalStretch(0)
      #sizePolicy2.setHeightForWidth(self.parent.ui.splitter.sizePolicy().hasHeightForWidth())
      #sizePolicy2.setHeightForWidth(self.parent.ui.test_bind_value.sizePolicy().hasHeightForWidth())
      for control_map in self.abbrevs: #self.currentJoystickObject.controller_mapping:
        self.joy_key_name = QLabel(self.parent.ui.verticalLayoutWidget_4)
        self.joy_key_name.setObjectName(u"Key_Map_Name_"+str(control_map))
        sizePolicy2.setHeightForWidth(self.joy_key_name.sizePolicy().hasHeightForWidth())
        self.joy_key_name.setSizePolicy(sizePolicy2)
        self.joy_key_name.setMinimumSize(QSize(0, 0))
        self.joy_key_name.setText(QCoreApplication.translate("MainWindow", str(control_map), None))
        self.joy_key_name.setFont(font5)
        self.joy_key_name.setStyleSheet("background-color: rgb(64, 64, 64);\npadding: 4px; /* To prevent the content from touching the border */\n border-radius: 3px;")
        self.parent.ui.verticalLayout_JoystickBinding_Key_Name.addWidget(self.joy_key_name)
        currentGeometry = self.parent.ui.verticalLayoutWidget_4.geometry()
        new_height_key_name = currentGeometry.height() + 28
        currentWidth = currentGeometry.width()
        self.parent.ui.verticalLayoutWidget_4.setGeometry(QRect(0, 4, currentWidth, new_height_key_name))

        #Joystic LineEdits
        self.joy_key_value = QPushButton(self.parent.ui.verticalLayoutWidget_5)
        self.joy_key_value.setObjectName(u"Key_Map_Value_"+str(control_map))
        sizePolicy2.setHeightForWidth(self.joy_key_value.sizePolicy().hasHeightForWidth())
        self.joy_key_value.setSizePolicy(sizePolicy2)
        self.joy_key_value.setMinimumSize(QSize(0, 0))
        self.joy_key_value.setText("")#str(self.currentJoystickObject.controller_mapping[control_map].keyname))
        self.joy_key_value.setFont(font5)
        self.joy_key_value.setStyleSheet("QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
        self.parent.ui.verticalLayout_JoystickBinding_Key_Value.addWidget(self.joy_key_value)
        currentGeometry = self.parent.ui.verticalLayoutWidget_5.geometry()
        new_height_key_value = currentGeometry.height() + 28
        currentWidth = currentGeometry.width()
        self.parent.ui.verticalLayoutWidget_5.setGeometry(QRect(0, 4, currentWidth, new_height_key_value))


      #Fix the size of the scroll area for the joystick binding names
      currentGeometry2 = self.parent.ui.joystic_bindings_row.geometry()
      currentWidth2 = currentGeometry2.width()
      currentGeometry3 = self.parent.ui.joystic_key_bindings_frame_poppable.geometry()
      currentWidth3 = currentGeometry3.width()
      self.parent.ui.scrollAreaWidgetContentsJoystickBindings.setMinimumSize(QSize(currentWidth, new_height_key_name+28))
      self.parent.ui.joystic_bindings_row.setGeometry(5,0, currentWidth2, new_height_key_name)
      self.parent.ui.joystic_key_bindings_frame_poppable.setGeometry(0,0, currentWidth3, new_height_key_name)

      #Fix the size of the scroll area for the joystick binding values
      currentGeometry2 = self.parent.ui.joystic_value_bindings_row.geometry()
      currentWidth2 = currentGeometry2.width()
      #currentGeometry3 = self.parent.ui.joystic_key_bindings_frame_poppable.geometry()
      #currentWidth3 = currentGeometry3.width()
      #self.parent.ui.scrollAreaWidgetContentsJoystickBindings.setMinimumSize(QSize(currentWidth, newHeight))
      self.parent.ui.joystic_value_bindings_row.setGeometry(144,0, currentWidth2, new_height_key_value)
      #self.parent.ui.joystic_key_bindings_frame_poppable.setGeometry(0,0, currentWidth3, newHeight)"""

    else:
      self.currentJoystickObject = None
    self.notInLimbo = True
    #print("Exiting change of Joystick")

  def initJoystickAndKeyboardManager(self):
    #inputs.get_gamepad()
    importlib.reload(inputs)
    devices = self.gamepad = inputs.devices #Joystick.get_joysticks()
    device_number = 0
    self.parent.ui.joystick_combo_box.clear()
    for device in devices:
      if device.device_type == "joystick":
        print(device.name)
        self.joystic_device[device.name + ":" + str(device_number)] = device
        self.parent.ui.joystick_combo_box.addItem(device.name + ":" + str(device_number))
        device_number += 1
    if self.parent.ui.joystick_combo_box.count() == 0:
      self.parent.ui.joystick_combo_box.addItem("<No controllers found>")

    #We need a reference for the first available keyboard (using it for interrupting bindings and such)
    if len(inputs.devices.keyboards) > 0:
      self.keyboard = inputs.devices.keyboards[0]
    else:
      self.keyboard = None
    #Testing bindings
    self.motion_bindings = BINDINGS


  def setJoystickBinding(self, object, parameter):
    if self.currentBindingButton != None:
      self.previousBindingButton = self.currentBindingButton
      QMetaObject.invokeMethod(self.parent, "setStyleSheet_to_normal_safe", Qt.QueuedConnection)
      #button_variant = QVariant(self.currentBindingButton)
    self.currentBindingButton = object
    self.currentMotionBindingParam = parameter
    self.shouldBind = True
    #self.currentBindingButton.setStyleSheet(u"QPushButton {\n    background-color: rgb(150, 0, 0); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
    QMetaObject.invokeMethod(self.parent, "setStyleSheet_to_active_safe", Qt.QueuedConnection)

  def handle_unknown_event(self, event, key):
    """Deal with unknown events."""
    if event.ev_type == 'Key':
      new_abbv = 'B' + str(self._other)
      self.btn_state[new_abbv] = 0
      self.old_btn_state[new_abbv] = 0
    elif event.ev_type == 'Absolute':
      new_abbv = 'A' + str(self._other)
      self.abs_state[new_abbv] = 0
      self.old_abs_state[new_abbv] = 0
    else:
      return None

    self.abbrevs[key] = new_abbv
    self._other += 1

    return self.abbrevs[key]

  def process_event(self, event):
    """Process the event into a state."""
    if event.ev_type == 'Sync':
      return
    if event.ev_type == 'Misc':
      return
    key = event.ev_type + '-' + event.code
    try:
      abbv = self.abbrevs[key]
    except KeyError:
      abbv = self.handle_unknown_event(event, key)
      if not abbv:
        return
    if event.ev_type == 'Key':
      self.old_btn_state[abbv] = self.btn_state[abbv]
      self.btn_state[abbv] = event.state
    if event.ev_type == 'Absolute':
      self.old_abs_state[abbv] = self.abs_state[abbv]
      self.abs_state[abbv] = event.state
    self.output_state(event.ev_type, abbv)

  def format_state(self):
    """Format the state."""
    output_string = ""
    for key, value in self.abs_state.items():
      output_string += key + ':' + '{:>4}'.format(str(value) + ' ')

      #if key == "A0":
      if key in self.controller_bindings:
        print("A0: " + str(value))
        corrected_value = float(value/32768)
        QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.controller_bindings[key].bindings_name]), Q_ARG("QString", str(corrected_value)))

    for key, value in self.btn_state.items():
      output_string += key + ':' + str(value) + ' '

    return output_string


  def output_state(self, ev_type, abbv):
    """Print out the output state."""
    """if ev_type == 'Key':
      if self.btn_state[abbv] != self.old_btn_state[abbv]:
        if abbv in self.controller_bindings:
          value = self.btn_state[abbv]
          QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.controller_bindings[abbv]]), Q_ARG("QString", str(value)))
          #print(self.format_state())
      return"""

    if abbv.startswith("HX"):
      value = self.abs_state[abbv]
      if value > 0:
        abbv = abbv + "_R"
      elif value < 0:
        abbv = abbv + "_L"
      else:
        if (abbv + "_L") in self.bindings:
          abbv = abbv + "_L"
        elif (abbv + "_R") in self.bindings:
          abbv = abbv + "_R"
      if abbv in self.bindings:
        QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(value)))
      return
    elif abbv.startswith("HY"):
      value = self.abs_state[abbv]
      if value > 0:
        abbv = abbv + "_D"
      elif value < 0:
        abbv = abbv + "_U"
      else:
        if (abbv + "_U") in self.bindings:
          abbv = abbv + "_U"
        elif (abbv + "_D") in self.bindings:
          abbv = abbv + "_D"
      if abbv in self.bindings:
        QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(value)))
      return
    elif abbv.startswith("A"):
      difference = self.abs_state[abbv] - self.old_abs_state[abbv]
      value = self.abs_state[abbv]
      if abbv.startswith('A4'):
        if abbv in self.bindings:
          #print("Zoom: " + str(value))
          #if not self.DeforumationMotions.should_use_deforumation_game_mode:
          #  corrected_value = -float(value/32768)
          #else:
          corrected_value = -float(value / 255)
          QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(corrected_value)))
      elif abbv.startswith('A5'):
        if abbv in self.bindings:
          #print("Zoom: " + str(value))
          corrected_value = float(value / 255)
          QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(corrected_value)))
      elif (abs(difference)) > MIN_ABS_DIFFERENCE:
        #print("A0: " + str(value))
        if abbv.startswith('A0') or abbv.startswith('A1') or abbv.startswith('A2') or abbv.startswith('A3'):
          corrected_value = float(value/32768)
          if abbv.startswith('A0') or abbv.startswith('A2'):
            if corrected_value > 0:
              abbv = abbv+"_R"
            else:
              abbv = abbv+"_L"
          elif abbv.startswith('A1') or abbv.startswith('A3'):
            if corrected_value > 0:
              abbv = abbv+"_U"
            else:
              abbv = abbv+"_D"
        if abbv in self.bindings:
          QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(corrected_value)))
        else:
          #print("Not connected yet")
          pass
        return
    else:
      if ev_type == 'Key':
        value = self.btn_state[abbv]
      else:
        value = self.abs_state[abbv]
      if abbv in self.bindings:
        QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", [self.bindings[abbv].bindings_name]), Q_ARG("QString", str(value)))
      return
      #print(self.format_state())

  def joystic_event_handler(self, stopped, q):
    #print("Inside joystic_event_event_handler thread")
    self.shouldRunJoystickManager = True
    while self.shouldRunJoystickManager:
      if self.currentJoystickObject != None and self.notInLimbo:
        try:
          events = self.currentJoystickObject.read()

        except Exception as e: #EOFError:
          events = []
          self.currentJoystickObject = None
          self.initJoystickAndKeyboardManager()

        #Check for special events
        for event in events:
          if event.ev_type == "Misc" and event.state == 1337:
            # We are aborting any ongoing binding of joystic controls
            if self.shouldBind:
              self.shouldBind = False
              if self.currentBindingButton != None:
                controller_code = self.currentBindingButton.text()
                if controller_code in self.bindings:
                  self.deforumation_settings.deleteGuiConfigKey(self.bindings[controller_code].button_object.objectName())
                  self.deforumation_settings.writeDeforumationGuiValuesToConfig(None)
                  del self.bindings[controller_code]
                  self.currentBindingButton.setText("<Unbound>")
                self.previousBindingButton = self.currentBindingButton
                QMetaObject.invokeMethod(self.parent, "setStyleSheet_to_normal_safe", Qt.QueuedConnection)
                  #self.currentBindingButton.setStyleSheet(u"QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
          elif event.ev_type == "Misc" and event.state == 1338:
            if self.shouldBind:
              self.shouldBind = False
              if self.currentBindingButton != None:
                self.previousBindingButton = self.currentBindingButton
                QMetaObject.invokeMethod(self.parent, "setStyleSheet_to_normal_safe", Qt.QueuedConnection)

        if self.shouldBind:
          event = events[0]
          if event.ev_type == 'Key' or event.ev_type == 'Absolute':
            key = event.ev_type + '-' + event.code
            abbv = self.abbrevs[key]
            value = event.state
            shouldBindNow = False
            controller_code = "Unbound"
            if abbv == 'A0' or abbv == 'A1' or abbv == 'A2' or abbv == 'A3':
              if abs(value) > 15000:
                shouldBindNow = True
                if abbv == 'A0' or abbv == 'A2':
                  if value > 0:
                    controller_code = self.abbrevs[key]+"_R"
                  else:
                    controller_code = self.abbrevs[key]+"_L"
                elif abbv == 'A1' or abbv == 'A3':
                  if value > 0:
                    controller_code = self.abbrevs[key]+"_U"
                  else:
                    controller_code = self.abbrevs[key]+"_D"

                if not controller_code in self.bindings:
                  self.bindings[controller_code] = binding()
                  self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                  self.bindings[controller_code].button_object = self.currentBindingButton
                else:
                  old_binding_name = self.bindings[controller_code].bindings_name
                  temp_bindings = self.bindings.copy()
                  for bind_object in temp_bindings:
                    if self.bindings[bind_object].bindings_name == old_binding_name:
                      self.bindings[bind_object].button_object.setText("<Unbound>")
                      del self.bindings[bind_object]
                    elif self.bindings[bind_object].bindings_name == self.currentMotionBindingParam:
                      self.bindings[bind_object].button_object.setText("<Unbound>")
                      del self.bindings[bind_object]

                  if not controller_code in self.bindings:
                    self.bindings[controller_code] = binding()
                    self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                    self.bindings[controller_code].button_object = self.currentBindingButton
                  self.bindings[controller_code].bindings_name = self.currentMotionBindingParam

                self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.bindings[controller_code].button_object.objectName(), controller_code)
                #self.motion_bindings[self.currentMotionBindingParam] = self.abbrevs[key]
            elif abbv.startswith("HX"):
              shouldBindNow = True
              if value == -1:
                controller_code = self.abbrevs[key]+"_L"
              else:
                controller_code = self.abbrevs[key]+"_R"

              if not controller_code in self.bindings:
                self.bindings[controller_code] = binding()
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                self.bindings[controller_code].button_object = self.currentBindingButton
              else:
                old_binding_name = self.bindings[controller_code].bindings_name
                temp_bindings = self.bindings.copy()
                for bind_object in temp_bindings:
                  if self.bindings[bind_object].bindings_name == old_binding_name:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]
                  elif self.bindings[bind_object].bindings_name == self.currentMotionBindingParam:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]

                if not controller_code in self.bindings:
                  self.bindings[controller_code] = binding()
                  self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                  self.bindings[controller_code].button_object = self.currentBindingButton
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
              self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.bindings[controller_code].button_object.objectName(), controller_code)
            elif abbv.startswith("HY"):
              shouldBindNow = True
              if value == -1:
                controller_code = self.abbrevs[key] + "_U"
              else:
                controller_code = self.abbrevs[key] + "_D"

              if not controller_code in self.bindings:
                self.bindings[controller_code] = binding()
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                self.bindings[controller_code].button_object = self.currentBindingButton
              else:
                old_binding_name = self.bindings[controller_code].bindings_name
                temp_bindings = self.bindings.copy()
                for bind_object in temp_bindings:
                  if self.bindings[bind_object].bindings_name == old_binding_name:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]
                  elif self.bindings[bind_object].bindings_name == self.currentMotionBindingParam:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]

                if not controller_code in self.bindings:
                  self.bindings[controller_code] = binding()
                  self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                  self.bindings[controller_code].button_object = self.currentBindingButton
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
              self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.bindings[controller_code].button_object.objectName(), controller_code)
            else:
              shouldBindNow = True
              controller_code = self.abbrevs[key]
              if not controller_code in self.bindings:
                self.bindings[controller_code] = binding()
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                self.bindings[controller_code].button_object = self.currentBindingButton
              else:
                old_binding_name = self.bindings[controller_code].bindings_name
                temp_bindings = self.bindings.copy()
                for bind_object in temp_bindings:
                  if self.bindings[bind_object].bindings_name == old_binding_name:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]
                  elif self.bindings[bind_object].bindings_name == self.currentMotionBindingParam:
                    self.bindings[bind_object].button_object.setText("<Unbound>")
                    del self.bindings[bind_object]
                if not controller_code in self.bindings:
                  self.bindings[controller_code] = binding()
                  self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
                  self.bindings[controller_code].button_object = self.currentBindingButton
                self.bindings[controller_code].bindings_name = self.currentMotionBindingParam
              self.deforumation_settings.writeDeforumationGuiValuesToConfig(self.bindings[controller_code].button_object.objectName(), controller_code)
            if shouldBindNow==True:
              self.currentBindingButton.setText(controller_code)
              self.shouldBind = False
              #self.currentBindingButton.setStyleSheet(u"QPushButton {\n    background-color: rgb(64, 64, 64); /* Matching the tab's base color */\n    border: none;\n    border-radius: 3px; /* Consistent with the tab's rounded corners */\n    padding: 4px; /* Comfortable padding for the button text */\n    color: white; /* White text for contrast */\n    text-align: center;\n\n}\n\nQPushButton:hover {\n    background-color: rgb(96, 96, 96); /* Lighter grey, similar to tab hover effect */\n\n}\n\nQPushButton:pressed {\n    background-color: rgb(128, 128, 128); /* Similar to the selected tab color */\n\n}\n")
              self.previousBindingButton = self.currentBindingButton
              QMetaObject.invokeMethod(self.parent, "setStyleSheet_to_normal_safe", Qt.QueuedConnection)
        else:
          for event in events:
              self.process_event(event)
      else:
        time.sleep(1)

  def keyboard_event_handler(self, stopped, q):
    print("Inside keyboard_event_handler thread")
    self.shouldRunKeyboardManager = True
    while self.shouldRunKeyboardManager:
      events = get_key()
      if events:
        for event in events:
          print(event.ev_type, event.code, event.state)

  def startJoystickManager(self):
    print("Starting Joystick manager")
    # Starts a thread for handling joystic/controller input
    self.joystic_event_stopped = threading.Event()
    self.joystic_event_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
    self.joystic_event_t = threading.Thread(target=self.joystic_event_handler, args=(self.joystic_event_stopped, self.joystic_event_q))
    self.joystic_event_t.start()

    #Starts another thread for keyboard input (a helper for interrupting or removing a bind)
    """if self.keyboard != None:
      self.keyboard_event_stopped = threading.Event()
      self.keyboard_event_q = queue.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK_SIZE)))
      self.keyboard_event_t = threading.Thread(target=self.keyboard_event_handler, args=(self.keyboard_event_stopped, self.keyboard_event_q))
      self.keyboard_event_t.start()
    else:
      print("No keyboard found... Some features will not be available.")"""

  def stopJoystickAndKeyboardManager(self):
    self.shouldRunJoystickManager = False
    self.shouldRunKeyboardManager = False
    if self.currentJoystickObject != None:
      self.free_current_joystick()
    #self.shouldRunJoystickManager = False
    print("Shutting down Joystick manager")
