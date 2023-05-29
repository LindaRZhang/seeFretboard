from pathlib import Path
import os 

#scale degree, later can add b or #
scaleDegrees = ["1", "b2", "2", "b3", "3", "4", "b5", "5", "b6", "6", "b7", "7","1"]

#notes
chromaticNotes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]

#chromatic notes with enharmonic    
chromaticWEnharmonicScale = ['C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb', 'G', 'G#', 'Ab', 'A', 'A#', 'Bb', 'B']
chromaticWEnharmonicScaleFindDistance = [['C'], ['C#', 'Db'], ['D'], ['D#', 'Eb'], ['E'], ['F'], ['F#', 'Gb'], ['G'], ['G#', 'Ab'], ['A'], ['A#', 'Bb'], ['B']]

#solfeges
chromaticSolfeges = ["do","di","re","ri","mi","fa","fi","sol","si","la","li","ti"]

#intervals
allInterval = ["P1", "m2", "M2", "m3", "M3", "P4", "#4", "P5", "m6", "M6", "m7", "M7", "P8", "m9", "M9", "m10", "M10", "P11", "#11", "P12", "m13", "M13", "m14", "M14", "m15", "M15", "P16"]

#common tunings in notes
STANDARD_TUNING = ['E', 'A', 'D', 'G', 'B', 'E']
DROP_D_TUNING = ['D', 'A', 'D', 'G', 'B', 'E']
OPEN_G_TUNING = ['D', 'G', 'D', 'G', 'B', 'D']
DADGAD_TUNING = ['D', 'A', 'D', 'G', 'A', 'D']
EBEEBE_TUNING = ['E', 'B', 'E', 'E', 'B', 'E']
OPEN_D_TUNING = ['D', 'A', 'D', 'F#', 'A', 'D']
OPEN_E_TUNING = ['E', 'B', 'E', 'G#', 'B', 'E']
OPEN_A_TUNING = ['E', 'A', 'E', 'A', 'C#', 'E']
OPEN_C_TUNING = ['C', 'G', 'C', 'G', 'C', 'E']
DROP_C_TUNING = ['C', 'G', 'C', 'F', 'A', 'D']
OPEN_B_TUNING = ['B', 'F#', 'B', 'F#', 'B', 'D#']
#in midi
STANDARD_TUNING_MIDI = [40, 45, 50, 55, 59, 64]
DROP_D_TUNING_MIDI = [38, 45, 50, 55, 59, 64]
OPEN_G_TUNING_MIDI = [38, 43, 47, 55, 59, 62]
DADGAD_TUNING_MIDI = [38, 45, 50, 55, 57, 62]
EBEEBE_TUNING_MIDI = [40, 47, 50, 50, 47, 50]
OPEN_D_TUNING_MIDI = [38, 45, 50, 54, 57, 62]
OPEN_E_TUNING_MIDI = [40, 47, 50, 56, 59, 64]
OPEN_A_TUNING_MIDI = [40, 45, 40, 45, 49, 52]
OPEN_C_TUNING_MIDI = [36, 43, 36, 43, 36, 40]
DROP_C_TUNING_MIDI = [36, 43, 36, 41, 45, 50]
OPEN_B_TUNING_MIDI = [35, 42, 35, 42, 35, 39]

#orientation
HORIZONTAL = ["horizontal", "h"]
VERTICAL = ["vertical", "v"]

BASE_PATH = Path(__file__).resolve().parent.parent

FRAMERATE = 30

#caged
#c shape

cShape = {
    "name": "C",
    "majNote": ["E", "C", "E", "G", "C", "E"],
    "majPosition": ["x", "3", "2", "0", "1", "0"],
    "majScaleDegree": ["", "1", "3", "5", "1", "3"],
    "maj7Note": ["E", "C", "E", "G", "B", "E"],
    "maj7Position": ["x", "3", "2", "0", "0", "0"],
    "maj7ScaleDegree": ["", "1", "3", "5", "7", "3"],
    "dom7Note": ["E", "C", "E", "Bb", "C", "E"],
    "dom7Position": ["x", "3", "2", "3", "1", "x"],
    "dom7ScaleDegree": ["", "1", "3", "b7", "1", "3"],

    "minNote": ["Eb", "C", "Eb", "G", "C", "Eb"],
    "minPosition": ["x", "3", "1", "0", "1", "x"],
    "minScaleDegree": ["", "1", "b3", "5", "1", ""],
    "min7Note": ["Eb", "C", "Eb", "Bb", "C", "G"],
    "min7Position": ["x", "3", "1", "3", "1", "3"],
    "min7ScaleDegree": ["", "1", "b3", "b7", "1", "5"],
    "min7b5Note": ["Eb", "C", "Eb", "Bb", "C", "Gb"],
    "min7b5Position": ["x", "3", "1", "3", "1", "2"],
    "min7b5ScaleDegree": ["", "1", "b3", "b7", "1", "b5"],

    "dimNote": ["Eb", "C", "Eb", "Gb", "C", "Eb"],
    "dimPosition": ["x", "3", "1", "-1", "x", "x"],
    "dimScaleDegree": ["", "1", "b3", "b5", "1", "b3"],
    "dim7Note": ["Eb", "C", "Eb", "A", "C", "Gb"],
    "dim7Position": ["x", "3", "1", "2", "1", "2"],
    "dim7ScaleDegree": ["", "1", "b3", "6", "1", "b3"],

    "augNote": ["E", "C", "E", "G#", "C", "E"],
    "augPosition": ["x", "3", "2", "1", "1", "x"],
    "augScaleDegree": ["", "1", "b3", "b7", "1", "b5"]
}

