class CircleNote():
    '''
    CircleNote is a class for displaying notes with customizable properties.

    Attributes:
    - noteFaceColor (str): The color of the note face. Default is 'blue'.
    - noteFill (bool): Indicates whether the note should be filled. Default is True.
    - noteEdgeColor (str): The color of the note edge. Default is 'black'.
    - noteEdgeWidth (int): The width of the note edge. Default is 2.
    - noteRadius (float): The radius of the note. Default is 0.4.
    - noteOpacity (float): The opacity of the note. Default is 1.
    - noteTextColor (str): The color of the text inside note.
    - noteTextFont (str): The font of the text inside note.

    - intervals (list): List of intervals associated with the note.
    - scaleDegrees (list): List of scale degrees associated with the note.
    - name (str): The name of the note.
    - nameWithOctave (str): The name of the note with octave information.

    - fret (int): The fret position of the note.
    - string (int): The string position of the note.
    '''
    def __init__(self, **kwargs):
        '''
        Initializes a CircleNote object with the specified properties.

        Parameters:
        - **kwargs (dict): Additional keyword arguments for customizing the note properties.
        '''
        #more for drawing part
        self.noteFaceColor = kwargs.get('noteFaceColor', 'blue')
        self.noteFill = kwargs.get('noteFill', True)
        self.noteEdgeColor = kwargs.get('noteEdgeColor', 'black')
        self.noteEdgeWidth = kwargs.get('noteEdgeWidth', 2)
        self.noteRadius = kwargs.get('noteRadius', 0.4)
        self.noteOpactiy = kwargs.get('noteOpactiy', 1)
        self.noteTextColor = kwargs.get('noteTextColor', "white")
        self.noteTextFont = kwargs.get('noteTextFont', "10pt")

        #text part
        self.intervals = kwargs.get('interval', None)
        self.scaleDegrees = kwargs.get('scaleDegree', None)
        self.name = kwargs.get('name', None)
        self.nameWithOctave = kwargs.get('nameWithOctave', None)
        
        #current note string and fret
        self.fret = kwargs.get('fret', None)
        self.string = kwargs.get('string', None)
        
    
    def getNoteRadius(self):
        '''
        Get the radius of the note.

        Returns:
        - noteRadius (float): The radius of the note.
        '''
        return self.noteRadius
    
    def setNoteRadius(self,radius):
        '''
        Set the radius of the note.

        Parameters:
        - radius (float): The radius of the note.
        '''
        self.noteRadius = radius
        
    def getNoteFaceColor(self):
        '''
        Get the color of the note face.

        Returns:
        - noteFaceColor (str): The color of the note face.
        '''
        return self.noteFaceColor
    
    def setNoteFaceColor(self,color):
        '''
        Set the color of the note face.

        Parameters:
        - color (str): The color of the note face.
        '''
        self.noteFaceColor = color
        
    def getNoteEdgeColor(self):
        '''
        Get the color of the note edge.

        Returns:
        - noteEdgeColor (str): The color of the note edge.
        '''
        return self.noteEdgeColor
    
    def setNoteEdgeColor(self,color):
        '''
        Set the color of the note edge.

        Parameters:
        - color (str): The color of the note edge.
        '''
        self.noteEdgeColor = color
        
    def getNoteEdgeWidth(self):
        '''
        Get the width of the note edge.

        Returns:
        - noteEdgeWidth (int): The width of the note edge.
        '''
        return self.noteEdgeWidth
    
    def setNoteEdgeWidth(self,lw):
        '''
        Set the width of the note edge.

        Parameters:
        - lw (int): The width of the note edge.
        '''
        self.noteEdgeWidth = lw
        
    def getNoteFill(self):
        '''
        Check if the note is filled.

        Returns:
        - noteFill (bool): True if the note is filled, False otherwise.
        '''
        return self.noteFill
    
    def setNoteFill(self,noteFill):
        '''
        Set whether the note should be filled.

        Parameters:
        - noteFill (bool): True to fill the note, False to leave it empty.
        '''
        self.noteFill = noteFill

    def getNoteOpacity(self):
        '''
        Get the opacity of the note.

        Returns:
        - noteOpacity (float): The opacity of the note.
        '''
        return self.noteOpactiy

    def setNoteOpacity(self,noteOpacity):
        '''
        Set the opacity of the note.

        Parameters:
        - noteOpacity (float): The opacity of the note.
        '''
        self.noteOpacity = noteOpacity
    
    def getIntervals(self):
        '''
        Get the intervals associated with the note.

        Returns:
        - intervals (list): List of intervals associated with the note.
        '''
        return self.intervals
    
    def setIntervals(self, interval):
        '''
        Set the intervals associated with the note.

        Parameters:
        - interval (list): List of intervals to associate with the note.
        '''

        self.intervals = interval
    
    def getScaleDegrees(self):
        '''
        Get the scale degrees associated with the note.

        Returns:
        - scaleDegrees (list): List of scale degrees associated with the note.
        '''
        return self.scaleDegrees
    
    def setScaleDegrees(self, scaleDegree):
        '''
        Set the scale degrees associated with the note.

        Parameters:
        - scaleDegree (list): List of scale degrees to associate with the note.
        '''
        self.scaleDegrees = scaleDegree
    
    def getName(self):
        '''
        Get the name of the note.

        Returns:
        - name (str): The name of the note.
        '''
        return self.name
    
    def setName(self, name):
        '''
        Set the name of the note.

        Parameters:
        - name (str): The name of the note.
        '''
        self.name = name
    
    def getNameWithOctave(self):
        '''
        Get the name of the note with octave information.

        Returns:
        - nameWithOctave (str): The name of the note with octave information.
        '''
        return self.nameWithOctave
    
    def setNameWithOctave(self, nameWithOctave):
        '''
        Set the name of the note with octave information.

        Parameters:
        - nameWithOctave (str): The name of the note with octave information.
        '''
        self.nameWithOctave = nameWithOctave

    def getNoteTextColor(self):
        """Get the color of the note text."""
        return self.noteTextColor

    def setNoteTextColor(self, value):
        """Set the color of the note text."""
        self.noteTextColor = value

    def getNoteTextFont(self):
        """Get the font of the note text."""
        return self.noteTextFont
    
    def setNoteTextFont(self, value):
        """Set the font of the note text."""
        self._noteTextFont = value