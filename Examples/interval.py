import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 6, 1, 12)
fretboard.drawVerticalFretboard()

fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

fretboard.addInterval("c","P8")#gota put words for interval
#if p11 nd stuff should just show that instead of all

fretboard.showFretboard()
