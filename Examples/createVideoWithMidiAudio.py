import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Frame import Frame
from Video import Video
from TabSequence import TabSequence
from SeeFretboard import SeeFretboard


fretboard = SeeFretboard("v", 6, 1, 12)
tabSeq = TabSequence(8)#guitar set track 8
video = Video(0, 0, 0, 0)
fretboard.drawVerticalFretboard()


tabSeq.makingFrames()#making fret frames, use for video
guitarSetSongString = tabSeq.getFretFrames()
video.setFrames(guitarSetSongString)
video.setAudioPathName(os.getcwd())
video.setAudioName("midiAudio_00_BN2_00_BN3-119-G_comp_hex_cln.wav")#set as midi audio name
fretboard.setVideo(video)
print("before audio path name")
print(video.getAudioPathWithName())

#create midi audio
tabSeq.setFrameType("midi")
tabSeq.makingFrames()
tabSeq.framesToNotesWithTime()
noteframes = tabSeq.getNotesWithTimeFrames()
fretboard.sonifyJams(noteframes)


fretboard.saveAsVideoImagesNoSeconds()#generate images for audio
fretboard.createVideoWithAudio("videoWithMidiAudio2_00_BN3-119-G_comp_hex_cln")#createVideoWithMidiAudio
