import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12)
fretboard.drawFretboard("v")#this function can change from h to v

#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

fretboard.addCagedPosChord("c","min", "c")
# fretboard.addCagedPosChord("bb", "maj", "a")
# fretboard.addCagedPosChord("bb", "maj", "g")
# fretboard.addCagedPosChord("bb", "maj", "e")
# fretboard.addCagedPosChord("bb", "maj", "d")


fretboard.showFretboard()