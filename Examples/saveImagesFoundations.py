import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seeFretboard import Utilities

from seeFretboard import SeeFretboard, Constants, Functions

#veritcal fretboard option
fretboard = SeeFretboard("h", 1, 12,theme="blue")
fretboard.getTheme().tuning.letterTuning = ["C", "F", "D", "F", "A", "C"]
# fretboard.getTheme().tuning.midiTuning = Functions.noteNamesToMidis(["E", "G", "E", "G", "A", "D"])
fretboard.getTheme().tuning.midiTuning = Functions.noteNamesToMidis(["C", "F", "D", "F", "A", "C"])

fretboard.drawHorizontalFretboard()

#fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
# fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")
fretboard.getPitchCollection().setPitchesType("pitchesNames")

saveImageAt="/Users/lindazhang/Downloads/"

# fretboard.addScale("G","chromatic")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"GChromatic.png", "png")
# fretboard.clearFretboard()

# fretboard.addScale("C","major")
# Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"CMajorScale.png", "png")
# fretboard.clearFretboard()

fretboard.addOctave("C")
Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"COct.png", "png")
fretboard.clearFretboard()

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


fretboard.addArpeggio("C","major")
Functions.saveImage(fretboard.getFretboardFig().fig, saveImageAt+"CMajArpeggio.png", "png")

fretboard.showFretboard()
