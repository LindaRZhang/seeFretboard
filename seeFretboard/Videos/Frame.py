class Frame():
    def __init__(self, frameRate):
        self.frameRate = frameRate
        self.framePeriod = 1/self.frameRate

    def getFrameRate(self):
        return self.frameRate

    def setFrameRate(self, fr):
        self.frameRate = fr

    def getFramePeriod(self):
        return 1/self.frameRate

    def setFramePeriod(self, fp):
        self.framePeriod = fp
