import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 6, 1, 12)
fretboard.drawVerticalFretboard()

fretboard.addScale("c","major")
#fretboard.addScale("c","harmonic minor")

fretboard.showFretboard()
