import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 1, 12)
fretboard.drawVerticalFretboard()

fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

fretboard.addOctave("c")

fretboard.showFretboard()
