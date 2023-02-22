class Video():
    def __init__(self):
        self.frames = []
        self.startFrame=0
        self.endFrame=0
        self.currentFrame = 0
        self.frameStep=.1

    def addFrame(self, timeFrame , notes):
        self.frames[timeFrame] = notes
    
    def removeFrame(self, timeFrame):
        del self.frames[timeFrame]
    
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