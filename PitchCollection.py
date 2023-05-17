class PitchCollection():
    def __init__(self, pitchesType = "pitchesNames"):
        """
        A class representing a collection of pitches.

        Args:
            pitchesType (str): The type of pitches to store.

        Attributes:
            pitchesNames (list): A list of pitch names.
            pitchesWithOctave (list): A list of pitches with octave.
            pitchesScaleDegrees (list): A list of pitch scale degrees.
            pitchesType (str): The type of pitches being stored.
            pitchesIndex (int): The current index for accessing pitches.
            frets (list): A list of fret values that correspond to the pitches.
            strings (list): A list of string values that correspond to the pitches.
            arrayTypeNow (list): The current array type based on pitchesType.
        """
        self.pitchesNames = [""]
        self.pitchesWithOctave = [""]
        self.pitchesScaleDegrees = [""]
        self.pitchesType = pitchesType
        self.pitchesIndex = 0

        self.frets = []
        self.strings = []
        self.arrayTypeNow = []
    
    # Getter methods for the lengths of pitch lists

    def getPitchesNamesLength(self):
        """Returns the length of pitchesNames list."""
        return len(self.pitchesNames)

    def getPitchesWithOctaveLength(self):
        """Returns the length of pitchesWithOctave list."""
        return len(self.pitchesWithOctave)

    def getPitchesScaleDegreesLength(self):
        """Returns the length of pitchesScaleDegrees list."""
        return len(self.pitchesScaleDegrees)

    def getArrayTypeNowLength(self):
        """Returns the length of arrayTypeNow list."""
        return len(self.arrayTypeNow)

    def getFretsLength(self):
        """Returns the length of frets list."""
        return len(self.frets)

    def getStringsLength(self):
        """Returns the length of strings list."""
        return len(self.strings)

    # Getter and setter methods for pitch lists
    def getPitchesNames(self):
        """Returns the pitchesNames list."""
        return self.pitchesNames
    
    def appendPitchesName(self, value):
        """Appends a value to the pitchesNames list."""
        self.pitchesNames.append(value)

    def setPitchesNames(self, value):
        """Sets the pitchesNames list to the given value."""
        self.pitchesNames = value

    def emptyPitchesNames(self):
        """Empties the pitchesNames list."""
        self.pitchesNames = []
    
    def getPitchWithOctave(self):
        """Returns the pitchesWithOctave list."""
        return self.pitchesWithOctave
    
    def appendPitchWithOctave(self, value):
        """Appends a value to the pitchesWithOctave list."""
        self.pitchesWithOctave.append(value)

    def setPitchWithOctave(self, value):
        """Sets the pitchesWithOctave list to the given value."""
        self.pitchesWithOctave = value
    
    def emptyPitchesWithOctaves(self):
        """Empties the pitchesWithOctave list."""
        self.pitcheshWithOctave = []

    def getPitchesScaleDegrees(self):
        """Returns the pitchesScaleDegrees list."""
        return self.pitchesScaleDegrees
    
    def appendPitchesScaleDegree(self, value):
        """Appends a value to the pitchesScaleDegrees list."""
        self.pitchesScaleDegrees.append(value)

    def setPitchesScaleDegrees(self, value):
        """Sets the pitchesScaleDegrees list to the given value."""
        self.pitchesScaleDegrees = value
    
    def emptyPitchesScaleDegree(self):
        """Empties the pitchesScaleDegrees list."""
        self.pitchesScaleDegrees = []

    def getPitchesType(self):
        """Returns the current pitchesType."""
        return self.pitchesType
    
    def setPitchesType(self, value):
        """Sets the pitchesType to the given value."""
        self.pitchesType = value

    def getArrayTypeNow(self):
        """
        Returns the current arrayType based on the pitchesType.

        Returns:
            list: The current arrayTypeNow list based on the pitchesType.
        """
        if self.pitchesType == "pitchesNames":
            pitchValue = self.pitchesNames
        elif self.pitchesType == "pitchesWithOctave":
            pitchValue = self.pitchesWithOctave
        elif self.pitchesType == "pitchesScaleDegrees":
            pitchValue = self.pitchesScaleDegrees
        
        self.arrayTypeNow = pitchValue
        
        return self.arrayTypeNow
    
    def getArrayTypeNowAt(self, index):
        """
        Returns the value at the specified index of the arrayTypeNow list.

        Args:
            index (int): The index of the value to retrieve.

        Returns:
            Any: The value at the specified index of the arrayTypeNow list.
        """
        return self.getArrayTypeNow()[index]
    
    def setArrayTypeNow(self):
        """Sets the arrayTypeNow to the current array type."""
        return self.arrayTypeNow
    
    def emptyArrayTypeNow(self):
        """Empties the arrayTypeNow list."""
        self.arrayTypeNow = []
    
    def getPitchesIndex(self):
        """Returns the current pitchesIndex."""
        return self.pitchesIndex
    
    def addPitchesIndex(self, amount=1):
        """Adds the specified amount to the pitchesIndex."""
        self.pitchesIndex += amount

    def setPitchesIndex(self, value):
        """Sets the pitchesIndex to the given value."""
        self.pitchesIndex = value
    
    def getFrets(self):
        """Returns the frets list."""
        return self.frets

    def getFretsAt(self,index):
        """
        Returns the value at the specified index of the frets list.

        Args:
            index (int): The index of the value to retrieve.

        Returns:
            Any: The value at the specified index of the frets list.
        """
        return self.frets[index]

    def appendFrets(self, value):
        """Appends a value to the frets list."""
        self.frets.append(value)

    def setFrets(self, value):
        """Sets the frets list to the given value."""
        self.frets = value
    
    def emptyFrets(self):
        """Empties the frets list."""
        self.frets = []
    
    def emptyStrings(self):
        """Empties the strings list."""
        self.strings = []

    def getStrings(self):
        """Returns the strings list."""
        return self.strings
    
    def getStringsAt(self,index):
        """
        Returns the value at the specified index of the strings list.

        Args:
            index (int): The index of the value to retrieve.

        Returns:
            Any: The value at the specified index of the strings list.
        """
        return self.strings[index]

    def appendStrings(self, value):
        """Appends a value to the strings list."""
        self.strings.append(value)

    def setStrings(self, value):
        """Sets the strings list to the given value."""
        self.strings = value

    def getFretStringCurrentPitch(self):
        """
        Returns the current fret, string, and pitch values based on the pitchesIndex.
        
        Returns:
            tuple: A tuple containing the current fret, string, and pitch values.

        """
        return self.getFretsAt(self.pitchesIndex), self.getStringsAt(self.pitchesIndex), self.getArrayTypeNowAt(self.pitchesIndex)

