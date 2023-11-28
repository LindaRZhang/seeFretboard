import mirdata
import math
import os
import numpy as np
from .Frame import Frame
from .VideoNote import VideoNote
import seeFretboard.Utilities.Functions as Functions
from seeFretboard.Utilities.Constants import BASE_PATH,FRAMERATE
# set for 6 string in standard tuning for now

# tab consist of many frames or the frames in certain period


class TabSequence(Frame):
    '''
    The TabSequence class is responsible for generating sequences of frame from audio files. 
    It uses the GuitarSet dataset to extract note information from audio tracks and converts 
    this information into tablature frames. The class can generate frames in either fret or 
    MIDI format and can convert between the two. It also provides methods for adding tablature 
    frames and converting frames to notes with time information.
    '''
    def __init__(self, trackNum=0, frameRate=FRAMERATE, filePath=os.path.join(BASE_PATH, 'GuitarSet')):
        '''
        Parameters:
            trackNum (int): The index of the track to load from the dataset.
            frameRate (float, optional): The frame rate of the tab sequence. Default is FRAMERATE.
            filePath (str, optional): The file path to the GuitarSet dataset. Default is 'BASE_PATH/GuitarSet'.
            '''
        super().__init__(frameRate)

        self.filePath = filePath
        self.guitarset = mirdata.initialize(
            'guitarset', data_home=self.filePath)

        self.guitarsetIds = self.guitarset.track_ids  # the list of guitar's track ids
        self.guitarsetData = self.guitarset.load_tracks()  # Load all tracks in the dataset
        # Get the first track
        self.track = self.guitarsetData[self.guitarsetIds[trackNum]]
        # trackNum starts at 0

        # strings and their Midi
        self.Elow = 40
        self.A = 45
        self.D = 50
        self.G = 55
        self.B = 59
        self.EHigh = 64

        self.EStringFrets = Functions.midiToFret(
            self.Elow, self.track.notes["E"].pitches)
        self.ETimeStamp = self.track.notes['E'].intervals
        self.AStringFrets = Functions.midiToFret(
            self.A, self.track.notes["A"].pitches)
        self.ATimeStamp = self.track.notes['A'].intervals
        self.DStringFrets = Functions.midiToFret(
            self.D, self.track.notes["D"].pitches)
        self.DTimeStamp = self.track.notes['D'].intervals
        self.GStringFrets = Functions.midiToFret(
            self.G, self.track.notes["G"].pitches)
        self.GTimeStamp = self.track.notes['G'].intervals
        self.BStringFrets = Functions.midiToFret(
            self.B, self.track.notes["B"].pitches)
        self.BTimeStamp = self.track.notes['B'].intervals
        self.eStringFrets = Functions.midiToFret(
            self.EHigh, self.track.notes["e"].pitches)
        self.eTimeStamp = self.track.notes['e'].intervals

        # guitarSet is automatically in midi notes
        self.EMidiPitches = self.track.notes["E"].pitches
        self.AMidiPitches = self.track.notes["A"].pitches
        self.DMidiPitches = self.track.notes["D"].pitches
        self.GMidiPitches = self.track.notes["G"].pitches
        self.BMidiPitches = self.track.notes["B"].pitches
        self.eMidiPitches = self.track.notes["e"].pitches

        self.maxEndTime = max(self.ETimeStamp[-1][-1], self.ATimeStamp[-1][-1],
                              self.DTimeStamp[-1][-1], self.GTimeStamp[-1][-1], self.BTimeStamp[-1][-1], self.eTimeStamp[-1][-1])

        self.numOfStrings = 6
        self.maxFrames = math.ceil(self.maxEndTime) * self.frameRate

        self.fretFrames = []
        self.midiFrames = []
        self.notesWithTimeFrames = []
        self.frameType = "fret"

        self.currentTime = 0

    def getNumOfStrings(self):
        """
        Get the number of strings in the tab sequence.

        Returns:
            int: The number of strings.
        """
        return self.numOfStrings

    def setNumOfStrings(self, strings):
        """
        Set the number of strings in the tab sequence.

        Parameters:
            strings (int): The number of strings to set.
        """
        self.numOfStrings = strings
    
    def getMaxFrames(self):
        """
        Get the maximum number of frames in the tab sequence.

        Returns:
            int: The maximum number of frames.
        """
        return math.ceil(self.getMaxEndTime()) * self.getFrameRate()

    def setMaxFrames(self, maxFrames):
        """
        Set the maximum number of frames in the tab sequence.

        Parameters:
            maxFrames (int): The maximum number of frames to set.
        """
        self.maxFrames = maxFrames
    
    def getMaxEndTime(self):
        """
        Get the maximum end time of the tab sequence.

        Returns:
            float: The maximum end time.
        """
        return self.maxEndTime

    def setMaxEndTime(self, maxEndTime):
        """
        Set the maximum end time of the tab sequence.

        Parameters:
            maxEndTime (float): The maximum end time to set.
        """
        self.maxEndTime = maxEndTime

    def getStringFrets(self):
        """
        Get the fret positions of each string in the tab sequence.

        Returns:
            list: A list of lists representing the fret positions of each string.
        """
        return [self.EStringFrets, self.AStringFrets, self.DStringFrets, self.GStringFrets, self.BStringFrets, self.eStringFrets]

    def getStringMidi(self):
        """
        Get the MIDI pitches of each string in the tab sequence.

        Returns:
            list: A list of MIDI pitches of each string.
        """
        return [self.Elow, self.A, self.D, self.G, self.B, self.EHigh]
    
    def getMidiPitches(self):
        """
        Get the MIDI pitches of all strings in the tab sequence.

        Returns:
            list: A list of lists representing the MIDI pitches of all strings.
        """
        arr = [self.EMidiPitches, self.AMidiPitches, self.DMidiPitches,
               self.GMidiPitches, self.BMidiPitches, self.eMidiPitches]
        roundedArray = [[round(num) for num in innerArr] for innerArr in arr]

        return roundedArray

    def makingFrames(self):
        """
        Create the frames for the tab sequence based on the string frets or MIDI pitches.

        This method populates the `fretFrames` attribute if the frame type is "fret",
        otherwise it populates the `midiFrames` attribute.

        Note: The method assumes that the frets or MIDI pitches have already been initialized.

        """
        frames = [['x'] * self.numOfStrings for _ in range(self.getMaxFrames())]
        pitchesArr = self.getStringFrets() if self.frameType == "fret" else self.getMidiPitches()

        for i, (pitch, time) in enumerate(zip(pitchesArr,
                                              [self.ETimeStamp, self.ATimeStamp, self.DTimeStamp,
                                               self.GTimeStamp, self.BTimeStamp, self.eTimeStamp])):
            for j in range(len(pitch)):
                startFrame = round(time[j][0] * self.frameRate)
                endFrame = round(time[j][1] * self.frameRate)
                for frame in range(startFrame, endFrame):
                    frames[frame][i] = pitch[j]

        if self.frameType == "fret":
            frames = [",".join([str(num) for num in frame]) for frame in frames]
            self.setFretFrames(frames)
        
        else:
            self.setMidiFrames(frames)

    def framesToNotesWithTime(self):
        """
        Convert the frames to video notes with time information.

        This method populates the `notesWithTimeFrames` attribute based on the `midiFrames` attribute.
        The video notes represent the notes being played along with their start and end times.
        """
        pitchesPlaying = {}
        output = []

        for i, frame in enumerate(self.midiFrames):

            for j, pitch in enumerate(frame):
                if pitch != 'x':
                    # Note being played
                    if (j, pitch) in pitchesPlaying:
                        # Note is already being played
                        # not should be string index and the note pitch
                        pitchesPlaying[(j, pitch)].setEndTime(pitchesPlaying[(j, pitch)].getEndTime() + self.getFramePeriod())
                    else:
                        # Note is starting to be played
                        pitchesPlaying[(j, pitch)] = VideoNote(pitch,i / self.frameRate,i / self.frameRate)

            # Loop through notes currently being played and check if it's in current frame, if not end time
            for (j, pitch) in list(pitchesPlaying):
                if (i == len(self.midiFrames)-1) or (pitch != self.midiFrames[i+1][j]):
                    output.append(pitchesPlaying[(j, pitch)])
                    del pitchesPlaying[(j, pitch)]
        
        self.setNotesWithTimeFrames(output)

    def framesToNotesWithTimeForTabsNonGuitarSet(self):
        output = []
        string_data = [
            (self.EMidiPitches, self.ETimeStamp),
            (self.AMidiPitches, self.ATimeStamp),
            (self.DMidiPitches, self.DTimeStamp),
            (self.GMidiPitches, self.GTimeStamp),
            (self.BMidiPitches, self.BTimeStamp),
            (self.eMidiPitches, self.eTimeStamp),
        ]

        for pitchs, timestamps in string_data:        
            for pitch, timestamp in zip(pitchs, timestamps):
                startTime, endTime = timestamp
                output.append(VideoNote(pitch, startTime, endTime))

        self.setNotesWithTimeFrames(output)


    def addTab(self, seconds, tab):
        """
        Add a tab to the tab sequence.

        Parameters:
            seconds (float): The duration of the tab in seconds.
            tab (str or list): The tab to add. If it's a string, it represents a single frame.
                               If it's a list, it represents multiple frames.
        """
        
        frames = seconds * self.frameRate
        for i in range(1, frames+1):
            self.addFretFrame(tab)
        
        tab = list(map(int, tab.split(',')))
        print(tab)

        timeStampes = [self.currentTime,self.currentTime+seconds]
         # Assign the lists to instance variables
        self.EStringFrets.append(tab[0])
        self.ETimeStamp.append(timeStampes)
        self.AStringFrets.append(tab[1])
        self.ATimeStamp.append(timeStampes)
        self.DStringFrets.append(tab[2])
        self.DTimeStamp.append(timeStampes)
        self.GStringFrets.append(tab[3])
        self.GTimeStamp.append(timeStampes)
        self.BStringFrets.append(tab[4])
        self.BTimeStamp.append(timeStampes)
        self.eStringFrets.append(tab[5])
        self.eTimeStamp.append(timeStampes)


        self.currentTime+=seconds
        print("HEREEE")
        print(self.EStringFrets, self.ETimeStamp)

        # Convert frets to MIDI pitches
        self.EMidiPitches = [Functions.fretToMidi(self.Elow, fret) for fret in self.EStringFrets]
        self.AMidiPitches = [Functions.fretToMidi(self.A, fret) for fret in self.AStringFrets]
        self.DMidiPitches = [Functions.fretToMidi(self.D, fret) for fret in self.DStringFrets]
        self.GMidiPitches = [Functions.fretToMidi(self.G, fret) for fret in self.GStringFrets]
        self.BMidiPitches = [Functions.fretToMidi(self.B, fret) for fret in self.BStringFrets]
        self.eMidiPitches = [Functions.fretToMidi(self.EHigh, fret) for fret in self.eStringFrets]

        self.maxEndTime = max(self.ETimeStamp[-1][-1], self.ATimeStamp[-1][-1],
                            self.DTimeStamp[-1][-1], self.GTimeStamp[-1][-1], self.BTimeStamp[-1][-1],
                            self.eTimeStamp[-1][-1])

    
    def getFretFrames(self):
        """
        Get the fret frames of the tab sequence.

        Returns:
            list: A list of strings representing the fret frames.
        """
        return self.fretFrames

    def getFramesAsString(self):
        """
        Get the fret frames of the tab sequence as strings.

        Returns:
            list: A list of strings representing the fret frames.
        """
        stringFrames = [",".join([str(num) for num in sublist]) for sublist in self.fretFrames]
        return stringFrames

    def addFretFrame(self, frame):
        """
        Add a fret frame to the tab sequence.

        Parameters:
            frame (str or list): The fret frame to add. If it's a string, it represents a single frame.
                                 If it's a list, it represents multiple frames.
        """
        self.fretFrames.append(frame)

    def setFretFrames(self, frames):
        """
        Set the fret frames of the tab sequence.

        Parameters:
            frames (list): A list of strings representing the fret frames.
        """
        self.fretFrames = frames

    def getFretFrames(self):
        """
        Get the fret frames of the tab sequence.

        Returns:
            list: A list of strings representing the fret frames.
        """
        return self.fretFrames

    def addMidiFrame(self, frame):
        """
        Add a MIDI frame to the tab sequence.

        Parameters:
            frame (str or list): The MIDI frame to add. If it's a string, it represents a single frame.
                                 If it's a list, it represents multiple frames.
        """
        self.midiFrames.append(frame)

    def setMidiFrames(self, frames):
        """
        Set the MIDI frames of the tab sequence.

        Parameters:
            frames (list): A list of strings representing the MIDI frames.
        """
        self.midiFrames = frames

    def getMidiFrames(self):
        """
        Get the MIDI frames of the tab sequence.

        Returns:
            list: A list of strings representing the MIDI frames.
        """
        return self.midiFrames

    def getNotesWithTimeFrames(self):
        """
        Get the video notes with time information of the tab sequence.

        Returns:
            list: A list of VideoNote objects representing the notes being played along with their start and end times.
        """
        return self.notesWithTimeFrames

    def setNotesWithTimeFrames(self, notes):
        """
        Set the video notes with time information of the tab sequence.

        Parameters:
            notes (list): A list of VideoNote objects representing the notes being played along with their start and end times.
        """
        self.notesWithTimeFrames = notes

    def getFrameType(self):
        """
        Get the frame type of the tab sequence.

        Returns:
            str: The frame type, either "fret" or "midi".
        """
        return self.frameType.lower()

    def setFrameType(self, frameType):
        """
        Set the frame type of the tab sequence.

        Parameters:
            frameType (str): The frame type to set, either "fret" or "midi".
        """
        self.frameType = frameType
    
    def resetTabAttributes(self):
        """Reset all tab attributes to empty or initial state."""
        # Set frets and timestamps to empty lists
        self.EStringFrets = []
        self.ETimeStamp = []
        self.AStringFrets = []
        self.ATimeStamp = []
        self.DStringFrets = []
        self.DTimeStamp = []
        self.GStringFrets = []
        self.GTimeStamp = []
        self.BStringFrets = []
        self.BTimeStamp = []
        self.eStringFrets = []
        self.eTimeStamp = []

        # Set MidiPitches to empty lists or initial state
        self.EMidiPitches = []
        self.AMidiPitches = []
        self.DMidiPitches = []
        self.GMidiPitches = []
        self.BMidiPitches = []
        self.eMidiPitches = []

        # Set maxEndTime to initial state or appropriate value
        self.maxEndTime = 0  # You can adjust this based on your needs
