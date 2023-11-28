import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seeFretboard import Utilities

from seeFretboard import SeeFretboard, Constants, Functions

#veritcal fretboard option
fretboard = SeeFretboard("h", 1, 12,theme="green")
fretboard.getTheme().tuning.letterTuning = ["C", "G", "D", "G", "A", "D"]
fretboard.getTheme().tuning.midiTuning = Functions.noteNamesToMidis(["C", "G", "D", "G", "A", "D"])
# fretboard.getTheme().tuning.midiTuning = Functions.noteNamesToMidis(["D", "A", "D", "G", "A", "D"])

fretboard.drawHorizontalFretboard()

#fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
# fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")
fretboard.getPitchCollection().setPitchesType("pitchesNames")

saveImageAt="/Users/lindazhang/Downloads/"

# fretboard.addScale("G","chromatic")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"GChromatic.png", "png")
# fretboard.clearFretboard()


#ADD ALL KEYS
#keys = Utilities.allKeys#
# for key in keys:
#     fretboard.addScale(key,"major")
#     Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+key+"MajorScale.png", "png")
#     fretboard.clearFretboard()

#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

key="G"
fretboard.addScale(key,"majorpentatonic")
Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+key+"p.png", "png")
fretboard.clearFretboard()

# fretboard.addOctave("D")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"DOct.png", "png")
# fretboard.clearFretboard()

# fretboard.addOctave("G")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"GOct.png", "png")
# fretboard.clearFretboard()

# fretboard.addOctave("D")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"DOct.png", "png")
# fretboard.clearFretboard()


# fretboard.addOctave("A")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"AOct.png", "png")
# fretboard.clearFretboard()


# fretboard.addOctave("E")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"EOct.png", "png")
# fretboard.clearFretboard()


fretboard.addArpeggio(key,"major")
Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+key+"MajArpeggio.png", "png")

fretboard.showFretboard()
