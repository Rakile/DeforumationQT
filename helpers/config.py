import json
import os
import pickle
import shutil

class Deforumation_Settings():

    def __init__(self, parent=None):
        """self.deforumation_settings = {
        "Main_ScreenSizeWidth" : 1486,
        "Main_ScreenSizeHeight" : 782,
        "Movie_Tab_ScreenSizeWidth" : 891,
        "Movie_Tab_ScreenSizeHeight" : 130,
        "Preview_Tab_ScreenSizeWidth" : 891,
        "Preview_Tab_ScreenSizeHeight" : 400,
        "Tab_Tabs_ScreenSizeWidth" : 891,
        "Tab_Tabs_ScreenSizeHeight" : 396,
        "Left_Splitter" : [446, 143, 358],
        "Right_Splitter" : [305, 305],
        "Middle_Splitter" : [843, 300],
        "Slider_Tab_ScreenSizeWidth": 245,
        "Slider_Tab_ScreenSizeHeight": 468,
        "LiveValue_Tab_ScreenSizeWidth": 245,
        "LiveValue_Tab_ScreenSizeHeight": 467,
        "Syrupmotion_Panning": 0,
        "Syrupmotion_Zoom": 0,
        "Syrupmotion_Rotation": 0,
        "Syrupmotion_Tilt": 0,
        }"""
        self.parent = parent
        if not os.path.isdir("./config"):
            os.mkdir("./config")
        self.deforumation_component_settings = {}
        self.deforumation_language_settings = {}
        self.default_DeforumationGuiConfig = "./helpers/DeforumationGUIconfig.json"
        self.default_DeforumationSendConfig = "./helpers/DeforumationSendConfig.json"
        self.DeforumationGuiConfig = "./config/DeforumationGUIconfig.json"
        self.DeforumationSendConfig = "./config/DeforumationSendConfig.json"
        self.DeforumationReceiveConfig = "./config/DeforumationReceiveConfig.json"
        self.DeforumationPromptMorphConfig = "./config/DeforumationPromptMorphConfig.json"
        self.deforumation_settings_send = {}
        self.deforumation_settings_receive = {}
        self.deforumation_settings_gui = {}
        self.deforumation_settings_promptmorph = {}
        self.is_verbose = False
    def writeToLanguageConfig(self, config = None, file = None):
        if config == None:
            if file == None:
                with open("default_language_config.json", "w") as jsonfile:
                    json.dump(self.deforumation_language_settings, jsonfile)
            else:
                with open(file, "w") as jsonfile:
                    json.dump(self.deforumation_language_settings, jsonfile)
        else:
            with open("default_language_config.json", "w") as jsonfile:
                json.dump(config, jsonfile)

    def readConfig(self, config_path, container = None):
        if not os.path.isfile(config_path):
            if config_path == self.DeforumationGuiConfig:
                #print("No GUI config file found (" + str(self.DeforumationGuiConfig) + ").")
                # Copy the default config to the config folder
                shutil.copy(self.default_DeforumationGuiConfig, self.DeforumationGuiConfig)
                # And return the default config as JSON
            elif config_path == self.DeforumationSendConfig:
                #print("No Parameter settings config file found (" + str(self.DeforumationSendConfig) + ").")
                # Copy the default config to the config folder
                shutil.copy(self.default_DeforumationSendConfig, self.DeforumationSendConfig)
                # And return the default config as JSON
            else:
                return {} # No values defined yet so just return empty (for Send & Receive Config)

        with open(config_path, "r", encoding='utf-8') as jsonfile:
            try:
                return json.load(jsonfile)
                #print("Read successful")
            except Exception as e:
                return -1



    def writeToConfig(self, config_path, blob):
            with open(config_path, "w") as jsonfile:
                json.dump(blob, jsonfile)

    def loadJSONconfig(self, file):
        if os.path.isfile(file):
            with open(file, "r", encoding='utf-8') as jsonfile:
                try:
                    self.tempBlob = json.load(jsonfile)
                    #print("Read successful")
                except Exception as e:
                    return -1
            return self.tempBlob
        return -1

    def openLanguageConfig(self, file = None):
        if file == None:
            if os.path.isfile("default_language_config.json"):
                with open("default_language_config.json", "r", encoding='utf-8') as jsonfile:
                    try:
                        self.deforumation_language_settings = json.load(jsonfile)
                        print("Read successful")
                    except Exception as e:
                        return -1
        else:
            if os.path.isfile(file):
                with open(file, "r", encoding='utf-8') as jsonfile:
                    try:
                        self.deforumation_language_settings = json.load(jsonfile)
                        #print("Read successful")
                    except Exception as e:
                        return -1
        return 0

    def getLanguageConfiguaration(self):
        return self.deforumation_language_settings

    def loadSentConfigIntoParameters(self):
        self.deforumation_settings_send = self.readConfig(self.DeforumationSendConfig, self.deforumation_settings_send)
    def loadReceivedConfigIntoParameters(self):
        self.deforumation_settings_receive = self.readConfig(self.DeforumationReceiveConfig, self.deforumation_settings_receive)
    def loadGuiConfigIntoParameters(self, configFile = None):
        if configFile != None:
            self.deforumation_settings_gui = self.readConfig(configFile, self.deforumation_settings_gui)
        else:
            self.deforumation_settings_gui = self.readConfig(self.DeforumationGuiConfig, self.deforumation_settings_gui)
    def loadAllSentDeforumValuesFromConfigIntoParameters(self):
        self.deforumation_settings_send = self.readConfig(self.DeforumationSendConfig, self.deforumation_settings_send)
        self.deforumation_settings_receive = self.readConfig(self.DeforumationReceiveConfig, self.deforumation_settings_receive)
        if self.deforumation_settings_receive == -1:
            self.deforumation_settings_receive = {}
        self.deforumation_settings_gui = self.readConfig(self.DeforumationGuiConfig, self.deforumation_settings_gui)

        self.deforumation_settings_promptmorph = self.readConfig(self.DeforumationPromptMorphConfig, self.deforumation_settings_promptmorph)
        if self.deforumation_settings_promptmorph == -1:
            self.deforumation_settings_promptmorph = {}


    def writeDeforumSendValuesToConfig(self, key, value=-1):
        try:
            if key == "<BLOCK>":
                for n in value:
                    arr = pickle.loads(n)
                    key = arr[1]
                    value = arr[2]
                    if value == -1:
                        for k in key:
                            self.deforumation_settings_send[k] = key[k]
                    else:
                        self.deforumation_settings_send[key] = value
                    self.writeToConfig(self.DeforumationSendConfig, self.deforumation_settings_send)

            elif isinstance(key, dict):
                for k in key:
                    self.deforumation_settings_send[k] = key[k]
            else:
                self.deforumation_settings_send[key] = value
            self.writeToConfig(self.DeforumationSendConfig, self.deforumation_settings_send)
        except Exception as e:
            print("Something went major wrong when writing to \"./Config/DeforumationSendConfig.json\"... The config file might be corrupt!!!:" + str(key) + " -- " + str(e))

    def writeDeforumReceiveValuesToConfig(self, key, value=-1):
        if isinstance(key, dict):
            for k in key:
                self.deforumation_settings_receive[k] = key[k]
        else:
            if isinstance(key, list):
                key_value_index = 0
                for n in key:
                    self.deforumation_settings_receive[n] = value[key_value_index]
                    key_value_index += 1
            else:
                self.deforumation_settings_receive[key] = value

            #self.deforumation_settings_receive[key] = value
        self.writeToConfig(self.DeforumationReceiveConfig, self.deforumation_settings_receive)

    def writeDeforumationGuiValuesToConfig(self, key, value=-1, configFile = None):
        if key != None:
            if isinstance(key, dict):
                for k in key:
                    self.deforumation_settings_gui[k] = key[k]
            else:
                self.deforumation_settings_gui[key] = value
        if configFile != None:
            self.writeToConfig(configFile, self.deforumation_settings_gui)
        else:
            self.writeToConfig(self.DeforumationGuiConfig, self.deforumation_settings_gui)

    def writeDeforumPromptMorphValuesToConfig(self, key = None, value=-1):
        if key != None:
            if isinstance(key, dict):
                for k in key:
                    self.deforumation_settings_promptmorph[k] = key[k]
            else:
                if isinstance(key, list):
                    key_value_index = 0
                    for n in key:
                        self.deforumation_settings_promptmorph[n] = value[key_value_index]
                        key_value_index += 1
                else:
                    self.deforumation_settings_promptmorph[key] = value

                #self.deforumation_settings_receive[key] = value
            self.writeToConfig(self.DeforumationPromptMorphConfig, self.deforumation_settings_promptmorph)
        else:
            self.writeToConfig(self.DeforumationPromptMorphConfig, self.deforumation_settings_promptmorph)

    def getGuiConfigValue(self, key):
        try:
            return self.deforumation_settings_gui[key]
        except Exception as e:
            if self.is_verbose:
                print("Error getGuiConfigValue, value:" + str(key) + " -- " + str(e))
        return -1
    def getSendConfigValue(self, key):
        try:
            return self.deforumation_settings_send[key]
        except Exception as e:
            if self.is_verbose:
                print("Error getSendConfigValue, value:" + str(key) + " -- " + str(e))
        return 0

    def getReceiveConfigValue(self, key):
        try:
            return self.deforumation_settings_receive[key]
        except Exception as e:
            if self.is_verbose:
                print("Error getReceiveConfigValue, value:" + str(key) + " -- " + str(e))
        return 0
    def deleteGuiConfigKey(self, key):
        if key in self.deforumation_settings_gui:
            del self.deforumation_settings_gui[key]
    def deletePromtMorphConfigKey(self, key=None):
        if key in self.deforumation_settings_promptmorph:
            del self.deforumation_settings_promptmorph[key]
        elif key == None:
            self.deforumation_settings_promptmorph = {}
    def addGuiConfigKey(self, key, value):
        self.deforumation_settings_gui[key] = value
    def getSendConfig(self):
        return self.deforumation_settings_send
    def getReceiveConfig(self):
        return self.deforumation_settings_receive
    def getGuiConfig(self):
        return self.deforumation_settings_gui
    def getPromtMorphConfig(self):
        return self.deforumation_settings_promptmorph
