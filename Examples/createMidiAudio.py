from TabSequence import TabSequence
from Video import Video
from SeeFretboard import SeeFretboard
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


f = SeeFretboard("v", 6, 1, 12)
f.addNotesAllString("-1,0,5,5,0,0")
f.drawVerticalFretboard()


tabS = TabSequence(0, 60)
# tabS.setFrameRate(60)
tabS.setFrameType("midi")
tabS.makingFrames()
# fr = [[60,-1,-1,-1,-1,-1],[60,-1,-1,-1,-1,-1],[60,-1,-1,-1,-1,-1],[60,-1,-1,-1,-1,-1],[60,-1,-1,-1,-1,-1],[60,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1]]
# tabS.setFrames(fr)
tabS.framesToNotesWithTime()
frames = tabS.getFrames()
f.sonifyJams(frames)
