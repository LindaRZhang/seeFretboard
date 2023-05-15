
class PitchCollection():
    def __init__(self, pitchesType = "pitchesNames"):
        #differentTypeOfNaming or displays for for scales, arpeggios, chord, intervals
        self.pitchesNames = [""]
        self.pitchesWithOctave = [""]
        self.pitchesScaleDegrees = [""]
        self.pitchesType = pitchesType
        self.pitchesIndex = 0
        self.frets = []
        self.strings = []
        self.arrayTypeNow = []
    

    def getPitchesNamesLength(self):
        return len(self.pitchesNames)

    def getPitchesShWithOctaveLength(self):
        return len(self.pitchesshWithOctave)

    def getPitchesScaleDegreesLength(self):
        return len(self.pitchesScaleDegrees)

    def getArrayTypeNowLength(self):
        return len(self.arrayTypeNow)

    def getFretsLength(self):
        return len(self.frets)

    def getStringsLength(self):
        return len(self.strings)

    def getPitchesNames(self):
        return self.pitchesNames
    
    def appendPitchesName(self, value):
        self.pitchesNames.append(value)

    def setPitchesNames(self, value):
        self.pitchesNames = value

    def emptyPitchesNames(self):
        self.pitchesNames = []
    
    def getPitchWithOctave(self):
        return self.pitchesWithOctave
    
    def appendPitchWithOctave(self, value):
        self.pitchesWithOctave.append(value)

    def setPitchWithOctave(self, value):
        self.pitchesWithOctave = value
    
    def emptyPitchesWithOctaves(self):
        self.pitcheshWithOctave = []

    def getPitchesScaleDegrees(self):
        return self.pitchesScaleDegrees
    
    def appendPitchesScaleDegree(self, value):
        self.pitchesScaleDegrees.append(value)

    def setPitchesScaleDegrees(self, value):
        self.pitchesScaleDegrees = value
    
    def emptyPitchesScaleDegree(self):
        self.pitchesshWithOctave = []

    def getPitchesType(self):
        return self.pitchesType
    
    def setPitchesType(self, value):
        self.pitchesType = value

    def getArrayTypeNow(self):
        if self.pitchesType == "pitchesNames":
            pitchValue = self.pitchesNames
        elif self.pitchesType == "pitchesWithOctave":
            pitchValue = self.pitchesWithOctave
        elif self.pitchesType == "pitchesScaleDegrees":
            pitchValue = self.pitchesScaleDegrees
        
        self.arrayTypeNow = pitchValue
        
        return self.arrayTypeNow
    
    def getArrayTypeNowAt(self, index):
        return self.getArrayTypeNow()[index]
    
    def setArrayTypeNow(self):
        return self.arrayTypeNow
    
    def emptyArrayTypeNow(self):
        self.arrayTypeNow = []
    
    
    def getPitchesIndex(self):
        return self.pitchesIndex
    
    def addPitchesIndex(self, amount=1):
        self.pitchesIndex+=amount

    def setPitchesIndex(self, value):
        self.pitchesIndex = value
    
    def getFrets(self):
        return self.frets

    def getFretsAt(self,index):
        return self.frets[index]

    def appendFrets(self, value):
        self.frets.append(value)

    def setFrets(self, value):
        self.frets = value
    
    def emptyFrets(self):
        self.frets = []
    
    def emptyStrings(self):
        self.strings = []

    def getStrings(self):
        return self.strings
    
    def getStringsAt(self,index):
        return self.strings[index]

    def appendStrings(self, value):
        self.strings.append(value)

    def setStrings(self, value):
        self.strings = value


    def getFretStringCurrentPitch(self):
        return self.getFretsAt(self.pitchesIndex),self.getStringsAt(self.pitchesIndex),self.getArrayTypeNowAt(self.pitchesIndex)
        