aShape = {
    "name": "A",
    "majNote": ["E", "A", "E", "A", "C#", "E"],
    "majPosition": ["0", "0", "2", "2", "2", "0"],
    "majScaleDegree": ["5", "1", "5", "1", "3", "5"],
    "maj7Note": ["E", "A", "E", "Ab", "C#", "E"],
    "maj7Position": ["0", "0", "2", "1", "2", "0"],
    "maj7ScaleDegree": ["5", "1", "5", "7", "3", "5"],
    "dom7Note": ["E", "A", "E", "G", "C#", "E"],
    "dom7Position": ["0", "0", "2", "0", "2", "0"],
    "dom7ScaleDegree": ["5", "1", "5", "b7", "3", "5"],

    "minNote": ["E", "A", "E", "A", "C", "E"],
    "minPosition": ["0", "0", "2", "2", "1", "0"],
    "minScaleDegree": ["5", "1", "5", "1", "b3", "5"],
    "min7Note": ["E", "A", "E", "G", "C", "E"],
    "min7Position": ["0", "0", "2", "0", "1", "0"],
    "min7ScaleDegree": ["5", "1", "5", "b7", "b3", "5"],
    "min7b5Note": ["E", "A", "Eb", "G", "C", "E"],
    "min7b5Position": ["x", "0", "1", "0", "1", "x"],
    "min7b5ScaleDegree": ["", "1", "b5", "b7", "b3", ""],

    "dimNote": ["Eb", "A", "Eb", "A", "C", "Eb"],
    "dimPosition": ["x", "0", "1", "2", "1", "x"],
    "dimScaleDegree": ["b5", "1", "b5", "1", "b3", "b5"],
    "dim7Note": ["E", "A", "Eb", "Gb", "C", "E"],
    "dim7Position": ["x", "0", "1", "-1", "1", "x"],
    "dim7ScaleDegree": ["", "1", "b5", "6", "b3", ""],

    "augNote": ["F", "A", "F", "A", "C#", "F"],
    "augPosition": ["1", "0", "3", "2", "2", "1"],
    "augScaleDegree": ["#5", "1", "#5", "1", "3", "#5"],
}

gShape = {
    "name": "G",
    "majNote": ["G", "B", "D", "G", "B", "G"],
    "majPosition": ["3", "2", "0", "0", "0", "3"],
    "majScaleDegree": ["1", "3", "5", "1", "3", "1"],

    "minNote": ["G", "Bb", "D", "G", "", ""],
    "minPosition": ["3", "1", "0", "0", "x", "x"],
    "minScaleDegree": ["1", "b3", "5", "1", "", ""],
    
    "dimNote": ["G", "Bb", "Db", "G", "Bb", "G"],
    "dimPosition": ["3", "1", "-1", "x", "x", "x"],
    "dimScaleDegree": ["1", "b3", "b5", "1", "b3", "1"],

    "augNote": ["G", "B", "D#", "G", "B", "G"],
    "augPosition": ["3", "2", "1", "0", "0", "x"],
    "augScaleDegree": ["1", "3", "#5", "1", "3", "1"],
}

