import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from seeFretboard.Videos import Video, TabSequence,Audio


from seeFretboard import SeeFretboard
from seeFretboard.Utilities import Constants

f = SeeFretboard("v", 1, 12)
f.drawVerticalFretboard()

video = Video()
video.setAudioName("00_BN3-119-G_comp_mix.wav")
tabS = TabSequence(8)
tabS.setFrameRate(Constants.FRAMERATE)
tabS.setFrameType("midi")
tabS.makingFrames()
tabS.framesToNotesWithTime()
noteFrames = tabS.getNotesWithTimeFrames()

video.audioPath = os.path.join(Constants.BASE_PATH, 'Outputs',"Audios")
#because initially the path is for inputting guitarSet, but now we want an place to out put it and defining it now

audio = Audio(video.getAudioPathWithName())
audio.sonifyJams(noteFrames)
print("Midi Wave Audio Created at",video.getAudioPathWithName() )
