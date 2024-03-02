from PySide6.QtCore import (Slot, Signal,)
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel


class Deforumation_Live_Values():

    def __init__(self, parent=None, deforumationtotalrecall = None, deforumationtools = None, deforumationwidgets = None, deforumationnamedpipes = None):
        self.DeforumationTotalRecall = deforumationtotalrecall
        self.deforumationtools = deforumationtools
        self.deforumationwidgets = deforumationwidgets
        self.deforumationnamedpipes = deforumationnamedpipes
        self.parent = parent

    def setImage(self, decline_object, rise_object, previous_value, current_value, decline_off_image, decline_on_image, rise_off_image, rise_on_image, motion_is_active):
        if previous_value == current_value and motion_is_active != 1:
            decline_object.setPixmap(QPixmap(decline_off_image))
            rise_object.setPixmap(QPixmap(rise_off_image))
            self.propagateAllImageComponents(decline_object, decline_off_image)
            self.propagateAllImageComponents(rise_object, rise_off_image)
        elif previous_value < current_value:
            decline_object.setPixmap(QPixmap(decline_off_image))
            rise_object.setPixmap(QPixmap(rise_on_image))
            self.propagateAllImageComponents(decline_object, decline_off_image)
            self.propagateAllImageComponents(rise_object, rise_on_image)
        elif previous_value > current_value:
            #print("Current_value is smaller:" + str(current_value) + "  -- than previous_value:" + str(previous_value))
            decline_object.setPixmap(QPixmap(decline_on_image))
            rise_object.setPixmap(QPixmap(rise_off_image))
            self.propagateAllImageComponents(decline_object, decline_on_image)
            self.propagateAllImageComponents(rise_object, rise_off_image)

    def propagateAllImageComponents(self, sender, image_name):
        original_component_name = self.deforumationtools.getOriginalComponentName(sender)
        for component in self.deforumationwidgets.getWidgetContainer():
            if component.startswith(original_component_name) and not component == sender.objectName():
                if len(component) <= len(original_component_name)+3:
                    if type(sender) == QLabel:
                        self.deforumationwidgets.getWidgetContainer()[component].widget.setPixmap(QPixmap(image_name))

    def setLiveValues(self, totalRecallFrame=-1):
        if totalRecallFrame == -1:
            total_recall_frame = self.DeforumationTotalRecall.getCurrentTotalRecallFrame()
        else:
            total_recall_frame = self.DeforumationTotalRecall.getCurrentTotalRecallFrame(totalRecallFrame)
        if total_recall_frame != 0:

            #motion_is_active = int(self.deforumationnamedpipes.readValue("start_zero_pan_motion_x"))
            self.setImage(self.parent.ui.panx_l, self.parent.ui.panx_r, round(float(self.parent.ui.panning_x_live_value.text()),2), round(float(total_recall_frame.deforum_translation_x),2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_pan_motion_x)
            self.parent.ui.panning_x_live_value.setText(str('%.2f' % total_recall_frame.deforum_translation_x))

            #motion_is_active = int(self.deforumationnamedpipes.readValue("start_zero_pan_motion_y"))
            self.setImage(self.parent.ui.pany_l, self.parent.ui.pany_r, round(float(self.parent.ui.panning_y_live_value.text()),2), round(float(total_recall_frame.deforum_translation_y),2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_pan_motion_y)
            self.parent.ui.panning_y_live_value.setText(str('%.2f' % total_recall_frame.deforum_translation_y))

            self.setImage(self.parent.ui.zoom_l, self.parent.ui.zoom_r, round(float(self.parent.ui.zoom_live_value.text()), 2), round(float(total_recall_frame.deforum_translation_z), 2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_pan_motion_z)
            self.parent.ui.zoom_live_value.setText(str('%.2f' % total_recall_frame.deforum_translation_z))

            self.parent.ui.fov_live_value.setText(str('%.2f' % total_recall_frame.deforum_fov))

            self.setImage(self.parent.ui.rotv_l, self.parent.ui.rotv_r, round(float(self.parent.ui.rotate_v_live_value.text()), 2), round(float(total_recall_frame.deforum_rotation_x), 2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_rotate_motion_x)
            self.parent.ui.rotate_v_live_value.setText(str('%.2f' % total_recall_frame.deforum_rotation_x))

            self.setImage(self.parent.ui.roth_l, self.parent.ui.roth_r, round(float(self.parent.ui.rotate_h_live_value.text()), 2), round(float(total_recall_frame.deforum_rotation_y), 2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_rotate_motion_y)
            self.parent.ui.rotate_h_live_value.setText(str('%.2f' % total_recall_frame.deforum_rotation_y))

            self.setImage(self.parent.ui.tilt_l, self.parent.ui.tilt_r, round(float(self.parent.ui.tilt_live_value.text()), 2), round(float(total_recall_frame.deforum_rotation_z), 2), "./images/value_declining_off.png", "./images/value_declining_on.png", "./images/value_rising_off.png", "./images/value_rising_on.png", total_recall_frame.start_zero_rotate_motion_z)
            self.parent.ui.tilt_live_value.setText(str('%.2f' % total_recall_frame.deforum_rotation_z))

            self.parent.ui.steps_live_value.setText(str(total_recall_frame.deforum_steps))
            self.parent.ui.strength_live_value.setText(str('%.2f' % total_recall_frame.deforum_strength))
            self.parent.ui.cfg_live_value.setText(str(total_recall_frame.deforum_cfg))
            self.parent.ui.cadence_live_value.setText(str(total_recall_frame.deforum_cadence))
            self.parent.ui.noise_multiplier_live.setText(str(total_recall_frame.deforum_noise_multiplier))
            self.parent.ui.seed_live_value.setText(str(total_recall_frame.seed_value))

            #print(str( total_recall_frame.seed_value))



            self.deforumationtools.propagateAllComponents(self.parent.ui.panning_x_live_value, str('%.2f' % total_recall_frame.deforum_translation_x))
            self.deforumationtools.propagateAllComponents(self.parent.ui.panning_y_live_value, str('%.2f' % total_recall_frame.deforum_translation_y))
            self.deforumationtools.propagateAllComponents(self.parent.ui.zoom_live_value, str('%.2f' % total_recall_frame.deforum_translation_z))
            self.deforumationtools.propagateAllComponents(self.parent.ui.fov_live_value, str('%.2f' % total_recall_frame.deforum_fov))
            self.deforumationtools.propagateAllComponents(self.parent.ui.rotate_v_live_value, str('%.2f' % total_recall_frame.deforum_rotation_x))
            self.deforumationtools.propagateAllComponents(self.parent.ui.rotate_h_live_value, str('%.2f' % total_recall_frame.deforum_rotation_y))
            self.deforumationtools.propagateAllComponents(self.parent.ui.tilt_live_value, str('%.2f' % total_recall_frame.deforum_rotation_z))
            self.deforumationtools.propagateAllComponents(self.parent.ui.steps_live_value, str(total_recall_frame.deforum_steps))
            self.deforumationtools.propagateAllComponents(self.parent.ui.strength_live_value, str('%.2f' % total_recall_frame.deforum_strength))
            self.deforumationtools.propagateAllComponents(self.parent.ui.cfg_live_value, str(total_recall_frame.deforum_cfg))
            self.deforumationtools.propagateAllComponents(self.parent.ui.cadence_live_value, str(total_recall_frame.deforum_cadence))
            self.deforumationtools.propagateAllComponents(self.parent.ui.noise_multiplier_live, str(total_recall_frame.deforum_noise_multiplier))
            self.deforumationtools.propagateAllComponents(self.parent.ui.seed_live_value, str(total_recall_frame.seed_value))


            """self.parent.ui.strength_slider_value.setText(str(total_recall_frame.deforum_strength))
            self.parent.ui.step_slider_value.setText(str(total_recall_frame.deforum_steps))
            self.parent.ui.cfg_slider_value.setText(str(total_recall_frame.deforum_cfg))
            #self.parent.ui.cadence_slider_value.setText(str(total_recall_frame.deforum_cadence))
            self.parent.ui.noise_slider_value.setText(str(total_recall_frame.deforum_noise_multiplier))

            self.parent.ui.step_slider.setValue(int(total_recall_frame.deforum_steps))
            self.parent.ui.strength_slider.setValue(int(total_recall_frame.deforum_strength * 100))
            self.parent.ui.cfg_slider.setValue(int(total_recall_frame.deforum_cfg))
            #self.parent.ui.cadence_slider.setValue(int(total_recall_frame.deforum_cadence))
            self.parent.ui.noise_slider.setValue(int(total_recall_frame.deforum_noise_multiplier * 100))"""