eShape = {
    "name": "E",
    "majNote": ["E", "B", "E", "G#", "B", "E"],
    "majPosition": ["0", "2", "2", "1", "0", "0"],
    "majScaleDegree": ["1", "5", "1", "3", "5", "1"],
    "maj7Note": ["E", "B", "D#", "G#", "B", "E"],
    "maj7Position": ["0", "2", "1", "1", "0", "0"],
    "maj7ScaleDegree": ["1", "5", "7", "3", "5", "1"],
    "dom7Note": ["E", "B", "D", "G#", "B", "E"],
    "dom7Position": ["0", "2", "0", "1", "0", "0"],
    "dom7ScaleDegree": ["1", "5", "b7", "3", "5", "1"],

    "minNote": ["E", "B", "E", "G", "B", "E"],
    "minPosition": ["0", "2", "2", "1", "0", "0"],
    "minScaleDegree": ["1", "5", "1", "b3", "5", "1"],
    "min7Note": ["E", "B", "D", "G", "B", "E"],
    "min7Position": ["0", "2", "0", "0", "0", "0"],
    "min7ScaleDegree": ["1", "5", "b7", "b3", "5", "1"],
    "min7b5Note": ["E", "Bb", "D", "G", "Bb", "E"],
    "min7b5Position": ["0", "1", "0", "0", "0", "0"],
    "min7b5ScaleDegree": ["1", "b5", "b7", "b3", "b5", "1"],

    "dimNote": ["E", "Bb", "E", "G", "Bb", "E"],
    "dimPosition": ["0", "1", "2", "1", "x", "0"],
    "dimScaleDegree": ["1", "b5", "1", "b3", "b5", "1"],
    "dim7Note": ["E", "Bb", "C#", "G", "", ""],
    "dim7Position": ["0", "1", "-1", "0", "x", "x"],
    "dim7ScaleDegree": ["1", "b5", "6", "b3", "", ""],

    "augNote": ["E", "C", "E", "G#", "C", "E"],
    "augPosition": ["0", "3", "2", "1", "1", "0"],
    "augScaleDegree": ["1", "#5", "1", "3", "#5", "1"],
}

dShape = {
    "name": "D",
    "majNote": ["", "", "D", "A", "D", "F#"],
    "majPosition": ["x", "x", "0", "2", "3", "2"],
    "majScaleDegree": ["", "", "1", "5", "1", "3"],
    "maj7Note": ["", "", "D", "A", "C#", "F#"],
    "maj7Position": ["x", "x", "0", "2", "2", "2"],
    "maj7ScaleDegree": ["", "", "1", "5", "7", "3"],
    "dom7Note": ["", "", "D", "A", "C", "F#"],
    "dom7Position": ["x", "x", "0", "2", "1", "2"],
    "dom7ScaleDegree": ["", "", "1", "5", "b7", "3"],

    "minNote": ["", "", "D", "A", "D", "F"],
    "minPosition": ["x", "x", "0", "2", "3", "1"],
    "minScaleDegree": ["", "", "1", "5", "1", "b3"],
    "min7Note": ["", "", "D", "A", "C", "F"],
    "min7Position": ["x", "x", "0", "2", "1", "1"],
    "min7ScaleDegree": ["", "", "1", "5", "b7", "b3"],
    "min7b5Note": ["", "", "D", "Ab", "C", "F"],
    "min7b5Position": ["x", "x", "0", "1", "1", "1"],
    "min7b5ScaleDegree": ["", "", "1", "b5", "b7", "b3"],

    "dimNote": ["", "", "D", "Ab", "D", "F"],
    "dimPosition": ["x", "x", "0", "1", "3", "1"],
    "dimScaleDegree": ["", "", "1", "b5", "1", "b3"],
    "dim7Note": ["", "", "D", "Ab", "B", "F"],
    "dim7Position": ["x", "x", "0", "1", "0", "1"],
    "dim7ScaleDegree": ["", "", "1", "b5", "6", "b3"],

    "augNote": ["", "", "D", "A#", "D", "F#"],
    "augPosition": ["x", "x", "0", "3", "3", "2"],
    "augScaleDegree": ["", "", "1", "#5", "1", "3"],
}

cagedShapes = {
    "C": cShape,
    "A": aShape,
    "G": gShape,
    "E": eShape,
    "D": dShape,
}

