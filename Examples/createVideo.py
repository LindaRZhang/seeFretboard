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


tabSeq.makingFrames()
guitarSetSongString = tabSeq.getFretFrames()
video.setFrames(guitarSetSongString)
video.setVideoName("video_00_BN3-119-G_comp_hex_cln")

videoManager = VideoManager(fretboard,video,Images())

#videoManager.saveAsVideoImagesNoSeconds()
videoManager.saveAsVideo()
