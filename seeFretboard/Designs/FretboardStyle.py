from seeFretboard.Utilities.Constants import STANDARD_TUNING, STANDARD_TUNING_MIDI
from seeFretboard.Designs.CirlceNote import CircleNote

"""
These classes can be used to configure and customize the settings of a guitar fretboard for various purposes.
"""

class FretboardTheme:
    """Represents a theme for the fretboard visualization."""

    def __init__(self, theme=None, **kwargs):
        """
        Initializes a FretboardTheme object.

        Parameters:
            theme (str): The theme to apply ("blue, dark, wood, or green"). If None, a custom theme (light basically) is applied.
            **kwargs: Additional keyword arguments for custom theme settings.
        """

        self.customTheme(**kwargs)
        if(theme == "blue"):
            self.BlueTheme()
        elif(theme== "dark"):
            self.darkTheme()
        elif (theme == "wood"):
            self.woodTheme()
        elif(theme == "green"):
            self.greenTheme()

    def customTheme(self, **kwargs):
        """
        Applies a custom theme to the FretboardTheme object.

        Parameters:
            **kwargs: Keyword arguments for custom theme settings.
        """
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
    
    
    def BlueTheme(self):
        self.fretboardDesign.stringsColor = "#5188D4"
        self.fretboardDesign.fretColor = "#5188D4"
        self.fretboardDesign.fretboardMarkerColor = "#F2F9FC"
        self.fretboardDesign.backgroundColor = "#ADC7EC"
        self.fretboardDesign.setNoteType("green")
        self.fretboardDesign.tuningLabelColor = "white"
        self.fretboardDesign.fretLabelColor = "white"
        

    def darkTheme(self):
        self.fretboardDesign.stringsColor = "black"
        self.fretboardDesign.fretColor = "black"
        self.fretboardDesign.fretboardMarkerColor = "black"
        self.fretboardDesign.backgroundColor = "#001f3f"
        self.fretboardDesign.setNoteType("green")
        self.fretboardDesign.tuningLabelColor = "white"
        self.fretboardDesign.fretLabelColor = "white"

    def woodTheme(self):
        self.fretboardDesign.stringsColor = "#DFFFED"
        self.fretboardDesign.fretColor = "#DFFFED"
        self.fretboardDesign.fretboardMarkerColor = "#223447"
        self.fretboardDesign.backgroundColor = "#63462D"
        self.fretboardDesign.setNoteType("black")
        self.fretboardDesign.tuningLabelColor = "white"
        self.fretboardDesign.fretLabelColor = "white"

    def greenTheme(self):
        self.fretboardDesign.stringsColor = "#001f3f"
        self.fretboardDesign.fretColor = "#001f3f"
        self.fretboardDesign.fretboardMarkerColor = "#1F2421"
        self.fretboardDesign.backgroundColor = "#DFFFED"
        self.fretboardDesign.setNoteType("darkBlue")

class FretboardOrientation:
    """Represents the orientation (horizontal or vertical) of the fretboard."""

    def __init__(self, orientation="h"):
        """
        Initializes a FretboardOrientation object.

        Parameters:
            orientation (str): The orientation of the fretboard ("horizontal" or "vertical").
                               Defaults to "horizontal" if not specified.
        """
        self.orientation = orientation
    
    @property
    def orientation(self):
        """
        Get the orientation of the fretboard.

        Returns:
            str: The orientation of the fretboard.
        """
        return self._orientation
    
    @orientation.setter
    def orientation(self, orientation):
        """
        Set the orientation of the fretboard.

        Parameters:
            orientation (str): The orientation of the fretboard.
                               Must be "horizontal" ("h") or "vertical" ("v").
        """
        if orientation is None or orientation.lower() not in ["horizontal", "h", "vertical", "v"]:
            raise ValueError("Invalid orientation value. Must be 'horizontal', 'h', 'vertical', or 'v'.")
        self._orientation = orientation.lower()