DROP2 = {
    "DROP2String6" : {
        "maj7Note1": ["C","G","B","E","",""],
        "maj7Position1": ["8","10","9","9","x","x"],
        "maj7ScaleDegree1": ["1","5","7","3","",""],
        "maj7Note2": ["E","B","C","G","",""],
        "maj7Position2": ["0","2","-2","0","x","x"],
        "maj7ScaleDegree2": ["3","7","1","5","",""],
        "maj7Note3": ["G","C","E","B","",""],
        "maj7Position3": ["3","3","2","4","x","x"],
        "maj7ScaleDegree3": ["5","1","3","7","",""],
        "maj7Note4": ["B","E","G","C","",""],
        "maj7Position4": ["7","7","5","5","x","x"],
        "maj7ScaleDegree4": ["7","3","5","1","",""],

        "dom7Note1": ["C","G","Bb","E","",""],
        "dom7Position1": ["8","10","8","9","x","x"],
        "dom7ScaleDegree1": ["1","5","b7","3","",""],
        "dom7Note2": ["E","Bb","C","G","",""],
        "dom7Position2": ["0","1","-2","0","x","x"],
        "dom7ScaleDegree2": ["3","b7","1","5","",""],
        "dom7Note3": ["G","C","E","Bb","",""],
        "dom7Position3": ["3","3","2","3","x","x"],
        "dom7ScaleDegree3": ["5","1","3","b7","",""],
        "dom7Note4": ["Bb","E","G","C","",""],
        "dom7Position4": ["6","7","5","5","x","x"],
        "dom7ScaleDegree4": ["b7","3","5","1","",""],

        "min7Note1": ["C", "G", "Bb", "Eb", "", ""],
        "min7Position1": ["8", "10", "8", "8", "x", "x"],
        "min7ScaleDegree1": ["1", "5", "b7", "b3", "", ""],
        "min7Note2": ["Eb", "Bb", "C", "G", "", ""],
        "min7Position2": ["-1", "1", "-2", "0", "x", "x"],
        "min7ScaleDegree2": ["b3", "b7", "1", "5", "", ""],
        "min7Note3": ["G","C","Eb","Bb","",""],
        "min7Position3": ["3","3","1","3","x","x"],
        "min7ScaleDegree3": ["5","1","b3","b7","",""],
        "min7Note4": ["Bb","Eb","G","C","",""],
        "min7Position4": ["6","6","5","5","x","x"],
        "min7ScaleDegree4": ["b7","b3","5","1","",""],

        "min7b5Note1": ["C", "Gb", "Bb", "Eb", "", ""],
        "min7b5Position1": ["8", "9", "8", "8", "x", "x"],
        "min7b5ScaleDegree1": ["1", "b5", "b7", "b3", "", ""],
        "min7b5Note2": ["Eb", "Bb", "C", "Gb", "", ""],
        "min7b5Position2": ["-1", "1", "-2", "-1", "x", "x"],
        "min7b5ScaleDegree2": ["b3", "b7", "1", "b5", "", ""],
        "min7b5Note3": ["Gb","C","Eb","Bb","",""],
        "min7b5Position3": ["2","3","1","3","x","x"],
        "min7b5ScaleDegree3": ["b5","1","b3","b7","",""],
        "min7b5Note4": ["Bb","Eb","Gb","C","",""],
        "min7b5Position4": ["6","6","4","5","x","x"],
        "min7b5ScaleDegree4": ["b7","b3","b5","1","",""],

        "dim7Note1": ["C", "Gb", "A", "Eb", "", ""],
        "dim7Position1": ["8", "9", "7", "8", "x", "x"],
        "dim7ScaleDegree1": ["1", "b5", "6", "b3", "", ""],
        "dim7Note2": ["Eb", "A", "C", "Gb", "", ""],
        "dim7Position2": ["-1", "0", "-2", "-1", "x", "x"],
        "dim7ScaleDegree2": ["b3", "6", "1", "b5", "", ""],
        "dim7Note3": ["Gb", "C", "Eb", "A", "", ""],
        "dim7Position3": ["2", "3", "1", "2", "x", "x"],
        "dim7ScaleDegree3": ["b5", "1", "b3", "6", "", ""],
        "dim7Note4": ["A", "Eb", "Gb", "C", "", ""],
        "dim7Position4": ["5", "6", "4", "5", "x", "x"],
        "dim7ScaleDegree4": ["6", "b3", "b5", "1", "", ""]

    },

    "DROP2String5": {
        "maj7Note1": ["", "C", "G", "B", "E", ""],
        "maj7Position1": ["x", "3", "5", "4", "5", "x"],
        "maj7ScaleDegree1": ["", "1", "5", "7", "3", ""],
        "maj7Note2": ["", "E", "B", "C", "G", ""],
        "maj7Position2": ["x", "7", "9", "5", "8", "x"],
        "maj7ScaleDegree2": ["", "3", "7", "1", "5", ""],
        "maj7Note3": ["", "G", "C", "E", "B", ""],
        "maj7Position3": ["x", "10", "10", "9", "12", "x"],
        "maj7ScaleDegree3": ["", "5", "1", "3", "7", ""],
        "maj7Note4": ["", "B", "E", "G", "C", ""],
        "maj7Position4": ["x", "2", "2", "0", "1", "x"],
        "maj7ScaleDegree4": ["", "7", "3", "5", "1", ""],

        "dom7Note1": ["", "C", "G", "Bb", "E", ""],
        "dom7Position1": ["x", "3", "5", "3", "5", "x"],
        "dom7ScaleDegree1": ["", "1", "5", "b7", "3", ""],
        "dom7Note2": ["", "E", "Bb", "C", "G", ""],
        "dom7Position2": ["x", "7", "8", "5", "8", "x"],
        "dom7ScaleDegree2": ["", "3", "b7", "1", "5", ""],
        "dom7Note3": ["", "G", "C", "E", "Bb", ""],
        "dom7Position3": ["x", "10", "10", "9", "11", "x"],
        "dom7ScaleDegree3": ["", "5", "1", "3", "b7", ""],
        "dom7Note4": ["", "Bb", "E", "G", "C", ""],
        "dom7Position4": ["x", "1", "2", "0", "1", "x"],
        "dom7ScaleDegree4": ["", "b7", "3", "5", "1", ""],

        "min7Note1": ["", "C", "G", "Bb", "Eb", ""],
        "min7Position1": ["x", "3", "5", "3", "4", "x"],
        "min7ScaleDegree1": ["", "1", "5", "b7", "b3", ""],
        "min7Note2": ["", "Eb", "Bb", "C", "G", ""],
        "min7Position2": ["x", "6", "8", "5", "8", "x"],
        "min7ScaleDegree2": ["", "b3", "b7", "1", "5", ""],
        "min7Note3": ["", "G", "C", "Eb", "Bb", ""],
        "min7Position3": ["x", "10", "10", "7", "11", "x"],
        "min7ScaleDegree3": ["", "5", "1", "b3", "b7", ""],
        "min7Note4": ["", "Bb", "Eb", "G", "C", ""],
        "min7Position4": ["x", "1", "1", "0", "1", "x"],
        "min7ScaleDegree4": ["", "b7", "b3", "5", "1", ""],

        "min7b5Note1": ["", "C", "Gb", "Bb", "Eb", ""],
        "min7b5Position1": ["x", "3", "4", "3", "4", "x"],
        "min7b5ScaleDegree1": ["", "1", "b5", "b7", "b3", ""],
        "min7b5Note2": ["", "Eb", "Bb", "C", "Gb", ""],
        "min7b5Position2": ["x", "6", "8", "5", "7", "x"],
        "min7b5ScaleDegree2": ["", "b3", "b7", "1", "b5", ""],
        "min7b5Note3": ["", "Gb", "C", "Eb", "Bb", ""],
        "min7b5Position3": ["x", "9", "10", "8", "11", "x"],
        "min7b5ScaleDegree3": ["", "b5", "1", "b3", "b7", ""],
        "min7b5Note4": ["", "Bb", "Eb", "Gb", "C", ""],
        "min7b5Position4": ["x", "1", "1", "-1", "1", "x"],
        "min7b5ScaleDegree4": ["", "b7", "b3", "b5", "1", ""],

        "dim7Note1": ["", "C", "Gb", "A", "Eb", ""],
        "dim7Position1": ["x", "3", "4", "2", "4", "x"],
        "dim7ScaleDegree1": ["", "1", "b5", "6", "b3", ""],
        "dim7Note2": ["", "Eb", "A", "C", "Gb", ""],
        "dim7Position2": ["x", "6", "7", "5", "7", "x"],
        "dim7ScaleDegree2": ["", "b3", "6", "1", "b5", ""],
        "dim7Note3": ["", "Gb", "C", "Eb", "A", ""],
        "dim7Position3": ["x", "9", "10", "8", "10", "x"],
        "dim7ScaleDegree3": ["", "b5", "1", "b3", "6", ""],
        "dim7Note4": ["", "A", "Eb", "Gb", "C", ""],
        "dim7Position4": ["x", "0", "1", "-1", "1", "x"],
        "dim7ScaleDegree4": ["", "6", "b3", "b5", "1", ""]

    },

    "DROP2String4" : {
        "maj7Note1": ["", "", "C", "G", "B", "E"],
        "maj7Position1": ["x", "x", "10", "12", "12", "12"],
        "maj7ScaleDegree1": ["", "", "1", "5", "7", "3"],
        "maj7Note2": ["", "", "E", "B", "C", "G"],
        "maj7Position2": ["x", "x", "2", "4", "1", "3"],
        "maj7ScaleDegree2": ["", "", "3", "7", "1", "5"],
        "maj7Note3": ["", "", "G", "C", "E", "B"],
        "maj7Position3": ["x", "x", "5", "5", "5", "7"],
        "maj7ScaleDegree3": ["", "", "5", "1", "3", "7"],
        "maj7Note4": ["", "", "B", "E", "G", "C"],
        "maj7Position4": ["x", "x", "9", "9", "8", "8"],
        "maj7ScaleDegree4": ["", "", "7", "3", "5", "1"],


        "dom7Note1": ["", "", "C", "G", "Bb", "E"],
        "dom7Position1": ["x", "x", "10", "12", "11", "12"],
        "dom7ScaleDegree1": ["", "", "1", "5", "b7", "3"],
        "dom7Note2": ["", "", "E", "Bb", "C", "G"],
        "dom7Position2": ["x", "x", "2", "3", "1", "3"],
        "dom7ScaleDegree2": ["", "", "3", "b7", "1", "5"],
        "dom7Note3": ["", "", "G", "C", "E", "Bb"],
        "dom7Position3": ["x", "x", "5", "5", "5", "6"],
        "dom7ScaleDegree3": ["", "", "5", "1", "3", "b7"],
        "dom7Note4": ["", "", "Bb", "E", "G", "C"],
        "dom7Position4": ["x", "x", "8", "9", "8", "8"],
        "dom7ScaleDegree4": ["", "", "b7", "3", "5", "1"],

        "min7Note1": ["", "", "C", "G", "Bb", "Eb"],
        "min7Position1": ["x", "x", "10", "12", "11", "11"],
        "min7ScaleDegree1": ["", "", "1", "5", "b7", "b3"],
        "min7Note2": ["", "", "Eb", "Bb", "C", "G"],
        "min7Position2": ["x", "x", "1", "3", "1", "3"],
        "min7ScaleDegree2": ["", "", "b3", "b7", "1", "5"],
        "min7Note3": ["", "", "G", "C", "Eb", "Bb"],
        "min7Position3": ["x", "x", "5", "5", "4", "6"],
        "min7ScaleDegree3": ["", "", "5", "1", "b3", "b7"],
        "min7Note4": ["", "", "Bb", "Eb", "G", "C"],
        "min7Position4": ["x", "x", "8", "8", "8", "8"],
        "min7ScaleDegree4": ["", "", "b7", "b3", "5", "1"],

        "min7b5Note1": ["", "", "C", "Gb", "Bb", "Eb"],
        "min7b5Position1": ["x", "x", "10", "11", "11", "11"],
        "min7b5ScaleDegree1": ["", "", "1", "b5", "b7", "b3"],
        "min7b5Note2": ["", "", "Eb", "Bb", "C", "Gb"],
        "min7b5Position2": ["x", "x", "1", "3", "1", "2"],
        "min7b5ScaleDegree2": ["", "", "b3", "b7", "1", "b5"],
        "min7b5Note3": ["", "", "Gb", "C", "Eb", "Bb"],
        "min7b5Position3": ["x", "x", "4", "5", "4", "6"],
        "min7b5ScaleDegree3": ["", "", "b5", "1", "b3", "b7"],
        "min7b5Note4": ["", "", "Bb", "Eb", "Gb", "C"],
        "min7b5Position4": ["x", "x", "8", "8", "7", "8"],
        "min7b5ScaleDegree4": ["", "", "b7", "b3", "b5", "1"],

        "dim7Note1": ["", "", "C", "Gb", "A", "Eb"],
        "dim7Position1": ["x", "x", "10", "11", "10", "11"],
        "dim7ScaleDegree1": ["", "", "1", "b5", "6", "b3"],
        "dim7Note2": ["", "", "Eb", "A", "C", "Gb"],
        "dim7Position2": ["x", "x", "1", "2", "1", "2"],
        "dim7ScaleDegree2": ["", "", "b3", "6", "1", "b5"],
        "dim7Note3": ["", "", "Gb", "C", "Eb", "A"],
        "dim7Position3": ["x", "x", "4", "5", "4", "5"],
        "dim7ScaleDegree3": ["", "", "b5", "1", "b3", "6"],
        "dim7Note4": ["", "", "A", "Eb", "Gb", "C"],
        "dim7Position4": ["x", "x", "7", "8", "7", "8"],
        "dim7ScaleDegree4": ["", "", "6", "b3", "b5", "1"]

    }

}
    
