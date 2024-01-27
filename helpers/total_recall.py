import time
import pickle


class Deforumation_Total_Recall():

    def __init__(self, parent=None, namedpipes = None):
        self.currentTotalRecallFrame = None
        self.deforumationnamedpipes = namedpipes
        self.currentFrameNumber = 0
    def setCurrentTotalRecallFrame(self, frameNumber):
        self.currentTotalRecallFrame = self.getOriginalFrameParameters(frameNumber)
        self.currentFrameNumber = frameNumber
        return self.currentTotalRecallFrame

    def getCurrentTotalRecallFrame(self, frameNumber=-1):
        if frameNumber == -1:
            return self.currentTotalRecallFrame
        else:
            return self.getOriginalFrameParameters(frameNumber)

    def getOriginalFrameParameters(self, frameNumber):
        parameter_container = pickle.loads(self.deforumationnamedpipes.readValue("saved_frame_params", frameNumber, True))
        return parameter_container
