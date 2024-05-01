import re
import sys
import asyncio
import copy
import time
import websockets
import pickle
import threading
import argparse

# Server-stuff
stop = None
server = None
serverShutDown = False
deforumation_address = 'localhost'
deforumation_port = 8767
mediator_deforumation_address ='localhost'
mediator_deforumation_port = 8766
mediator_deforum_address = 'localhost'
mediator_deforum_port = 8765
# Run/Steps
steps = 25
deforum_steps = 25
# Keyframes/Strength
strength_value = 0.65
deforum_strength = 0.65
# Keyframes/CFG
cfg_scale = 6.0
deforum_cfg = 6.0
# Keyframes/3D/Motion
rotation_x = 0.0
rotation_y = 0.0
rotation_z = 0.0
deforum_rotation_x = 0.0
deforum_rotation_y = 0.0
deforum_rotation_z = 0.0
translation_x = 0.0
translation_y = 0.0
translation_z = 0.0
deforum_translation_x = 0.0
deforum_translation_y = 0.0
deforum_translation_z = 0.0
Prompt_Positive = ""
Prompt_Negative = ""
positive_prompt_mixed = ""
should_resume = 0
shouldPause = 0
start_frame = 0
number_of_generated_images = 0
frame_outdir = ""
resume_timestring = ""
seed_value = -1
seed_iter_n = 1
did_seed_change = 0
seed_behavior = "iter"
should_use_deforumation_prompt_scheduling = 1
should_use_before_deforum_prompt = 0
should_use_after_deforum_prompt = 0

# Keyframes/Field Of View/FOV schedule
fov = 70.0
deforum_fov = 70.0
doVerbose = False
doVerbose2 = False
should_use_deforumation_strength = 1
should_use_deforumation_cfg = 1
should_use_deforumation_cadence = 1
should_use_deforumation_panning = 1
should_use_deforumation_zoom = 1
should_use_deforumation_fov = 1
should_use_deforumation_rotation = 1
should_use_deforumation_tilt = 1
cadence = 2
deforum_cadence = 2
should_use_optical_flow = 1
should_use_deforumation_graph = {"Strength":0,"Zoom":0,"PanLR":0,"PanUD":0,"RotateH":0,"RotateV":0,"Tilt":0}
deforumation_graph = {"Strength":[],"Zoom":[],"PanLR":[],"PanUD":[],"RotateH":[],"RotateV":[],"Tilt":[]}
deforumation_graph_xshift = {"Strength":0,"Zoom":0,"PanLR":0,"PanUD":0,"RotateH":0,"RotateV":0,"Tilt":0}
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
should_use_deforumation_noise = 0

noise_multiplier = 1.05
deforum_noise_multiplier = 1.05
perlin_octaves = 4
deforum_perlin_octaves = 4
perlin_persistence = 0.5
deforum_perlin_persistence = 0.5

use_deforumation_cadence_scheduling = 0

deforumation_cadence_scheduling_manifest = "0:(3)"

parameter_container = {}

should_use_total_recall = 0
total_recall_from = 0
total_recall_to = 0
should_use_deforumation_timestring = 0

#Touched params (for total recall)
Prompt_Positive_touched = 0

#Under recall values (live values from deforumation)
translation_x_under_recall = 0
translation_y_under_recall = 0
translation_z_under_recall = 0
rotation_x_under_recall = 0
rotation_y_under_recall = 0
rotation_z_under_recall = 0

number_of_recalled_frames = 0

should_use_total_recall_prompt = 0
should_use_total_recall_movements = 0
should_use_total_recall_others = 0

start_motion = 0
start_zero_pan_motion = 0

start_zero_pan_motion_x = 0
start_zero_pan_motion_y = 0
start_zero_pan_motion_z = 0
start_zero_rotate_motion_x = 0
start_zero_rotate_motion_y = 0
start_zero_rotate_motion_z = 0

start_zero_zoom_motion = 0
start_zero_rotation_motion = 0
start_zero_tilt_motion = 0

prepared_motion = []
prepared_zero_pan_motion = []
prepared_zero_pan_motion_x = []
prepared_zero_pan_motion_y = []
prepared_zero_rotate_motion_x = []
prepared_zero_rotate_motion_y = []
prepared_zero_rotate_motion_z = []
prepared_zero_pan_motion_z = []
prepared_zero_zoom_motion = []
prepared_zero_rotation_motion = []
prepared_zero_tilt_motion = []

prepared_motion_start = -1
prepared_zero_pan_motion_start = -1
prepared_zero_pan_motion_x_start = -1
prepared_zero_pan_motion_y_start = -1
prepared_zero_rotate_motion_x_start = -1
prepared_zero_rotate_motion_y_start = -1
prepared_zero_rotate_motion_z_start = -1
prepared_zero_pan_motion_z_start = -1
prepared_zero_zoom_motion_start = -1
prepared_zero_rotation_motion_start = -1
prepared_zero_tilt_motion_start = -1

motion_current_status_string = "P-D Motion: None"

motion_current_zero_pan_string = "0-Pan: None"
motion_current_zero_pan_x_string = "0-Pan_X: None"
motion_current_zero_pan_y_string = "0-Pan_Y: None"
motion_current_zero_zoom_string = "0-Zoom: None"
motion_current_zero_rotate_string = "0-Rotation: None"
motion_current_zero_tilt_string = "0-Tilt: None"
frame_idx = 0
positive_prompt_weight_1 = 1.0
positive_prompt_weight_2 = 1.0
positive_prompt_1 = ""
positive_prompt_2 = ""
negative_prompt_1 = ""

deforumation_prompt_morph_container = {}
prepare_prompt_morph_motion_container = {}
start_prompt_morph_motion_container = {}
prepare_prompt_morph_motion_start_container = {}
prompt_morphing_container = {}
current_prompt_morph_progressions = []

deforum_interrupted = 0
render_loopback = 0
ShouldBeRunning = True

def RecallValues(frame):
    global serverShutDown
    global Prompt_Positive
    global Prompt_Negative
    global rotation_x
    global rotation_y
    global rotation_z
    global translation_x
    global translation_y
    global translation_z
    global deforum_translation_x
    global deforum_translation_y
    global deforum_translation_z
    global fov
    global cfg_scale
    global strength_value
    global steps
    global should_resume
    global start_frame
    global frame_outdir
    global resume_timestring
    global shouldPause
    global seed_value
    global did_seed_change
    global should_use_deforumation_strength
    global should_use_deforumation_cfg
    global cadence
    global should_use_deforumation_prompt_scheduling
    global should_use_before_deforum_prompt
    global should_use_after_deforum_prompt
    global cn_weight
    global cn_stepstart
    global cn_stepend
    global cn_lowt
    global cn_hight
    global cn_udcn
    global parseq_keys
    global use_parseq
    global parseq_manifest
    global parseq_strength
    global parseq_movements
    global deforum_rotation_x
    global deforum_rotation_y
    global deforum_rotation_z
    global deforum_fov
    global deforum_strength
    global deforum_cfg
    global deforum_steps
    global parseq_prompt
    global noise_multiplier
    global deforum_perlin_octaves
    global deforum_perlin_persistence
    global deforum_noise_multiplier
    global perlin_octaves
    global perlin_persistence
    global deforum_cadence
    global should_use_deforumation_cadence
    global should_use_deforumation_noise
    global should_use_deforumation_panning
    global should_use_deforumation_zoom
    global should_use_deforumation_fov
    global should_use_deforumation_rotation
    global should_use_deforumation_tilt
    global use_deforumation_cadence_scheduling
    global deforumation_cadence_scheduling_manifest
    global should_use_optical_flow
    global cadence_flow_factor
    global generation_flow_factor
    global translation_x_under_recall
    global translation_y_under_recall
    global translation_z_under_recall
    global rotation_x_under_recall
    global rotation_y_under_recall
    global rotation_z_under_recall

    if not int(frame) in parameter_container:
        print("Mediator has no data for frame (" + str(frame) + ")" +" to send!")
        return
    #Movement
    if should_use_total_recall_movements:
        rotation_x = parameter_container[frame].rotation_x + rotation_x_under_recall
        rotation_y = parameter_container[frame].rotation_y + rotation_y_under_recall
        rotation_z = parameter_container[frame].rotation_z + rotation_z_under_recall
        translation_x = parameter_container[frame].translation_x + translation_x_under_recall
        #print("Total Recall: parameter_container[frame].translation_x (" + str(parameter_container[frame].translation_x)+")"+" translation_x_under_recall ("+ str(translation_x_under_recall)+")")
        translation_y = parameter_container[frame].translation_y + translation_y_under_recall
        translation_z = parameter_container[frame].translation_z + translation_z_under_recall
        fov = parameter_container[frame].fov
    #prompt
    if should_use_total_recall_prompt == 1:
        Prompt_Positive = parameter_container[frame].Prompt_Positive
        Prompt_Negative = parameter_container[frame].Prompt_Negative

    if should_use_total_recall_others:
        #Other values
        # Keyframes/Field Of View/FOV schedule
        # Run/Steps
        seed_value = parameter_container[frame].seed_value
        steps = parameter_container[frame].steps
        # Keyframes/Strength
        strength_value = parameter_container[frame].strength_value
        # Keyframes/CFG
        cfg_scale = parameter_container[frame].cfg_scale
        # Keyframes/3D/Motion
        cadence = parameter_container[frame].cadence
        should_use_optical_flow = parameter_container[frame].should_use_optical_flow
        cadence_flow_factor = parameter_container[frame].cadence_flow_factor
        generation_flow_factor = parameter_container[frame].generation_flow_factor
        for i in range(5):
            cn_weight[i] = parameter_container[frame].cn_weight[i]
            cn_stepstart[i] = parameter_container[frame].cn_stepstart[i]
            cn_stepend[i] = parameter_container[frame].cn_stepend[i]
            cn_lowt[i] = parameter_container[frame].cn_lowt[i]
            cn_hight[i] = parameter_container[frame].cn_hight[i]
            cn_udcn[i] = parameter_container[frame].cn_udcn[i]
        parseq_keys = parameter_container[frame].parseq_keys
        use_parseq = parameter_container[frame].use_parseq
        parseq_manifest = parameter_container[frame].parseq_manifest
        parseq_strength = parameter_container[frame].parseq_strength
        parseq_movements = parameter_container[frame].parseq_movements
        parseq_prompt = parameter_container[frame].parseq_prompt
        noise_multiplier = parameter_container[frame].noise_multiplier
        perlin_octaves = parameter_container[frame].perlin_octaves
        perlin_persistence = parameter_container[frame].perlin_persistence
        #frame_outdir = parameter_container[frame].frame_outdir
        #resume_timestring = parameter_container[frame].resume_timestring



