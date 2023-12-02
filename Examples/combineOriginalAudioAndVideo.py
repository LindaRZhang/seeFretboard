import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard
from seeFretboard.Videos import Video, VideoManager, Images

fretboard = SeeFretboard("v", 1, 12)
fretboard.drawVerticalFretboard()

video = Video()
video.setVideoName("video_00_BN3-119-G_comp_hex_cln.mp4")
video.setAudioName("00_BN3-119-G_comp_mix.wav")#combine with original audio
video.setVideoWAudioName("VideoWithCombinedAudio00_BN3-119-G_comp_hex_cln")
videoManager = VideoManager(fretboard,video,Images())

videoManager.createVideoWithAudio()#createVideoWithMidiAudio