class Tuning:
    """Represents the tuning of the strings on the fretboard.
       """

    def __init__(self, **kwargs):
        """
        Initializes a Tuning object.

        Parameters:
            **kwargs: Keyword arguments for tuning settings.
            letterTuning (list) A list of letter based tuning
            midiTuning (list) A list of midi based tuning
            numOfString (int) Number of Strings on Guitar
        """
        self.letterTuning = kwargs.get("letterTuning", STANDARD_TUNING)
        self.midiTuning = kwargs.get("midiTuning", STANDARD_TUNING_MIDI)
        self.numOfStrings = kwargs.get("numOfStrings", 6)
        
    @property
    def letterTuning(self):
        """
        Get the letter-based tuning of the strings.

        Returns:
            list: The letter-based tuning of the strings.
        """
        return self._letterTuning
    
    @letterTuning.setter
    def letterTuning(self, value):
        """
        Set the letter-based tuning of the strings.

        Parameters:
            value (list): The letter-based tuning of the strings.
        """
        self._letterTuning = value
        
    @property
    def midiTuning(self):
        """
        Get the MIDI note-based tuning of the strings.

        Returns:
            list: The MIDI note-based tuning of the strings.
        """
        return self._midiTuning
    
    @midiTuning.setter
    def midiTuning(self, value):
        """
        Set the MIDI note-based tuning of the strings.

        Parameters:
            value (list): The MIDI note-based tuning of the strings.
        """
        self._midiTuning = value
        
    @property
    def numOfStrings(self):
        """
        Get the number of strings on the fretboard.

        Returns:
            int: The number of strings on the fretboard.
        """
        return self._numOfStrings
    
    @numOfStrings.setter
    def numOfStrings(self, value):
        """
        Set the number of strings on the fretboard.

        Parameters:
            value (int): The number of strings on the fretboard.
        """
        self._numOfStrings = value

class FretboardRange:
    """Represents the range of frets and strings on the fretboard."""

    def __init__(self, fretFrom=1, fretTo=12, numOfString=6):
        """
        Initializes a FretboardRange object.

        Parameters:
            fretFrom (int): The starting fret number.
            fretTo (int): The ending fret number.
            numOfString (int): The number of strings on the fretboard.
        """
        if fretFrom <= 0:
            raise ValueError("fretFrom must be a positive integer.")
        if fretTo <= fretFrom:
            raise ValueError("fretTo must be greater than fretFrom.")
        if numOfString <= 0:
            raise ValueError("numOfString must be a positive integer.")
        self.fretFrom = fretFrom
        self.fretTo = fretTo
        self.numOfFrets = fretTo - fretFrom
        self.numOfStrings = numOfString
    
    @property
    def fretFrom(self):
        """
        Get the starting fret number.

        Returns:
            int: The starting fret number.
        """
        return self._fretFrom

    @fretFrom.setter
    def fretFrom(self, newFretFrom):
        """
        Set the starting fret number.

        Parameters:
            newFretFrom (int): The new starting fret number.
        """
        self._fretFrom = newFretFrom

    @property
    def fretTo(self):
        """
        Get the ending fret number.

        Returns:
            int: The ending fret number.
        """
        return self._fretTo

    @fretTo.setter
    def fretTo(self, newFretTo):
        """
        Set the ending fret number.

        Parameters:
            newFretTo (int): The new ending fret number.
        """
        self._fretTo = newFretTo

    @property
    def numOfFrets(self):
        """
        Get the number of frets in the range.

        Returns:
            int: The number of frets in the range.
        """
        return int(self.fretTo - self.fretFrom)

    @numOfFrets.setter
    def numOfFrets(self, numOfFrets):
        """
        Set the number of frets in the range.

        Parameters:
            numOfFrets (int): The new number of frets in the range.
        """
        self._numOfFrets = numOfFrets

    @property
    def numOfStrings(self):
        """
        Get the number of strings on the fretboard.

        Returns:
            int: The number of strings on the fretboard.
        """
        return self._numOfStrings

    @numOfStrings.setter
    def numOfStrings(self, numOfStrings):
        """
        Set the number of strings on the fretboard.

        Parameters:
            numOfStrings (int): The new number of strings on the fretboard.
        """
        self._numOfStrings = numOfStrings