def RecallValuesTemp(copyof_parameter_container):
    global serverShutDown
    global Prompt_Positive
    global Prompt_Negative
    global rotation_x
    global rotation_y
    global rotation_z
    global translation_x
    global translation_y
    global translation_z
    global deforum_translation_x
    global deforum_translation_y
    global deforum_translation_z
    global fov
    global cfg_scale
    global strength_value
    global steps
    global should_resume
    global start_frame
    global frame_outdir
    global resume_timestring
    global shouldPause
    global seed_value
    global did_seed_change
    global should_use_deforumation_strength
    global should_use_deforumation_cfg
    global cadence
    global should_use_deforumation_prompt_scheduling
    global cn_weight
    global cn_stepstart
    global cn_stepend
    global cn_lowt
    global cn_hight
    global cn_udcn
    global parseq_keys
    global use_parseq
    global parseq_manifest
    global parseq_strength
    global parseq_movements
    global deforum_rotation_x
    global deforum_rotation_y
    global deforum_rotation_z
    global deforum_fov
    global deforum_strength
    global deforum_cfg
    global deforum_steps
    global parseq_prompt
    global noise_multiplier
    global deforum_perlin_octaves
    global deforum_perlin_persistence
    global deforum_noise_multiplier
    global perlin_octaves
    global perlin_persistence
    global deforum_cadence
    global should_use_deforumation_cadence
    global should_use_deforumation_noise
    global should_use_deforumation_panning
    global should_use_deforumation_zoom
    global should_use_deforumation_fov
    global should_use_deforumation_rotation
    global should_use_deforumation_tilt
    global use_deforumation_cadence_scheduling
    global deforumation_cadence_scheduling_manifest
    global should_use_optical_flow
    global cadence_flow_factor
    global generation_flow_factor
    global translation_x_under_recall
    global translation_y_under_recall
    global translation_z_under_recall
    global rotation_x_under_recall
    global rotation_y_under_recall
    global rotation_z_under_recall

    if not should_use_total_recall_movements:
        #print("-Original translation_x is:" + str(copyof_parameter_container.translation_x))
        #print("--But sending:" + str(translation_x))
        #print("-Original translation_y is:" + str(copyof_parameter_container.translation_y))
        #print("--But sending:" + str(translation_y))
        copyof_parameter_container.rotation_x = rotation_x
        copyof_parameter_container.rotation_y = rotation_y
        copyof_parameter_container.rotation_z = rotation_z
        copyof_parameter_container.translation_x = translation_x
        #print("Total RecallValuesTemp: copyof_parameter_container.translation_x (" + str(copyof_parameter_container.translation_x) + ")")
        copyof_parameter_container.translation_y = translation_y
        copyof_parameter_container.translation_z = translation_z
        copyof_parameter_container.fov = fov
    else:
        copyof_parameter_container.rotation_x += rotation_x_under_recall
        #print("Total RecallValuesTemp (should_use_total_recall_movements): copyof_parameter_container.translation_x (" + str(copyof_parameter_container.translation_x) + ")")
        copyof_parameter_container.rotation_y += rotation_y_under_recall
        copyof_parameter_container.rotation_z += rotation_z_under_recall
        copyof_parameter_container.translation_x += translation_x_under_recall
        copyof_parameter_container.translation_y += translation_y_under_recall
        copyof_parameter_container.translation_z += translation_z_under_recall

    # prompt
    if not should_use_total_recall_prompt:
        #print("-Original prompt is:" + str(copyof_parameter_container.Prompt_Positive))
        #print("--But sending:" + str(Prompt_Positive))
        copyof_parameter_container.Prompt_Positive = Prompt_Positive
        copyof_parameter_container.Prompt_Negative = Prompt_Negative
    if not should_use_total_recall_others:
        # Other values
        # Run/Steps
        copyof_parameter_container.steps = steps
        # Keyframes/Strength
        copyof_parameter_container.strength_value = strength_value
        # Keyframes/CFG
        copyof_parameter_container.cfg_scale = cfg_scale

        # Keyframes/Field Of View/FOV schedule
        copyof_parameter_container.seed_value = seed_value

        copyof_parameter_container.cadence = cadence
        copyof_parameter_container.should_use_optical_flow = should_use_optical_flow
        copyof_parameter_container.cadence_flow_factor = cadence_flow_factor
        copyof_parameter_container.generation_flow_factor = generation_flow_factor
        for i in range(5):
            copyof_parameter_container.cn_weight[i] = cn_weight[i]
            copyof_parameter_container.cn_stepstart[i] = cn_stepstart[i]
            copyof_parameter_container.cn_stepend[i] = cn_stepend[i]
            copyof_parameter_container.cn_lowt[i] = cn_lowt[i]
            copyof_parameter_container.cn_hight[i] = cn_hight[i]
            copyof_parameter_container.cn_udcn[i] = cn_udcn[i]
        copyof_parameter_container.parseq_keys = parseq_keys
        copyof_parameter_container.use_parseq = use_parseq
        copyof_parameter_container.parseq_manifest = parseq_manifest
        copyof_parameter_container.parseq_strength = parseq_strength
        copyof_parameter_container.parseq_movements = parseq_movements
        copyof_parameter_container.parseq_prompt = parseq_prompt
        copyof_parameter_container.noise_multiplier = noise_multiplier
        copyof_parameter_container.perlin_octaves = perlin_octaves
        copyof_parameter_container.perlin_persistence = perlin_persistence
        # frame_outdir = parameter_container[frame].frame_outdir
        # resume_timestring = parameter_container[frame].resume_timestring
    return copyof_parameter_container
class ParameterContainer():
    #Values in the eyes of Deforum
    deforum_translation_x = 0
    deforum_translation_y = 0
    deforum_translation_z = 0
    deforum_rotation_x = 0
    deforum_rotation_y = 0
    deforum_rotation_z = 0
    deforum_fov = 70
    deforum_strength = 0.65
    deforum_cfg = 6.0
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
    cfg_scale = 6.0
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
    should_use_optical_flow = 0
    cadence_flow_factor = 1
    generation_flow_factor = 1
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
    def __init__(self):
        self.cn_weight = []
        self.cn_stepstart = []
        self.cn_stepend = []
        self.cn_lowt = []
        self.cn_hight = []
        self.cn_udcn = []
        for i in range(5):
            self.cn_weight.append(1.0)
            self.cn_stepstart.append(0.0)
            self.cn_stepend.append(1.0)
            self.cn_lowt.append(0)
            self.cn_hight.append(255)
            self.cn_udcn.append(0)

    def SetValues(self):
        # Set values that Deforum think it is working with
        self.deforum_translation_x = deforum_translation_x
        self.deforum_translation_y = deforum_translation_y
        self.deforum_translation_z = deforum_translation_z
        self.deforum_rotation_x = deforum_rotation_x
        self.deforum_rotation_y = deforum_rotation_y
        self.deforum_rotation_z = deforum_rotation_z
        self.deforum_fov = deforum_fov
        self.deforum_strength = deforum_strength
        self.deforum_cfg = deforum_cfg
        self.deforum_steps = deforum_steps
        self.deforum_cadence = deforum_cadence
        self.deforum_perlin_octaves = deforum_perlin_octaves
        self.deforum_perlin_persistence = deforum_perlin_persistence
        self.deforum_noise_multiplier = deforum_noise_multiplier
        # Run/Steps
        self.steps = steps
        # Keyframes/Strength
        self.strength_value = strength_value
        # Keyframes/CFG
        self.cfg_scale = cfg_scale
        # Keyframes/3D/Motion
        self.rotation_x = rotation_x
        self.rotation_y = rotation_y
        self.rotation_z = rotation_z
        self.translation_x = translation_x
        self.translation_y = translation_y
        self.translation_z = translation_z
        #print("Setting recall value translation_z:" + str(translation_z))
        self.should_use_deforumation_prompt_scheduling = should_use_deforumation_prompt_scheduling
        if should_use_before_deforum_prompt == 1 or should_use_after_deforum_prompt == 1:
            self.Prompt_Positive = positive_prompt_mixed
        else:
            self.Prompt_Positive = Prompt_Positive
            #print("setting prompt:" + str(Prompt_Positive))
        self.Prompt_Negative = Prompt_Negative
        self.positive_prompt_1 = positive_prompt_1
        self.positive_prompt_2 = positive_prompt_2
        self.negative_prompt_1 = negative_prompt_1
        self.positive_prompt_weight_1 = positive_prompt_weight_1
        self.positive_prompt_weight_2 = positive_prompt_weight_2
        self.seed_value = seed_value
        # Keyframes/Field Of View/FOV schedule
        self.fov = fov
        self.cadence = cadence
        self.should_use_optical_flow = should_use_optical_flow
        self.cadence_flow_factor = cadence_flow_factor
        self.generation_flow_factor = generation_flow_factor
        for i in range(5):
            self.cn_weight[i] = float(cn_weight[i])
            self.cn_stepstart[i] = float(cn_stepstart[i])
            self.cn_stepend[i] = float(cn_stepend[i])
            self.cn_lowt[i] = int(cn_lowt[i])
            self.cn_hight[i] = int(cn_hight[i])
            self.cn_udcn[i] = int(cn_udcn[i])
        self.parseq_keys = parseq_keys
        self.use_parseq = use_parseq
        self.parseq_manifest = parseq_manifest
        self.parseq_strength = parseq_strength
        self.parseq_movements = parseq_movements
        self.parseq_prompt = parseq_prompt
        self.noise_multiplier = noise_multiplier
        self.perlin_octaves = perlin_octaves
        self.perlin_persistence = perlin_persistence
        self.start_zero_pan_motion_x = start_zero_pan_motion_x
        self.start_zero_pan_motion_y = start_zero_pan_motion_y
        self.start_zero_pan_motion_z = start_zero_pan_motion_z
        self.start_zero_rotate_motion_x = start_zero_rotate_motion_x
        self.start_zero_rotate_motion_y = start_zero_rotate_motion_y
        self.start_zero_rotate_motion_z = start_zero_rotate_motion_z
        #self.self.frame_outdir = frame_outdir
        #self.self.resume_timestring = resume_timestring


def find_str(s, char):
    index = 0

    if char in s:
        c = char[0]
        for ch in s:
            if ch == c:
                if s[index:index + len(char)] == char:
                    return index

            index += 1

    return -1

