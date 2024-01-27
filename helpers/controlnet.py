import pickle


class Deforumation_ControlNet():
  def __init__(self, deforumation_settings=None, parent=None, named_pipes=None, deforumation_tools=None):
    self.deforumation_settings = deforumation_settings
    self.parent = parent
    self.deforumationnamedpipes = named_pipes
    self.deforumation_tools = deforumation_tools

    self.control_net_weight_slider = {}
    self.control_net_weight_slider_Text = {}
    self.control_net_stepstart_slider = {}
    self.control_net_stepstart_slider_Text = {}
    self.control_net_stepend_slider = {}
    self.control_net_stepend_slider_Text = {}
    self.control_net_lowt_slider = {}
    self.control_net_lowt_slider_Text = {}
    self.control_net_hight_slider = {}
    self.control_net_hight_slider_Text = {}
    self.control_net_active_checkbox = {}
    self.cn_udcn1 = self.deforumation_settings.getSendConfigValue("cn_udcn1")
    self.cn_udcn2 = self.deforumation_settings.getSendConfigValue("cn_udcn2")
    self.cn_udcn3 = self.deforumation_settings.getSendConfigValue("cn_udcn3")
    self.cn_udcn4 = self.deforumation_settings.getSendConfigValue("cn_udcn4")
    self.cn_udcn5 = self.deforumation_settings.getSendConfigValue("cn_udcn5")
    if self.cn_udcn1:
      self.parent.ui.cn_udcn1.setChecked(True)
    if self.cn_udcn2:
      self.parent.ui.cn_udcn2.setChecked(True)
    if self.cn_udcn3:
      self.parent.ui.cn_udcn3.setChecked(True)
    if self.cn_udcn4:
      self.parent.ui.cn_udcn4.setChecked(True)
    if self.cn_udcn5:
      self.parent.ui.cn_udcn5.setChecked(True)

  def slider_changed(self, sender):
    cnIndex = sender.objectName()[3]
    if "weight_slider" in sender.objectName():
      #print("cnIndex:"+str(cnIndex))
      #print("Weightslider moved:" + str(sender.objectName()) + " --- " + str(sender.value()))
      self.control_net_weight_slider["cn_weight"+str(cnIndex)] = float(sender.value() * 0.01)
      CnLabel = "CN_" + str(cnIndex) + "_weight_slider_value"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setText(str(self.control_net_weight_slider["cn_weight"+str(cnIndex)]))
      self.deforumationnamedpipes.writeValue("cn_weight"+str(cnIndex), self.control_net_weight_slider["cn_weight"+str(cnIndex)])
      #print(str(self.control_net_weight_slider))
    elif "starting_control_step_slider" in sender.objectName():
      self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)] = float(sender.value() * 0.01)
      CnLabel = "CN_" + str(cnIndex) + "_starting_control_step_slider_value"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setText(str(self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)]))
      self.deforumationnamedpipes.writeValue("cn_stepstart" + str(cnIndex), self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)])
      #print(str(self.control_net_stepstart_slider))
    elif "ending_control_step_slider" in sender.objectName():
      self.control_net_stepend_slider["cn_stepend" + str(cnIndex)] = float(sender.value() * 0.01)
      CnLabel = "CN_" + str(cnIndex) + "_ending_control_step_slider_value"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setText(str(self.control_net_stepend_slider["cn_stepend" + str(cnIndex)]))
      self.deforumationnamedpipes.writeValue("cn_stepend" + str(cnIndex), self.control_net_stepend_slider["cn_stepend" + str(cnIndex)])
      #print(str(self.control_net_stepend_slider))
    elif "low_threshold_slider" in sender.objectName():
      self.control_net_lowt_slider["cn_lowt" + str(cnIndex)] = int(sender.value())
      CnLabel = "CN_" + str(cnIndex) + "_low_threshold_slider_value"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setText(str(self.control_net_lowt_slider["cn_lowt" + str(cnIndex)]))
      self.deforumationnamedpipes.writeValue("cn_lowt" + str(cnIndex), self.control_net_lowt_slider["cn_lowt" + str(cnIndex)])
      #print(str(self.control_net_lowt_slider))
    elif "high_threshold_slider" in sender.objectName():
      self.control_net_hight_slider["cn_hight" + str(cnIndex)] = int(sender.value())
      CnLabel = "CN_" + str(cnIndex) + "_high_threshold_slider_value"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setText(str(self.control_net_hight_slider["cn_hight" + str(cnIndex)]))
      self.deforumationnamedpipes.writeValue("cn_hight" + str(cnIndex), self.control_net_hight_slider["cn_hight" + str(cnIndex)])
      #print(str(self.control_net_hight_slider))
    else:
      pass

  def setComponetValues(self):
    self.getCNvaluesFromConfig(self.parent.ui.cn_udcn1)
    self.getCNvaluesFromConfig(self.parent.ui.cn_udcn2)
    self.getCNvaluesFromConfig(self.parent.ui.cn_udcn3)
    self.getCNvaluesFromConfig(self.parent.ui.cn_udcn4)
    self.getCNvaluesFromConfig(self.parent.ui.cn_udcn5)

  def getCNvaluesFromConfig(self, check_box_object):
    cnIndex = check_box_object.objectName()[7]
    sendConfig = self.deforumation_settings.getSendConfig()
    if "cn_weight" + str(cnIndex) in sendConfig:
      self.control_net_weight_slider["cn_weight" + str(cnIndex)] = float(sendConfig["cn_weight" + str(cnIndex)])
      CnLabel = "CN_" + str(cnIndex) + "_weight_slider"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setValue(int(self.control_net_weight_slider["cn_weight" + str(cnIndex)] * 100))
    if "cn_stepstart" + str(cnIndex) in sendConfig:
      self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)] = float(sendConfig["cn_stepstart" + str(cnIndex)])
      CnLabel = "CN_" + str(cnIndex) + "_starting_control_step_slider"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setValue(int(self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)] * 100))
    if "cn_stepend" + str(cnIndex) in sendConfig:
      self.control_net_stepend_slider["cn_stepend" + str(cnIndex)] = float(sendConfig["cn_stepend" + str(cnIndex)])
      CnLabel = "CN_" + str(cnIndex) + "_ending_control_step_slider"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setValue(int(self.control_net_stepend_slider["cn_stepend" + str(cnIndex)] * 100))
    if "cn_lowt" + str(cnIndex) in sendConfig:
      self.control_net_lowt_slider["cn_lowt" + str(cnIndex)] = int(sendConfig["cn_lowt" + str(cnIndex)])
      CnLabel = "CN_" + str(cnIndex) + "_low_threshold_slider"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setValue(int(self.control_net_lowt_slider["cn_lowt" + str(cnIndex)]))
    if "cn_hight" + str(cnIndex) in sendConfig:
      self.control_net_hight_slider["cn_hight" + str(cnIndex)] = int(sendConfig["cn_hight" + str(cnIndex)])
      CnLabel = "CN_" + str(cnIndex) + "_high_threshold_slider"
      obj = self.deforumation_tools.getWidgetFromContainer(CnLabel)
      obj.setValue(int(self.control_net_hight_slider["cn_hight" + str(cnIndex)]))
    if getattr(self, "cn_udcn"+str(cnIndex)) == 1:
      SendBlock = []
      SendBlock.append(pickle.dumps([1, "cn_udcn"+str(cnIndex), 1]))
      SendBlock.append(pickle.dumps([1, "cn_weight" + str(cnIndex), self.control_net_weight_slider["cn_weight" + str(cnIndex)]]))
      SendBlock.append(pickle.dumps([1, "cn_stepstart" + str(cnIndex), self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)]]))
      SendBlock.append(pickle.dumps([1, "cn_stepend" + str(cnIndex), self.control_net_stepend_slider["cn_stepend" + str(cnIndex)]]))
      SendBlock.append(pickle.dumps([1, "cn_lowt" + str(cnIndex), self.control_net_lowt_slider["cn_lowt" + str(cnIndex)]]))
      SendBlock.append(pickle.dumps([1, "cn_hight" + str(cnIndex), self.control_net_hight_slider["cn_hight" + str(cnIndex)]]))
      self.deforumationnamedpipes.writeValue("<BLOCK>", SendBlock)
    else:
      self.deforumationnamedpipes.writeValue("cn_udcn" + str(cnIndex), 0)
    return self.deforumation_settings.getSendConfigValue(check_box_object.objectName())
  def switchCNcheckbox(self, check_box_object, onOff):
    # self.p = self.deforumation_settings.getSendConfig()
    try:
        #setattr(self, check_box_object.objectName(), onOff)
        # self.p[mediator_communication_string] = new_value
      self.deforumation_settings.writeDeforumSendValuesToConfig(check_box_object.objectName(), int(onOff))
      cnIndex = check_box_object.objectName()[7]
      if onOff:
        SendBlock = []
        SendBlock.append(pickle.dumps([1, check_box_object.objectName(), 1]))
        if not "cn_weight"+str(cnIndex) in self.control_net_weight_slider:
          self.control_net_weight_slider["cn_weight" + str(cnIndex)] = 1.0
        SendBlock.append(pickle.dumps([1, "cn_weight" + str(cnIndex), self.control_net_weight_slider["cn_weight"+str(cnIndex)]]))

        if not "cn_stepstart"+str(cnIndex) in self.control_net_stepstart_slider:
          self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)] = 0.0
        SendBlock.append(pickle.dumps([1, "cn_stepstart" + str(cnIndex), self.control_net_stepstart_slider["cn_stepstart" + str(cnIndex)]]))

        if not "cn_stepend"+str(cnIndex) in self.control_net_stepend_slider:
          self.control_net_stepend_slider["cn_stepend" + str(cnIndex)] = 1.0
        SendBlock.append(pickle.dumps([1, "cn_stepend" + str(cnIndex), self.control_net_stepend_slider["cn_stepend" + str(cnIndex)]]))

        if not "cn_lowt"+str(cnIndex) in self.control_net_lowt_slider:
          self.control_net_lowt_slider["cn_lowt" + str(cnIndex)] = 100
        SendBlock.append(pickle.dumps([1, "cn_lowt" + str(cnIndex), self.control_net_lowt_slider["cn_lowt" + str(cnIndex)]]))

        if not "cn_hight"+str(cnIndex) in self.control_net_hight_slider:
          self.control_net_hight_slider["cn_hight" + str(cnIndex)] = 200
        SendBlock.append(pickle.dumps([1, "cn_hight" + str(cnIndex), self.control_net_hight_slider["cn_hight" + str(cnIndex)]]))
        self.deforumationnamedpipes.writeValue("<BLOCK>", SendBlock)
      else:
        self.deforumationnamedpipes.writeValue(check_box_object.objectName(), 0)
      # Communicate values to the mediator, if neccessary
      """if mediator_values_to_write != None:
        for parameter_name in mediator_values_to_write:
          parameter_value = mediator_values_to_write[parameter_name]
          self.deforumationnamedpipes.writeValue(parameter_name, parameter_value)"""

      """if should_set_checkbox_state:
        check_box_object.setChecked(getattr(self, mediator_communication_string))
      self.deforumation_tools.propagateAllCheckboxes(check_box_object)"""
    except Exception as e:
      if self.parent.is_verbose:
        print("(setShouldUseDeforumationParameter), has not yet a value (" + str(check_box_object.objectName()) + "), in config, and don't know if checkbox should be checked or not.")