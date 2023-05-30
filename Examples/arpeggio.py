import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12)
fretboard.drawHorizontalFretboard()

fretboard.getPitchCollection().setPitchesType("pitchesWithOctave")
#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

#fretboard.addArpeggio("f","major-13th")
fretboard.addArpeggio("f","major")
# fretboard.addArpeggio("c","suspended-second")#gota put words for arpeggio kinds
#fretboard.addArpeggio("c","","P1 M3 P5 M7")

fretboard.showFretboard()
