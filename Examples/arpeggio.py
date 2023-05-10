import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 6, 1, 12)
fretboard.drawVerticalFretboard()

#fretboard.setPitchesType("pitchesWithOctave")
#fretboard.setPitchesType("pitchesScaleDegrees")

#fretboard.addArpeggio("c","minor")
#fretboard.addArpeggio("c") #just show 1 note or octaves
fretboard.addArpeggio("c","","P1 M3 P5 M7")

fretboard.showFretboard()
