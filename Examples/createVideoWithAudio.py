import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Frame import Frame
from Video import Video
from TabSequence import TabSequence
from SeeFretboard import SeeFretboard


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
video.setAudioPathName(os.getcwd())
video.setAudioName("00_BN3-119-G_comp_hex_cln.wav")
fretboard.setVideo(video)
fretboard.saveAsVideoImagesNoSeconds()
fretboard.createVideoWithAudio("videoWithAudio2_00_BN3-119-G_comp_hex_cln")