DROP3 = {
    "DROP3String6" : {
        "maj7Note1": ["C","","B","E","G",""],
        "maj7Position1": ["8","x","9","9","8","x"],
        "maj7ScaleDegree1": ["1","","7","3","5",""],
        "maj7Note2": ["E","","C","G","B",""],
        "maj7Position2": ["0","x","-2","0","0","x"],
        "maj7ScaleDegree2": ["3","","1","5","7",""],
        "maj7Note3": ["G","","E","B","C",""],
        "maj7Position3": ["3","x","2","4","1","x"],
        "maj7ScaleDegree3": ["5","","3","7","1",""],
        "maj7Note4": ["B","","G","C","E",""],
        "maj7Position4": ["7","x","5","5","5","x"],
        "maj7ScaleDegree4": ["7","","5","1","3",""],

        "dom7Note1": ["C","","Bb","E","G",""],
        "dom7Position1": ["8","x","8","9","8","x"],
        "dom7ScaleDegree1": ["1","","b7","3","5",""],
        "dom7Note2": ["E","","C","G","Bb",""],
        "dom7Position2": ["0","x","-2","0","-1","x"],
        "dom7ScaleDegree2": ["3","","1","5","b7",""],
        "dom7Note3": ["G","","E","Bb","C",""],
        "dom7Position3": ["3","x","2","3","1","x"],
        "dom7ScaleDegree3": ["5","","3","b7","1",""],
        "dom7Note4": ["Bb","","G","C","E",""],
        "dom7Position4": ["6","x","5","5","5","x"],
        "dom7ScaleDegree4": ["b7","","5","1","3",""],

        "min7Note1": ["C","","Bb","Eb","G",""],
        "min7Position1": ["8","x","8","8","8","x"],
        "min7ScaleDegree1": ["1","","b7","b3","5",""],
        "min7Note2": ["Eb","","C","G","Bb",""],
        "min7Position2": ["-1","x","-2","0","-1","x"],
        "min7ScaleDegree2": ["b3","","1","5","b7",""],
        "min7Note3": ["G","","Eb","Bb","C",""],
        "min7Position3": ["3","x","1","3","1","x"],
        "min7ScaleDegree3": ["5","","b3","b7","1",""],
        "min7Note4": ["Bb","","G","C","Eb",""],
        "min7Position4": ["6","x","5","5","4","x"],
        "min7ScaleDegree4": ["b7","","5","0","b3",""],

        "min7b5Note1": ["C","","Bb","Eb","Gb",""],
        "min7b5Position1": ["8","x","8","8","7","x"],
        "min7b5ScaleDegree1": ["1","","b7","b3","b5",""],
        "min7b5Note2": ["Eb","","C","Gb","Bb",""],
        "min7b5Position2": ["11","x","10","11","11","x"],
        "min7b5ScaleDegree2": ["b3","","1","b5","b7",""],
        "min7b5Note3": ["Gb","","Eb","Bb","C",""],
        "min7b5Position3": ["2","x","1","3","1","x"],
        "min7b5ScaleDegree3": ["b5","","b3","b7","1",""],
        "min7b5Note4": ["Bb","","Gb","C","Eb",""],
        "min7b5Position4": ["6","x","4","5","4","x"],
        "min7b5ScaleDegree4": ["b7","","b5","0","b3",""],

        "dim7Note1": ["C","","A","Eb","Gb",""],
        "dim7Position1": ["8","x","7","8","7","x"],
        "dim7ScaleDegree1": ["1","","6","b3","b5",""],
        "dim7Note2": ["Eb","","C","Gb","A",""],
        "dim7Position2": ["11","x","10","11","10","x"],
        "dim7ScaleDegree2": ["b3","","1","b5","6",""],
        "dim7Note3": ["Gb","","Eb","A","C",""],
        "dim7Position3": ["2","x","1","2","1","x"],
        "dim7ScaleDegree3": ["b5","","b3","6","1",""],
        "dim7Note4": ["A","","Gb","C","Eb",""],
        "dim7Position4": ["5","x","4","5","4","x"],
        "dim7ScaleDegree4": ["6","","b5","0","b3",""],
    },

    "DROP3String5": {
        "maj7Note1": ["", "C", "", "B", "E", "G"],
        "maj7Position1": ["x", "3", "x", "4", "5", "3"],
        "maj7ScaleDegree1": ["", "1", "", "7", "3", "5"],
        "maj7Note2": ["", "E", "", "C", "G", "B"],
        "maj7Position2": ["x", "7", "x", "5", "8", "7"],
        "maj7ScaleDegree2": ["", "3", "x", "1", "5", "7"],
        "maj7Note3": ["", "G", "", "E", "B", "C"],
        "maj7Position3": ["x", "10", "x", "9", "12", "8"],
        "maj7ScaleDegree3": ["", "5", "", "3", "7", "1"],
        "maj7Note4": ["", "B", "", "G", "C", "E"],
        "maj7Position4": ["x", "2", "x", "0", "1", "0"],
        "maj7ScaleDegree4": ["", "7", "", "5", "1", "3"],

        "dom7Note1": ["", "C", "", "Bb", "E", "G"],
        "dom7Position1": ["x", "3", "x", "3", "5", "3"],
        "dom7ScaleDegree1": ["", "1", "", "b7", "3", "5"],
        "dom7Note2": ["", "E", "", "C", "G", "Bb"],
        "dom7Position2": ["x", "7", "x", "5", "8", "6"],
        "dom7ScaleDegree2": ["", "3", "", "1", "5", "6"],
        "dom7Note3": ["", "G", "", "E", "Bb", "C"],
        "dom7Position3": ["x", "10", "x", "9", "11", "8"],
        "dom7ScaleDegree3": ["", "5", "", "3", "b7", "1"],
        "dom7Note4": ["", "Bb", "", "G", "C", "E"],
        "dom7Position4": ["x", "1", "x", "0", "1", "0"],
        "dom7ScaleDegree4": ["", "b7", "", "5", "1", "3"],

        "min7Note1": ["", "C", "", "Bb", "Eb", "G"],
        "min7Position1": ["x", "3", "x", "3", "4", "3"],
        "min7ScaleDegree1": ["", "1", "", "b7", "b3", "5"],
        "min7Note2": ["", "Eb", "", "C", "G", "Bb"],
        "min7Position2": ["x", "6", "x", "5", "8", "6"],
        "min7ScaleDegree2": ["", "b3", "", "1", "5", "b7"],
        "min7Note3": ["", "G", "", "Eb", "Bb", "C"],
        "min7Position3": ["x", "10", "x", "8", "11", "8"],
        "min7ScaleDegree3": ["", "5", "", "b3", "b7", "1"],
        "min7Note4": ["", "Bb", "", "G", "C", "Eb"],
        "min7Position4": ["x", "1", "x", "0", "1", "-1"],
        "min7ScaleDegree4": ["", "b7", "", "5", "0", "b3"],

        "min7b5Note1": ["", "C", "", "Bb", "Eb", "Gb"],
        "min7b5Position1": ["x", "3", "x", "3", "4", "2"],
        "min7b5ScaleDegree1": ["", "1", "", "b7", "b3", "b5"],
        "min7b5Note2": ["", "Eb", "", "C", "Gb", "Bb"],
        "min7b5Position2": ["x", "6", "x", "5", "-1", "6"],
        "min7b5ScaleDegree2": ["", "b3", "", "1", "b5", "b7"],
        "min7b5Note3": ["", "Gb", "", "Eb", "Bb", "C"],
        "min7b5Position3": ["x", "9", "x", "8", "11", "8"],
        "min7b5ScaleDegree3": ["", "b5", "", "b3", "b7", "1"],
        "min7b5Note4": ["", "Bb", "", "Gb", "C", "Eb"],
        "min7b5Position4": ["x", "1", "x", "-1", "1", "-1"],
        "min7b5ScaleDegree4": ["", "b7", "", "b5", "0", "b3"],

        "dim7Note1": ["", "C", "", "A", "Eb", "Gb"],
        "dim7Position1": ["x", "3", "x", "2", "4", "2"],
        "dim7ScaleDegree1": ["", "1", "", "6", "b3", "b5"],
        "dim7Note2": ["", "Eb", "", "C", "Gb", "A"],
        "dim7Position2": ["x", "6", "x", "5", "7", "5"],
        "dim7ScaleDegree2": ["", "b3", "", "1", "b5", "6"],
        "dim7Note3": ["", "Gb", "", "Eb", "A", "C"],
        "dim7Position3": ["x", "9", "x", "8", "10", "8"],
        "dim7ScaleDegree3": ["", "b5", "", "b3", "6", "1"],
        "dim7Note4": ["", "A", "", "Gb", "C", "Eb"],
        "dim7Position4": ["x", "0", "x", "-1", "1", "-1"],
        "dim7ScaleDegree4": ["", "6", "", "b5", "1", "b3"],
    },
}

