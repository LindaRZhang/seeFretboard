import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from TabSequence import TabSequence
from Video import Video
from SeeFretboard import SeeFretboard

f = SeeFretboard("v", 6, 1, 12)
f.addNotesAllString("-1,0,5,5,0,0")
f.drawVerticalFretboard()

tabS = TabSequence(0)
tabS.setFrameType("midi")
tabS.setFrames([])
tabS.addTab(1, [50, 51, 51, 50, 51, 51])
tabS.addTab(1, [55, 55, 55, 55, 55, 55])

frame = tabS.getFrames()
f.sonifyJams(frame)

print("CREATED AND SAVE MIDI")
