import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 1, 12)
fretboard.drawVerticalFretboard()

fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

fretboard.addArpeggio("c","suspended-second")#gota put words for arpeggio kinds
#fretboard.addArpeggio("c") #just show 1 note or octaves
#fretboard.addArpeggio("c","","P1 M3 P5 M7")

fretboard.showFretboard()