DROPShapes = {
    "DROP2": DROP2,
    "DROP3": DROP3,
}

class customShapes():
    """
    A class representing a collection of custom shapes.

    Custom shapes can be added to the collection and retrieved based on their shape name.

    Attributes:
        customShapes (dict): A dictionary containing custom guitar shapes.
            The dictionary structure should be as follows:
            {
                shapeName1: {
                    note: [list of notes],
                    position: [list of positions],
                    scaleDegree: [list of scale degrees]
                },
                shapeName2: {
                    note: [list of notes],
                    position: [list of positions],
                    scaleDegree: [list of scale degrees]
                },
                ...
            }
    """
    def __init__(self):
        """
        Initializes a new instance of the CustomShape class.
        """
        self.customShapes = {

        }
        
    def addShape(self, shapeName, notes, positions, scaleDegrees):
        """Add a custom guitar shape to the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.
            notes (list): A list of notes for the custom shape.
            positions (list): A list of positions for the custom shape.
            scale_degrees (list): A list of scale degrees for the custom shape.

        Returns:
            None
        """
        self.customShapes[shapeName] = {
            'note': notes,
            'position': positions,
            'scaleDegree': scaleDegrees
        }

    def getShape(self, shapeName):
        """Retrieve a custom guitar shape from the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.

        Returns:
            dict: A dictionary representing the custom shape, containing the following keys:
                - 'note': List of notes
                - 'position': List of positions
                - 'scaleDegree': List of scale degrees
        """
        return self.customShapes.get(shapeName, None)

    def removeShape(self, shapeName):
        """Remove a custom guitar shape from the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.

        Returns:
            bool: True if the shape was successfully removed, False otherwise.
        """
        if shapeName in self.customShapes:
            del self.customShapes[shapeName]
            return True
        else:
            return False