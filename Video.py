class Video():

    def __init__(self, startTime, endTime, currentFrame, frameStep, frameRate, name="defaultVid", fileExtension = "mpeg", codec="PIM1"):
        #format = {{frameNumber:chordString},{0:"5,0,5,5,0,0"},{1:"5,0,5,5,0,0"}}
        self.frames = {}

        #all these are digits or the keys
        self.startTime=round(startTime,2)
        self.endTime=round(endTime,2)
        self.currentFrame = round(currentFrame,2)

        self.frameStep=frameStep

        #number of frames per second
        self.frameRate = frameRate
        self.framePeriod = 1/self.frameRate

        self.currentAddTabFrames = 0
        self.name = name
        self.fileExtension = fileExtension
        self.codec = codec

    def getCurrentSecond(self):
        return self.currentFrame/self.frameRate

    def addTab(self, seconds, tab):
        frames = seconds * self.frameRate
        for i in range (1,frames+1):
            self.addFrame(self.currentAddTabFrames+i,tab)
        
        self.currentAddTabFrames = self.currentAddTabFrames+frames

    def addFrame(self, timeFrame , notes):
        timeFrame = round(timeFrame,2)
        self.frames[timeFrame] = notes
    
    def removeFrame(self, timeFrame):
        del self.frames[timeFrame]
    
    def getFrame(self, frame):
        return self.frames[frame]

    def getFrames(self):
        return self.frames
    
    def setFrames(self, frames):
        self.frames = frames
    
    def getFramesItems(self):
        return self.frames.items()

    def getFramesLength(self):
        return len(self.frames)
    
    def getFramesKeys(self):
        return self.frames.keys()
    
    def getFramesValues(self):
        return self.frames.values()
    
    def getFrameRate(self):
        return self.frameRate
    
    def setFrameRate(self, fr):
        self.frameRate = fr
    
    def getFramePeriod(self):
        return self.framePeriod

    def setFramePeriod(self, fp):
        self.framePeriod = fp

    def getCodec(self):
        return self.codec

    def setCodec(self, codec):
        self.codec = codec

    def getFileExtension(self):
        return self.fileExtension

    def setFileExtension(self, ext):
        self.fileExtension = ext

    def saveVideo(self):
        pass

    def getStartTime(self):
        return self.startTime
    
    def setStartTime(self, frame):
        self.startTime = round(frame,2)

    def getEndTime(self):
        return self.endTime
    
    def setEndTime(self, frame):
        self.endTime = round(frame,2)

    def getCurrentFrame(self):
        return self.currentFrame
    
    def setCurrentFrame(self, frame):
        self.currentFrame = round(frame,2)

    def getFrameStep(self):
        return self.frameStep
    
    def setFrameStep(self, step):
        self.frameStep = round(step,2)

    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name