
# in colab right will update later
import mirdata
import math
import os
from Frame import Frame

# set for 6 string in standard tuning for now

# tab consist of many frames or the frames in certain period


class TabSequence(Frame):
    def __init__(self, trackNum, frameRate=10, filePath=os.path.join(os.getcwd(), 'GuitarSet')):
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

        self.EStringFrets = self.midiToFret(
            self.Elow, self.track.notes["E"].pitches)
        self.ETimeStamp = self.track.notes['E'].intervals
        self.AStringFrets = self.midiToFret(
            self.A, self.track.notes["A"].pitches)
        self.ATimeStamp = self.track.notes['A'].intervals
        self.DStringFrets = self.midiToFret(
            self.D, self.track.notes["D"].pitches)
        self.DTimeStamp = self.track.notes['D'].intervals
        self.GStringFrets = self.midiToFret(
            self.G, self.track.notes["G"].pitches)
        self.GTimeStamp = self.track.notes['G'].intervals
        self.BStringFrets = self.midiToFret(
            self.B, self.track.notes["B"].pitches)
        self.BTimeStamp = self.track.notes['B'].intervals
        self.eStringFrets = self.midiToFret(
            self.EHigh, self.track.notes["e"].pitches)
        self.eTimeStamp = self.track.notes['e'].intervals

        # guitarSet is automatically in midi notes
        self.EMidiNotes = self.track.notes["E"].pitches
        self.AMidiNotes = self.track.notes["A"].pitches
        self.DMidiNotes = self.track.notes["D"].pitches
        self.GMidiNotes = self.track.notes["G"].pitches
        self.BMidiNotes = self.track.notes["B"].pitches
        self.eMidiNotes = self.track.notes["e"].pitches

        self.maxEndTime = max(self.ETimeStamp[-1][-1], self.ATimeStamp[-1][-1],
                              self.DTimeStamp[-1][-1], self.GTimeStamp[-1][-1], self.BTimeStamp[-1][-1], self.eTimeStamp[-1][-1])

        self.frameRate = 70
        self.numOfStrings = 6
        self.maxFrames = math.ceil(self.maxEndTime) * self.frameRate

        self.frames = []
        self.frameType = "fret"

    def getNumOfStrings(self):
        return self.numOfStrings

    def setNumOfStrings(self, strings):
        self.numOfStrings = strings

    def midiToFret(self, string, midiNotes):
        notes = []
        for m in midiNotes:
            fret = round(abs(string - m))
            notes.append(fret)

        return notes

    def fretToMidi(self, string, frets):
        midiNotes = []
        for fret in frets:
            midi = round(abs(string - fret))
            midiNotes.append(midi)

        return midiNotes

    def getStringFrets(self):
        return [self.EStringFrets, self.AStringFrets, self.DStringFrets, self.GStringFrets, self.BStringFrets, self.eStringFrets]

    def getMidiNotes(self):
        arr = [self.EMidiNotes, self.AMidiNotes, self.DMidiNotes,
               self.GMidiNotes, self.BMidiNotes, self.eMidiNotes]
        roundedArray = [[round(num) for num in innerArr] for innerArr in arr]

        return roundedArray

    def makingFrames(self):
        frames = [[-1] * self.numOfStrings for _ in range(self.maxFrames)]

        notesArr = self.getStringFrets() if self.frameType == "fret" else self.getMidiNotes()

        for i, (note, time) in enumerate(zip(notesArr,
                                             [self.ETimeStamp, self.ATimeStamp, self.DTimeStamp, self.GTimeStamp, self.BTimeStamp, self.eTimeStamp])):
            for j in range(len(note)):
                startFrame = round(time[j][0] * self.frameRate)
                endFrame = round(time[j][1] * self.frameRate)
                for frame in range(startFrame, endFrame):
                    frames[frame][i] = note[j]

        if (self.frameType == "fret"):
            frames = [",".join([str(num) for num in frame])
                      for frame in frames]
        self.setFrames(frames)

    def addTab(self, seconds, tab):
        frames = seconds * self.frameRate
        for i in range(1, frames+1):
            self.addFrame(tab)

    def getFrames(self):
        return self.frames

    def getFramesAsString(self):
        stringFrames = [",".join([str(num) for num in sublist])
                        for sublist in self.frames]
        return stringFrames

    def addFrame(self, frame):
        self.frames.append(frame)

    def setFrames(self, frames):
        self.frames = frames

    def getFrameType(self):
        return self.frameType

    def setFrameType(self, type):
        self.frameType = type
