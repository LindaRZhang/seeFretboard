#chromatic first and later can get conversions

#scale degree, later can add b or #
scaleDegrees = ["1", "b2", "2", "b3", "3", "4", "#4/b5", "5", "b6", "6", "b7", "7","1"]

#notes
chromaticNotes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]

#solfeges
chromaticSolfeges = ["do","di","re","ri","mi","fa","fi","sol","si","la","li","ti"]

#intervals
allInterval = ["P1","m2","M2","m3","M3","P4","D5","P5","m6","M6","m7","M7","P8"]

def intervalsToScaleDegrees(intervals):
    scaleDegrees = []
    for i in intervals:
        scaleDegrees.append(intervalToScaleDegree(i))
    return scaleDegrees

def scaleDegreesToIntervals(degrees):
    intervals = []
    for i in degrees:
        intervals.append(scaleDegreeToInterval(i))
    return intervals

def intervalToScaleDegree(interval):
    return scaleDegrees[allInterval.index(interval)]

def scaleDegreeToInterval(degree):
    return allInterval[scaleDegrees.index(degree)]