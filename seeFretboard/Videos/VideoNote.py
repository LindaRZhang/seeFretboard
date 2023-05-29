class VideoNote():
    def __init__(self, pitch, startTime, endTime):
        """
        The VideoNote class represents a video note, which contains information about 
        the pitch, start time, and end time of a note in a video. 
        The main functionalities of this class are to store and retrieve this information,
        as well as to update it if necessary.

        Args:
            pitch (str): The pitch of the note.
            startTime (float): The start time of the note in seconds.
            endTime (float): The end time of the note in seconds.
        """
        self.pitch = pitch
        self.startTime = startTime
        self.endTime = endTime
    
    def getPitch(self):
        """
        Returns the pitch of the note.

        Returns:
            str: The pitch of the note.
        """
        return self.pitch
    
    def setPitch(self, pitch):
        """
        Sets the pitch of the note.

        Args:
            pitch (str): The pitch of the note.
        """
        self.pitch = pitch
    
    def getStartTime(self):
        """
        Returns the start time of the note.

        Returns:
            float: The start time of the note in seconds.
        """
        return self.startTime
    
    def setStartTime(self, startTime):
        """
        Sets the start time of the note.

        Args:
            startTime (float): The start time of the note in seconds.
        """
        self.startTime = startTime

    def getEndTime(self):
        """
        Returns the end time of the note.

        Returns:
            float: The end time of the note in seconds.
        """
        return self.endTime
    
    def setEndTime(self, endTime):
        """
        Sets the end time of the note.

        Args:
            endTime (float): The end time of the note in seconds.
        """
        self.endTime = endTime
