import librosa
import numpy as np

class Audio_Wave_Librosa_Tools():
    def __init__(self, parent=None):
        self.parent = parent

    def getAudioBPM(self, audioPath):
        y, sr = librosa.load(audioPath, sr=None)
        tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
        #print("This audio file has tempo1:" + str(tempo))

        #onset_env = librosa.onset.onset_strength(y=y, sr=sr,aggregate=np.median)
        #tempo, beats = librosa.beat.beat_track(onset_envelope=onset_env,sr=sr)
        #print("This audio file has tempo2:" + str(tempo))
        return tempo, beats