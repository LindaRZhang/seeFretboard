from seeFretboard.Utilities.Constants import STANDARD_TUNING, STANDARD_TUNING_MIDI

class FretboardTheme:
    def __init__(self, theme=None, **kwargs):
        # if(theme == "light"):
        #     self.lightTheme(kwargs.get("orientation"))
        
        # else:
            self.customTheme(**kwargs)

    def customTheme(self,  **kwargs):
        orientation = kwargs.get("orientation", "h")
        if isinstance(orientation, FretboardOrientation):
            self.orientation = orientation
        else:
            self.orientation = FretboardOrientation(orientation)

        tuning = kwargs.get("tuning")
        if tuning is not None and not isinstance(tuning, Tuning):
            raise TypeError("Invalid tuning input. Expected instance of Tuning.")
        if isinstance(tuning, Tuning):
            self.tuning = tuning
        else:
            self.tuning = Tuning(**kwargs)
            
        fretboardRange = kwargs.get("fretboardRange")
        if isinstance(fretboardRange, FretboardRange):
            self.fretboardRange = fretboardRange
        else:
            self.fretboardRange = FretboardRange(kwargs.get("fretFrom", 1),
                                                    kwargs.get("fretTo", 12),
                                                     kwargs.get("numOfString", 6))

        fretboardDesign = kwargs.get("fretboardDesign")

        if fretboardDesign is not None and not isinstance(fretboardDesign, FretboardDesign):
            raise TypeError("Invalid fretboardDesign input. Expected instance of FretboardDesign.")
        if isinstance(fretboardDesign, FretboardDesign):
            self.fretboardDesign = fretboardDesign
        else:
            self.fretboardDesign = FretboardDesign(**kwargs)
    
    # def lightTheme(self, orientation):
    #     self.orientation = FretboardOrientation(orientation)
    #     self.tuning = Tuning()
    #     self.fretboardRange = FretboardRange(fretFrom = 0, fretTo = 12)
    #     self.fretboardDesign = FretboardDesign()

class FretboardOrientation:
    def __init__(self, orientation = "h"):
        self.orientation = orientation
    
    @property
    def orientation(self):
        return self._orientation
    
    @orientation.setter
    def orientation(self, orientation):
        if orientation is None or orientation.lower() not in ["horizontal", "h", "vertical", "v"]:
            raise ValueError("Invalid orientation value. Must be 'horizontal', 'h', 'vertical', or 'v'.")
        self._orientation = orientation.lower()

class Tuning:
    def __init__(self, **kwargs):
        self.letterTuning = kwargs.get("letterTuning", STANDARD_TUNING)
        self.midiTuning = kwargs.get("midiTuning", STANDARD_TUNING_MIDI)
        self.numOfStrings = kwargs.get("numOfStrings", 6)
        
    @property
    def letterTuning(self):
        return self._letterTuning
    
    @letterTuning.setter
    def letterTuning(self, value):
        self._letterTuning = value
        
    @property
    def midiTuning(self):
        return self._midiTuning
    
    @midiTuning.setter
    def midiTuning(self, value):
        self._midiTuning = value
        
    @property
    def numOfStrings(self):
        return self._numOfStrings
    
    @numOfStrings.setter
    def numOfStrings(self, value):
        self._numOfStrings = value

class FretboardRange:
    def __init__(self, fretFrom, fretTo, numOfString):
        if fretFrom <= 0:
            raise ValueError("fretFrom must be a positive integer.")
        if fretTo <= fretFrom:
            raise ValueError("fretTo must be greater than fretFrom.")
        if numOfString < 0:
            raise ValueError("numOfString must be a positive integer.")
        self.fretFrom = fretFrom
        self.fretTo = fretTo
        self.numOfFrets = fretTo - fretFrom
        self.numOfStrings = numOfString
    
    @property
    def fretFrom(self):
        return self._fretFrom

    @fretFrom.setter
    def fretFrom(self, newFretFrom):
        self._fretFrom = newFretFrom

    @property
    def fretTo(self):
        return self._fretTo

    @fretTo.setter
    def fretTo(self, newFretTo):
        self._fretTo = newFretTo

    @property
    def numOfFrets(self):
        return int(self.fretTo - self.fretFrom)

    @numOfFrets.setter
    def numOfFrets(self, numOfFrets):
        self._numOfFrets = numOfFrets

    @property
    def numOfStrings(self):
        return self._numOfStrings

    @numOfStrings.setter
    def numOfStrings(self, numOfStrings):
        self._numOfStrings = numOfStrings

class FretboardDesign:
    def __init__(self, **kwargs):
        # display
        self.showTuning = kwargs.get("showTuning", True)
        self.showFretboardNumber = kwargs.get("showFretboardNumber", True)
        self.toolBar = kwargs.get("toolBar", True)

        # fretboard design
        self.distanceBetweenFrets = kwargs.get("distanceBetweenFrets", 5)
        self.distanceBetweenStrings = kwargs.get("distanceBetweenStrings", 2)
        self.fretColor = kwargs.get("fretColor", "black")
        self.stringsColor = kwargs.get("stringsColor", "black")
        self.fretOpacity = kwargs.get("fretOpacity", 0.3)
        self.stringsOpacity = kwargs.get("stringsOpacity", 1)

        #width of them both later add
        self.fretboardMarkerColor = kwargs.get("fretboardMarkerColor", "#DCDCDC")



    @property
    def showTuning(self):
        return self._showTuning

    @showTuning.setter
    def showTuning(self, value):
        self._showTuning = value

    @property
    def showFretboardNumber(self):
        return self._showFretboardNumber

    @showFretboardNumber.setter
    def showFretboardNumber(self, value):
        self._showFretboardNumber = value

    @property
    def toolBar(self):
        return self._toolBar

    @showFretboardNumber.setter
    def toolBar(self, value):
        self._toolBar = value

    @property
    def distanceBetweenFrets(self):
        return self._distanceBetweenFrets

    @distanceBetweenFrets.setter
    def distanceBetweenFrets(self, distanceBetweenFrets):
        self._distanceBetweenFrets = distanceBetweenFrets

    @property
    def distanceBetweenStrings(self):
        return self._distanceBetweenStrings

    @distanceBetweenStrings.setter
    def distanceBetweenStrings(self, distanceBetweenStrings):
        self._distanceBetweenStrings = distanceBetweenStrings

    @property
    def fretboardColor(self):
        return self._fretboardColor

    @fretboardColor.setter
    def fretboardColor(self, color):
        self._fretboardColor = color

    @property
    def stringsColor(self):
        return self._stringsColor

    @stringsColor.setter
    def stringsColor(self, color):
        self._stringsColor = color

    @property
    def fretboardOpacity(self):
        return self._fretboardOpacity

    @fretboardOpacity.setter
    def fretboardOpacity(self, value):
        self._fretboardOpacity = value

    @property
    def stringsOpacity(self):
        return self._stringsOpacity

    @stringsOpacity.setter
    def stringsOpacity(self, value):
        self._stringsOpacity = value

    @property
    def fretboardMarkerColor(self):
        return self._fretboardMarkerColor

    @fretboardMarkerColor.setter
    def fretboardMarkerColor(self, color):
        self._fretboardMarkerColor = color