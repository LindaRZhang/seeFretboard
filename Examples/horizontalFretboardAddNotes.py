import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 3, 6)
fretboard.drawHorizontalFretboard()
fretboard.addNotesAllString("0,0,2,2,0,0")
fretboard.showFretboard()