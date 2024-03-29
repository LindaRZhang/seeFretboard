import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard.Videos.Frame import Frame
from seeFretboard.Videos.Video import Video
from seeFretboard.Videos.TabSequence import TabSequence
from seeFretboard import SeeFretboard


fretboard = SeeFretboard("v", 1, 12)
tabSeq = TabSequence(8)
video = Video(0, 0, 0, 0)
fretboard.drawVerticalFretboard()

video.setVideoPathName(os.getcwd())
video.setVideoName("video_00_BN3-119-G_comp_hex_cln")
video.setAudioPathName(os.getcwd())
video.setAudioName("00_BN3-119-G_comp_hex_cln.wav")
fretboard.setVideo(video)
fretboard.createVideoWithAudio("videoWithAudio_00_BN3-119-G_comp_hex_cln")
