import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

#veritcal fretboard option
# fretboard = SeeFretboard("v", 6, 1, 12)
# fretboard.drawVerticalFretboard()

#horizontal option
fretboard = SeeFretboard("h", 6, 1, 12)
fretboard.drawHorizontalFretboard()

#fretboard.setPitchesType("pitchesWithOctave")
#fretboard.setPitchesType("pitchesScaleDegrees")

fretboard.addScale("c","major")
#fretboard.addScale("c","major pentatonic", [1,2,3,5,6])
#fretboard.addScale("c","harmonic minor")

fretboard.showFretboard()
