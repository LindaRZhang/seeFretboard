class Video():
    def __init__(self, startFrame, endFrame, currentFrame, frameStep):
        #format = {{time:chordString},{0:"5,0,5,5,0,0"},{1:"5,0,5,5,0,0"}}
        self.frames = {}

        #all these are digits or the keys
        self.startFrame=round(startFrame,2)
        self.endFrame=round(endFrame,2)
        self.currentFrame = round(currentFrame,2)

        self.frameStep=frameStep

    def addFrame(self, timeFrame , notes):
        timeFrame = round(timeFrame,2)
        self.frames[timeFrame] = notes
    
    def removeFrame(self, timeFrame):
        del self.frames[timeFrame]
    
    def getFrame(self, frame):
        return self.frames[frame]

    def getFrames(self):
        return self.frames

    def getFramesLength(self):
        return len(self.frames)
    
    def getFramesKeys(self):
        return self.frames.keys()
    
    def getFramesValues(self):
        return self.frames.values()

    def saveVideo(self):
        pass

    def getStartFrame(self):
        return self.startFrame
    
    def setStartFrame(self, frame):
        self.startFrame = round(frame,2)

    def getEndFrame(self):
        return self.endFrame
    
    def setEndFrame(self, frame):
        self.endFrame = round(frame,2)

    def getCurrentFrame(self):
        return self.currentFrame
    
    def setCurrentFrame(self, frame):
        self.currentFrame = round(frame,2)

    def getFrameStep(self):
        return self.frameStep
    
    def setFrameStep(self, step):
        self.frameStep = round(step,2)