
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12, theme="green")
fretboard.drawHorizontalFretboard()
fretboard.showFretboard()