def doSyrup():
    global start_zero_pan_motion_x
    global start_zero_pan_motion_y
    global start_zero_rotate_motion_x
    global start_zero_rotate_motion_y
    global start_zero_rotate_motion_z
    global start_zero_pan_motion_z

    global frame_idx
    global translation_x
    global translation_y
    global rotation_x
    global rotation_y
    global rotation_z
    global translation_z

    global start_prompt_morph_motion_container
    global deforumation_prompt_morph_container
    global current_prompt_morph_progressions

    # ZERO PAN X
    if len(prepared_zero_pan_motion_x) > 0:
        if start_zero_pan_motion_x == 1 and (frame_idx < (prepared_zero_pan_motion_x_start + len(prepared_zero_pan_motion_x))):
            if (frame_idx >= prepared_zero_pan_motion_x_start):
                motionIndex = frame_idx - prepared_zero_pan_motion_x_start
                if doVerbose:
                    print("Using Zero PanX at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_pan_motion_x)))
                    print("prepared_motion value is:" + str(prepared_zero_pan_motion_x[motionIndex]))
                translation_x = float(prepared_zero_pan_motion_x[motionIndex])
        elif start_zero_pan_motion_x == 1:
            start_zero_pan_motion_x = -1
            if doVerbose:
                print("0-Pan_X complete")
        elif start_zero_pan_motion_x == -2:
            start_zero_pan_motion_x = -1
            if doVerbose:
                print("0-Pan_X complete")

    # ZERO PAN Y
    if len(prepared_zero_pan_motion_y) > 0:
        if start_zero_pan_motion_y == 1 and (frame_idx < (prepared_zero_pan_motion_y_start + len(prepared_zero_pan_motion_y))):
            if (frame_idx >= prepared_zero_pan_motion_y_start):
                motionIndex = frame_idx - prepared_zero_pan_motion_y_start
                if doVerbose:
                    print("Using Zero PanY at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_pan_motion_y)))
                    print("prepared_motion value is:" + str(prepared_zero_pan_motion_y[motionIndex]))
                translation_y = float(prepared_zero_pan_motion_y[motionIndex])
        elif start_zero_pan_motion_y == 1:
            start_zero_pan_motion_y = -1
            if doVerbose:
                print("0-Pan_Y complete")
        elif start_zero_pan_motion_y == -2:
            start_zero_pan_motion_y = -1
            if doVerbose:
                print("0-Pan_Y complete")
    # ZERO ROTATION X
    if len(prepared_zero_rotate_motion_x) > 0:
        if start_zero_rotate_motion_x == 1 and (frame_idx < (prepared_zero_rotate_motion_x_start + len(prepared_zero_rotate_motion_x))):
            if (frame_idx >= prepared_zero_rotate_motion_x_start):
                motionIndex = frame_idx - prepared_zero_rotate_motion_x_start
                if doVerbose:
                    print("Using Zero RotateX at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_rotate_motion_x)))
                    print("prepared_motion value is:" + str(prepared_zero_rotate_motion_x[motionIndex]))
                rotation_x = float(prepared_zero_rotate_motion_x[motionIndex])
        elif start_zero_rotate_motion_x == 1:
            start_zero_rotate_motion_x = -1
            if doVerbose:
                print("0-Rotate_X complete")
        elif start_zero_rotate_motion_x == -2:
            start_zero_rotate_motion_x = -1
            if doVerbose:
                print("0-Rotate_X complete")

    # ZERO ROTATION Y
    if len(prepared_zero_rotate_motion_y) > 0:
        if start_zero_rotate_motion_y == 1 and (frame_idx < (prepared_zero_rotate_motion_y_start + len(prepared_zero_rotate_motion_y))):
            if (frame_idx >= prepared_zero_rotate_motion_y_start):
                motionIndex = frame_idx - prepared_zero_rotate_motion_y_start
                if doVerbose:
                    print("Using Zero RotateY at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_rotate_motion_y)))
                    print("prepared_motion value is:" + str(prepared_zero_rotate_motion_y[motionIndex]))
                rotation_y = float(prepared_zero_rotate_motion_y[motionIndex])
        elif start_zero_rotate_motion_y == 1:
            start_zero_rotate_motion_y = -1
            if doVerbose:
                print("0-Rotate_Y complete")
        elif start_zero_rotate_motion_y == -2:
            start_zero_rotate_motion_y = -1
            if doVerbose:
                print("0-Rotate_Y complete")

    # ZERO ROTATION Z
    if len(prepared_zero_rotate_motion_z) > 0:
        if start_zero_rotate_motion_z == 1 and (frame_idx < (prepared_zero_rotate_motion_z_start + len(prepared_zero_rotate_motion_z))):
            if (frame_idx >= prepared_zero_rotate_motion_z_start):
                motionIndex = frame_idx - prepared_zero_rotate_motion_z_start
                if doVerbose:
                    print("Using Zero Rotate> at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_rotate_motion_z)))
                    print("prepared_motion value is:" + str(prepared_zero_rotate_motion_z[motionIndex]))
                rotation_z = float(prepared_zero_rotate_motion_z[motionIndex])
        elif start_zero_rotate_motion_z == 1:
            start_zero_rotate_motion_z = -1
            if doVerbose:
                print("0-Rotate_Z complete")
        elif start_zero_rotate_motion_z == -2:
            start_zero_rotate_motion_z = -1
            if doVerbose:
                print("0-Rotate_Z complete")

    # ZERO ZOOM
    if len(prepared_zero_pan_motion_z) > 0:
        if start_zero_pan_motion_z == 1 and (frame_idx < (prepared_zero_pan_motion_z_start + len(prepared_zero_pan_motion_z))):
            if (frame_idx >= prepared_zero_pan_motion_z_start):
                motionIndex = frame_idx - prepared_zero_pan_motion_z_start
                if doVerbose:
                    print("Using Zero Zoom at frame " + str(frame_idx))
                    print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_pan_motion_z)))
                    print("prepared_motion value is:" + str(prepared_zero_pan_motion_z[motionIndex]))
                translation_z = float(prepared_zero_pan_motion_z[motionIndex])
        elif start_zero_pan_motion_z == 1:
            start_zero_pan_motion_z = -1
            if doVerbose:
                print("0-Zoom complete")
        elif start_zero_pan_motion_z == -2:
            start_zero_pan_motion_z = -1
            if doVerbose:
                print("0-Zoom complete")

    # ZERO PROMPT MORPH
    current_prompt_morph_progressions = []
    might_have_to_remove_these_prompt_morphs = []
    for morphs in prepare_prompt_morph_motion_container:
        if morphs in prepare_prompt_morph_motion_start_container:
            prepare_prompt_morph_motion_start_value = prepare_prompt_morph_motion_start_container[morphs]
        else:
            print("The motion has disappeared for morph:" + str(morphs) + ". This can happen if the an ongoing prompt morph is deleted while also doing a smooth motion that has not completed yet. Removing from container.")
            might_have_to_remove_these_prompt_morphs.append(morphs)
            continue
        if len(prepare_prompt_morph_motion_container[morphs]) > 0:
            if start_prompt_morph_motion_container[morphs] == 1 and (frame_idx < (prepare_prompt_morph_motion_start_value + len(prepare_prompt_morph_motion_container[morphs]))):
                if (frame_idx >= prepare_prompt_morph_motion_start_value):
                    motionIndex = frame_idx - prepare_prompt_morph_motion_start_value
                    if doVerbose:
                        print("Using Prompt Morph ("+str(morphs)+") syrup at frame " + str(frame_idx))
                        print("Which is step " + str(motionIndex + 1) + " in syrup motion out of " + str(len(prepare_prompt_morph_motion_container[morphs])))
                        print("prepared_motion value for ("+str(morphs)+") is:" + str(prepare_prompt_morph_motion_container[morphs][motionIndex]))
                    deforumation_prompt_morph_container[morphs] = float(prepare_prompt_morph_motion_container[morphs][motionIndex])
                    #Prepare the progress status array
                    current_step_progress = motionIndex #frame_idx - prepare_prompt_morph_motion_start_container[morphs]  # prepared_zero_pan_motion_z_start
                    current_total_steps = len(prepare_prompt_morph_motion_container[morphs])  # len(prepared_zero_pan_motion_z)
                    current_prompt_morph_progressions.append((morphs, current_step_progress, current_total_steps, deforumation_prompt_morph_container[morphs]))

            elif start_prompt_morph_motion_container[morphs] == 1:
                start_prompt_morph_motion_container[morphs] = -1
                if doVerbose:
                    print("0-morph motion "+str(morphs)+" complete")
            elif start_prompt_morph_motion_container[morphs] == -2:
                start_prompt_morph_motion_container[morphs] = -1
                if doVerbose:
                    print("0-morph motion "+str(morphs)+" complete")
    #Clean old morphs
    for morph in might_have_to_remove_these_prompt_morphs:
        if morph in prepare_prompt_morph_motion_container:
            del prepare_prompt_morph_motion_container[morph]
            print("Cleaned up old morph:" + str(morph))



def replace_with_prompt_morph_bindings(promptItem):
    #prompt_morphing_container contains the array [promptA, promptB, isPromptBlending, is_enabled, current_value]
    modified_prompt = promptItem
    for morphFrame in prompt_morphing_container:#prepare_prompt_morph_motion_container:
        is_enabled = prompt_morphing_container[morphFrame][3] #not self.prompt_morphing_container[morphFrame].morph_prompt_enabled
        if not is_enabled:
            continue
        binding = morphFrame #self.prompt_morphing_container[morphFrame].morph_prompt_binding.text()
        #print("Binding:" + str(binding))
        if binding == "":
            continue
        if prompt_morphing_container[morphFrame][2]: #.isPromptBlending:
            promptA = prompt_morphing_container[morphFrame][0] #.morph_promptA.text()
            promptB = prompt_morphing_container[morphFrame][1] #.morph_promptB.text()
            shouldContinue = True
            if promptA == "":
                #print("No promptA found for morphFrame " + "{{" + str(binding) + "}}")
                shouldContinue = False
            if promptB == "":
                #print("No promptB found for morphFrame " + "{{" + str(binding) + "}}")
                shouldContinue = False
            if shouldContinue == False:
                modified_prompt = modified_prompt.replace("{{" + binding + "}}", "")
                #print("Modified text:" + str(modified_prompt))
                continue
            #motionIndex = frame_idx - prepare_prompt_morph_motion_start_container[morphFrame]
            #prepare_prompt_morph_motion_container[morphFrame][motionIndex]
            if morphFrame in deforumation_prompt_morph_container:
                prompt_value = deforumation_prompt_morph_container[morphFrame] #self.prompt_morphing_container[morphFrame].morph_prompt_value.text()
            else:
                prompt_value = prompt_morphing_container[morphFrame][4]
                deforumation_prompt_morph_container[morphFrame] = prompt_value
            substituedText = "[" + promptB + ":" + promptA + ":" + str(prompt_value) + "]"
            #print("Substituting {{" + str(binding) + "}}, with " + str(substituedText))
        else:
            promptA = prompt_morphing_container[morphFrame][0] #.morph_promptA.text()
            if promptA == "":
                #print("No promptA found for morphFrame " + "{{" + str(binding) + "}}")
                modified_prompt = modified_prompt.replace("{{" + binding + "}}", "")
                #print("Modified text:" + str(modified_prompt))
                continue
            if morphFrame in deforumation_prompt_morph_container:
                prompt_value = deforumation_prompt_morph_container[morphFrame] #prompt_morphing_container[morphFrame].morph_prompt_value.text()
            else:
                prompt_value = prompt_morphing_container[morphFrame][4]
                deforumation_prompt_morph_container[morphFrame] = prompt_value
            substituedText = "(" + promptA + ":" + str(prompt_value) + ")"
            #print("Substituting {{" + str(binding) + "}}, with " + str(substituedText))


        #print("Original text:" + promptItem)
        modified_prompt = modified_prompt.replace("{{" + binding + "}}", substituedText)
        #print("Modified text:" + str(modified_prompt))

    #pattern = re.escape("\{\{.*\}\}")
    match = re.findall(r'\{\{(.*?)\}\}',modified_prompt) #re.search(pattern, modified_prompt)
    for matchings in match:
        modified_prompt = modified_prompt.replace("{{" + matchings + "}}", "")
    return modified_prompt

async def handleMesssage(arr, pipe = None, pipeName = None, websocketCommunication = None):
    global serverShutDown
    global Prompt_Positive
    global Prompt_Negative
    global positive_prompt_mixed
    global rotation_x
    global rotation_y
    global rotation_z
    global translation_x
    global translation_y
    global translation_z
    global deforum_translation_x
    global deforum_translation_y
    global deforum_translation_z
    global fov
    global cfg_scale
    global strength_value
    global steps
    global should_resume
    global start_frame
    global frame_outdir
    global resume_timestring
    global shouldPause
    global seed_value
    global did_seed_change
    global should_use_deforumation_strength
    global should_use_deforumation_cfg
    global cadence
    global should_use_deforumation_prompt_scheduling
    global should_use_before_deforum_prompt
    global should_use_after_deforum_prompt
    global cn_weight
    global cn_stepstart
    global cn_stepend
    global cn_lowt
    global cn_hight
    global parseq_keys
    global use_parseq
    global parseq_manifest
    global parseq_strength
    global parseq_movements
    global deforum_rotation_x
    global deforum_rotation_y
    global deforum_rotation_z
    global deforum_fov
    global deforum_strength
    global deforum_cfg
    global deforum_steps
    global parseq_prompt
    global noise_multiplier
    global deforum_perlin_octaves
    global deforum_perlin_persistence
    global deforum_noise_multiplier
    global perlin_octaves
    global perlin_persistence
    global deforum_cadence
    global should_use_deforumation_cadence
    global should_use_deforumation_noise
    global should_use_deforumation_panning
    global should_use_deforumation_zoom
    global should_use_deforumation_fov
    global should_use_deforumation_rotation
    global should_use_deforumation_tilt
    global use_deforumation_cadence_scheduling
    global deforumation_cadence_scheduling_manifest
    global should_use_optical_flow
    global deforumation_graph
    global should_use_deforumation_graph
    global deforumation_graph_xshift
    global cadence_flow_factor
    global generation_flow_factor
    global should_use_total_recall
    global total_recall_from
    global total_recall_to
    global Prompt_Positive_touched
    global translation_x_under_recall
    global translation_y_under_recall
    global translation_z_under_recall
    global rotation_x_under_recall
    global rotation_y_under_recall
    global rotation_z_under_recall
    global should_use_deforumation_timestring
    global should_use_total_recall_prompt
    global parameter_container
    global number_of_recalled_frames
    global should_use_total_recall_movements
    global should_use_total_recall_prompt
    global should_use_total_recall_others
    global deforum_interrupted
    global start_motion
    global prepared_motion
    global prepared_motion_start
    global motion_current_status_string
    global prepared_zero_pan_motion
    global prepared_zero_pan_motion_x
    global prepared_zero_pan_motion_y
    global prepared_zero_rotate_motion_x
    global prepared_zero_rotate_motion_y
    global prepared_zero_rotate_motion_z
    global prepared_zero_pan_motion_z
    global prepared_zero_zoom_motion
    global prepared_zero_rotation_motion
    global prepared_zero_tilt_motion
    global start_zero_pan_motion
    global prepared_zero_pan_motion_start
    global prepared_zero_rotate_motion_start
    global prepared_zero_pan_motion_x_start
    global prepared_zero_pan_motion_y_start
    global prepared_zero_rotate_motion_x_start
    global prepared_zero_rotate_motion_y_start
    global prepared_zero_rotate_motion_z_start
    global prepared_zero_pan_motion_z_start
    global start_zero_zoom_motion
    global prepared_zero_zoom_motion_start
    global start_zero_rotation_motion
    global prepared_zero_rotation_motion_start
    global prepared_zero_tilt_motion_start
    global start_zero_tilt_motion
    global start_zero_pan_motion_x
    global start_zero_pan_motion_y
    global start_zero_rotate_motion_x
    global start_zero_rotate_motion_y
    global start_zero_rotate_motion_z
    global start_zero_pan_motion_z
    global motion_current_zero_pan_string
    global motion_current_zero_pan_x_string
    global motion_current_zero_pan_y_string
    global motion_current_zero_zoom_string
    global motion_current_zero_rotate_string
    global motion_current_zero_tilt_string
    global number_of_generated_images
    global frame_idx
    global positive_prompt_weight_1
    global positive_prompt_weight_2
    global positive_prompt_1
    global positive_prompt_2
    global negative_prompt_1
    global ShouldBeRunning
    global deforumation_prompt_morph_container
    global prepare_prompt_morph_motion_container
    global start_prompt_morph_motion_container
    global prepare_prompt_morph_motion_start_container
    global prompt_morphing_container
    global current_prompt_morph_progressions
    global seed_behavior
    global seed_iter_n
    global render_loopback

    totalToSend = []

    shouldWrite = arr[0]
    parameter = arr[1]
    value = arr[2]
    should_return_many = False
    should_unpack_block = False
    original_parameter = None  # Just to get rid of (this parameter might not have been set yet)
    original_value = None  # Just to get rid of (this parameter might not have been set yet)
    if not type(parameter) is str:
        should_return_many = True
        number_of_blocks = len(parameter)
        original_parameter = parameter
    elif str(parameter) == "<BLOCK>":
        # print("Number of blocks in block:"+str(len(value)))
        number_of_blocks = len(value)
        should_unpack_block = True
        original_value = value
    else:
        number_of_blocks = 1

    for block_index in range(0, number_of_blocks):
        if should_return_many:
            shouldWrite = 0
            parameter = original_parameter[block_index]
            # print("return manny, add:" + str(parameter))
            value = 0
        elif should_unpack_block:
            arr = pickle.loads(original_value[block_index])
            if len(arr) == 3:
                shouldWrite = arr[0]
                parameter = arr[1]
                value = arr[2]
                # print("Writing param: " + parameter)
            else:
                if doVerbose:
                    if isWindows and websocketCommunication == None:
                        win32file.WriteFile(pipe, b"ERROR")
                    else:
                        await websocketCommunication.send("ERROR")
                break
        # Prompts Params
        ###########################################################################
        if str(parameter) == "is_paused_rendering":
            if shouldWrite:
                shouldPause = int(value)
            else:
                if doVerbose:
                    print("is_paused_rendering:" + str(shouldPause))
                totalToSend.append((str(shouldPause)))
        elif str(parameter) == "total_recall_relive":
            frame_idx = int(value)
            if should_use_total_recall and (frame_idx >= total_recall_from and frame_idx <= total_recall_to):
                print("total_recall_relive at frame number:" + str(frame_idx))
                RecallValues(frame_idx)
                print("This means we set translation_z to:" + str(translation_z))
            else:
                if start_motion and (frame_idx >= prepared_motion_start) and (
                        frame_idx < (prepared_motion_start + len(prepared_motion))):
                    motionIndex = frame_idx - prepared_motion_start
                    # print("---------------------------------------")
                    # print("Using pre-defined motion at frame: " + str(frame_idx))
                    # print("Which is step " + str(motionIndex + 1) + " in motions out of " + str(
                    #    len(prepared_motion)))
                    # print("prepared_motion:" + str(prepared_motion[motionIndex]))
                    # print("---------------------------------------")
                    motion_current_status_string = "P-D Motion: " + str(motionIndex + 1) + "/" + str(
                        len(prepared_motion))
                    motions = prepared_motion[motionIndex]
                    translation_x = float(motions[0])
                    translation_y = float(motions[1])
                    translation_z = float(motions[2])
                    rotation_x = float(motions[4])
                    rotation_y = float(motions[3])
                    rotation_z = float(motions[5])
                elif start_motion:
                    start_motion = 0
                    prepared_motion_start = -1
                    prepared_motion = []
                    print(
                        "Motion was active, but has now been canceled/stopped, at frame: " + str(frame_idx))
                    motion_current_status_string = "P-D Motion: None"
                elif not start_motion:
                    motion_current_status_string = "P-D Motion: None"
                    prepared_motion = []

                    # ZERO ZOOM - READ VALUES FROM PREPARED ZOOM ARRAY IN CORRECT ORDER
                    if len(prepared_zero_zoom_motion) > 0:
                        if start_zero_zoom_motion == 1 and (frame_idx < (prepared_zero_zoom_motion_start + len(prepared_zero_zoom_motion))):
                            if (frame_idx >= prepared_zero_zoom_motion_start):
                                motionIndex = frame_idx - prepared_zero_zoom_motion_start
                                # print("Using Zero Zoom at frame " +str(frame_idx))
                                # print("Which is step " + str(motionIndex+1) + " in zoom motions out of " + str(len(prepared_zero_zoom_motion)))
                                # print("prepared_motion value is:" + str(prepared_zero_zoom_motion[motionIndex]))
                                translation_z = float(prepared_zero_zoom_motion[motionIndex])
                                motion_current_zero_zoom_string = "0-Zoom:" + str(
                                    motionIndex + 1) + "/" + str(len(prepared_zero_zoom_motion))
                        elif start_zero_zoom_motion == 1:
                            start_zero_zoom_motion = -1
                            motion_current_zero_zoom_string = "0-Zoom: None"
                            print("0-Zoom complete")

                    # ZERO PAN X- READ VALUES FROM PREPARED PAN X ARRAY IN CORRECT ORDER
                    if len(prepared_zero_pan_motion_x) > 0:
                        if start_zero_pan_motion_x == 1 and (frame_idx < (
                                prepared_zero_pan_motion_x_start + len(prepared_zero_pan_motion_x))):
                            if (frame_idx >= prepared_zero_pan_motion_x_start):
                                motionIndex = frame_idx - prepared_zero_pan_motion_x_start
                                print("Using Zero PanX at frame " + str(frame_idx))
                                print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_pan_motion_x)))
                                print("prepared_motion value is:" + str(prepared_zero_pan_motion_x[motionIndex]))
                                translation_x = float(prepared_zero_pan_motion_x[motionIndex])
                                motion_current_zero_pan_x_string = "0-Pan_X:" + str(motionIndex + 1) + "/" + str(len(prepared_zero_pan_motion_x))
                        elif start_zero_pan_motion_x == 1:
                            start_zero_pan_motion_x = -1
                            motion_current_zero_pan_x_string = "0-Pan_X: None"
                            print("0-Pan_X complete")
                        elif start_zero_pan_motion_x == -2:
                            start_zero_pan_motion_x = -1
                            motion_current_zero_pan_x_string = "0-Pan_X: None"
                            print("0-Pan_X complete")

                    # ZERO PAN Y- READ VALUES FROM PREPARED PAN X ARRAY IN CORRECT ORDER
                    if len(prepared_zero_pan_motion_y) > 0:
                        if start_zero_pan_motion_y == 1 and (frame_idx < (prepared_zero_pan_motion_y_start + len(prepared_zero_pan_motion_y))):
                            if (frame_idx >= prepared_zero_pan_motion_y_start):
                                motionIndex = frame_idx - prepared_zero_pan_motion_y_start
                                print("Using Zero PanY at frame " + str(frame_idx))
                                print("Which is step " + str(motionIndex + 1) + " in pan motions out of " + str(len(prepared_zero_pan_motion_y)))
                                print("prepared_motion value is:" + str(prepared_zero_pan_motion_y[motionIndex]))
                                translation_y = float(prepared_zero_pan_motion_y[motionIndex])
                                motion_current_zero_pan_y_string = "0-Pan_Y:" + str(motionIndex + 1) + "/" + str(len(prepared_zero_pan_motion_y))
                        elif start_zero_pan_motion_y == 1:
                            start_zero_pan_motion_y = -1
                            motion_current_zero_pan_y_string = "0-Pan_Y: None"
                            print("0-Pan_Y complete")
                        elif start_zero_pan_motion_y == -2:
                            start_zero_pan_motion_y = -1
                            motion_current_zero_pan_y_string = "0-Pan_Y: None"
                            print("0-Pan_Y complete")

                    # ZERO PAN - READ VALUES FROM PREPARED PAN ARRAY IN CORRECT ORDER
                    if len(prepared_zero_pan_motion) > 0:
                        if start_zero_pan_motion == 1 and (frame_idx < (prepared_zero_pan_motion_start + len(prepared_zero_pan_motion[0]))):
                            if (frame_idx >= prepared_zero_pan_motion_start):
                                motionIndex = frame_idx - prepared_zero_pan_motion_start
                                # print("Using Zero Pan at frame " +str(frame_idx))
                                # print("Which is step " + str(motionIndex+1) + " in pan motions out of " + str(len(prepared_zero_pan_motion[0])))
                                # print("prepared_motion value is X-value:" + str(prepared_zero_pan_motion[0][motionIndex]))
                                # print("prepared_motion value is Y-value:" + str(prepared_zero_pan_motion[1][motionIndex]))
                                translation_x = float(prepared_zero_pan_motion[0][motionIndex])
                                translation_y = float(prepared_zero_pan_motion[1][motionIndex])
                                motion_current_zero_pan_string = "0-Pan:" + str(
                                    motionIndex + 1) + "/" + str(len(prepared_zero_pan_motion[0]))
                        elif start_zero_pan_motion == 1:
                            start_zero_pan_motion = -1
                            motion_current_zero_pan_string = "0-Pan: None"
                            print("0-Pan complete")

                    # ZERO ROTATION - READ VALUES FROM PREPARED ROTATION ARRAY IN CORRECT ORDER
                    if len(prepared_zero_rotation_motion) > 0:
                        if start_zero_rotation_motion == 1 and (frame_idx < (prepared_zero_rotation_motion_start + len(prepared_zero_rotation_motion[0]))):
                            if (frame_idx >= prepared_zero_rotation_motion_start):
                                motionIndex = frame_idx - prepared_zero_rotation_motion_start
                                # print("Using Zero Rotation at frame " +str(frame_idx))
                                # print("Which is step " + str(motionIndex+1) + " in pan motions out of " + str(len(prepared_zero_rotation_motion[0])))
                                # print("prepared_motion value is X-value:" + str(prepared_zero_rotation_motion[0][motionIndex]))
                                # print("prepared_motion value is Y-value:" + str(prepared_zero_rotation_motion[1][motionIndex]))
                                rotation_x = float(prepared_zero_rotation_motion[0][motionIndex])
                                rotation_y = float(prepared_zero_rotation_motion[1][motionIndex])
                                motion_current_zero_rotate_string = "0-Rotation:" + str(motionIndex + 1) + "/" + str(len(prepared_zero_rotation_motion[0]))
                        elif start_zero_rotation_motion == 1:
                            start_zero_rotation_motion = -1
                            motion_current_zero_rotate_string = "0-Rotation: None"
                            print("0-Rotation complete")

                    # ZERO TILT - READ VALUES FROM PREPARED TILT ARRAY IN CORRECT ORDER
                    if len(prepared_zero_tilt_motion) > 0:
                        if start_zero_tilt_motion == 1 and (frame_idx < (prepared_zero_tilt_motion_start + len(prepared_zero_tilt_motion))):
                            if (frame_idx >= prepared_zero_tilt_motion_start):
                                motionIndex = frame_idx - prepared_zero_tilt_motion_start
                                # print("Using Zero Tilt at frame " +str(frame_idx))
                                # print("Which is step " + str(motionIndex+1) + " in tilt motions out of " + str(len(prepared_zero_tilt_motion)))
                                # print("prepared_motion value is:" + str(prepared_zero_tilt_motion[motionIndex]))
                                rotation_z = float(prepared_zero_tilt_motion[motionIndex])
                                motion_current_zero_tilt_string = "0-Tilt:" + str(motionIndex + 1) + "/" + str(len(prepared_zero_tilt_motion))
                        elif start_zero_tilt_motion == 1:
                            start_zero_tilt_motion = -1
                            motion_current_zero_tilt_string = "0-Tilt: None"
                            print("0-Tilt complete")

        elif str(parameter) == "deforum_panmotion_x_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_pan_x_string)))
        elif str(parameter) == "deforum_panmotion_y_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_pan_y_string)))
        elif str(parameter) == "deforum_panmotion_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_pan_string)))
        elif str(parameter) == "deforum_zoommotion_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_zoom_string)))
        elif str(parameter) == "deforum_rotationmotion_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_rotate_string)))
        elif str(parameter) == "deforum_tiltmotion_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_zero_tilt_string)))
        elif str(parameter) == "deforum_pdmotion_status":
            if not shouldWrite:
                totalToSend.append((str(motion_current_status_string)))
        elif str(parameter) == "should_erase_total_recall_memory":
            if shouldWrite:
                parameter_container.clear()
                number_of_recalled_frames = 0
                print("The total recall memory has been cleared.")
        elif str(parameter) == "should_use_deforumation_timestring":
            if shouldWrite:
                should_use_deforumation_timestring = int(value)
            else:
                if doVerbose:
                    print("should_use_deforumation_timestring:" + str(should_use_deforumation_timestring))
                totalToSend.append((str(should_use_deforumation_timestring)))
        elif str(parameter) == "should_use_total_recall_prompt":
            if shouldWrite:
                should_use_total_recall_prompt = int(value)
                if should_use_total_recall_prompt:
                    print("Manual Prompt has been Allowed!")
                else:
                    print("Manual Prompt has been Dis-Allowed!")
            else:
                if doVerbose:
                    print("should_use_total_recall_prompt:" + str(should_use_total_recall_prompt))
                totalToSend.append((str(should_use_total_recall_prompt)))
        elif str(parameter) == "should_use_total_recall_movements":
            if shouldWrite:
                should_use_total_recall_movements = int(value)
                if not should_use_total_recall_movements:
                    print("Manual Movements has been Allowed!")
                else:
                    print("Manual Movements has been Dis-Allowed!")
            else:
                if doVerbose:
                    print("should_use_total_recall_movements:" + str(should_use_total_recall_movements))
                totalToSend.append((str(should_use_total_recall_movements)))
        elif str(parameter) == "should_use_total_recall_others":
            if shouldWrite:
                should_use_total_recall_others = int(value)
                if not should_use_total_recall_others:
                    print("Manual Others has been Allowed!")
                else:
                    print("Manual Others has been Dis-Allowed!")
            else:
                if doVerbose:
                    print("should_use_total_recall_others:" + str(should_use_total_recall_others))
                totalToSend.append((str(should_use_total_recall_others)))

        elif str(parameter) == "should_use_total_recall":
            if shouldWrite:
                should_use_total_recall = int(value)
                Prompt_Positive_touched = 0
                if should_use_total_recall == 1:
                    translation_x_under_recall = 0
                    translation_y_under_recall = 0
                    translation_z_under_recall = 0
                    rotation_x_under_recall = 0
                    rotation_y_under_recall = 0
                    rotation_z_under_recall = 0
            else:
                if doVerbose:
                    print("should_use_total_recall:" + str(should_use_total_recall))
                totalToSend.append((str(should_use_total_recall)))
        elif str(parameter) == "is_inside_total_recall_range":
            if not shouldWrite:
                if should_use_total_recall and ((start_frame >= total_recall_from) and (start_frame <= total_recall_to)):
                    # print("Returning that it is inside TOTAL RECALL RANGE, frame:"+str(start_frame))
                    # print("total_recall_from and to:"+ str(total_recall_from) + " -> " + str(total_recall_to))
                    totalToSend.append((str("1")))
                else:
                    totalToSend.append((str("0")))
        elif str(parameter) == "total_recall_from":
            if shouldWrite:
                total_recall_from = int(value)
            else:
                if doVerbose:
                    print("total_recall_from:" + str(total_recall_from))
                totalToSend.append((str(total_recall_from)))
        elif str(parameter) == "total_recall_to":
            if shouldWrite:
                total_recall_to = int(value)
            else:
                if doVerbose:
                    print("total_recall_to:" + str(total_recall_to))
                totalToSend.append((str(total_recall_to)))
        elif str(parameter) == "should_use_deforumation_prompt_scheduling":
            if shouldWrite:
                should_use_deforumation_prompt_scheduling = value
            else:
                if doVerbose:
                    print("should_use_deforumation_prompt_scheduling:" + str(
                        should_use_deforumation_prompt_scheduling))
                totalToSend.append((str(should_use_deforumation_prompt_scheduling)))
        elif str(parameter) == "should_use_before_deforum_prompt":
            if shouldWrite:
                should_use_before_deforum_prompt = value
            else:
                if doVerbose:
                    print("should_use_before_deforum_prompt:" + str(should_use_before_deforum_prompt))
                totalToSend.append((str(should_use_before_deforum_prompt)))
        elif str(parameter) == "should_use_after_deforum_prompt":
            if shouldWrite:
                should_use_after_deforum_prompt = value
            else:
                if doVerbose:
                    print("should_use_after_deforum_prompt:" + str(should_use_after_deforum_prompt))
                totalToSend.append((str(should_use_after_deforum_prompt)))
        elif str(parameter) == "use_deforumation_cadence_scheduling":
            if shouldWrite:
                use_deforumation_cadence_scheduling = value
            else:
                if doVerbose:
                    print("use_deforumation_cadence_scheduling:" + str(use_deforumation_cadence_scheduling))
                totalToSend.append((str(use_deforumation_cadence_scheduling)))
        elif str(parameter) == "deforumation_cadence_scheduling_manifest":
            if shouldWrite:
                deforumation_cadence_scheduling_manifest = value
            else:
                if doVerbose:
                    print("deforumation_cadence_scheduling_manifest:" + str(
                        deforumation_cadence_scheduling_manifest))
                totalToSend.append((str(deforumation_cadence_scheduling_manifest)))
        elif str(parameter) == "positive_prompt_weight_1":
            if shouldWrite:
                positive_prompt_weight_1 = value
            else:
                if doVerbose:
                    print("positive_prompt_weight_1:" + str(positive_prompt_weight_1))
                totalToSend.append((str(positive_prompt_weight_1)))
        elif str(parameter) == "positive_prompt_weight_2":
            if shouldWrite:
                positive_prompt_weight_2 = value
            else:
                if doVerbose:
                    print("positive_prompt_weight_2:" + str(positive_prompt_weight_2))
                totalToSend.append((str(positive_prompt_weight_2)))
        elif str(parameter) == "positive_prompt_1":
            if shouldWrite:
                positive_prompt_1 = value
                # print("Writing the positive_prompt:" + str(Prompt_Positive))
            else:
                if doVerbose:
                    print("positive_prompt_1:" + str(positive_prompt_1))
                totalToSend.append((str(positive_prompt_1)))
        elif str(parameter) == "positive_prompt_2":
            if shouldWrite:
                positive_prompt_2 = value
                # print("Writing the positive_prompt:" + str(Prompt_Positive))
            else:
                if doVerbose:
                    print("positive_prompt_2:" + str(positive_prompt_2))
                totalToSend.append((str(positive_prompt_2)))
        elif str(parameter) == "negative_prompt_1":
            if shouldWrite:
                negative_prompt_1 = value
                # print("Writing the positive_prompt:" + str(Prompt_Positive))
            else:
                if doVerbose:
                    print("negative_prompt_1:" + str(negative_prompt_1))
                totalToSend.append((str(negative_prompt_1)))
        elif str(parameter) == "positive_prompt":
            if shouldWrite:
                Prompt_Positive = value
                # print("Writing the positive_prompt:" + str(Prompt_Positive))
            else:
                if doVerbose:
                    print("positive_prompt:" + str(Prompt_Positive))
                modified_prompt = replace_with_prompt_morph_bindings(str(Prompt_Positive))
                totalToSend.append((str(modified_prompt)))
                #totalToSend.append((str(Prompt_Positive)))
        elif str(parameter) == "negative_prompt":
            if shouldWrite:
                Prompt_Negative = value
            else:
                if doVerbose:
                    print("negative_prompt:" + str(Prompt_Negative))
                modified_prompt = replace_with_prompt_morph_bindings(str(Prompt_Negative))
                totalToSend.append((str(modified_prompt)))
                #totalToSend.append((str(Prompt_Negative)))
        elif str(parameter) == "positive_prompt_mixed":
            if shouldWrite:
                positive_prompt_mixed = value
            else:
                if doVerbose:
                    print("positive_prompt_mixed:" + str(positive_prompt_mixed))
                totalToSend.append((str(positive_prompt_mixed)))
        elif str(parameter) == "prompts_touched":
            # if should_use_total_recall == 1:
            #    Prompt_Positive_touched = 1
            #    print("Changing prompt for ever for total recall")
            empty = 0
        # Translation Params
        ###########################################################################
        elif str(parameter) == "translation_x":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    translation_x = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        translation_x_under_recall = float(value)
                        print("Received translation_x_under_recall: " + str(translation_x_under_recall))
                    else:
                        translation_x = float(value)
            else:
                if doVerbose:
                    print("sending translation_x:" + str(translation_x))
                if should_use_deforumation_graph["PanLR"]:
                    xshift = deforumation_graph_xshift["PanLR"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["PanLR"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["PanLR"][realIdx]
                            #print("Sending PanLR value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["PanLR"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(translation_x)))

        elif str(parameter) == "translation_y":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    translation_y = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        translation_y_under_recall = float(value)
                    else:
                        translation_y = float(value)
            else:
                if doVerbose:
                    print("sending translation_y:" + str(translation_y))
                if should_use_deforumation_graph["PanUD"]:
                    xshift = deforumation_graph_xshift["PanUD"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["PanUD"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["PanUD"][realIdx]
                            #print("Sending PanUD value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["PanUD"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(translation_y)))

        elif str(parameter) == "translation_z":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    translation_z = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        translation_z_under_recall = float(value)
                    else:
                        translation_z = float(value)
            else:
                if doVerbose:
                    print("sending translation_z:" + str(translation_z))
                if should_use_deforumation_graph["Zoom"]:
                    xshift = deforumation_graph_xshift["Zoom"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["Zoom"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["Zoom"][realIdx]
                            #print("Sending zoom value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["Zoom"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(translation_z)))
        # What Deforum thinks it has for Translation
        elif str(parameter) == "deforum_translation_x":
            if shouldWrite:
                deforum_translation_x = float(value)
            else:
                if doVerbose:
                    print("sending deforum_translation_x:" + str(deforum_translation_x))
                # totalToSend.append((str(deforum_translation_x)))
                totalToSend.append(str(deforum_translation_x))
        elif str(parameter) == "deforum_translation_y":
            if shouldWrite:
                deforum_translation_y = float(value)
            else:
                if doVerbose:
                    print("sending deforum_translation_y:" + str(deforum_translation_y))
                # totalToSend.append((str(deforum_translation_y)))
                totalToSend.append(str(deforum_translation_y))
        elif str(parameter) == "deforum_translation_z":
            if shouldWrite:
                deforum_translation_z = float(value)
            else:
                if doVerbose:
                    print("sending deforum_translation_z:" + str(deforum_translation_z))
                # totalToSend.append((str(deforum_translation_z)))
                totalToSend.append(str(deforum_translation_z))
        # What Deforum thinks it has for Rotation
        elif str(parameter) == "deforum_rotation_x":
            if shouldWrite:
                deforum_rotation_x = float(value)
            else:
                if doVerbose:
                    print("sending deforum_rotation_x:" + str(deforum_rotation_x))
                totalToSend.append((str(deforum_rotation_x)))
        elif str(parameter) == "deforum_rotation_y":
            if shouldWrite:
                deforum_rotation_y = float(value)
            else:
                if doVerbose:
                    print("sending deforum_translation_y:" + str(deforum_rotation_y))
                totalToSend.append((str(deforum_rotation_y)))
        elif str(parameter) == "deforum_rotation_z":
            if shouldWrite:
                deforum_rotation_z = float(value)
            else:
                if doVerbose:
                    print("sending deforum_rotation_z:" + str(deforum_rotation_z))
                totalToSend.append((str(deforum_rotation_z)))
        # Rotation Params
        ###########################################################################
        elif str(parameter) == "rotation_x":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    rotation_x = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        rotation_x_under_recall = float(value)
                    else:
                        rotation_x = float(value)
                # print("writing rotation_x:" + str(rotation_x))
                # time.sleep(20)
            else:
                if doVerbose:
                    print("sending rotation_x:" + str(rotation_x))
                if should_use_deforumation_graph["RotateV"]:
                    xshift = deforumation_graph_xshift["RotateV"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["RotateV"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["RotateV"][realIdx]
                            #print("Sending RotateV value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["RotateV"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(rotation_x)))
        elif str(parameter) == "rotation_y":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    rotation_y = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        rotation_y_under_recall = float(value)
                    else:
                        rotation_y = float(value)
            else:
                if doVerbose:
                    print("sending rotation_y:" + str(rotation_y))
                if should_use_deforumation_graph["RotateH"]:
                    xshift = deforumation_graph_xshift["RotateH"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["RotateH"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["RotateH"][realIdx]
                            #print("Sending RotateH value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["RotateH"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(rotation_y)))
        elif str(parameter) == "rotation_z":
            if shouldWrite:
                if not should_use_total_recall or (should_use_total_recall and not should_use_total_recall_movements):
                    rotation_z = float(value)
                else:
                    if (start_frame >= total_recall_from and start_frame <= total_recall_to):
                        rotation_z_under_recall = float(value)
                    else:
                        rotation_z = float(value)
            else:
                if doVerbose:
                    print("sending rotation_z:" + str(rotation_z))
                if should_use_deforumation_graph["Tilt"]:
                    xshift = deforumation_graph_xshift["Tilt"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["Tilt"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_graph = deforumation_graph["Tilt"][realIdx]
                            #print("Sending Tilt value to deforum:" + str(value_from_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_graph)))
                        else:
                            value_from_graph = deforumation_graph["Tilt"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_graph)))
                else:
                    totalToSend.append((str(rotation_z)))
        # FOV Params
        ###########################################################################
        elif str(parameter) == "fov":
            if shouldWrite:
                fov = float(value)
            else:
                if doVerbose:
                    print("sending fov:" + str(fov))
                totalToSend.append((str(fov)))
        # what Deforum think it has
        ###########################################################################
        elif str(parameter) == "deforum_fov":
            if shouldWrite:
                deforum_fov = float(value)
            else:
                if doVerbose:
                    print("sending deforum_fov:" + str(deforum_fov))
                totalToSend.append((str(deforum_fov)))
        # CFG Params
        ###########################################################################
        elif str(parameter) == "cfg":
            if shouldWrite:
                cfg_scale = float(value)
            else:
                if doVerbose:
                    print("sending CFG:" + str(cfg_scale))
                totalToSend.append((str(cfg_scale)))
        # What Deforum think the CFG Value is
        ###########################################################################
        elif str(parameter) == "deforum_cfg":
            if shouldWrite:
                deforum_cfg = float(value)
            else:
                if doVerbose:
                    print("sending deforum_cfg:" + str(deforum_cfg))
                totalToSend.append((str(deforum_cfg)))
        # Strength Params
        ###########################################################################
        elif str(parameter) == "strength":
            if shouldWrite:
                strength_value = float(value)
            else:
                if doVerbose:
                    print("sending STRENGTH:" + str(strength_value))
                if should_use_deforumation_graph["Strength"]:
                    xshift = deforumation_graph_xshift["Strength"]
                    if start_frame > 0:
                        realIdx = start_frame+1
                    else:
                        realIdx = start_frame
                    if (len(deforumation_graph["Strength"]) + xshift) > realIdx:
                        if xshift <= realIdx:
                            realIdx = realIdx - xshift
                            value_from_strength_graph = deforumation_graph["Strength"][realIdx]
                            print("Sending strengh value to deforum:" + str(value_from_strength_graph) + " (realIdx:"+str(realIdx)+")")
                            totalToSend.append((str(value_from_strength_graph)))
                        else:
                            value_from_strength_graph = deforumation_graph["Strength"][0]
                            #print("Graph uses [0] because of xshift:" + str(value_from_strength_graph) + " (realIdx:" + str(realIdx) + ")")
                            totalToSend.append((str(value_from_strength_graph)))
                    else:
                        totalToSend.append((str(strength_value)))
                else:
                    totalToSend.append((str(strength_value)))
        # What Deforum think the Strength Value is
        ###########################################################################
        elif str(parameter) == "deforum_strength":
            if shouldWrite:
                deforum_strength = float(value)
            else:
                if doVerbose:
                    print("sending deforum_strength:" + str(deforum_strength))
                totalToSend.append((str(deforum_strength)))
        #Prompt Morph Values
        elif str(parameter).startswith("deforumation_prompt_morph_value_binding_"):
            bind_name = parameter[len("deforumation_prompt_morph_value_binding_"):]
            if shouldWrite:
                #deforum_translation_z = float(value)
                deforumation_prompt_morph_container[bind_name] = float(value)
            else:
                if doVerbose:
                    print("sending deforumation_prompt_morph_container:")
                # totalToSend.append((str(deforum_translation_z)))
                if bind_name in deforumation_prompt_morph_container:
                    totalToSend.append((str(deforumation_prompt_morph_container[bind_name])))
                else:
                    totalToSend.append(("NONE"))
                #totalToSend.append(str(deforum_translation_z))

        # ControlNet Weight Params
        ###########################################################################
        elif str(parameter).startswith("cn_weight"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_weight[cnIndex - 1] = float(value)
                # print("Writing weight:" + str(value) + " to Controlnet:" + str(cnIndex))
            else:
                if doVerbose:
                    print("sending cn_weight:" + str(cn_weight[cnIndex - 1]))
                # print("Sending weight:" + str(cn_weight[cnIndex - 1]) + " to Controlnet:" + str(cnIndex))
                totalToSend.append((str(cn_weight[cnIndex - 1])))
        # ControlNet step start Params
        ###########################################################################
        elif str(parameter).startswith("cn_stepstart"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_stepstart[cnIndex - 1] = float(value)
            else:
                if doVerbose:
                    print("sending cn_stepstart:" + str(cn_stepstart[cnIndex - 1]))
                totalToSend.append((str(cn_stepstart[cnIndex - 1])))
        # ControlNet step end Params
        ###########################################################################
        elif str(parameter).startswith("cn_stepend"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_stepend[cnIndex - 1] = float(value)
            else:
                if doVerbose:
                    print("sending cn_stepend:" + str(cn_stepend[cnIndex - 1]))
                totalToSend.append((str(cn_stepend[cnIndex - 1])))
        # ControlNet low threshold Params
        ###########################################################################
        elif str(parameter).startswith("cn_lowt"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_lowt[cnIndex - 1] = int(value)
            else:
                if doVerbose:
                    print("sending cn_lowt:" + str(cn_lowt[cnIndex - 1]))
                totalToSend.append((str(cn_lowt[cnIndex - 1])))
        # ControlNet high threshold Params
        ###########################################################################
        elif str(parameter).startswith("cn_hight"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_hight[cnIndex - 1] = int(value)
            else:
                if doVerbose:
                    print("sending cn_hight:" + str(cn_hight[cnIndex - 1]))
                totalToSend.append((str(cn_hight[cnIndex - 1])))
        # ControlNet active or not
        ###########################################################################
        elif str(parameter).startswith("cn_udcn"):
            cnIndex = int(parameter[len(parameter) - 1])
            if shouldWrite:
                cn_udcn[cnIndex - 1] = int(value)
            else:
                if doVerbose:
                    print("sending cn_udcn:" + str(cn_udcn[cnIndex - 1]))
                totalToSend.append((str(cn_udcn[cnIndex - 1])))
        # Seed Params
        ###########################################################################
        elif str(parameter) == "seed":
            if shouldWrite:
                seed_value = int(value)
            else:
                if doVerbose:
                    print("sending SEED:" + str(seed_value))
                totalToSend.append((str(seed_value)))
        elif str(parameter) == "seed_iter_n":
            if shouldWrite:
                seed_iter_n = int(value)
            else:
                if doVerbose:
                    print("sending seed_iter_n:" + str(seed_iter_n))
                totalToSend.append((str(seed_iter_n)))
        elif str(parameter) == "seed_changed":
            if shouldWrite:
                did_seed_change = int(value)
            else:
                totalToSend.append((str(did_seed_change)))
        elif str(parameter) == "seed_behavior":
            if shouldWrite:
                seed_behavior = str(value)
            else:
                if doVerbose:
                    print("sending seed behavior:" + str(seed_behavior))
                totalToSend.append((str(seed_behavior)))

        # Perlin persistence Param
        ###########################################################################
        elif str(parameter) == "perlin_persistence":
            if shouldWrite:
                perlin_persistence = float(value)
            else:
                if doVerbose:
                    print("sending perlin_persistence:" + str(perlin_persistence))
                totalToSend.append((str(perlin_persistence)))
        # Perlin octaves Param
        ###########################################################################
        elif str(parameter) == "perlin_octaves":
            if shouldWrite:
                perlin_octaves = int(value)
            else:
                if doVerbose:
                    print("sending perlin_octaves:" + str(perlin_octaves))
                totalToSend.append((str(perlin_octaves)))

        # Should use Pan params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_panning":
            if shouldWrite:
                should_use_deforumation_panning = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_panning:" + str(should_use_deforumation_panning))
                totalToSend.append((str(should_use_deforumation_panning)))

        # Should use Tilt params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_tilt":
            if shouldWrite:
                should_use_deforumation_tilt = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_tilt:" + str(should_use_deforumation_tilt))
                totalToSend.append((str(should_use_deforumation_tilt)))
        # Should use Rotation params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_rotation":
            if shouldWrite:
                should_use_deforumation_rotation = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_rotation:" + str(should_use_deforumation_rotation))
                totalToSend.append((str(should_use_deforumation_rotation)))
        # Should use ZOOM/FOV params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_zoom":
            if shouldWrite:
                should_use_deforumation_zoom = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_zoom:" + str(should_use_deforumation_zoom))
                totalToSend.append((str(should_use_deforumation_zoom)))
        # Should use ZOOM/FOV params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_fov":
            if shouldWrite:
                should_use_deforumation_fov = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_fov:" + str(should_use_deforumation_fov))
                totalToSend.append((str(should_use_deforumation_fov)))

        # Should use Noise Params
        ###########################################################################
        elif str(parameter) == "should_use_deforumation_noise":
            if shouldWrite:
                should_use_deforumation_noise = int(value)
            else:
                if doVerbose:
                    print("sending should_use_deforumation_noise:" + str(should_use_deforumation_noise))
                totalToSend.append((str(should_use_deforumation_noise)))
        # Noise Multiplier Param
        ###########################################################################
        elif str(parameter) == "noise_multiplier":
            if shouldWrite:
                noise_multiplier = float(value)
            else:
                if doVerbose:
                    print("sending noise_multiplier:" + str(noise_multiplier))
                totalToSend.append((str(noise_multiplier)))
        # What Deforum thinks the noise multiplier Value is
        ###########################################################################
        elif str(parameter) == "deforum_noise_multiplier":
            if shouldWrite:
                deforum_noise_multiplier = float(value)
            else:
                if doVerbose:
                    print("sending deforum_noise_multiplier:" + str(deforum_noise_multiplier))
                totalToSend.append((str(deforum_noise_multiplier)))
        # What Deforum thinks the perlin octaves Value is
        ###########################################################################
        elif str(parameter) == "deforum_perlin_octaves":
            if shouldWrite:
                deforum_perlin_octaves = int(value)
            else:
                if doVerbose:
                    print("sending deforum_perlin_octaves:" + str(deforum_perlin_octaves))
                totalToSend.append((str(deforum_perlin_octaves)))
        # What Deforum thinks the perlin octaves Value is
        ###########################################################################
        elif str(parameter) == "deforum_perlin_persistence":
            if shouldWrite:
                deforum_perlin_persistence = float(value)
            else:
                if doVerbose:
                    print("sending deforum_perlin_persistence:" + str(deforum_perlin_persistence))
                totalToSend.append((str(deforum_perlin_persistence)))
        # Steps Params
        ###########################################################################
        elif str(parameter) == "steps":
            if shouldWrite:
                steps = int(value)
            else:
                if doVerbose:
                    print("sending STEPS:" + str(steps))
                totalToSend.append((str(steps)))
        # What Deforum thinks the Steps Value is
        ###########################################################################
        elif str(parameter) == "deforum_steps":
            if shouldWrite:
                deforum_steps = int(value)
            else:
                if doVerbose:
                    print("sending deforum_steps:" + str(deforum_steps))
                totalToSend.append((str(deforum_steps)))
        # Resume and rewind
        ##########################################################################
        elif str(parameter) == "should_resume":
            if shouldWrite:
                # print("The value is:"+str(value))
                should_resume = int(value)
                if doVerbose2:
                    print("writing should_resume:" + str(should_resume))
            else:
                totalToSend.append((str(should_resume)))

        elif str(parameter) == "get_number_of_recalled_frames":
            totalToSend.append((str(number_of_recalled_frames)))


        elif str(parameter).startswith("deforumation_prompt_morph_remove_"):
            bind_name = parameter[len("deforumation_prompt_morph_remove_"):]
            if shouldWrite:
                if bind_name in prepare_prompt_morph_motion_container:
                    del prepare_prompt_morph_motion_container[bind_name]
                if bind_name in prompt_morphing_container:
                    del prompt_morphing_container[bind_name]
                if bind_name in start_prompt_morph_motion_container:
                    del start_prompt_morph_motion_container[bind_name]
                if bind_name in prepare_prompt_morph_motion_start_container:
                    del prepare_prompt_morph_motion_start_container[bind_name]
                if bind_name in deforumation_prompt_morph_container:
                    del deforumation_prompt_morph_container[bind_name]

                print(str("deleting prepare_prompt_morph_motion_container:" + str(bind_name)))
            else:
                print("deforumation_prompt_morph_remove_???")
        elif str(parameter).startswith("remove_all_deforumation_prompt_morph"):
            if shouldWrite:
                deforumation_prompt_morph_container = {}
                prepare_prompt_morph_motion_container = {}
                start_prompt_morph_motion_container = {}
                prepare_prompt_morph_motion_start_container = {}
                prompt_morphing_container = {}
                current_prompt_morph_progressions = []
                if doVerbose:
                    print(str("deleting all prepare_prompt_morph_motion_containers:"))
            else:
                print("deforumation_prompt_morph_remove_???")
        #Prepare prompt morph syrup motion
        elif str(parameter).startswith("prepare_prompt_morph_motion_"):
            bind_name = parameter[len("prepare_prompt_morph_motion_"):]
            if shouldWrite:
                prepare_prompt_morph_motion_container[bind_name] = value
                print(str("prepared prompt motion:" + str(parameter)))
            else:
                print("prepare_prompt_morph_motion_???")
        elif str(parameter).startswith("set_prompt_morph_values_"):
            bind_name = parameter[len("set_prompt_morph_values_"):]
            if shouldWrite:
                #[promptA, promptB, None, None, None]
                if bind_name in prompt_morphing_container and value[2] == None and value[3] == None and value[4] == None:
                    print("Only writing new promptValues")
                    temp_val = prompt_morphing_container[bind_name]
                    temp_val[0] = value[0]
                    temp_val[1] = value[1]
                    prompt_morphing_container[bind_name] = temp_val
                else:
                    prompt_morphing_container[bind_name] = value
                    if bind_name in deforumation_prompt_morph_container:
                        deforumation_prompt_morph_container[bind_name] = float(value[4])
                        #print("Overriding deforumation_prompt_morph_container[bind_name]")
                #print(str("prepared prompt motion container(" + str(bind_name) + "):" + str(value)))
            else:
                print("set_prompt_morph_values_???")

        elif str(parameter).startswith("start_prompt_morph_motion_"):
            bind_name = parameter[len("start_prompt_morph_motion_"):]
            if shouldWrite:
                start_prompt_morph_motion_container[bind_name] = int(value)
                if start_prompt_morph_motion_container[bind_name] == 1:
                    prepare_prompt_morph_motion_start_container[bind_name] = start_frame
                    start_motion = 0
                    #print("Prepare rotate motion z from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_rotate_motion_z)))


        elif str(parameter) == "prepare_zero_pan_motion_x":
            if shouldWrite:
                prepared_zero_pan_motion_x = value
                #print(str(prepared_zero_pan_motion_x))
            else:
                print("prepare_zero_pan_motion_x")
        elif str(parameter) == "prepare_zero_pan_motion_y":
            if shouldWrite:
                prepared_zero_pan_motion_y = value
                #print(str(prepared_zero_pan_motion_y))
            else:
                print("prepare_zero_pan_motion_y")
        elif str(parameter) == "prepare_zero_rotate_motion_x":
            if shouldWrite:
                prepared_zero_rotate_motion_x = value
                #print(str(prepared_zero_rotate_motion_x))
            else:
                print("prepare_zero_rotate_motion_x")
        elif str(parameter) == "prepare_zero_rotate_motion_y":
            if shouldWrite:
                prepared_zero_rotate_motion_y = value
                #print(str(prepared_zero_rotate_motion_y))
            else:
                print("prepare_zero_rotate_motion_y")
        elif str(parameter) == "prepare_zero_rotate_motion_z":
            if shouldWrite:
                prepared_zero_rotate_motion_z = value
                #print(str(prepared_zero_rotate_motion_z))
            else:
                print("prepare_zero_rotate_motion_z")
        elif str(parameter) == "prepare_zero_pan_motion_z":
            if shouldWrite:
                prepared_zero_pan_motion_z = value
                #print(str(prepared_zero_pan_motion_z))
            else:
                print("prepare_zero_pan_motion_z")

        elif str(parameter) == "prepare_zero_pan_motion":
            if shouldWrite:
                prepared_zero_pan_motion = value
                # print(str(prepared_zero_pan_motion))
            else:
                print("prepare_zero_pan_motion")
        elif str(parameter) == "prepare_zero_zoom_motion":
            if shouldWrite:
                prepared_zero_zoom_motion = value
                # print(str(prepared_zero_zoom_motion))
            else:
                print("prepare_zero_zoom_motion")
        elif str(parameter) == "prepare_zero_rotation_motion":
            if shouldWrite:
                prepared_zero_rotation_motion = value
                # print(str(prepared_zero_rotation_motion))
            else:
                print("prepare_zero_rotation_motion")
        elif str(parameter) == "prepare_zero_tilt_motion":
            if shouldWrite:
                prepared_zero_tilt_motion = value
                # print(str(prepared_zero_rotation_motion))
            else:
                print("prepare_zero_tilt_motion")
        elif str(parameter) == "prepare_motion":
            if shouldWrite:
                prepared_motion = value
                # print(str(prepared_motion))
            else:
                print("prepared motion")
        elif str(parameter) == "start_zero_pan_motion_x":
            if shouldWrite:
                start_zero_pan_motion_x = int(value)
                if start_zero_pan_motion_x == 1:
                    prepared_zero_pan_motion_x_start = start_frame
                    start_motion = 0
                    #print("Prepare pan motion x from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_pan_motion_x)))
        elif str(parameter) == "start_zero_pan_motion_y":
            if shouldWrite:
                start_zero_pan_motion_y = int(value)
                if start_zero_pan_motion_y == 1:
                    prepared_zero_pan_motion_y_start = start_frame
                    start_motion = 0
                    #print("Prepare pan motion y from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_pan_motion_y)))
        elif str(parameter) == "start_zero_rotate_motion_x":
            if shouldWrite:
                start_zero_rotate_motion_x = int(value)
                if start_zero_rotate_motion_x == 1:
                    prepared_zero_rotate_motion_x_start = start_frame
                    start_motion = 0
                    #print("Prepare rotate motion x from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_rotate_motion_x)))
        elif str(parameter) == "start_zero_rotate_motion_y":
            if shouldWrite:
                start_zero_rotate_motion_y = int(value)
                if start_zero_rotate_motion_y == 1:
                    prepared_zero_rotate_motion_y_start = start_frame
                    start_motion = 0
                    #print("Prepare rotate motion y from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_rotate_motion_y)))
        elif str(parameter) == "start_zero_rotate_motion_z":
            if shouldWrite:
                start_zero_rotate_motion_z = int(value)
                if start_zero_rotate_motion_z == 1:
                    prepared_zero_rotate_motion_z_start = start_frame
                    start_motion = 0
                    #print("Prepare rotate motion z from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_rotate_motion_z)))
        elif str(parameter) == "start_zero_pan_motion_z":
            if shouldWrite:
                start_zero_pan_motion_z = int(value)
                if start_zero_pan_motion_z == 1:
                    prepared_zero_pan_motion_z_start = start_frame
                    start_motion = 0
                    #print("Prepare pan motion z from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_pan_motion_z)))
        elif str(parameter) == "start_zero_pan_motion":
            if shouldWrite:
                start_zero_pan_motion = int(value)
                if start_zero_pan_motion == 1:
                    prepared_zero_pan_motion_start = start_frame
                    start_motion = 0
                    #print("Prepare pan motion from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_pan_motion)))
        elif str(parameter) == "start_zero_zoom_motion":
            if shouldWrite:
                start_zero_zoom_motion = int(value)
                if start_zero_zoom_motion == 1:
                    prepared_zero_zoom_motion_start = start_frame
                    start_motion = 0
                    #print("Prepare zoom motion from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_zoom_motion)))
        elif str(parameter) == "start_zero_rotation_motion":
            if shouldWrite:
                start_zero_rotation_motion = int(value)
                if start_zero_rotation_motion == 1:
                    prepared_zero_rotation_motion_start = start_frame
                    start_motion = 0
                    #print("Prepare rotation motion from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_rotation_motion)))
        elif str(parameter) == "start_zero_tilt_motion":
            if shouldWrite:
                start_zero_tilt_motion = int(value)
                if start_zero_tilt_motion == 1:
                    prepared_zero_tilt_motion_start = start_frame
                    start_motion = 0
                    #print("Prepare tilt motion from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_zero_tilt_motion)))
        elif str(parameter) == "start_motion":
            if shouldWrite:
                start_motion = int(value)
                if start_motion == 1:
                    prepared_zero_pan_motion_start = 0
                    start_zero_zoom_motion = 0
                    start_zero_rotation_motion = 0
                    start_zero_tilt_motion = 0
                    prepared_motion_start = start_frame
                    #print("Prepare motion from frame: " + str(start_frame))
            else:
                totalToSend.append((str(start_motion)))
        elif str(parameter) == "saved_frame_params":
            if shouldWrite:
                if not should_use_total_recall:
                    if not int(value) in parameter_container:
                        # print("Setting values for frame:"+str(value))
                        parameter_container[int(value)] = ParameterContainer()
                    # print("Mediator asked to work at frame:>>" + str(value))
                    parameter_container[int(value)].SetValues()
                elif (int(value) < total_recall_from) or (int(value) > total_recall_to):
                    if not int(value) in parameter_container:
                        parameter_container[int(value)] = ParameterContainer()
                    # print("Mediator asked to work at frame:>>>" + str(value))
                    parameter_container[int(value)].SetValues()
            else:
                if doVerbose2:
                    print("sending parameter_container")
                if int(value) == -1:
                    bytesToSend = pickle.dumps(parameter_container)
                elif int(value) in parameter_container:
                    if not should_use_total_recall:
                        bytesToSend = pickle.dumps(parameter_container[int(value)])
                        # print("Sending ALL original parameters.")
                    else:
                        # print("Sending some or all original parameters:")
                        copyof_parameter_container = copy.deepcopy(parameter_container[int(value)])
                        copyof_parameter_container = RecallValuesTemp(copyof_parameter_container)
                        bytesToSend = pickle.dumps(copyof_parameter_container)
                    # if should_use_total_recall_prompt:
                    #    copyof_parameter_container = copy.deepcopy(parameter_container)
                    #    copyof_parameter_container[int(value)].Prompt_Positive = Prompt_Positive
                    #    bytesToSend = pickle.dumps(copyof_parameter_container[int(value)])
                    # else:
                    #    bytesToSend = pickle.dumps(parameter_container[int(value)], HIGHEST_PROTOCOL)
                    #    arne = 1
                else:
                    bytesToSend = pickle.dumps(0x0)
                if isWindows and websocketCommunication == None:
                    win32file.WriteFile(pipe, bytesToSend)
                    win32file.CloseHandle(pipe)
                else:
                    await websocketCommunication.send(bytesToSend)

            number_of_recalled_frames = len(parameter_container)
        elif str(parameter) == "upload_recall_file":
            if shouldWrite:
                parameter_container.clear()
                parameter_container = pickle.loads(value)
                number_of_recalled_frames = len(parameter_container)
        elif str(parameter) == "total_generated_images":
            if shouldWrite:
                number_of_generated_images = int(value)
            else:
                if doVerbose2:
                    print("sending number_of_generated_images:" + str(number_of_generated_images))
                totalToSend.append((str(number_of_generated_images)))
        elif str(parameter) == "syrup_steps_pan_x":
            if shouldWrite:
                pass
            else:
                if start_zero_pan_motion_x == 1:
                    current_step_progress = frame_idx - prepared_zero_pan_motion_x_start
                    current_total_steps = len(prepared_zero_pan_motion_x)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_pan_x:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_pan_y":
            if shouldWrite:
                pass
            else:
                if start_zero_pan_motion_y == 1:
                    current_step_progress = frame_idx - prepared_zero_pan_motion_y_start
                    current_total_steps = len(prepared_zero_pan_motion_y)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_pan_y:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_rotate_x":
            if shouldWrite:
                pass
            else:
                if start_zero_rotate_motion_x == 1:
                    current_step_progress = frame_idx - prepared_zero_rotate_motion_x_start
                    current_total_steps = len(prepared_zero_rotate_motion_x)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_rotate_x:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_rotate_y":
            if shouldWrite:
                pass
            else:
                if start_zero_rotate_motion_y == 1:
                    current_step_progress = frame_idx - prepared_zero_rotate_motion_y_start
                    current_total_steps = len(prepared_zero_rotate_motion_y)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_rotate_y:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_rotate_z":
            if shouldWrite:
                pass
            else:
                if start_zero_rotate_motion_z == 1:
                    current_step_progress = frame_idx - prepared_zero_rotate_motion_z_start
                    current_total_steps = len(prepared_zero_rotate_motion_z)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_rotate_z:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_pan_z":
            if shouldWrite:
                pass
            else:
                if start_zero_pan_motion_z == 1:
                    current_step_progress = frame_idx - prepared_zero_pan_motion_z_start
                    current_total_steps = len(prepared_zero_pan_motion_z)
                else:
                    current_step_progress = 100
                    current_total_steps = 100
                totalToSend.append((current_step_progress, current_total_steps))
                if doVerbose2:
                    print("sending syrup_steps_pan_z:" + str((current_step_progress, current_total_steps)))
        elif str(parameter) == "syrup_steps_prompt_morph_motions":
            if shouldWrite:
                pass
            else:
                totalToSend.append((current_prompt_morph_progressions))
                if doVerbose2:
                    print("sending syrup_steps_prompt_morph_motions:" + str(current_prompt_morph_progressions))
        elif str(parameter) == "start_frame":
            if shouldWrite:
                start_frame = int(value)
                if number_of_generated_images > start_frame:
                    print("number_of_generated_images was:" + str(number_of_generated_images) + " but start_frame was set to:" + str(start_frame) + ". Deleting recall frames bigger than start_frame")
                    temp_parameter_container = parameter_container.copy()
                    for recall_frame in temp_parameter_container:
                        if recall_frame > start_frame:
                            del parameter_container[recall_frame]
                    del temp_parameter_container
                # if start_frame > number_of_generated_images:
                number_of_generated_images = start_frame
                # Call and act on syrup motions
                doSyrup()
                # Signal to deforumation that new frame has been received/created
                if isWindows and websocketCommunication == None:
                    if pipeName == "Deforum":
                        bufSize = 64 * 1024
                        try:
                            handle = win32file.CreateFile('\\\\.\\pipe\\deforumation_pipe_in', win32file.GENERIC_READ | win32file.GENERIC_WRITE, 0, None, win32file.OPEN_EXISTING, 0, None)
                            value = [1, "new_image_created", start_frame]
                            bytesToSend = pickle.dumps(value)
                            win32file.WriteFile(handle, bytesToSend)
                            # Need to receive back data to close the write call (but totally discards this)
                            # print("AWaiting reply")
                            result, data = win32file.ReadFile(handle, bufSize)
                            message = data
                            while len(data) == bufSize:
                                print("More data has to be read (normal pipe async):" + str(len(data)))
                                result, data = win32file.ReadFile(handle, bufSize)
                                message += data
                            # print("Got reply:" + str(message))
                        except pywintypes.error as e:
                            # print("Deforumation Live view, not up and running at the moment")
                            pass
                else:
                    try:
                        timeout = 0.2
                        websocket = await asyncio.wait_for(websockets.connect("ws://"+deforumation_address+":"+str(deforumation_port)), timeout)
                        #async with websockets.connect("ws://localhost:8767") as websocket:
                        try:
                            value = [1, "new_image_created", start_frame]
                            bytesToSend = pickle.dumps(value)
                            await asyncio.wait_for(websocket.send(bytesToSend), timeout=10.0)
                            message = await asyncio.wait_for(websocket.recv(), timeout=10.0) #We don't care about the message
                        except TimeoutError:
                            print('timeout!')
                    except Exception as e:
                        #print("Deforumation Live view, not up and running at the moment")
                        pass


            else:
                if doVerbose2:
                    print("sending start frame:" + str(start_frame))
                totalToSend.append((str(start_frame)))
        elif str(parameter) == "frame_outdir":
            if shouldWrite:
                frame_outdir = str(value)
            else:
                if doVerbose2:
                    print("sending frame_outdir:" + str(frame_outdir))
                totalToSend.append((str(frame_outdir)))
        elif str(parameter) == "resume_timestring":
            if shouldWrite:
                resume_timestring = str(value)
            else:
                if doVerbose2:
                    print("sending resume_timestring:" + str(resume_timestring))
                totalToSend.append((str(resume_timestring)))
        elif str(parameter) == "should_use_deforumation_strength":
            if shouldWrite:
                # print("Setting should use deforumation strength to:"+str(int(value)))
                should_use_deforumation_strength = int(value)
            else:
                if doVerbose2:
                    print("sending should_use_deforumation_strength:" + str(should_use_deforumation_strength))
                totalToSend.append((str(should_use_deforumation_strength)))
        elif str(parameter) == "should_use_deforumation_cfg":
            if shouldWrite:
                # print("Setting should use deforumation strength to:"+str(int(value)))
                should_use_deforumation_cfg = int(value)
            else:
                if doVerbose2:
                    print("sending should_use_deforumation_cfg:" + str(should_use_deforumation_cfg))
                totalToSend.append((str(should_use_deforumation_cfg)))
        elif str(parameter) == "cadence":
            if shouldWrite:
                cadence = str(value)
            else:
                if doVerbose2:
                    print("sending cadence:" + str(cadence))
                totalToSend.append((str(cadence)))
        elif str(parameter) == "should_use_deforumation_cadence":
            if shouldWrite:
                should_use_deforumation_cadence = str(value)
            else:
                if doVerbose2:
                    print("sending should_use_deforumation_cadence:" + str(should_use_deforumation_cadence))
                totalToSend.append((str(should_use_deforumation_cadence)))
        elif str(parameter) == "render_loopback":
            if shouldWrite:
                render_loopback = str(value)
            else:
                if doVerbose2:
                    print("sending render_loopback:" + str(render_loopback))
                totalToSend.append((str(render_loopback)))
        # What Deforum thinks the cadence Value is
        ###########################################################################
        elif str(parameter) == "deforum_cadence":
            if shouldWrite:
                deforum_cadence = int(value)
            else:
                if doVerbose:
                    print("sending deforum_cadence:" + str(deforum_cadence))
                totalToSend.append((str(deforum_cadence)))
        elif str(parameter) == "parseq_keys":
            if shouldWrite:
                parseq_keys = value
            else:
                if doVerbose2:
                    print("sending parseq_keys:")
                if isWindows and websocketCommunication == None:
                    win32file.WriteFile(pipe, pickle.dumps(parseq_keys))
                else:
                    await websocketCommunication.send(pickle.dumps(parseq_keys))

        elif str(parameter) == "use_parseq":
            if shouldWrite:
                use_parseq = value
            else:
                if doVerbose2:
                    print("sending use_parseq:")
                totalToSend.append((str(use_parseq)))
        elif str(parameter) == "parseq_manifest":
            if shouldWrite:
                parseq_manifest = value
                print("Got parseq_manifest:" + str(value))
            else:
                if doVerbose2:
                    print("sending parseq_manifest:")
                totalToSend.append((str(parseq_manifest)))
        elif str(parameter) == "should_use_optical_flow":
            if shouldWrite:
                should_use_optical_flow = value
            else:
                if doVerbose2:
                    print("sending should_use_optical_flow:")
                totalToSend.append((str(should_use_optical_flow)))
        elif str(parameter) == "parseq_strength":
            if shouldWrite:
                parseq_strength = value
            else:
                if doVerbose2:
                    print("sending parseq_strength:")
                totalToSend.append((str(parseq_strength)))
        elif str(parameter) == "parseq_movements":
            if shouldWrite:
                print("parseq_movements:" + str(parseq_movements))
                parseq_movements = value
            else:
                if doVerbose2:
                    print("sending parseq_movements:" + str(parseq_movements))
                totalToSend.append((str(parseq_movements)))
        elif str(parameter) == "cadence_flow_factor":
            if shouldWrite:
                cadence_flow_factor = value
            else:
                if doVerbose2:
                    print("sending cadence_flow_factor:" + str(cadence_flow_factor))
                totalToSend.append((str(cadence_flow_factor)))
        elif str(parameter) == "generation_flow_factor":
            if shouldWrite:
                generation_flow_factor = value
            else:
                if doVerbose2:
                    print("sending generation_flow_factor:" + str(generation_flow_factor))
                totalToSend.append((str(generation_flow_factor)))
        ######## Here Audio Synq Graphs are handled
        elif str(parameter) == "should_use_deforumation_graph":
            graph_types = ["Strength", "Zoom", "PanLR", "PanUD", "RotateH", "RotateV", "Tilt"]
            if shouldWrite:
                if value[0] in graph_types:
                    should_use_deforumation_graph[value[0]] = value[1]
                else:
                    print("ERROR in should_use_deforumation_graph! Cant set graph " + str(value[0]) + "   ---- NO SUCH GRAPH exists!")
            else:
                if doVerbose2:
                    print("sending should_use_deforumation_graph:")
                if value in graph_types:
                    totalToSend.append((str(should_use_deforumation_graph[value])))
                else:
                    print("ERROR in should_use_deforumation_graph! NO SUCH GRAPH exists:" + str(value))

        elif str(parameter) == "set_deforumation_graph":
            graph_types = ["Strength", "Zoom", "PanLR", "PanUD", "RotateH", "RotateV", "Tilt"]
            if shouldWrite:
                if value[0] in graph_types:
                    deforumation_graph[value[0]] = value[1]
                #print("Received:" + str(deforumation_graph[value[0]]))
            else:
                if doVerbose2:
                    print("sending deforumation_graph:")
                if value in graph_types:
                    totalToSend.append((str(deforumation_graph[value])))
                else:
                    print("ERROR in set_deforumation_graph! NO SUCH GRAPH exists:" + str(value))

        elif str(parameter) == "deforumation_graph_xshift":
            graph_types = ["Strength", "Zoom", "PanLR", "PanUD", "RotateH", "RotateV", "Tilt"]
            if shouldWrite:
                if value[0] in graph_types:
                    deforumation_graph_xshift[value[0]] = value[1]
                #print("Received:" + str(deforumation_graph_xshift[value[0]]))
            else:
                if doVerbose2:
                    print("sending deforumation_graph_xshift:")
                if value in graph_types:
                    totalToSend.append((str(deforumation_graph_xshift[value])))
                else:
                    print("ERROR in deforumation_graph_xshift! NO SUCH GRAPH exists:" + str(value))
        ##############
        elif str(parameter) == "deforum_interrupted":
            if shouldWrite:
                deforum_interrupted = value
            else:
                if doVerbose2:
                    print("sending deforum_interrupted:" + str(deforum_interrupted))
                totalToSend.append((str(deforum_interrupted)))
        elif str(parameter) == "shutdown":
            serverShutDown = True
        else:
            print(
                "NO SUCH COMMAND:" + parameter + "\nPlease make sure Mediator, Deforumation and the Deforum (render.py, animation.py) are in sync.")
            if not shouldWrite:
                totalToSend.append((str("NO SUCH COMMAND:" + parameter)))

    return totalToSend



async def main_named_pipe(pipeName):
    global ShouldBeRunning
    print("pipe server:" + str(pipeName))
    count = 0
    bufSize = 64 * 1024

    while 1 == 1:
        #print("Creating pipe:" + str(pipeName))
        try:
            try:
                pipe = win32pipe.CreateNamedPipe('\\\\.\\pipe\\' + str(pipeName), win32pipe.PIPE_ACCESS_DUPLEX, win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT, 1, 65536, 65536, 0, None)
            except pywintypes.error as e:
                print("Another instance is already running. Closing this one.(" + str(e) + ")")
                ShouldBeRunning = False
                break
            win32pipe.ConnectNamedPipe(pipe, None)
            message = win32pipe.SetNamedPipeHandleState(pipe, win32pipe.PIPE_READMODE_MESSAGE, None, None)
            if message == 0:
                print(f"SetNamedPipeHandleState return code: {message}")
                continue
            else:
                totalToSend = []
                result, data = win32file.ReadFile(pipe, bufSize)
                message = data
                while len(data) == bufSize:
                    print("More data has to be read (special pipe async):" + str(len(data)))
                    result, data = win32file.ReadFile(pipe, bufSize)
                    message += data

                arr = pickle.loads(message)

            if len(arr) == 3:
                shouldWrite = arr[0]
                totalToSend = await handleMesssage(arr, pipe, pipeName)

                if shouldWrite:  # Return an "OK" if the writes went OK
                    win32file.WriteFile(pipe, pickle.dumps(b"OK"))
                    #print("Closing pipe:" + str(pipeName))
                    win32file.CloseHandle(pipe)
                elif len(totalToSend) != 0:
                    bytesToSend = pickle.dumps(totalToSend)
                    win32file.WriteFile(pipe, bytesToSend)
                    #win32file.WriteFile(pipe, str(totalToSend).encode())
                    #print("Closing 0 pipe:" + str(pipeName))
                    win32file.CloseHandle(pipe)


            else:  # Array was not a length of 3 [True/False,<parameter value>,<value>
                if doVerbose:
                    win32file.WriteFile(pipe, pickle.dumps(b"ERROR"))
                    win32file.CloseHandle(pipe)
        except pywintypes.error as e:
            print("Error (in the " + str(pipeName) + " pipe thread). Error message:" + str(e))
            win32file.CloseHandle(pipe)
            #pipe = win32pipe.CreateNamedPipe('\\\\.\\pipe\\' + str(pipeName), win32pipe.PIPE_ACCESS_DUPLEX, win32pipe.PIPE_TYPE_MESSAGE | win32pipe.PIPE_READMODE_MESSAGE | win32pipe.PIPE_WAIT,1, 65536, 65536, 0, None)
            # asyncio.get_event_loop().stop()
            # await websocket.close()
            # loop = asyncio.get_event_loop()
            # loop.stop()

def between_main_named_pipe(pipeName):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main_named_pipe(pipeName))
    loop.close()

def between_main_websockets(host, port):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    loop.run_until_complete(main_websockets(host, port))
    loop.close()

async def main_websocket(port):
    #print("websocket:" + str(websocket))

    async for message in port:
        # print("Incomming message:"+str(message))

        totalToSend = []
        arr = pickle.loads(message)
        shouldWrite = False
        if len(arr) == 3:
            shouldWrite = arr[0]
            totalToSend = await handleMesssage(arr, websocketCommunication=port)

        if shouldWrite:  # Return an "OK" if the writes went OK
            await port.send(pickle.dumps(b"OK"))
        elif len(totalToSend) != 0:
            bytesToSend = pickle.dumps(totalToSend)
            await port.send(bytesToSend)

        else:  # Array was not a length of 3 [True/False,<parameter value>,<value>
            if doVerbose:
                await port.send("ERROR")

async def main_websockets(host, port):
    global stop
    global server
    global ShouldBeRunning
    try:
        stop = asyncio.Future()  # run forever
        server = await websockets.serve(main_websocket, host, int(port))
        # loop = asyncio.get_event_loop()

        while True:
            if serverShutDown:
                print("Shutting down Server")
                # pending = asyncio.Task.all_tasks()
                # group = asyncio.gather(*pending, return_exceptions=True)
                server.close()
                # server. run_until_complete(server)
                # loop.close()
                # server.close()
                break
            await asyncio.sleep(5)
    except Exception as e: #KeyboardInterrupt:
        if server != None:
            server.close()
        print("Mediator instance already running. Exiting.")
        ShouldBeRunning = False

    # await stop
    # await server.close()
    # async with websockets.serve(echo, "localhost", 8765):
    #    await stop


if __name__ == '__main__':
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

    parser = argparse.ArgumentParser(description='Mediator arguments.')
    parser.add_argument('--deforumation_address', default='127.0.0.1', help='Mediator will use this address to connect to Deforumation')
    parser.add_argument('--deforumation_port', default='8767', help='The mediator will use this port to connect to Deforumation')
    parser.add_argument('--mediator_deforumation_address', default='127.0.0.1', help='The mediator will listen on this address for deforumation traffic')
    parser.add_argument('--mediator_deforumation_port', default='8766', help='The mediator will use this port for lisening for deforumation traffic')
    parser.add_argument('--mediator_deforum_address', default='127.0.0.1', help='The mediator will listen on this address for deforum traffic')
    parser.add_argument('--mediator_deforum_port', default='8765', help='The mediator will use this port for lisening for deforum traffic')
    parser.add_argument('--use_named_pipes', action='store_true',  help='The mediator will use named pipes instead of websocket')

    args = parser.parse_args()
    """if args.listen:
        host = "0.0.0.0"
    else:
        host = "127.0.0.1"""
    if sys.platform.startswith('win'):
        isWindows = True
    else:
        isWindows = False
    if args.use_named_pipes:
        if isWindows:
            import win32pipe, win32file, pywintypes
            shouldUseNamedPipes = True
            print("Starting DMQT Mediator with Named Pipes communication, version 0.1.9")
        else:
            shouldUseNamedPipes = False
            print("Named DMQT Pipes communication is only supported on Windows OS, version 0.1.9... exiting..")
            exit(0)
    else:
        shouldUseNamedPipes = False
        print("Starting DMQT Mediator (version 0.1.9) with WebSocket communication, listening for Deforum at " + args.mediator_deforum_address + ":" + args.mediator_deforum_port + ", version 0.1.9")
        print("   -- And listening for Deforumation at " + args.mediator_deforumation_address + ":" + args.mediator_deforumation_port + ", version 0.1.9")
        print("Connecting to Deforumation's live view server using " + args.deforumation_address + ":" + args.deforumation_port)
        deforumation_address = args.deforumation_address
        deforumation_port = args.deforumation_port
        mediator_deforumation_address = args.mediator_deforumation_address
        mediator_deforumation_port = args.mediator_deforumation_port
        mediator_deforum_address = args.mediator_deforum_address
        mediator_deforum_port = args.mediator_deforum_port




    try:
        #deforum_port = 8765
        #deforumation_port = 8766
        if not shouldUseNamedPipes:
            #print("Starting Mediator <-> Deforum on port:" + str(deforum_port))
            deforum_thread = threading.Thread(target=between_main_websockets, args=([mediator_deforum_address, mediator_deforum_port])) #Mediator to Deforum communication
            deforum_thread.daemon = True
            deforum_thread.start()
            #print("Starting Mediator <-> Deforumation on port:" + str(deforumation_port))
            deforumation_thread = threading.Thread(target=between_main_websockets, args=([mediator_deforumation_address, mediator_deforumation_port])) #Mediator to Deforumation communication
            deforumation_thread.daemon = True
            deforumation_thread.start()
            while (ShouldBeRunning):
                time.sleep(0.1)
        else:
            deforum_thread = threading.Thread(target=between_main_named_pipe, args=(['Deforum']))
            deforum_thread.daemon = True
            deforum_thread.start()
            deforumation_thread = threading.Thread(target=between_main_named_pipe, args=(['Deforumation']))
            deforumation_thread.daemon = True
            deforumation_thread.start()
            while (ShouldBeRunning):
                time.sleep(0.1)
    except KeyboardInterrupt:
        serverShutDown = True
        # server.close()
        print("Shutting down Server")


