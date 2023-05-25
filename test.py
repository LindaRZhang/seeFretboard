import os
import sys
from bokeh.plotting import show
from seeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 1, 12)
fretboard.drawVerticalFretboard()
fretboard.addNotesAllString("0,0,2,2,0,0")
fretboard.showFretboard()#in your local repo, just need this
