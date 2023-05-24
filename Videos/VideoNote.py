class VideoNote():
    def __init__(self, pitch, startTime, endTime):
        self.pitch = pitch
        self.startTime = startTime
        self.endTime = endTime
    
    def getPitch(self):
        return self.pitch
    
    def setPitch(self, pitch):
        self.pitch = pitch
    
    def getStartTime(self):
        return self.startTime
    
    def setStartTime(self, startTime):
        self.startTime = startTime

    def getEndTime(self):
        return self.endTime
    
    def setEndTime(self, endTime):
        self.endTime = endTime
