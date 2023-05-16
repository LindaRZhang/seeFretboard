import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

#veritcal fretboard option
fretboard = SeeFretboard("v", 3, 12)
fretboard.drawVerticalFretboard()

#horizontal option
# fretboard = SeeFretboard("h", 1, 12)
# fretboard.drawHorizontalFretboard()

fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

fretboard.addScale("c","major")
#fretboard.addScale("c#","major")
#fretboard.addScale("bb","major")
#fretboard.addScale("c","chromatic")
#fretboard.addScale("a","minorpentatonic")
#fretboard.addScale("c","majorpentatonic")
#fretboard.addScale("c","random", 'P1 m2 M2 M3 P5 M6 M7')
#fretboard.addScale("c","harmonic minor")

fretboard.showFretboard()
