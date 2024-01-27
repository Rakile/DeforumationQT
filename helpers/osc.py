"""Small example OSC server

This program listens to several addresses, and prints some information about
received packets.
"""
import argparse
import math

from PySide6.QtCore import Slot, QMetaObject, Q_ARG
from PySide6.QtGui import Qt
from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server

class Deforumation_OSC():
  def __init__(self, osc_port=5005, deforumation_settings=None, parent=None):
    if deforumation_settings != None:
      self.deforumation_settings = deforumation_settings
    else:
      pass
    self.parent = parent
    self.ip="127.0.0.1"
    self.port = int(osc_port)
    self.server = None
    self.dispatcher = Dispatcher()
    self.previous_zoom_value = 0
    self.previous_zoom_forward_value = 0
    self.previous_zoom_backward_value = 0
    self.previous_pan_x_value = 0
    self.previous_pan_y_value = 0
    self.previous_rot_x_value = 0
    self.previous_rot_y_value = 0
    self.previous_tilt_value = 0
    self.previous_tilt_left_value = 0
    self.previous_tilt_right_value = 0
    self.previous_sampler_steps = 30
    #dispatcher.map("", print)


  def startServer(self):
    self.dispatcher.map("/Zoom", self.zoom_handler, "Zoom")
    self.dispatcher.map("/Zoom_Forwards", self.zoom_forwards_handler, "Zoom")
    self.dispatcher.map("/Zoom_Backwards", self.zoom_backwards_handler, "Zoom")
    self.dispatcher.map("/Tilt", self.tilt_handler, "Tilt")
    self.dispatcher.map("/Tilt_Left", self.tilt_left_handler, "Tilt")
    self.dispatcher.map("/Tilt_Right", self.tilt_right_handler, "Tilt")
    self.dispatcher.map("/Pan_X", self.pan_x_handler, "Pan_X")
    self.dispatcher.map("/Pan_Y", self.pan_y_handler, "Pan_Y")
    self.dispatcher.map("/Rot_V", self.rot_v_handler, "Rot_V")
    self.dispatcher.map("/Rot_H", self.rot_h_handler, "Rot_H")

    #Live Parameters
    self.dispatcher.map("/Sampler_Steps", self.live_param_handler, "Sampler_Steps")
    self.dispatcher.map("/CFG_Scale", self.live_param_handler, "CFG_Scale")
    self.dispatcher.map("/Strength", self.live_param_handler, "Strength")
    self.dispatcher.map("/Cadence", self.live_param_handler, "Cadence")
    self.dispatcher.map("/Noise_Multiplier", self.live_param_handler, "Noise_Multiplier")

    self.server = osc_server.ThreadingOSCUDPServer((self.ip, self.port), self.dispatcher)
    print("Starting DeforumationQT OSC server on {}".format(self.server.server_address))
    self.server.serve_forever()

  def stopServer(self):
    if not self.server == None:
      print("Shutting down OSC server")
      self.server.shutdown()
      print("OSC server shut down")

  def live_param_handler(self, unused_addr, args, value):
    QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))


  def tilt_handler(self, unused_addr, args, value):
    if self.previous_tilt_value != value:
      self.previous_tilt_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def tilt_left_handler(self, unused_addr, args, value):
    if self.previous_tilt_left_value != value:
      self.previous_tilt_left_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def tilt_right_handler(self, unused_addr, args, value):
    value = -value
    if self.previous_tilt_right_value != value:
      self.previous_tilt_right_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def zoom_handler(self, unused_addr, args, value):
    if self.previous_zoom_value != value:
      self.previous_zoom_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def zoom_forwards_handler(self, unused_addr, args, value):
    if self.previous_zoom_forward_value != value:
      self.previous_zoom_forward_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def zoom_backwards_handler(self, unused_addr, args, value):
    value = -value
    if self.previous_zoom_backward_value != value:
      self.previous_zoom_backward_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def pan_x_handler(self, unused_addr, args, value):
    if self.previous_pan_x_value != value:
      self.previous_pan_x_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def pan_y_handler(self, unused_addr, args, value):
    if self.previous_pan_y_value != value:
      self.previous_pan_y_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def rot_v_handler(self, unused_addr, args, value):
    if self.previous_rot_x_value != value:
      self.previous_rot_x_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

  def rot_h_handler(self, unused_addr, args, value):
    if self.previous_rot_y_value != value:
      self.previous_rot_y_value = value
      QMetaObject.invokeMethod(self.parent, "handler", Qt.QueuedConnection, Q_ARG("QVariantList", args), Q_ARG("QString", str(value)))

    #self.parent.ui.motion_zoom_slider.setValue(int(zoom*100))


  """if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip",
        default="127.0.0.1", help="The ip to listen on")
    parser.add_argument("--port",
        type=int, default=5005, help="The port to listen on")
    args = parser.parse_args()

    dispatcher = Dispatcher()
    #dispatcher.map("", print)
    dispatcher.map("/Zoom", print_zoom_handler, "Zoom")
    dispatcher.map("/Value0", print_zoom_handler, "Zoom")
    dispatcher.map("/v1", print)
    dispatcher.map("/volume", print_volume_handler, "Volume")
    dispatcher.map("/logvolume", print_compute_handler, "Log volume", math.log)

    server = osc_server.ThreadingOSCUDPServer(
        (args.ip, args.port), dispatcher)
    print("Serving on {}".format(server.server_address))
    server.serve_forever()"""