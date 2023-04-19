import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard
from TabSequence import TabSequence
from Video import Video
from Frame import Frame

fretboard = SeeFretboard("v", 6, 1, 12)
tabSeq = TabSequence(0)
video = Video(0, 0, 0, 0)
fretboard.drawVerticalFretboard()

'''
Use guitar set track 0 to make frames
Then frames to images
then images to video with audio
'''
tabSeq.makingFrames()
guitarSetSongString = tabSeq.getFrames()
video.setFrames(guitarSetSongString)
fretboard.setVideo(video)
fretboard.saveAsVideoImagesNoSeconds()
fretboard.saveAsVideoWithAudio()
