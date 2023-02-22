class Video():
    def __init__(self, startFrame, endFrame, currentFrame, frameStep):
        self.frames = {}
        self.startFrame=startFrame
        self.endFrame=endFrame
        self.currentFrame = currentFrame
        self.frameStep=frameStep

    def addFrame(self, timeFrame , notes):
        self.frames[timeFrame] = notes
    
    def removeFrame(self, timeFrame):
        del self.frames[timeFrame]
    
    def getFrame(self, frame):
        return self.frames[frame]

    def getFrames(self):
        return self.frames

    def saveVideo(self):
        pass

    def getStartFrame(self):
        return self.startFrame
    
    def setStartFrame(self, frame):
        self.startFrame = frame

    def getEndFrame(self):
        return self.endFrame
    
    def setEndFrame(self, frame):
        self.endFrame = frame

    def getCurrentFrame(self):
        return self.currentFrame
    
    def setCurrentFrame(self, frame):
        self.currentFrame = frame

    def getFrameStep(self):
        return self.frameStep
    
    def setFrameStep(self, step):
        self.frameStep = step