
#in colab right will update later
import mirdata
import math

class TabSequence():
    def __init__(self, filePath, trackNum):
        self.filePath = filePath
        self.guitarset = mirdata.initialize('guitarset', data_home=self.filePath)

        self.guitarsetIds = self.guitarset.track_ids  # the list of guitar's track ids
        self.guitarsetData = self.guitarset.load_tracks()  # Load all tracks in the dataset
        self.exampleTrack = self.guitarsetData[self.guitarsetIds[trackNum]]  # Get the first track
        #trackNum starts at 0

        #strings and their Midi
        self.Elow = 40
        self.A = 45
        self.D = 50
        self.G = 55
        self.B = 59
        self.EHigh = 64

        self.ENotes = self.midiToFret(self.Elow, self.exampleTrack.notes["E"].pitches)
        self.ETimeStamp = self.exampleTrack.notes['E'].intervals
        self.ANotes = self.midiToFret(self.A,self.exampleTrack.notes["A"].pitches)
        self.ATimeStamp = self.example_track.notes['A'].intervals
        self.DNotes = self.midiToFret(self.D,self.exampleTrack.notes["D"].pitches)
        self.DTimeStamp = self.exampleTrack.notes['D'].intervals
        self.GNotes = self.midiToFret(self.G,self.exampleTrack.notes["G"].pitches)
        self.GTimeStamp = self.exampleTrack.notes['G'].intervals
        self.BNotes = self.midiToFret(self.B,self.exampleTrack.notes["B"].pitches)
        self.BTimeStamp = self.exampleTrack.notes['B'].intervals
        self.eNotes = self.midiToFret(self.EHigh,self.exampleTrack.notes["e"].pitches)
        self.eTimeStamp = self.exampleTrack.notes['e'].intervals
        
        self.maxEndTime = max(self.ETimeStamp[-1][-1],self.ATimeStamp[-1][-1], 
                 self.DTimeStamp[-1][-1], self.GTimeStamp[-1][-1], self.BTimeStamp[-1][-1], self.eTimeStamp[-1][-1])
        self.framesPerSeconds = 70
        self.numOfStrings = 6
        self.maxFrames = math.ceil(self.maxEndTime) * self.framesPerSeconds

    def midiToFret(string, midiNotes):
        notes = []
        for m in midiNotes:
            fret = round(abs(string - m))
            notes.append(fret)
        
        return notes
    
    def makingFrames(self):
        frames = [[-1] * self.numOfStrings for _ in range(self.maxFrames)]

        for i, (note, time) in enumerate(zip([self.ENotes, self.ANotes, self.DNotes, self.GNotes, self.BNotes, self.eNotes],
                                             self.ETimeStamp, self.ATimeStamp, self.DTimeStamp, self.GTimeStamp, self.BTimeStamp, self.eTimeStamp])):
            for j in range(len(note)):
                startFrame = round(time[j][0] * self.framesPerSeconds)
                endFrame = round(time[j][1] * self.framesPerSeconds)
                for frame in range(startFrame, endFrame):
                    frames[frame][i] = note[j]