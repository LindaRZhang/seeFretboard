import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Videos.Frame import Frame
from Videos.Video import Video
from Videos.TabSequence import TabSequence
from SeeFretboard import SeeFretboard
from Videos import Video, TabSequence, Audio, VideoManager, Images


fretboard = SeeFretboard("v", 1, 12)
tabSeq = TabSequence(8)
video = Video(0, 0, 0, 0)
fretboard.drawVerticalFretboard()
video.setVideoName("OpenStringG")

'''
Use guitar set track 0 to make frames
Then frames to images
then images to video with audio
'''
tabSeq.makingFrames()
video.setAudioName("00_BN3-119-G_comp_hex_cln.wav")

videoManager = VideoManager(fretboard,video,Images())
#videoManager.saveAsVideoImagesNoSeconds()#generate images for audio
videoManager.createVideoWithAudio()#createVideoWithMidiAudio
