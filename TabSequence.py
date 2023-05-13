
# in colab right will update later
import mirdata
import math
import os
from Frame import Frame
from Note import Note
import Util

# set for 6 string in standard tuning for now

# tab consist of many frames or the frames in certain period


class TabSequence(Frame):
    def __init__(self, trackNum, frameRate=30, filePath=os.path.join(os.getcwd(), 'GuitarSet')):
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

        self.EStringFrets = Util.midiToFret(
            self.Elow, self.track.notes["E"].pitches)
        self.ETimeStamp = self.track.notes['E'].intervals
        self.AStringFrets = Util.midiToFret(
            self.A, self.track.notes["A"].pitches)
        self.ATimeStamp = self.track.notes['A'].intervals
        self.DStringFrets = Util.midiToFret(
            self.D, self.track.notes["D"].pitches)
        self.DTimeStamp = self.track.notes['D'].intervals
        self.GStringFrets = Util.midiToFret(
            self.G, self.track.notes["G"].pitches)
        self.GTimeStamp = self.track.notes['G'].intervals
        self.BStringFrets = Util.midiToFret(
            self.B, self.track.notes["B"].pitches)
        self.BTimeStamp = self.track.notes['B'].intervals
        self.eStringFrets = Util.midiToFret(
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

    def getNumOfStrings(self):
        return self.numOfStrings

    def setNumOfStrings(self, strings):
        self.numOfStrings = strings
    
    def getMaxFrames(self):
        return math.ceil(self.getMaxEndTime()) * self.getFrameRate()

    def setMaxFrames(self, maxFrames):
        self.maxFrames = maxFrames
    
    def getMaxEndTime(self):
        return self.maxEndTime

    def setMaxEndTime(self, maxEndTime):
        self.maxEndTime = maxEndTime

    def getStringFrets(self):
        return [self.EStringFrets, self.AStringFrets, self.DStringFrets, self.GStringFrets, self.BStringFrets, self.eStringFrets]

    def getStringMidi(self):
        return [self.Elow,self.A,self.D,self.G,self.B,self.EHigh]
    
    def getMidiPitches(self):
        arr = [self.EMidiPitches, self.AMidiPitches, self.DMidiPitches,
               self.GMidiPitches, self.BMidiPitches, self.eMidiPitches]
        roundedArray = [[round(num) for num in innerArr] for innerArr in arr]

        return roundedArray

    def makingFrames(self):
        frames = [[-1] * self.numOfStrings for _ in range(self.getMaxFrames())]
        pitchesArr = self.getStringFrets() if self.frameType == "fret" else self.getMidiPitches()

        for i, (pitch, time) in enumerate(zip(pitchesArr,
                                             [self.ETimeStamp, self.ATimeStamp, self.DTimeStamp, self.GTimeStamp, self.BTimeStamp, self.eTimeStamp])):
            for j in range(len(pitch)):
                startFrame = round(time[j][0] * self.frameRate)
                endFrame = round(time[j][1] * self.frameRate)
                for frame in range(startFrame, endFrame):
                    frames[frame][i] = pitch[j]

        if (self.frameType == "fret"):
            frames = [",".join([str(num) for num in frame])
                      for frame in frames]
            self.setFretFrames(frames)
        
        else:
            self.setMidiFrames(frames)

    def framesToNotesWithTime(self):
        pitchesPlaying = {}
        output = []

        for i, frame in enumerate(self.midiFrames):

            for j, pitch in enumerate(frame):
                if pitch != -1:
                    # Note being played
                    if (j, pitch) in pitchesPlaying:
                        # Note is already being played
                        # not should be string index and the note pitch
                        pitchesPlaying[(j, pitch)].setEndTime(pitchesPlaying[(j, pitch)].getEndTime() + self.getFramePeriod())
                    else:
                        # Note is starting to be played
                        pitchesPlaying[(j, pitch)] = Note(pitch,i / self.frameRate,i / self.frameRate)

            # Loop through notes currently being played n c if it's in current frame, if not end time
            for (j, pitch) in list(pitchesPlaying):
                if (i == len(self.midiFrames)-1) or (pitch != self.midiFrames[i+1][j]):
                    output.append(pitchesPlaying[(j, pitch)])
                    del pitchesPlaying[(j, pitch)]

        self.setNotesWithTimeFrames(output)

    def addTab(self, seconds, tab):
        frames = seconds * self.frameRate
        for i in range(1, frames+1):
            self.addFretFrame(tab)

    def getFretFrames(self):
        return self.fretFrames

    def getFramesAsString(self):#edit later
        stringFrames = [",".join([str(num) for num in sublist])
                        for sublist in self.fretFrames]
        return stringFrames

    def addFretFrame(self, frame):
        self.fretFrames.append(frame)

    def setFretFrames(self, frames):
        self.fretFrames = frames

    def getFretFrames(self):
        return self.fretFrames

    def addMidiFramesFrame(self, frame):
        self.midiFrames.append(frame)

    def setMidiFrames(self, frames):
        self.midiFrames = frames
    
    def getMidiFrames(self):
        return self.midiFrames

    def getFrameType(self):
        return self.frameType

    def setFrameType(self, type):
        self.frameType = type

    def getNotesWithTimeFrames(self):
        return self.notesWithTimeFrames

    def setNotesWithTimeFrames(self, arr):
        self.notesWithTimeFrames = arr
