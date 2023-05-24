from pathlib import Path
import os 

#scale degree, later can add b or #
scaleDegrees = ["1", "b2", "2", "b3", "3", "4", "b5", "5", "b6", "6", "b7", "7","1"]

#notes
chromaticNotes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]

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

