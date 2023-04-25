import os
from Frame import Frame


class Video(Frame):

    def __init__(self, startTime, endTime, currentFrame, frameStep, frameRate=10, videoName="defaultVid", fileExtension="mp4", codec="mp4v"):
        super().__init__(frameRate)

        # format = {{frameNumber:chordString},{0:"5,0,5,5,0,0"},{1:"5,0,5,5,0,0"}}
        self.frames = {}

        # all these are digits or the keys
        self.startTime = round(startTime, 2)
        self.endTime = round(endTime, 2)
        self.currentFrame = round(currentFrame, 2)

        self.frameStep = frameStep

        self.currentAddTabFrames = 0
        self.fileExtension = fileExtension
        self.codec = codec

        # paths
        self.videoPath = os.getcwd()
        self.videoName = videoName
        self.videoPathWithName = os.path.join(self.videoPath,self.videoName)
        self.audioPath = os.getcwd()
        self.audioName = ""#'00_BN1-129-Eb_comp_hex.wav'
        self.audioPathWithName = os.path.join(self.audioPath,self.audioName)

    def getVideoPathName(self):
        return self.videoPath

    def setVideoPathName(self, path):
        self.videoPath = path

    def getAudioPathName(self):
        return self.audioPath

    def setAudioPathName(self, path):
        self.audioPath = path

    def getCurrentSecond(self):
        return self.currentFrame/self.frameRate

    def addTab(self, seconds, tab):
        frames = seconds * self.frameRate
        for i in range(1, frames+1):
            self.addFrame(self.currentAddTabFrames+i, tab)

        self.currentAddTabFrames = self.currentAddTabFrames+frames

    def addFrame(self, timeFrame, notes):
        timeFrame = round(timeFrame, 2)
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
        self.startTime = round(frame, 2)

    def getEndTime(self):
        return self.endTime

    def setEndTime(self, frame):
        self.endTime = round(frame, 2)

    def getCurrentFrame(self):
        return self.currentFrame

    def setCurrentFrame(self, frame):
        self.currentFrame = round(frame, 2)

    def getFrameStep(self):
        return self.frameStep

    def setFrameStep(self, step):
        self.frameStep = round(step, 2)

    def getVideoName(self):
        return self.videoName

    def setVideoName(self, name):
        self.videoName = name
    
    def getAudioName(self):
        return self.audioName

    def setAudioName(self, name):
        self.audioName = name
    
    def getVideoPathWithName(self):
        return os.path.join(self.videoPath,self.videoName)

    def setVideoPathWithName(self, path):
        self.videoPathWithName = path
    
    def getAudioPathWithName(self):
        return os.path.join(self.audioPath,self.audioName)

    def setAudioPathWithName(self, path):
        self.audioPathWithName = path