class FretboardDesign:
    """Represents the design settings of the fretboard."""

    def __init__(self, **kwargs):
        """
        Initializes a FretboardDesign object.

        Parameters:
            **kwargs: Keyword arguments for design settings.
            showTuning (bool): Determines whether the tuning of the strings is displayed on the fretboard. Default is True.
            showFretboardNumber (bool): Determines whether the fretboard number is displayed on the fretboard. Default is True.
            toolBar (str): Determines whether a toolbar is displayed on the fretboard. "right" is default and means display on right side. None means don't display. Other Options: 'above', 'below', 'left'
            distanceBetweenFrets (int): The distance between two consecutive frets on the fretboard. Default is 5.
            distanceBetweenStrings (int): The distance between two consecutive strings on the fretboard. Default is 2.
            fretColor (str): The color of the frets on the fretboard. Default is "black".
            fretThinkness (int): The thickness of the fret lines on the fretboard. Default is 1.
            stringsColor (str): The color of the strings on the fretboard. Default is "black".
            stringThinkness (float): The thickness of the string lines on the fretboard. Default is 1.5.
            fretOpacity (float): The opacity of the frets on the fretboard. Default is 0.3.
            stringsOpacity (float): The opacity of the strings on the fretboard. Default is 1.0.
            backgroundColor (str): The background color of the fretboard. Default is "white".
            fretboardMarkerColor (str): The color of the fretboard markers. Default is "#DCDCDC".
        """
        # display
        self.showTuning = kwargs.get("showTuning", True)
        self.showFretboardNumber = kwargs.get("showFretboardNumber", True)
        self.toolBar = kwargs.get("toolBar", "right")

        # fretboard design
        self.distanceBetweenFrets = kwargs.get("distanceBetweenFrets", 5)
        self.distanceBetweenStrings = kwargs.get("distanceBetweenStrings", 2)
        self.fretColor = kwargs.get("fretColor", "black")
        self.fretThinkness = kwargs.get("stringThinkness", 1)
        self.stringsColor = kwargs.get("stringsColor", "black")
        self.stringThinkness = kwargs.get("stringThinkness", 1.5)
        self.fretOpacity = kwargs.get("fretOpacity", 0.3)
        self.stringsOpacity = kwargs.get("stringsOpacity", 1)

        self.backgroundColor = kwargs.get("backgroundColor", "white")
        self.fretboardMarkerColor = kwargs.get("fretboardMarkerColor", "#DCDCDC")

        #notes colors
        self.noteType = kwargs.get("noteType","prediction")

        self.noteTypes = {
            'prediction': CircleNote(), #default using that
            'groundTruth': CircleNote(noteFaceColor="red"),
            'white':CircleNote(noteFaceColor="white", noteTextColor = "black"),
            'black':CircleNote(noteFaceColor="black", noteTextColor="white",noteEdgeColor="#DFFFED", noteEdgeWidth=1), 
            'darkBlue':CircleNote(noteFaceColor="#001f3f", noteTextColor="#DFFFED"),
            'green':CircleNote(noteFaceColor="#DFFFED",noteTextColor="#001f3f",noteEdgeColor="#white" ),
        }

        self.tuningLabelColor = kwargs.get("tuningLabelColor","black")
        self.tuningLabelFontSize = kwargs.get("tuningLabelFontSize","10pt")
        self.fretLabelColor = kwargs.get("fretLabelColor","black")
        self.fretLabelFontsize = kwargs.get("fretLabelFontsize","10pt")

    @property
    def backgroundColor(self):
        """
        Get the background color.

        Returns:
            str: The background color.
        """
        return self._backgroundColor

    @backgroundColor.setter
    def backgroundColor(self, value):
        """
        Set the background color.

        Args:
            value (str): The background color to set.
        """
        self._backgroundColor = value

    @property
    def showTuning(self):
        """
        Get the flag indicating whether to display tuning information.

        Returns:
            bool: True if tuning information should be displayed, False otherwise.
        """
        return self._showTuning

    @showTuning.setter
    def showTuning(self, value):
        """
        Set the flag indicating whether to display tuning information.

        Parameters:
            value (bool): True to display tuning information, False otherwise.
        """
        self._showTuning = value

    @property
    def showFretboardNumber(self):
        """
        Get the flag indicating whether to display fretboard numbers.

        Returns:
            bool: True if fretboard numbers should be displayed, False otherwise.
        """
        return self._showFretboardNumber

    @showFretboardNumber.setter
    def showFretboardNumber(self, value):
        """
        Set the flag indicating whether to display fretboard numbers.

        Parameters:
            value (bool): True to display fretboard numbers, False otherwise.
        """
        self._showFretboardNumber = value

    @property
    def toolBar(self):
        """
        Get the position indicating whether to display the toolbar.

        Returns:
            str: None, right, left, above, below
        """
        return self._toolBar

    @toolBar.setter
    def toolBar(self, value):
        """
        Set the position indicating whether to display the toolbar.

        Parameters:
            value (str): None, right, left, above, below
        """
        self._toolBar = value

    @property
    def distanceBetweenFrets(self):
        """
        Get the distance between frets.

        Returns:
            float: The distance between frets.
        """
        return self._distanceBetweenFrets

    @distanceBetweenFrets.setter
    def distanceBetweenFrets(self, value):
        """
        Set the distance between frets.

        Parameters:
            value (float): The distance between frets.
        """
        self._distanceBetweenFrets = value

    @property
    def distanceBetweenStrings(self):
        """
        Get the distance between strings.

        Returns:
            float: The distance between strings.
        """
        return self._distanceBetweenStrings

    @distanceBetweenStrings.setter
    def distanceBetweenStrings(self, value):
        """
        Set the distance between strings.

        Parameters:
            value (float): The distance between strings.
        """
        self._distanceBetweenStrings = value

    @property
    def fretColor(self):
        """
        Get the color of the frets.

        Returns:
            str: The color of the frets.
        """
        return self._fretColor

    @fretColor.setter
    def fretColor(self, value):
        """
        Set the color of the frets.

        Parameters:
            value (str): The color of the frets.
        """
        self._fretColor = value

    @property
    def stringsColor(self):
        """
        Get the color of the strings.

        Returns:
            str: The color of the strings.
        """
        return self._stringsColor

    @stringsColor.setter
    def stringsColor(self, value):
        """
        Set the color of the strings.

        Parameters:
            value (str): The color of the strings.
        """
        self._stringsColor = value

    @property
    def fretOpacity(self):
        """
        Get the opacity of the frets.

        Returns:
            float: The opacity of the frets.
        """
        return self._fretOpacity

    @fretOpacity.setter
    def fretOpacity(self, value):
        """
        Set the opacity of the frets.

        Parameters:
            value (float): The opacity of the frets.
        """
        self._fretOpacity = value

    @property
    def stringsOpacity(self):
        """
        Get the opacity of the strings.

        Returns:
            float: The opacity of the strings.
        """
        return self._stringsOpacity

    @stringsOpacity.setter
    def stringsOpacity(self, value):
        """
        Set the opacity of the strings.

        Parameters:
            value (float): The opacity of the strings.
        """
        self._stringsOpacity = value

    @property
    def fretboardMarkerColor(self):
        """
        Get the color of the fretboard markers.

        Returns:
            str: The color of the fretboard markers.
        """
        return self._fretboardMarkerColor

    @fretboardMarkerColor.setter
    def fretboardMarkerColor(self, value):
        """
        Set the color of the fretboard markers.

        Parameters:
            value (str): The color of the fretboard markers.
        """
        self._fretboardMarkerColor = value

    @property
    def stringThinkness(self):
        """Get the thickness of the strings."""
        return self._stringThinkness
    
    @stringThinkness.setter
    def stringThinkness(self, value):
        """Set the thickness of the strings.

        Parameters:
            value (float): The thickness of the strings.
        """
        self._stringThinkness = value

    @property
    def fretThinkness(self):
        """Get the thickness of the frets."""
        return self._fretThinkness

    @fretThinkness.setter
    def fretThinkness(self, value):
        """Set the thickness of the frets.

        Parameters:
            value (float): The thickness of the frets.
        """
        self._fretThinkness = value

    def getNoteTypes(self):
        """Get the note types dictionary."""
        return self.noteTypes
    
    def getNoteType(self, key):
        """Get the note types associated with a specific key."""
        return self.noteTypes.get(key)

    def setNoteTypes(self, key, value):
        """Set the note types for a specific key."""
        self.noteTypes[key] = value

    def getCurrentNoteType(self):
        """Get the current note type."""
        return self.noteType

    def setNoteType(self, noteType):
        """Set the current note type."""
        self.noteType = noteType

    def getCurrentNoteTypeValue(self):
        """Get the note types associated with the current note type."""
        return self.getNoteType(self.getCurrentNoteType())

    @property
    def tuningLabelColor(self):
        """Get the color of the tuning labels."""
        return self._tuningLabelColor

    @tuningLabelColor.setter
    def tuningLabelColor(self, color):
        """Set the color of the tuning labels."""
        self._tuningLabelColor = color

    @property
    def tuningLabelFontSize(self):
        """Get the font size of the tuning labels."""
        return self._tuningLabelFontSize

    @tuningLabelFontSize.setter
    def tuningLabelFontSize(self, size):
        """Set the font size of the tuning labels."""
        self._tuningLabelFontSize = size

    @property
    def fretLabelColor(self):
        """Get the color of the fret labels."""
        return self._fretLabelColor

    @fretLabelColor.setter
    def fretLabelColor(self, color):
        """Set the color of the fret labels."""
        self._fretLabelColor = color

    @property
    def fretLabelFontSize(self):
        """Get the font size of the fret labels."""
        return self._fretLabelFontSize

    @fretLabelFontSize.setter
    def fretLabelFontSize(self, size):
        """Set the font size of the fret labels."""
        self._fretLabelFontSize = size