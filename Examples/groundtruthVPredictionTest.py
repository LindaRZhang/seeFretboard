import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 6, 1, 12)
fretboard.drawHorizontalFretboard()


fretboard.addNotesAllString("-1,0,2,2,0,0")
fretboard.setNoteType("groundTruth")
fretboard.addNotesAllString("-1,-1,5,2,0,0")
fretboard.showFretboard()
