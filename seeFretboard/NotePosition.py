class NotePositionsOnCurrentFretboard():
    """
    The NotePositionsOnCurrentFretboard class represents a position of a note on a guitar fretboard. 
    It has two main attributes: the string number and the fret number. 
    The class provides methods to get and set these attributes.
    """
    def __init__(self, string, fret):
        self.string = string
        self.fret = fret
    
    def getFret(self):
        """
        Returns the fret number of the note position.

        Returns:
            int: The fret number of the note position.
        """
        return self.fret
    
    def setFret(self, fret):
        """
        Sets the fret number of the note position.

        Args:
            fret (int): The fret number of the note position.
        """
        self.fret = fret
    
    def getString(self):
        """
        Returns the string number of the note position.

        Returns:
            int: The string number of the note position.
        """
        return self.string
    
    def setString(self, string):
        """
        Sets the string number of the note position.

        Args:
            string (int): The string number of the note position.
        """
        self.string = string