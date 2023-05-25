import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seeFretboard.Videos.TabSequence import TabSequence
from seeFretboard.Videos.Video import Video
from seeFretboard import SeeFretboard

f = SeeFretboard("v", 1, 12)
f.addNotesAllString("-1,0,5,5,0,0")
f.drawVerticalFretboard()

f.video.setAudioName("midiAudio_00_BN1-129-Eb_comp_hex.wav")
tabS = TabSequence(0)
tabS.setFrameRate(60)
tabS.setFrameType("midi")
tabS.makingFrames()
tabS.framesToNotesWithTime()
noteFrames = tabS.getNotesWithTimeFrames()
f.sonifyJams(noteFrames)
