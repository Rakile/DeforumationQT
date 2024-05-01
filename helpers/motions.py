import pickle

from PySide6.QtCore import (Qt, Slot, QMetaObject, Q_ARG)
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtWidgets import QSlider, QCheckBox, QLineEdit, QLabel, QProgressBar
from pyeaze import pyeaze

"""from helpers.named_pipes import Deforumation_Named_Pipes
from helpers.config import Deforumation_Settings"""

class Deforumation_Motions():

    def __init__(self, parent=None, ui=None, deforumation_settings=None, deforumationwidgets=None, named_pipes=None):
        #super().__init__(parent)
        self.deforumation_settings = deforumation_settings
        self.deforumationwidgets = deforumationwidgets
        self.Translation_X = 0
        self.Translation_Y = 0
        self.Translation_RX = 0
        self.Translation_RY = 0
        self.Translation_RZ = 0
        self.Translation_Z = 0
        self.Zoom_Max = 100.0
        self.Zoom_Min = 100.0
        self.Translation_X_EXPONENTIAL = 0
        self.Translation_Y_EXPONENTIAL = 0
        self.Translation_RX_EXPONENTIAL = 0
        self.Translation_RY_EXPONENTIAL = 0
        self.Translation_RZ_EXPONENTIAL = 0
        self.Translation_Z_EXPONENTIAL = 0
        self.fov = 70
        self.steps = 50
        self.strength = 0.68
        self.cfg = 3
        self.cfg_float = 3.0
        self.cadence = 3
        self.Syrup_Panning_Motion = 0
        self.Syrup_Rotation_Motion = 0
        self.Syrup_Zooming_Motion = 0
        self.Syrup_Tilt_Motion = 0
        self.Motion_Pan_Granularity = 0.2
        self.Motion_Rotate_Granularity = 0.2
        self.Motion_Zoom_Granularity = 0.2
        self.Motion_Zoom_Granularity_Special = 0.2
        self.Motion_Tilt_Granularity = 0.2
        self.noise_multiplier = 1.05
        self.exponential_pan_motion = False
        self.exponential_rotate_motion = False
        self.exponential_tilt_motion = False
        #self.Exponential_Zoom_Motion = False
        self.parent = parent
        self.ui = ui
        self.deforumationnamedpipes = named_pipes
        self.ui.motion_pan_granularity.setText(str('%.2f' % self.Motion_Pan_Granularity))
        self.ui.motion_rotate_granularity.setText(str('%.2f' % self.Motion_Rotate_Granularity))
        self.ui.motion_zoom_granularity_special.setText(str('%.2f' % self.Motion_Zoom_Granularity_Special))
        self.ui.motion_tilt_granularity.setText(str('%.2f' % self.Motion_Tilt_Granularity))
        self.ui.pan_x_value.setText(str('%.2f' % self.Translation_X))
        self.ui.pan_y_value.setText(str('%.2f' % self.Translation_Y))
        self.ui.rotate_x_value.setText(str('%.2f' % self.Translation_RY))
        self.ui.rotate_y_value.setText(str('%.2f' % self.Translation_RX))
        self.ui.rotate_z_value.setText(str('%.2f' % self.Translation_RZ))
        self.should_use_deforumation_panning = 1
        self.should_use_deforumation_zoomfov = 1
        self.should_use_deforumation_rotation = 1
        self.should_use_deforumation_tilt = 1
        self.should_use_deforumation_zoom = 1
        self.should_use_deforumation_fov = 1
        self.should_use_deforumation_game_mode = False
        self.should_stay_on_top = False
        self.ui.panx_l.setPixmap(QPixmap(u"images/value_declining_on.png"))
        self.is_verbose = False

    def askMediatorIfDeforumationShouldBeInCharge(self, parameter_judge_question):
        return self.deforumationnamedpipes.readValue(parameter_judge_question)
    def setParameterAccordingToCircumstances(self, parameter, parameter_judge_question):
        #First let's see if our own config says anything about who should be in charge
        default_config_value_exists = False
        default_config = self.deforumation_settings.getSendConfig()
        if parameter_judge_question in default_config:
            config_says_deforumation_parameter_should_be_used = default_config[parameter_judge_question]
            default_config_value_exists = True
        else:
            config_says_deforumation_parameter_should_be_used = False #Nothing was specified about it in config, so we say NO

        #Now let's see what the mediator has to say about who should be in charge
        mediator_says_deforumation_parameter_should_be_used = self.askMediatorIfDeforumationShouldBeInCharge(parameter_judge_question)

        #Let our our config have more say in the dispute
        if default_config_value_exists:
            return config_says_deforumation_parameter_should_be_used
    def haltAllSyrupMotions(self):
        SendBlock = []
        SendBlock.append(pickle.dumps([1, "start_zero_pan_motion_x", -2]))
        SendBlock.append(pickle.dumps([1, "start_zero_pan_motion_y", -2]))
        SendBlock.append(pickle.dumps([1, "start_zero_pan_motion_z", -2]))
        SendBlock.append(pickle.dumps([1, "start_zero_rotate_motion_x", -2]))
        SendBlock.append(pickle.dumps([1, "start_zero_rotate_motion_y", -2]))
        SendBlock.append(pickle.dumps([1, "start_zero_rotate_motion_z", -2]))
        self.deforumationnamedpipes.writeValue("<BLOCK>", SendBlock)

    def setComponetValuesThroughTotalRecall(self, totalRecallFrame):
        try:
            if totalRecallFrame != 0:
                # Set all values
                self.steps = totalRecallFrame.steps
                self.strength = totalRecallFrame.strength_value
                self.cfg_float = totalRecallFrame.cfg_scale #self.deforumation_settings.getSendConfigValue("cfg")
                self.cfg = self.cfg_float * 10
                #self.cfg = totalRecallFrame.cfg_scale
                self.cadence = totalRecallFrame.cadence
                self.noise_multiplier = totalRecallFrame.noise_multiplier
                self.fov = totalRecallFrame.fov
                self.Translation_X = totalRecallFrame.translation_x
                self.Translation_Y = totalRecallFrame.translation_y
                self.Translation_Z = totalRecallFrame.translation_z
                self.Translation_RX = totalRecallFrame.rotation_x
                self.Translation_RY = totalRecallFrame.rotation_y
                self.Translation_RZ = totalRecallFrame.rotation_z
                SendBlock = []
                SendBlock.append(pickle.dumps([1, "translation_x", self.Translation_X]))
                SendBlock.append(pickle.dumps([1, "translation_y", self.Translation_Y]))
                SendBlock.append(pickle.dumps([1, "translation_z", self.Translation_Z]))
                SendBlock.append(pickle.dumps([1, "rotation_x", self.Translation_RX]))
                SendBlock.append(pickle.dumps([1, "rotation_y", self.Translation_RY]))
                SendBlock.append(pickle.dumps([1, "rotation_z", self.Translation_RZ]))
                SendBlock.append(pickle.dumps([1, "deforum_translation_x", self.Translation_X]))
                SendBlock.append(pickle.dumps([1, "deforum_translation_y", self.Translation_Y]))
                SendBlock.append(pickle.dumps([1, "deforum_translation_z", self.Translation_Z]))
                SendBlock.append(pickle.dumps([1, "deforum_rotation_x", self.Translation_RX]))
                SendBlock.append(pickle.dumps([1, "deforum_rotation_y", self.Translation_RY]))
                SendBlock.append(pickle.dumps([1, "deforum_rotation_z", self.Translation_RZ]))
                self.deforumationnamedpipes.writeValue("<BLOCK>", SendBlock)
                self.Translation_X_EXPONENTIAL = self.Translation_X
                self.Translation_Y_EXPONENTIAL = self.Translation_Y
                self.Translation_RX_EXPONENTIAL = self.Translation_RX
                self.Translation_RY_EXPONENTIAL = self.Translation_RY
                self.Translation_RZ_EXPONENTIAL = self.Translation_RZ
                self.Translation_Z_EXPONENTIAL = self.Translation_Z


                # Adjust component sliders
                self.ui.step_slider.setValue(self.steps)
                self.ui.strength_slider.setValue(int(self.strength * 100))
                self.ui.cfg_slider.setValue(self.cfg)
                self.ui.cadence_slider.setValue(int(self.cadence))
                self.ui.noise_slider.setValue(int(self.noise_multiplier * 100))
                self.ui.motion_zoom_slider.setValue(int(self.Translation_Z * 100))
                self.ui.motion_fov_slider.setValue(int(self.fov))


                # Set Component label values
                self.ui.step_slider_value.setText(str(self.steps))
                self.ui.strength_slider_value.setText(str(float('%.2f' % self.strength)))
                #self.cfg_float = round((self.cfg / 10 - 0.1) + 1,1)
                self.ui.cfg_slider_value.setText(str(self.cfg_float))
                #self.ui.cfg_slider_value.setText(str(self.cfg))
                self.ui.cadence_slider_value.setText(str(self.cadence))
                self.ui.noise_slider_value.setText(str(float('%.2f' % self.noise_multiplier)))
                self.ui.pan_x_value.setText(str(float('%.2f' % self.Translation_X)))
                self.ui.pan_y_value.setText(str(float('%.2f' % self.Translation_Y)))
                self.ui.pan_z_value.setText(str(float('%.2f' % self.Translation_Z)))
                self.ui.fov_value.setText(str(int(self.fov)))
                self.ui.rotate_x_value.setText(str(float('%.2f' % self.Translation_RY)))
                self.ui.rotate_y_value.setText(str(float('%.2f' % self.Translation_RX)))
                self.ui.rotate_z_value.setText(str(float('%.2f' % self.Translation_RZ)))

                # Special for handling total recall seed value
                seed_value = totalRecallFrame.seed_value
                if str(seed_value) == "None":
                    seed_value = -1
                self.parent.ui.IterSeed_Inputbox.setText(str(seed_value))
                self.parent.ui.fixedSeed_Inputbox.setText(str(seed_value))
                self.deforumationnamedpipes.writeValue("seed", seed_value)
                self.deforumationnamedpipes.writeValue("seed_changed", 1)
                #seed_iter_n = int(self.parent.ui.IterSeed_N_Inputbox.text())
                #self.deforumationnamedpipes.writeValue("seed_iter_n", seed_iter_n)


            else:
                if self.is_verbose:
                    print("No ongoing rendering, so can't populate component values")
        except Exception as e:
            if self.is_verbose:
                print("Error when trying to populate component values:" + str(e))

        #print("Looking at current frame")
    def setComponetValues(self, totalRecallFrame):
        #try:

        #if totalRecallFrame != 0:
        self.config = self.deforumation_settings.getSendConfig()
        #Set all values
        """self.steps = totalRecallFrame.steps
        self.strength = totalRecallFrame.strength_value
        self.cfg = totalRecallFrame.cfg_scale
        self.setParameterAccordingToCircumstances("cadence", "should_use_deforumation_cadence")
        self.cadence = totalRecallFrame.cadence
        self.noise_multiplier = totalRecallFrame.noise_multiplier
        self.fov = totalRecallFrame.fov
        self.Translation_X = totalRecallFrame.translation_x
        self.Translation_Y = totalRecallFrame.translation_y
        self.Translation_Z = totalRecallFrame.translation_z
        self.Translation_RX = totalRecallFrame.rotation_x
        self.Translation_RY = totalRecallFrame.rotation_y
        self.Translation_RZ = totalRecallFrame.rotation_z"""
        #Set values from config

        self.steps = self.deforumation_settings.getSendConfigValue("steps")
        self.strength = self.deforumation_settings.getSendConfigValue("strength")
        self.cfg_float = self.deforumation_settings.getSendConfigValue("cfg")
        self.cfg = self.cfg_float * 10
        #self.setParameterAccordingToCircumstances("cadence", "should_use_deforumation_cadence")
        self.cadence = self.deforumation_settings.getSendConfigValue("cadence")
        self.noise_multiplier = self.deforumation_settings.getSendConfigValue("noise_multiplier")
        self.fov = self.deforumation_settings.getSendConfigValue("fov")
        self.Translation_X = self.deforumation_settings.getSendConfigValue("translation_x")
        self.Translation_X_EXPONENTIAL = self.Translation_X
        self.Translation_Y = self.deforumation_settings.getSendConfigValue("translation_y")
        self.Translation_Y_EXPONENTIAL = self.Translation_Y
        self.Translation_Z = self.deforumation_settings.getSendConfigValue("translation_z")
        self.Translation_Z_EXPONENTIAL = self.Translation_Z
        self.Translation_RX = self.deforumation_settings.getSendConfigValue("rotation_x")
        self.Translation_RX_EXPONENTIAL = self.Translation_RX
        self.Translation_RY = self.deforumation_settings.getSendConfigValue("rotation_y")
        self.Translation_RY_EXPONENTIAL = self.Translation_RY
        self.Translation_RZ = self.deforumation_settings.getSendConfigValue("rotation_z")
        self.Translation_RZ_EXPONENTIAL = self.Translation_RZ
        self.Syrup_Panning_Motion = self.deforumation_settings.getGuiConfigValue("Syrupmotion_Panning")# getGuiConfig()["Syrupmotion_Panning"]
        self.Syrup_Panning_Motion = self.deforumation_settings.getGuiConfigValue("Syrupmotion_Panning")
        self.Syrup_Zooming_Motion = self.deforumation_settings.getGuiConfigValue("Syrupmotion_Zoom")
        self.Syrup_Rotation_Motion = self.deforumation_settings.getGuiConfigValue("Syrupmotion_Rotation")
        self.Syrup_Tilt_Motion = self.deforumation_settings.getGuiConfigValue("Syrupmotion_Tilt")
        self.Pan_Granularity = self.deforumation_settings.getGuiConfigValue("Pan_Granularity")
        self.should_use_deforumation_steps = True #self.config["should_use_deforumation_steps"] #Steps should always be controlled from Deforumation
        self.should_use_deforumation_strength = self.deforumation_settings.getSendConfigValue("should_use_deforumation_strength")
        self.should_use_deforumation_cfg = self.deforumation_settings.getSendConfigValue("should_use_deforumation_cfg")
        self.should_use_deforumation_cadence = self.deforumation_settings.getSendConfigValue("should_use_deforumation_cadence")
        self.should_use_deforumation_noise = self.deforumation_settings.getSendConfigValue("should_use_deforumation_noise")
        self.should_use_deforumation_noise = self.deforumation_settings.getSendConfigValue("should_use_deforumation_noise")
        self.should_use_deforumation_panning = self.deforumation_settings.getSendConfigValue("should_use_deforumation_panning")
        self.should_use_deforumation_rotation = self.deforumation_settings.getSendConfigValue("should_use_deforumation_rotation")
        self.should_use_deforumation_zoom = self.deforumation_settings.getSendConfigValue("should_use_deforumation_zoom")
        self.should_use_deforumation_fov = self.deforumation_settings.getSendConfigValue("should_use_deforumation_fov")
        self.should_use_deforumation_tilt = self.deforumation_settings.getSendConfigValue("should_use_deforumation_tilt")
        self.should_use_deforumation_game_mode = self.deforumation_settings.getGuiConfigValue("should_use_deforumation_game_mode")
        self.Rotation_Granularity = self.deforumation_settings.getGuiConfigValue("Rotation_Granularity")
        self.Tilt_Granularity = self.deforumation_settings.getGuiConfigValue("Tilt_Granularity")
        self.Zoom_Granularity_Special = self.deforumation_settings.getGuiConfigValue("Zoom_Granularity_Special")
        if self.Zoom_Granularity_Special == None:
            self.Zoom_Granularity_Special = 0.1
        self.exponential_pan_motion = self.deforumation_settings.getGuiConfigValue("exponential_pan_motion")
        self.exponential_rotate_motion = self.deforumation_settings.getGuiConfigValue("exponential_rotate_motion")
        self.exponential_tilt_motion = self.deforumation_settings.getGuiConfigValue("exponential_tilt_motion")
        self.should_stay_on_top = self.deforumation_settings.getGuiConfigValue("should_stay_on_top")
        #Special handling of seed stuff
        self.seed = self.deforumation_settings.getSendConfigValue("seed")
        if self.seed == None:
            self.seed = -1
        self.seed_fixed = self.deforumation_settings.getGuiConfigValue("seed_fixed")
        self.seed_iter_n = self.deforumation_settings.getSendConfigValue("seed_iter_n")
        if self.seed_iter_n == None:
            self.seed_iter_n = 1
        if self.seed_fixed == None:
            self.seed_fixed = 0
        if self.seed_iter_n <=0:
                self.seed_iter_n = 1
        self.parent.ui.IterSeed_N_Inputbox.setText(str(self.seed_iter_n))
        self.parent.ui.IterSeed_Inputbox.setText(str(self.seed))
        self.parent.ui.fixedSeed_Inputbox.setText(str(self.seed_fixed))
        self.seed_behavior = self.deforumation_settings.getSendConfigValue("seed_behavior")
        if str(self.seed_behavior) == "0":
            if self.is_verbose:
                print("No render active so using seed_behaviour from saved GUI-state")
            self.seed_behavior = self.deforumation_settings.getGuiConfigValue("seed_radio_button_checked")
        else:
            if self.is_verbose:
                print("Render active so using seed_behaviour from active render send-state")

        if str(self.seed_behavior) != "-1" and str(self.seed_behavior) != "0":
            if self.seed_behavior ==  "iter":
                self.parent.ui.iter_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("iter_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "iter")
                self.deforumationnamedpipes.writeValue("seed_behavior", "iter")
            elif self.seed_behavior == "fixed":
                self.parent.ui.fixed_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("fixed_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "fixed")
                self.deforumationnamedpipes.writeValue("seed_behavior", "fixed")
            elif self.seed_behavior == "random":
                self.parent.ui.random_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("random_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "random")
                self.deforumationnamedpipes.writeValue("seed_behavior", "random")
            elif self.seed_behavior == "ladder":
                self.parent.ui.ladder_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("ladder_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "ladder")
                self.deforumationnamedpipes.writeValue("seed_behavior", "ladder")
            elif self.seed_behavior == "alternate":
                self.parent.ui.alternate_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("alternate_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "alternate")
                self.deforumationnamedpipes.writeValue("seed_behavior", "alternate")
            elif self.seed_behavior == "schedule":
                self.parent.ui.scheduled_RadioButton.setChecked(True)
                if self.is_verbose:
                    print("scheduled_RadioButton checked")
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "schedule")
                self.deforumationnamedpipes.writeValue("seed_behavior", "schedule")



        #Adjust checkboxes
        #self.setShouldUseDeforumationSteps(self.should_use_deforumation_steps)
        self.setShouldUseDeforumationStrength(self.should_use_deforumation_strength)
        self.setShouldUseDeforumationCFG(self.should_use_deforumation_cfg)
        self.setShouldUseDeforumationCadence(self.should_use_deforumation_cadence)
        self.setShouldUseDeforumationNoiseMultiplier(self.should_use_deforumation_noise)
        self.parent.ui.strength_active_checkbox.setChecked(self.should_use_deforumation_strength)
        self.parent.ui.cfg_active_checkbox.setChecked(self.should_use_deforumation_cfg)
        self.parent.ui.cadence_active_checkbox.setChecked(self.should_use_deforumation_cadence)
        self.parent.ui.noise_multiplier_active_checkbox.setChecked(self.should_use_deforumation_noise)
        self.deforumationnamedpipes.writeValue("translation_x", self.Translation_X)
        self.deforumationnamedpipes.writeValue("translation_y", self.Translation_Y)
        self.setShouldUseDeforumationParameter(self.ui.Motion_panning_checkbox, self.should_use_deforumation_panning, "should_use_deforumation_panning", True, True, {"translation_x": self.Translation_X, "translation_y": self.Translation_Y})
        self.setShouldUseDeforumationParameter(self.ui.Motion_rotation_checkbox, self.should_use_deforumation_rotation, "should_use_deforumation_rotation", True, True, {"rotation_x": self.Translation_RX, "rotation_y": self.Translation_RY})
        self.setShouldUseDeforumationParameter(self.ui.Motion_zoom_checkbox, self.should_use_deforumation_zoom, "should_use_deforumation_zoom", True, True, {"translation_z": self.Translation_Z})
        self.setShouldUseDeforumationParameter(self.ui.Motion_fow_checkbox, self.should_use_deforumation_fov, "should_use_deforumation_fov", True, True, {"fov": self.fov})
        self.setShouldUseDeforumationParameter(self.ui.Motion_tilt_checkbox, self.should_use_deforumation_tilt, "should_use_deforumation_tilt", True, True, {"rotation_z": self.Translation_RZ})
        self.setShouldUseDeforumationParameter(self.ui.stay_on_top_checkbox, self.should_stay_on_top, "should_stay_on_top", True)

        if self.should_use_deforumation_game_mode:
            self.ui.controller_mode_checkbox.setChecked(False)
        else:
            self.ui.controller_mode_checkbox.setChecked(True)
        #self.setShouldUseDeforumationParameter(self.ui.controller_mode_checkbox, not self.should_use_deforumation_game_mode, "should_use_deforumation_game_mode", True)

        #Set initial values depending on config
        if self.parent.deforumationVideoPlayerIsOnTop:
            self.parent.makeAllWindowsOnTop(True)
            """self.parent.deforumationPreviewWindowIsOnTop = True
            self.parent.deforumationDetachedTabsAreOnTop = True
            self.parent.deforumationVideoPlayerIsOnTop = True"""
        #Adjust component sliders
        self.ui.step_slider.setValue(self.steps)
        self.ui.strength_slider.setValue(int(self.strength*100))
        self.ui.cfg_slider.setValue(self.cfg)
        self.ui.cadence_slider.setValue(int(self.cadence))
        self.ui.noise_slider.setValue(int(self.noise_multiplier*100))

        """self.ui.step_slider.setValue(int(self.steps))
        self.ui.noise_slider.setValue(int(self.noise_multiplier*100))
        self.ui.noise_slider.setValue(int(self.noise_multiplier*100))
        self.ui.noise_slider.setValue(int(self.noise_multiplier*100))"""


        self.ui.motion_zoom_slider.setValue(int(self.Translation_Z*100))
        self.ui.motion_fov_slider.setValue(int(self.fov))

        #Set values from Config
        self.ui.syrup_pan_motion_slider.setValue(int(self.Syrup_Panning_Motion))
        self.ui.syrup_zoom_motion_slider.setValue(int(self.Syrup_Zooming_Motion))
        self.ui.syrup_rotate_motion_slider.setValue(int(self.Syrup_Rotation_Motion))
        self.ui.syrup_tilt_motion_slider.setValue(int(self.Syrup_Tilt_Motion))

        self.parent.ui.motion_pan_granularity.setText(str('%.2f' % self.Pan_Granularity))
        self.parent.ui.motion_rotate_granularity.setText(str('%.2f' % self.Rotation_Granularity))
        self.parent.ui.motion_zoom_granularity_special.setText(str('%.2f' % self.Zoom_Granularity_Special))
        self.parent.ui.motion_tilt_granularity.setText(str('%.2f' % self.Tilt_Granularity))
        if self.exponential_pan_motion:
            self.parent.ui.exponential_pan_motion.setChecked(True)
        else:
            self.parent.ui.exponential_pan_motion.setChecked(False)
        if self.exponential_rotate_motion:
            self.parent.ui.exponential_rotate_motion.setChecked(True)
        else:
            self.parent.ui.exponential_rotate_motion.setChecked(False)
        if self.exponential_tilt_motion:
            self.parent.ui.exponential_tilt_motion.setChecked(True)
        else:
            self.parent.ui.exponential_tilt_motion.setChecked(False)

        #Set Component label values
        self.ui.step_slider_value.setText(str(self.steps))
        self.ui.strength_slider_value.setText(str(float('%.2f' % self.strength)))
        #self.cfg_float = round((self.cfg / 10 - 0.1) + 1,1)
        self.ui.cfg_slider_value.setText(str(self.cfg_float))
        #self.ui.cfg_slider_value.setText(str(self.cfg))
        self.ui.cadence_slider_value.setText(str(self.cadence))
        self.ui.noise_slider_value.setText(str(float('%.2f' % self.noise_multiplier)))
        self.ui.pan_x_value.setText(str(float('%.2f' % self.Translation_X)))
        self.ui.pan_y_value.setText(str(float('%.2f' % self.Translation_Y)))
        self.ui.pan_z_value.setText(str(float('%.2f' % self.Translation_Z)))
        self.ui.fov_value.setText(str(int(self.fov)))
        self.ui.rotate_x_value.setText(str(float('%.2f' % self.Translation_RY)))
        self.ui.rotate_y_value.setText(str(float('%.2f' % self.Translation_RX)))
        self.ui.rotate_z_value.setText(str(float('%.2f' % self.Translation_RZ)))
        self.ui.syrup_pan_motion_slider_frame_number.setText(str(self.Syrup_Panning_Motion))
        self.ui.syrup_zoom_motion_slider_frame_number.setText(str(self.Syrup_Zooming_Motion))
        self.ui.syrup_rotate_motion_slider_frame_number.setText(str(self.Syrup_Rotation_Motion))
        self.ui.syrup_tilt_motion_slider_frame_number.setText(str(self.Syrup_Tilt_Motion))

        if self.should_stay_on_top:
            self.parent.makeAllWindowsOnTop(True)
        #else:
        #    print("No ongoing rendering, so can't populate component values")
        #except Exception as e:
        #    print("Error when trying to populate component values:" + str(e))


        #print("Looking at current frame")

    def adjustSyrupProgressBarPan(self, mediator_strings, progressbar_x, progressbar_y, progress_y, progress_x):
        numberOfPanXsyrupSteps = self.deforumationnamedpipes.readValue(mediator_strings[0])
        numberOfPanYsyrupSteps = self.deforumationnamedpipes.readValue(mediator_strings[1])
        currentStepX = numberOfPanXsyrupSteps[0]
        totalStepX = numberOfPanXsyrupSteps[1]
        currentStepY = numberOfPanYsyrupSteps[0]
        totalStepY = numberOfPanYsyrupSteps[1]
        progressX = int(100 / totalStepX * currentStepX)
        progressbar_x.setValue(progressX)
        self.propagateAllComponents(progressbar_x, progressX)
        progressY = int(100 / totalStepY * currentStepY)
        progressbar_y.setValue(progressY)
        self.propagateAllComponents(progressbar_y, progressY)
        self.Translation_X = float(self.deforumationnamedpipes.readValue("translation_x"))
        progress_y.setText(str('%.2f' % self.Translation_X))
        self.propagateAllComponents(progress_x, str('%.2f' % self.Translation_X))
        self.Translation_Y = float(self.deforumationnamedpipes.readValue("translation_y"))
        progress_x.setText(str('%.2f' % self.Translation_Y))
        self.propagateAllComponents(progress_y, str('%.2f' % self.Translation_Y))

    def adjustSyrupMotionProgressBarPan(self, values):
        numberOfPanXsyrupSteps = values[0] #self.deforumationnamedpipes.readValue("syrup_steps_pan_x")
        numberOfPanYsyrupSteps = values[1] #self.deforumationnamedpipes.readValue("syrup_steps_pan_y")
        currentStepX = numberOfPanXsyrupSteps[0]
        totalStepX = numberOfPanXsyrupSteps[1]
        currentStepY = numberOfPanYsyrupSteps[0]
        totalStepY = numberOfPanYsyrupSteps[1]
        progressX = int(100 / totalStepX * currentStepX)
        self.ui.motion_syrup_progressbar_x.setValue(progressX)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_x, progressX)
        progressY = int(100 / totalStepY * currentStepY)
        self.ui.motion_syrup_progressbar_y.setValue(progressY)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_y, progressY)
        self.Translation_X = float(values[2]) #float(self.deforumationnamedpipes.readValue("translation_x"))
        self.ui.pan_x_value_progress.setText(str('%.2f' % self.Translation_X))
        self.propagateAllComponents(self.ui.pan_x_value_progress, str('%.2f' % self.Translation_X))
        self.Translation_Y = float(values[3]) #float(self.deforumationnamedpipes.readValue("translation_y"))
        self.ui.pan_y_value_progress.setText(str('%.2f' % self.Translation_Y))
        self.propagateAllComponents(self.ui.pan_y_value_progress, str('%.2f' % self.Translation_Y))

    def adjustSyrupRotationProgressBarPan(self, values):
        numberOfRotateXsyrupSteps = values[0] #self.deforumationnamedpipes.readValue("syrup_steps_rotate_x")
        numberOfRotateYsyrupSteps = values[1] #self.deforumationnamedpipes.readValue("syrup_steps_rotate_y")
        currentStepX = numberOfRotateXsyrupSteps[0]
        totalStepX = numberOfRotateXsyrupSteps[1]
        currentStepY = numberOfRotateYsyrupSteps[0]
        totalStepY = numberOfRotateYsyrupSteps[1]
        progressX = int(100 / totalStepX * currentStepX)
        self.ui.motion_syrup_progressbar_rx.setValue(progressX)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_rx, progressX)
        progressY = int(100 / totalStepY * currentStepY)
        self.ui.motion_syrup_progressbar_ry.setValue(progressY)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_ry, progressY)
        self.Translation_RX = float(values[2]) #float(self.deforumationnamedpipes.readValue("rotation_x"))
        self.ui.rotate_y_value_progress.setText(str('%.2f' % self.Translation_RX))
        self.propagateAllComponents(self.ui.rotate_y_value_progress, str('%.2f' % self.Translation_RX))
        self.Translation_RY = float(values[3]) #float(self.deforumationnamedpipes.readValue("rotation_y"))
        self.ui.rotate_x_value_progress.setText(str('%.2f' % self.Translation_RY))
        self.propagateAllComponents(self.ui.rotate_x_value_progress, str('%.2f' % self.Translation_RY))
    def adjustSyrupMotionProgressBarZoom(self, values):
        numberOfPanZsyrupSteps = values[0] #self.deforumationnamedpipes.readValue("syrup_steps_pan_z")
        currentStepZ = numberOfPanZsyrupSteps[0]
        totalStepZ = numberOfPanZsyrupSteps[1]
        progressZ = int(100 / totalStepZ * currentStepZ)
        self.ui.motion_syrup_progressbar_z.setValue(progressZ)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_z, progressZ)
        self.Translation_Z = float(values[1]) #float(self.deforumationnamedpipes.readValue("translation_z"))
        self.ui.pan_z_value_progress.setText(str('%.2f' % self.Translation_Z))
        self.propagateAllComponents(self.ui.pan_z_value_progress, str('%.2f' % self.Translation_Z))
    def adjustSyrupTiltProgressBarPan(self, values):
        numberOfRotateZsyrupSteps =  values[0] #self.deforumationnamedpipes.readValue("syrup_steps_rotate_z")
        currentStepZ = numberOfRotateZsyrupSteps[0]
        totalStepZ = numberOfRotateZsyrupSteps[1]
        progressZ = int(100 / totalStepZ * currentStepZ)
        self.ui.motion_syrup_progressbar_rz.setValue(progressZ)
        self.propagateAllComponents(self.ui.motion_syrup_progressbar_rz, progressZ)
        self.Translation_RZ = float(values[1]) #float(self.deforumationnamedpipes.readValue("rotation_z"))
        self.ui.rotate_z_value_progress.setText(str('%.2f' % self.Translation_RZ))
        self.propagateAllComponents(self.ui.rotate_z_value_progress, str('%.2f' % self.Translation_RZ))

    """def adjustSyrupMotionProgressBar(self, values):
        self.adjustSyrupMotionProgressBarPan(values)
        self.adjustSyrupRotationProgressBarPan(values)
        self.adjustSyrupMotionProgressBarZoom(values)
        self.adjustSyrupTiltProgressBarPan(values)"""

    def setExponentialPanMotion(self, value):
        self.exponential_pan_motion = value
        # save to config
        #self.config["Exponential_Pan_Motion"] = value
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.config)
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Exponential_Pan_Motion", value)
    def setExponentialRotateMotion(self, value):
        self.exponential_rotate_motion = value
        # save to config
        #self.config["exponential_rotate_motion"] = value
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.config)
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_rotate_motion", value)
    def setExponentialTiltMotion(self, value):
        self.exponential_tilt_motion = value
        # save to config
        #self.config["exponential_tilt_motion"] = value
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.config)
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("exponential_tilt_motion", value)

    def setCurrentCadenceValueOnly(self, item):
        #orgName = self.getOriginalComponentName(item)
        self.cadence = item.value()
        self.parent.ui.cadence_slider_value.setText(str(self.cadence))
        #cadence_identifier = int(orgName[len("morph_prompt_slider"):])
        #cadence_identifier.setText(str('%.2f' % float(item.value() / 100)))

    def slider_changed(self, sender):
        if sender.objectName().startswith("syrup_pan_motion_slider"):
            self.Syrup_Panning_Motion = sender.value()
            self.ui.syrup_pan_motion_slider.setValue(int(sender.value()))
            self.ui.syrup_pan_motion_slider_frame_number.setText(str(sender.value()))
            self.propagateAllComponents(sender, sender.value())
            self.propagateAllComponents(self.ui.syrup_pan_motion_slider_frame_number, str(sender.value()))
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Panning", sender.value())
        elif sender.objectName().startswith("syrup_rotate_motion_slider"):
            self.Syrup_Rotation_Motion = sender.value()
            self.ui.syrup_rotate_motion_slider.setValue(int(sender.value()))
            self.ui.syrup_rotate_motion_slider_frame_number.setText(str(sender.value()))
            self.propagateAllComponents(sender, sender.value())
            self.propagateAllComponents(self.ui.syrup_rotate_motion_slider_frame_number, str(sender.value()))
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Rotation", sender.value())
        elif sender.objectName().startswith("syrup_zoom_motion_slider"):
            self.Syrup_Zooming_Motion = sender.value()
            self.ui.syrup_zoom_motion_slider.setValue(int(sender.value()))
            self.propagateAllComponents(sender, sender.value())
            self.ui.syrup_zoom_motion_slider_frame_number.setText(str(sender.value()))
            self.propagateAllComponents(self.ui.syrup_zoom_motion_slider_frame_number, str(sender.value()))
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Zoom", sender.value())
        elif sender.objectName().startswith("syrup_tilt_motion_slider"):
            self.Syrup_Tilt_Motion = sender.value()
            self.ui.syrup_tilt_motion_slider.setValue(int(sender.value()))
            self.ui.syrup_tilt_motion_slider_frame_number.setText(str(sender.value()))
            self.propagateAllComponents(sender, sender.value())
            self.propagateAllComponents(self.ui.syrup_tilt_motion_slider_frame_number, str(sender.value()))
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Tilt", sender.value())
        elif sender.objectName().startswith("motion_zoom_slider"):
            bezierTupple = self.getBezierTuple(self.ui.syrup_zoom_curve_type)
            if self.Syrup_Zooming_Motion == 0:
                self.deforumationnamedpipes.writeValue("start_zero_pan_motion_z", -2)
                self.Translation_Z = round(sender.value()/100, 2)
                self.Translation_Z_EXPONENTIAL = self.Translation_Z
                self.propagateAllComponents(sender, sender.value())
                self.ui.pan_z_value.setText(str('%.2f' % self.Translation_Z))
                self.propagateAllComponents(self.ui.pan_z_value, str('%.2f' % self.Translation_Z))
                self.deforumationnamedpipes.writeValue("translation_z", self.Translation_Z)
                # Write the value to our config
                #self.deforumation_settings.writeDeforumSendValuesToConfig("translation_z", sender.value()/100)
            else:
                #print("Sender value: ", sender.value())
                self.Translation_Z = float(self.deforumationnamedpipes.readValue("deforum_translation_z"))
                #granularity = float(self.ui.motion_zoom_granularity_special.text())
                #self.Translation_Z_EXPONENTIAL = self.Translation_Z_EXPONENTIAL - granularity
                #self.Translation_Z = self.Translation_Z_EXPONENTIAL
                #self.Translation_Z = float(sender.value() / 100)
                self.Translation_Z_EXPONENTIAL = float(sender.value() / 100)
                bezierArray = pyeaze.Animator(current_value=self.Translation_Z, target_value=(self.Translation_Z_EXPONENTIAL), duration=1, fps=int(self.Syrup_Zooming_Motion), easing=bezierTupple, reverse=False)
                #bezierArray = pyeaze.Animator(current_value=self.Translation_Z, target_value=(sender.value() / 100), duration=1, fps=int(self.Syrup_Zooming_Motion), easing=bezierTupple, reverse=False)
                #self.Translation_X = round(self.Translation_X - granularity, 2)
                #else:
                #bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=self.Translation_X_EXPONENTIAL, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                #self.Translation_X = self.Translation_X_EXPONENTIAL
                self.Translation_Z = sender.value() / 100
                self.ui.pan_z_value.setText(str('%.2f' % self.Translation_Z))
                self.propagateAllComponents(sender, sender.value())
                self.propagateAllComponents(self.ui.pan_z_value, self.Translation_Z)
                if not self.isComponentAduplicated(sender.objectName()):
                    self.deforumation_settings.writeDeforumSendValuesToConfig("translation_z", self.Translation_Z)
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_z", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_z", 1)
            #Write the value to our config
            #self.deforumation_settings.writeDeforumSendValuesToConfig(sender.objectName(), sender.value()/100)
        elif sender.objectName().startswith("motion_fov_slider"):
           self.fov = sender.value()
           self.propagateAllComponents(sender, sender.value())
           self.ui.fov_value.setText(str(self.fov))
           self.propagateAllComponents(self.ui.fov_value, str(sender.value()))
           self.deforumationnamedpipes.writeValue("fov", self.fov)
           # Write the value to our config
           #self.deforumation_settings.writeDeforumSendValuesToConfig("fov", sender.value())
        elif sender.objectName().startswith("step_slider"):
           self.steps = sender.value()
           for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
               if sliderwidgets.startswith("step_slider_value"):
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText(str(self.steps))
               elif sliderwidgets.startswith("step_slider") and type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sender.value())
           self.deforumationnamedpipes.writeValue("steps", self.steps)
           # Write the value to our config
           #self.deforumation_settings.writeDeforumSendValuesToConfig("steps", sender.value())
        elif sender.objectName().startswith("strength_slider"):
            self.strength = float(sender.value() / 100)
            for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
                    if sliderwidgets.startswith("strength_slider_value"):
                        self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText('%.2f' % self.strength)
                    elif sliderwidgets.startswith("strength_slider") and type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                        self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sender.value())
            self.deforumationnamedpipes.writeValue("strength", self.strength)
            #Write the value to our config
            #self.deforumation_settings.writeDeforumSendValuesToConfig("strength", sender.value())
        elif sender.objectName().startswith("cfg_slider"):
           self.cfg = sender.value()
           for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
               if sliderwidgets.startswith("cfg_slider_value"):
                   self.cfg_float = round((self.cfg / 10),1)
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText(str(self.cfg_float))
                   #self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText(str(self.cfg))
               elif sliderwidgets.startswith("cfg_slider") and type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sender.value())
           self.deforumationnamedpipes.writeValue("cfg", self.cfg_float) #self.cfg)
           # Write the value to our config
           #self.deforumation_settings.writeDeforumSendValuesToConfig("cfg", sender.value())
        elif sender.objectName().startswith("cadence_slider"):
           self.cadence = sender.value()
           for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
               if sliderwidgets.startswith("cadence_slider_value"):
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText(str(self.cadence))
               elif sliderwidgets.startswith("cadence_slider") and type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                   self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sender.value())
           self.deforumationnamedpipes.writeValue("cadence", self.cadence)
           # Write the value to our config
           #self.deforumation_settings.writeDeforumSendValuesToConfig("cadence", sender.value())
        elif sender.objectName().startswith("noise_slider"):
            self.noise_multiplier = float(sender.value()/100)
            for sliderwidgets in self.deforumationwidgets.getWidgetContainer():
                if sliderwidgets.startswith("noise_slider_value"):
                    self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setText('%.2f' % self.noise_multiplier)
                elif sliderwidgets.startswith("noise_slider") and type(self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget) == QSlider:
                    self.deforumationwidgets.getWidgetContainer()[sliderwidgets].widget.setValue(sender.value())
            self.deforumationnamedpipes.writeValue("noise_multiplier", self.noise_multiplier)
            # Write the value to our config
            #self.deforumation_settings.writeDeforumSendValuesToConfig("noise_multiplier", sender.value())

    def getBezierTuple(self, combobox):
        currentSelection = combobox.currentText()
        if currentSelection == "Linear":
            return list(((0.0, 0.0), (0, 0), (1.0, 1.0), (1.0, 1.0)))
        elif currentSelection == "Ease":
            return list(((0.0, 0.0), (0.25, 0.1), (0.25, 1), (1.0, 1.0)))
        elif currentSelection == "Ease-In":
            return list(((0.0, 0.0), (.42, 0), (1, 1), (1.0, 1.0)))
        elif currentSelection == "Ease-Out":
            return list(((0.0, 0.0), (0, 0), (.58, 1), (1.0, 1.0)))
        elif currentSelection == "Ease-In-Out":
            return list(((0.0, 0.0), (.42, 0), (.58, 1), (1.0, 1.0)))
        else:
            print("!!No such curve exists, using linear curve!!")
        return list(((0.0, 0.0), (0, 0), (1.0, 1.0), (1.0, 1.0)))

    def getOriginalComponentName(self, sender):
        # Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(sender.objectName()):
            if c.isdigit():
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

    def propagateAllComponents(self, sender, value = None):
        original_component_name = self.getOriginalComponentName(sender)
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
                    elif type(sender) == QProgressBar:
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setValue(sender.value())




    def clicked_button(self, event, sender):
        #print("Got a motion from sender:" + str(sender))
        ############################################################################################
        # Pan Motions
        #####################################################################
        if sender.objectName().startswith("motion_zoom_button_backwards"):
            sender = self.ui.motion_zoom_slider
            if event.button() == Qt.LeftButton:
                granularity = float(self.ui.motion_zoom_granularity_special.text())
                self.Translation_Z = round(self.Translation_Z - granularity, 2)
                self.Translation_Z_EXPONENTIAL = round(self.Translation_Z_EXPONENTIAL - granularity, 2)
                #print("Sending Translation_Z:" + str(self.Translation_Z_EXPONENTIAL))
                sender.setValue(int(self.Translation_Z_EXPONENTIAL * 100))
        elif sender.objectName().startswith("motion_zoom_button_forwards"):
            sender = self.ui.motion_zoom_slider
            if event.button() == Qt.LeftButton:
                granularity = float(self.ui.motion_zoom_granularity_special.text())
                self.Translation_Z = round(self.Translation_Z + granularity, 2)
                self.Translation_Z_EXPONENTIAL = round(self.Translation_Z_EXPONENTIAL + granularity, 2)
                #print("Sending Translation_Z:" + str(self.Translation_Z_EXPONENTIAL))
                sender.setValue(int(self.Translation_Z_EXPONENTIAL * 100))
        elif sender.objectName().startswith("motion_pan_button_left"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_pan_granularity.text())
                if self.Syrup_Panning_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_X = 0
                        self.Translation_X_EXPONENTIAL = 0
                    else:
                        self.Translation_X = round(self.Translation_X - granularity, 2)
                        self.Translation_X_EXPONENTIAL = self.Translation_X
                    self.deforumationnamedpipes.writeValue("translation_x", self.Translation_X)
                    # Write the value to our config
                    #self.deforumation_settings.writeDeforumSendValuesToConfig("translation_x", self.Translation_X)
                else:
                    #print("You have selected:" + self.ui.syrup_pan_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_X = float(self.deforumationnamedpipes.readValue("deforum_translation_x"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_X = 0
                        self.Translation_X_EXPONENTIAL = 0
                    else:
                        self.Translation_X = float(self.deforumationnamedpipes.readValue("deforum_translation_x"))
                        self.Translation_X_EXPONENTIAL = self.Translation_X_EXPONENTIAL - granularity
                        if not self.exponential_pan_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=self.Translation_X - granularity, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_X = round(self.Translation_X - granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=self.Translation_X_EXPONENTIAL, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_X = self.Translation_X_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("translation_x", self.Translation_X)
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_x", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", 1)
            self.ui.pan_x_value.setText(str('%.2f' % self.Translation_X))
            self.propagateAllComponents(self.ui.pan_x_value, self.Translation_X)
        elif sender.objectName().startswith("motion_pan_button_right"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_pan_granularity.text())
                if self.Syrup_Panning_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_X = 0
                        self.Translation_X_EXPONENTIAL = 0
                    else:
                        self.Translation_X = round(self.Translation_X + granularity, 2)
                        self.Translation_X_EXPONENTIAL = self.Translation_X
                    self.deforumationnamedpipes.writeValue("translation_x", self.Translation_X)
                else:
                    #print("You have selected:" + self.ui.syrup_pan_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_X = float(self.deforumationnamedpipes.readValue("deforum_translation_x"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_X = 0
                        self.Translation_X_EXPONENTIAL = 0
                    else:
                        self.Translation_X = float(self.deforumationnamedpipes.readValue("deforum_translation_x"))
                        self.Translation_X_EXPONENTIAL = self.Translation_X_EXPONENTIAL + granularity
                        if not self.exponential_pan_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=self.Translation_X + granularity, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_X = round(self.Translation_X + granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_X, target_value=self.Translation_X_EXPONENTIAL, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_X = self.Translation_X_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("translation_x", self.Translation_X)
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_x", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", 1)
            self.ui.pan_x_value.setText(str('%.2f' % self.Translation_X))
            self.propagateAllComponents(self.ui.pan_x_value, self.Translation_X)
        elif sender.objectName().startswith("motion_pan_button_up"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_pan_granularity.text())
                if self.Syrup_Panning_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_Y = 0
                        self.Translation_Y_EXPONENTIAL = 0
                    else:
                        self.Translation_Y = round(self.Translation_Y + granularity, 2)
                        self.Translation_Y_EXPONENTIAL = self.Translation_Y
                    self.deforumationnamedpipes.writeValue("translation_y", self.Translation_Y)
                else:
                    #print("You have selected:" + self.ui.syrup_pan_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_Y = float(self.deforumationnamedpipes.readValue("deforum_translation_y"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_Y = 0
                        self.Translation_Y_EXPONENTIAL = 0
                    else:
                        self.Translation_Y = float(self.deforumationnamedpipes.readValue("deforum_translation_y"))
                        self.Translation_Y_EXPONENTIAL = self.Translation_Y_EXPONENTIAL + granularity
                        if not self.exponential_pan_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=self.Translation_Y + granularity, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_Y = round(self.Translation_Y + granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=self.Translation_Y_EXPONENTIAL, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_Y = self.Translation_Y_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("translation_y", self.Translation_Y)
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_y", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", 1)
            self.ui.pan_y_value.setText(str('%.2f' % self.Translation_Y))
            self.propagateAllComponents(self.ui.pan_y_value, self.Translation_Y)
        elif sender.objectName().startswith("motion_pan_button_down"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_pan_granularity.text())
                if self.Syrup_Panning_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_Y = 0
                        self.Translation_Y_EXPONENTIAL = 0
                    else:
                        self.Translation_Y = round(self.Translation_Y - granularity, 2)
                        self.Translation_Y_EXPONENTIAL = self.Translation_Y
                    self.deforumationnamedpipes.writeValue("translation_y", self.Translation_Y)
                else:
                    #print("You have selected:" + self.ui.syrup_pan_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_Y = float(self.deforumationnamedpipes.readValue("deforum_translation_y"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_Y = 0
                        self.Translation_Y_EXPONENTIAL = 0
                    else:
                        self.Translation_Y = float(self.deforumationnamedpipes.readValue("deforum_translation_y"))
                        self.Translation_Y_EXPONENTIAL = self.Translation_Y_EXPONENTIAL - granularity
                        if not self.exponential_pan_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=self.Translation_Y - granularity, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_Y = round(self.Translation_Y - granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_Y, target_value=self.Translation_Y_EXPONENTIAL, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_Y = self.Translation_Y_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("translation_y", self.Translation_Y)
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_y", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", 1)
            self.ui.pan_y_value.setText(str('%.2f' % self.Translation_Y))
            self.propagateAllComponents(self.ui.pan_y_value, self.Translation_Y)
        ############################################################################################
        # Rotate Motions
        #####################################################################
        elif sender.objectName().startswith("motion_rotate_button_down"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                # Is there any sirup motion?
                granularity = float(self.ui.motion_rotate_granularity.text())
                if self.Syrup_Rotation_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RX = 0
                        self.Translation_RX_EXPONENTIAL = 0
                    else:
                        self.Translation_RX = round(self.Translation_RX - granularity, 2)
                        self.Translation_RX_EXPONENTIAL = self.Translation_RX
                    self.deforumationnamedpipes.writeValue("rotation_x", self.Translation_RX)
                else:
                    #print("You have selected:" + self.ui.syrup_rotation_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_rotation_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RX = float(self.deforumationnamedpipes.readValue("deforum_rotation_x"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RX = 0
                        self.Translation_RX_EXPONENTIAL = 0
                    else:
                        self.Translation_RX = float(self.deforumationnamedpipes.readValue("deforum_rotation_x"))
                        self.Translation_RX_EXPONENTIAL = self.Translation_RX_EXPONENTIAL - granularity
                        if not self.exponential_rotate_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=self.Translation_RX - granularity, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RX = round(self.Translation_RX - granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=self.Translation_RX_EXPONENTIAL, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RX = self.Translation_RX_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_x", self.Translation_RX)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_x", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", 1)
            self.ui.rotate_y_value.setText(str('%.2f' % self.Translation_RX))
            self.propagateAllComponents(self.ui.rotate_y_value, self.Translation_RX)
        elif sender.objectName().startswith("motion_rotate_button_up"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                # Is there any sirup motion?
                granularity = float(self.ui.motion_rotate_granularity.text())
                if self.Syrup_Rotation_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RX = 0
                        self.Translation_RX_EXPONENTIAL = 0
                    else:
                        self.Translation_RX = round(self.Translation_RX + granularity, 2)
                        self.Translation_RX_EXPONENTIAL = self.Translation_RX
                    self.deforumationnamedpipes.writeValue("rotation_x", self.Translation_RX)
                else:
                    #print("You have selected:" + self.ui.syrup_rotation_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_rotation_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RX = float(self.deforumationnamedpipes.readValue("deforum_rotation_x"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RX = 0
                        self.Translation_RX_EXPONENTIAL = 0
                    else:
                        self.Translation_RX = float(self.deforumationnamedpipes.readValue("deforum_rotation_x"))
                        self.Translation_RX_EXPONENTIAL = self.Translation_RX_EXPONENTIAL + granularity
                        if not self.exponential_rotate_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=self.Translation_RX + granularity, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RX = round(self.Translation_RX + granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RX, target_value=self.Translation_RX_EXPONENTIAL, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RX = self.Translation_RX_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_x", self.Translation_RX)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_x", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", 1)
            self.ui.rotate_y_value.setText(str('%.2f' % self.Translation_RX))
            self.propagateAllComponents(self.ui.rotate_y_value, self.Translation_RX)
        elif sender.objectName().startswith("motion_rotate_button_right"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                # Is there any sirup motion?
                granularity = float(self.ui.motion_rotate_granularity.text())
                if self.Syrup_Rotation_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RY = 0
                        self.Translation_RY_EXPONENTIAL = 0
                    else:
                        self.Translation_RY = round(self.Translation_RY + granularity, 2)
                        self.Translation_RY_EXPONENTIAL = self.Translation_RY
                    self.deforumationnamedpipes.writeValue("rotation_y", self.Translation_RY)
                else:
                    #print("You have selected:" + self.ui.syrup_rotation_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_rotation_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RY = float(self.deforumationnamedpipes.readValue("deforum_rotation_y"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RY = 0
                        self.Translation_RY_EXPONENTIAL = 0
                    else:
                        self.Translation_RY = float(self.deforumationnamedpipes.readValue("deforum_rotation_y"))
                        self.Translation_RY_EXPONENTIAL = self.Translation_RY_EXPONENTIAL + granularity
                        if not self.exponential_rotate_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=self.Translation_RY + granularity, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RY = round(self.Translation_RY + granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=self.Translation_RY_EXPONENTIAL, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RY = self.Translation_RY_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_y", self.Translation_RY)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_y", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", 1)
            self.ui.rotate_x_value.setText(str('%.2f' % self.Translation_RY))
            self.propagateAllComponents(self.ui.rotate_x_value, self.Translation_RY)
        elif sender.objectName().startswith("motion_rotate_button_left"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                # Is there any sirup motion?
                granularity = float(self.ui.motion_rotate_granularity.text())
                if self.Syrup_Rotation_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RY = 0
                        self.Translation_RY_EXPONENTIAL = 0
                    else:
                        self.Translation_RY = round(self.Translation_RY - granularity, 2)
                        self.Translation_RY_EXPONENTIAL = self.Translation_RY
                    self.deforumationnamedpipes.writeValue("rotation_y", self.Translation_RY)
                else:
                    #print("You have selected:" + self.ui.syrup_rotation_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_rotation_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RY = float(self.deforumationnamedpipes.readValue("deforum_rotation_y"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RY = 0
                        self.Translation_RY_EXPONENTIAL = 0
                    else:
                        self.Translation_RY = float(self.deforumationnamedpipes.readValue("deforum_rotation_y"))
                        self.Translation_RY_EXPONENTIAL = self.Translation_RY_EXPONENTIAL - granularity
                        if not self.exponential_rotate_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=self.Translation_RY - granularity, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RY = round(self.Translation_RY - granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RY, target_value=self.Translation_RY_EXPONENTIAL, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RY = self.Translation_RY_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_y", self.Translation_RY)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_y", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", 1)
            self.ui.rotate_x_value.setText(str('%.2f' % self.Translation_RY))
            self.propagateAllComponents(self.ui.rotate_x_value, self.Translation_RY)
        #######################################################################################################################
        #TILT MOTIONS
        ########################################################################################
        elif sender.objectName().startswith("motion_tilt_button_left"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_tilt_granularity.text())
                if self.Syrup_Tilt_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RZ = 0
                        self.Translation_RZ_EXPONENTIAL = 0
                    else:
                        self.Translation_RZ = round(self.Translation_RZ - granularity, 2)
                        self.Translation_RZ_EXPONENTIAL = self.Translation_RZ
                    self.deforumationnamedpipes.writeValue("rotation_z", self.Translation_RZ)
                else:
                    #print("You have selected:" + self.ui.syrup_tilt_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_tilt_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RZ = float(self.deforumationnamedpipes.readValue("deforum_rotation_z"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=0, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RZ = 0
                        self.Translation_RZ_EXPONENTIAL = 0
                    else:
                        self.Translation_RZ = float(self.deforumationnamedpipes.readValue("deforum_rotation_z"))
                        self.Translation_RZ_EXPONENTIAL = self.Translation_RZ_EXPONENTIAL - granularity
                        if not self.exponential_tilt_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=self.Translation_RZ - granularity, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RZ = round(self.Translation_RZ - granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=self.Translation_RZ_EXPONENTIAL, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RZ = self.Translation_RZ_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_z", self.Translation_RZ)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_z", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", 1)
            self.ui.rotate_z_value.setText(str('%.2f' % self.Translation_RZ))
            self.propagateAllComponents(self.ui.rotate_z_value, self.Translation_RZ)
        elif sender.objectName().startswith("motion_tilt_button_right"):
            if event.button() == Qt.LeftButton or event.button() == Qt.RightButton:
                #Is there any sirup motion?
                granularity = float(self.ui.motion_tilt_granularity.text())
                if self.Syrup_Tilt_Motion == 0:
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", -2)
                    if event.button() == Qt.RightButton:
                        self.Translation_RZ = 0
                        self.Translation_RZ_EXPONENTIAL = 0
                    else:
                        self.Translation_RZ = round(self.Translation_RZ + granularity, 2)
                        self.Translation_RZ_EXPONENTIAL = self.Translation_RZ
                    self.deforumationnamedpipes.writeValue("rotation_z", self.Translation_RZ)
                else:
                    #print("You have selected:" + self.ui.syrup_tilt_curve_type.currentText())
                    bezierTupple = self.getBezierTuple(self.ui.syrup_tilt_curve_type)
                    if event.button() == Qt.RightButton:
                        self.Translation_RZ = float(self.deforumationnamedpipes.readValue("deforum_rotation_z"))
                        bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=0, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                        self.Translation_RZ = 0
                        self.Translation_RZ_EXPONENTIAL = 0
                    else:
                        self.Translation_RZ = float(self.deforumationnamedpipes.readValue("deforum_rotation_z"))
                        self.Translation_RZ_EXPONENTIAL = self.Translation_RZ_EXPONENTIAL + granularity
                        if not self.exponential_tilt_motion:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=self.Translation_RZ + granularity, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RZ = round(self.Translation_RZ + granularity, 2)
                        else:
                            bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=self.Translation_RZ_EXPONENTIAL, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                            self.Translation_RZ = self.Translation_RZ_EXPONENTIAL
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_z", self.Translation_RZ)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_z", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", 1)
            self.ui.rotate_z_value.setText(str('%.2f' % self.Translation_RZ))
            self.propagateAllComponents(self.ui.rotate_z_value, self.Translation_RZ)
        elif sender.objectName().startswith("motion_zoom_slider") and event.button() == Qt.RightButton:
            sender.setValue(0)
        elif sender.objectName().startswith("pan_middle_button"):
            if self.Syrup_Panning_Motion == 0:
                self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", -2)
                self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", -2)
                self.Translation_X = 0
                self.Translation_Y = 0
                self.Translation_X_EXPONENTIAL = 0
                self.Translation_Y_EXPONENTIAL = 0
                self.ui.pan_x_value.setText(str('%.2f' % self.Translation_X))
                self.ui.pan_y_value.setText(str('%.2f' % self.Translation_Y))
                self.propagateAllComponents(self.ui.pan_x_value, self.Translation_X)
                self.propagateAllComponents(self.ui.pan_y_value, self.Translation_Y)
                self.deforumationnamedpipes.writeValue("translation_x", self.Translation_X)
                self.deforumationnamedpipes.writeValue("translation_y", self.Translation_X)
            else:
                bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)
                if self.Translation_X != 0:
                    self.Translation_X = float(self.deforumationnamedpipes.readValue("deforum_translation_x"))
                    bezierArrayX = pyeaze.Animator(current_value=self.Translation_X, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                    self.Translation_X = 0
                    self.Translation_X_EXPONENTIAL = 0
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_x", bezierArrayX.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_x", 1)

                if self.Translation_Y != 0:
                    self.Translation_Y = float(self.deforumationnamedpipes.readValue("deforum_translation_y"))
                    bezierArrayY = pyeaze.Animator(current_value=self.Translation_Y, target_value=0, duration=1, fps=int(self.Syrup_Panning_Motion), easing=bezierTupple, reverse=False)
                    self.Translation_Y = 0
                    self.Translation_Y_EXPONENTIAL = 0
                    self.deforumationnamedpipes.writeValue("prepare_zero_pan_motion_y", bezierArrayY.values)
                    self.deforumationnamedpipes.writeValue("start_zero_pan_motion_y", 1)
                self.deforumation_settings.writeDeforumSendValuesToConfig("translation_x", self.Translation_X)
                self.deforumation_settings.writeDeforumSendValuesToConfig("translation_y", self.Translation_Y)
                self.ui.pan_x_value.setText(str('%.2f' % self.Translation_X))
                self.ui.pan_y_value.setText(str('%.2f' % self.Translation_Y))
                self.propagateAllComponents(self.ui.pan_x_value, self.Translation_X)
                self.propagateAllComponents(self.ui.pan_y_value, self.Translation_Y)
        elif sender.objectName().startswith("rotate_middle_button"):
            if self.Syrup_Rotation_Motion == 0:
                self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", -2)
                self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", -2)
                self.Translation_RX = 0
                self.Translation_RY = 0
                self.Translation_RX_EXPONENTIAL = 0
                self.Translation_RY_EXPONENTIAL = 0
                self.ui.rotate_x_value.setText(str('%.2f' % self.Translation_RY))
                self.ui.rotate_y_value.setText(str('%.2f' % self.Translation_RX))
                self.propagateAllComponents(self.ui.rotate_x_value, self.Translation_RY)
                self.propagateAllComponents(self.ui.rotate_y_value, self.Translation_RX)
                self.deforumationnamedpipes.writeValue("rotation_x", self.Translation_RX)
                self.deforumationnamedpipes.writeValue("rotation_y", self.Translation_RY)
            else:
                bezierTupple = self.getBezierTuple(self.ui.syrup_pan_curve_type)

                if self.Translation_RX != 0:
                    self.Translation_RX = float(self.deforumationnamedpipes.readValue("rotation_x"))
                    bezierArrayX = pyeaze.Animator(current_value=self.Translation_RX, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                    self.Translation_RX = 0
                    self.Translation_RX_EXPONENTIAL = 0
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_x", bezierArrayX.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_x", 1)

                if self.Translation_RY != 0:
                    self.Translation_RY = float(self.deforumationnamedpipes.readValue("rotation_y"))
                    bezierArrayY = pyeaze.Animator(current_value=self.Translation_RY, target_value=0, duration=1, fps=int(self.Syrup_Rotation_Motion), easing=bezierTupple, reverse=False)
                    self.Translation_RY = 0
                    self.Translation_RY_EXPONENTIAL = 0
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_y", bezierArrayY.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_y", 1)
                self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_x", self.Translation_RX)
                self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_y", self.Translation_RY)
                self.ui.rotate_x_value.setText(str('%.2f' % self.Translation_RY))
                self.ui.rotate_y_value.setText(str('%.2f' % self.Translation_RX))
                self.propagateAllComponents(self.ui.rotate_x_value, self.Translation_RY)
                self.propagateAllComponents(self.ui.rotate_y_value, self.Translation_RX)
        elif sender.objectName().startswith("tilt_middle_button"):
            if self.Syrup_Tilt_Motion == 0:
                self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", -2)
                self.Translation_RZ = 0
                self.Translation_RZ_EXPONENTIAL = 0
                self.deforumationnamedpipes.writeValue("rotation_z", self.Translation_RZ)
            else:
                if self.Translation_RZ != 0:
                    bezierTupple = self.getBezierTuple(self.ui.syrup_tilt_curve_type)
                    self.Translation_RZ = float(self.deforumationnamedpipes.readValue("deforum_rotation_z"))
                    bezierArray = pyeaze.Animator(current_value=self.Translation_RZ, target_value=0, duration=1, fps=int(self.Syrup_Tilt_Motion), easing=bezierTupple, reverse=False)
                    self.Translation_RZ = 0
                    self.Translation_RZ_EXPONENTIAL = 0
                    self.deforumation_settings.writeDeforumSendValuesToConfig("rotation_z", self.Translation_RZ)
                    self.deforumationnamedpipes.writeValue("prepare_zero_rotate_motion_z", bezierArray.values)
                    self.deforumationnamedpipes.writeValue("start_zero_rotate_motion_z", 1)
            self.ui.rotate_z_value.setText(str('%.2f' % self.Translation_RZ))
            self.propagateAllComponents(self.ui.rotate_z_value, self.Translation_RZ)

        elif sender.objectName().startswith("motion_fov_slider") and event.button() == Qt.RightButton:
            sender.setValue(70)

    def setSyrupPanningMotion(self, value):
        self.Syrup_Panning_Motion = value
        self.ui.syrup_pan_motion_slider.setValue(int(self.Syrup_Panning_Motion))
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Panning", value)
    def setSyrupRotationMotion(self, value):
        self.Syrup_Rotation_Motion = value
        self.ui.syrup_rotate_motion_slider.setValue(int(self.Syrup_Rotation_Motion))
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Rotation", value)
    def setSyrupZoomingMotion(self, value):
        self.Syrup_Zooming_Motion = value
        self.ui.syrup_zoom_motion_slider.setValue(int(self.Syrup_Zooming_Motion))
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Zoom", value)
    def setSyrupTiltMotion(self, value):
        self.Syrup_Tilt_Motion = value
        self.ui.syrup_tilt_motion_slider.setValue(int(self.Syrup_Tilt_Motion))
        self.deforumation_settings.writeDeforumationGuiValuesToConfig("Syrupmotion_Tilt", value)

    def set_zoom_granularity(self, value):
        #print("Zoom granularity=" + str(value.value()))
        self.Zoom_Max = value.value() * 100.0
        self.Zoom_Min = value.value() * -100.0
        self.ui.motion_zoom_slider.setTickInterval(int(self.Zoom_Max / 10.0))
        #self.propagateAllComponents(self.ui.motion_zoom_slider, str('%.2f' % -value.value()))

        self.ui.motion_zoom_slider.setMaximum(int(self.Zoom_Max))
        self.ui.motion_zoom_slider.setMinimum(int(self.Zoom_Min))
        self.propagateAllZoomSpecial(value, self.ui.motion_zoom_slider)

        self.propagateAllComponents(value, value.value())
        self.ui.max_zoom.setText(str('%.2f' % value.value()))
        self.propagateAllComponents(self.ui.max_zoom, str('%.2f' % value.value()))
        self.ui.min_zoom.setText(str('%.2f' % -value.value()))
        self.propagateAllComponents(self.ui.min_zoom, str('%.2f' % -value.value()))

    def propagateAllZoomSpecial(self, granularity_slider, zoom_slider):
        original_component_name = self.getOriginalComponentName(zoom_slider)
        for component in self.deforumationwidgets.getWidgetContainer():
            if component.startswith(original_component_name) and not component == zoom_slider.objectName():
                if len(component) <= len(original_component_name)+3:
                    if type(zoom_slider) == QSlider:
                        Zoom_Max = granularity_slider.value() * 100.0
                        Zoom_Min = granularity_slider.value() * -100.0
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setTickInterval(int(Zoom_Max / 10.0))
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setMaximum(int(Zoom_Max))
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setMinimum(int(Zoom_Min))

    def setMotionGranularity(self, sender):
        original_component_name = self.getOriginalComponentName(sender)
        if original_component_name == "motion_pan_granularity":
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Pan_Granularity", float(sender.text()))
        elif original_component_name == "motion_rotate_granularity":
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Rotation_Granularity", float(sender.text()))
        elif original_component_name == "motion_tilt_granularity":
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Tilt_Granularity", float(sender.text()))
        elif original_component_name == "motion_zoom_granularity_special":
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("Zoom_Granularity_Special", float(sender.text()))
        self.propagateAllComponents(sender, sender.text())


    def setShouldUseDeforumationStrength(self, value=-1):
        #self.p = self.deforumation_settings.getSendConfig()
        if value != -1:
            self.should_use_deforumation_strength = value
            #self.p["should_use_deforumation_strength"] = self.should_use_deforumation_strength
            self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_deforumation_strength", value)
        else:
            if "should_use_deforumation_strength" in self.deforumation_settings.getSendConfig(): #self.p:
                self.should_use_deforumation_strength = self.deforumation_settings.getSendConfig()["should_use_deforumation_strength"] #self.p["should_use_deforumation_strength"]
        if self.should_use_deforumation_strength:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_strength", 1)
        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_strength", 0)
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)

    def setShouldUseDeforumationCFG(self, value=-1):
        #self.p = self.deforumation_settings.getSendConfig()
        if value != -1:
            self.should_use_deforumation_cfg = value
            #self.p["should_use_deforumation_cfg"] = self.should_use_deforumation_cfg
            self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_deforumation_cfg", value)
        else:
            if "should_use_deforumation_cfg" in self.deforumation_settings.getSendConfig(): #self.p:
                self.should_use_deforumation_cfg = self.deforumation_settings.getSendConfig()["should_use_deforumation_cfg"] #self.p["should_use_deforumation_cfg"]
        if self.should_use_deforumation_cfg:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_cfg", 1)
            self.deforumationnamedpipes.writeValue("cfg", self.cfg_float) #self.cfg)
        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_cfg", 0)
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)

    def setShouldUseDeforumationCadence(self, value=-1):
        #self.p = self.deforumation_settings.getSendConfig()
        if value != -1:
            self.should_use_deforumation_cadence = value
            #self.p["should_use_deforumation_cadence"] = self.should_use_deforumation_cadence
            self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_deforumation_cadence", value)
        else:
            if "should_use_deforumation_cadence" in self.deforumation_settings.getSendConfig():
                self.should_use_deforumation_cadence = self.deforumation_settings.getSendConfig()["should_use_deforumation_cadence"] #self.p["should_use_deforumation_cadence"]
        if self.should_use_deforumation_cadence:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_cadence", 1)
            self.deforumationnamedpipes.writeValue("cadence", self.cadence)

        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_cadence", 0)
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)

    def setShouldUseDeforumationNoiseMultiplier(self, value=-1):
        #self.p = self.deforumation_settings.getSendConfig()
        if value != -1:
            self.should_use_deforumation_noise = value
            #self.p["should_use_deforumation_noise"] = self.should_use_deforumation_noise
            self.deforumation_settings.writeDeforumSendValuesToConfig("should_use_deforumation_noise", value)
        else:
            if "should_use_deforumation_noise" in self.deforumation_settings.getSendConfig():
                self.should_use_deforumation_noise =  self.deforumation_settings.getSendConfig()["should_use_deforumation_noise"] #self.p["should_use_deforumation_noise"]
        if self.should_use_deforumation_noise:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_noise", 1)
        else:
            self.deforumationnamedpipes.writeValue("should_use_deforumation_noise", 0)
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)

    def setShouldUseDeforumationParameter(self, check_box_object, new_value, mediator_communication_string, should_set_checkbox_state, send_mediator_communication_string_on_off = False, mediator_values_to_write = None, configType = None):
        #self.p = self.deforumation_settings.getSendConfig()
        try:
            if new_value != -1:
                setattr(self, mediator_communication_string, new_value)
                #self.p[mediator_communication_string] = new_value
                if configType == None:
                    self.deforumation_settings.writeDeforumSendValuesToConfig(mediator_communication_string, new_value)
                else:
                    if configType == "gui":
                        self.deforumation_settings.writeDeforumationGuiValuesToConfig(mediator_communication_string, new_value)
                    elif configType == "send":
                        self.deforumation_settings.writeDeforumSendValuesToConfig(mediator_communication_string, new_value)
                    elif configType == "receive":
                        self.deforumation_settings.writeDeforumReceiveValuesToConfig(mediator_communication_string, new_value)
            else:
                if mediator_communication_string in self.deforumation_settings.getSendConfig():
                    setattr(self, mediator_communication_string, self.deforumation_settings.getSendConfig()[mediator_communication_string])
            if send_mediator_communication_string_on_off:
                if getattr(self, mediator_communication_string):
                    self.deforumationnamedpipes.writeValue(mediator_communication_string, 1)
                else:
                    self.deforumationnamedpipes.writeValue(mediator_communication_string, 0)
            #Communicate values to the mediator, if neccessary
            if mediator_values_to_write != None:
                for parameter_name in mediator_values_to_write:
                    parameter_value = mediator_values_to_write[parameter_name]
                    self.deforumationnamedpipes.writeValue(parameter_name, parameter_value)

            if should_set_checkbox_state:
                check_box_object.setChecked(getattr(self, mediator_communication_string))
            self.propagateAllCheckboxes(check_box_object)
        except Exception as e:
            if self.is_verbose:
                print("(setShouldUseDeforumationParameter), has not yet a value (" + str(mediator_communication_string) +"), in config, and don't know if checkbox should be checked or not.")
        #self.deforumation_settings.writeDeforumSendValuesToConfig(self.p)

    def propagateAllCheckboxes(self, sender):
        #Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(sender.objectName()):
            if c.isdigit():
                digitPosition = i
                break
        if digitPosition == -1:
            original_checkbox_name = sender.objectName()
        else:
            original_checkbox_name = sender.objectName()[:digitPosition-1]
        for checkboxwidgets in self.deforumationwidgets.getWidgetContainer():
            if checkboxwidgets.startswith(original_checkbox_name) and not checkboxwidgets == sender.objectName():
                self.deforumationwidgets.getWidgetContainer()[checkboxwidgets].widget.setChecked(not sender.isChecked())

    def propagateAllRadioButtons(self, sender):
        #Check if the checkbox is a copy of the original
        digitPosition = -1
        for i, c in enumerate(sender.objectName()):
            if c.isdigit():
                digitPosition = i
                break
        if digitPosition == -1:
            original_checkbox_name = sender.objectName()
        else:
            original_checkbox_name = sender.objectName()[:digitPosition-1]
        for checkboxwidgets in self.deforumationwidgets.getWidgetContainer():
            if checkboxwidgets.startswith(original_checkbox_name) and not checkboxwidgets == sender.objectName():
                self.deforumationwidgets.getWidgetContainer()[checkboxwidgets].widget.setChecked(True)


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

    def setSeedAndScheme(self, event, object):
        #print("Action:" + str(event.type()) + "    --  Object Name:" + str(object.objectName()))
        if object.objectName().startswith("iter_RadioButton") or object.objectName().startswith("fixed_RadioButton") or object.objectName().startswith("random_RadioButton") or object.objectName().startswith("ladder_RadioButton") or object.objectName().startswith("alternate_RadioButton")  or object.objectName().startswith("scheduled_RadioButton"):
            object.setChecked(True)
            self.propagateAllRadioButtons(object)
        if object.objectName().startswith("update_seed_button"):
            if self.parent.ui.iter_RadioButton.isChecked():
                seedValue = int(self.parent.ui.IterSeed_Inputbox.text())
                self.deforumationnamedpipes.writeValue("seed", seedValue)
                self.deforumationnamedpipes.writeValue("seed_changed", 1)
            elif self.parent.ui.fixed_RadioButton.isChecked():
                seedValue = int(self.parent.ui.fixedSeed_Inputbox.text())
                self.deforumationnamedpipes.writeValue("seed", seedValue)
                self.deforumationnamedpipes.writeValue("seed_changed", 1)
                self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_fixed", seedValue)
            seed_iter_n = int(self.parent.ui.IterSeed_N_Inputbox.text())
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_iter_n", seed_iter_n)
            self.deforumationnamedpipes.writeValue("seed_iter_n", seed_iter_n)

        if object.objectName().startswith("update_seed_iter_n_button"):
            seed_iter_n = int(self.parent.ui.IterSeed_N_Inputbox.text())
            self.deforumationnamedpipes.writeValue("seed_iter_n", seed_iter_n)
        if self.parent.ui.iter_RadioButton.isChecked():
            print("iter_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "iter")
            self.deforumationnamedpipes.writeValue("seed_behavior", "iter")
        elif self.parent.ui.fixed_RadioButton.isChecked():
            print("fixed_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "fixed")
            self.deforumationnamedpipes.writeValue("seed_behavior", "fixed")
        elif self.parent.ui.random_RadioButton.isChecked():
            print("random_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "random")
            self.deforumationnamedpipes.writeValue("seed_behavior", "random")
        elif self.parent.ui.ladder_RadioButton.isChecked():
            print("ladder_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "ladder")
            self.deforumationnamedpipes.writeValue("seed_behavior", "ladder")
        elif self.parent.ui.alternate_RadioButton.isChecked():
            print("alternate_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "alternate")
            self.deforumationnamedpipes.writeValue("seed_behavior", "alternate")
        elif self.parent.ui.scheduled_RadioButton.isChecked():
            print("scheduled_RadioButton checked")
            self.deforumation_settings.writeDeforumationGuiValuesToConfig("seed_radio_button_checked", "schedule")
            self.deforumationnamedpipes.writeValue("seed_behavior", "schedule")

    def setLoobackButtonState(self):
        #Set looback button to on or off depending on state
        isLoobackOn = int(self.deforumationnamedpipes.readValue("render_loopback"))
        if isLoobackOn:
            loobObjectName = "loop_button"
            self.deforumationwidgets.getWidgetContainer()[loobObjectName].isActivated = True
            self.parent.ui.loop_button.setIcon(self.deforumationwidgets.getWidgetContainer()["loop_button"].icon.pixmap(self.parent.ui.loop_button.iconSize(), QIcon.Active, QIcon.On))

    def toggleLoopBack(self,event, object):
        is_in_loopback = int(self.deforumationnamedpipes.readValue("render_loopback"))
        if is_in_loopback:
            self.deforumationnamedpipes.writeValue("render_loopback", 0)
            if self.is_verbose:
                print("Exiting LoopBack Mode.")
            self.deforumationwidgets.getWidgetContainer()[object.objectName()].isActivated = False
            object.setIcon(self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon.pixmap(object.iconSize(), QIcon.Active, QIcon.Off))
        else:
            self.deforumationnamedpipes.writeValue("render_loopback", 1)
            if self.is_verbose:
                print("Entering LoopBack Mode.")
            self.deforumationwidgets.getWidgetContainer()[object.objectName()].isActivated = True
            object.setIcon(self.deforumationwidgets.getWidgetContainer()[object.objectName()].icon.pixmap(object.iconSize(), QIcon.Active, QIcon.On))
