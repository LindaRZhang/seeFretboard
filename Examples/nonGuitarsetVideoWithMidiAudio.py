import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard.Videos import Video, TabSequence, Audio, VideoManager, Images
from seeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 1, 15)
fretboard.drawVerticalFretboard()
fretboard.fretboardFig.fig.title = "am7/#11"
# fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

#fretboard.addArpeggio("f","major-13th")
fretboard.showFretboard()


# Initialize the TabSequence object
tabSeq = TabSequence(8)  # Use track 8 from the GuitarSet dataset

# Add the tabs for the chords
tabSeq.resetTabAttributes()
tabSeq.addTab(3, "-1,12,-1,12,13,10")  # Add the 032010 chord for 3 seconds
tabSeq.addTab(3, "12,1,10,12,-1,10")  # Add the 033010 chord for 3 seconds
tabSeq.addTab(2, "5,-1,5,5,3,0")  
tabSeq.addTab(2, "5,-1,-1,5,8,10")  
tabSeq.addTab(2, "-1,7,10,-1,8,10")  


# Get the frames as a string
guitarSetSongString = tabSeq.getFretFrames()

# Initialize the Video object
video = Video()
video.setFrames(guitarSetSongString)

# Set the audio name
video.setAudioName("test.wav")

# Create the audio
tabSeq.setFrameType("midi")
tabSeq.makingFrames()
# tabSeq.framesToNotesWithTime()
tabSeq.framesToNotesWithTimeForTabsNonGuitarSet()

noteframes = tabSeq.getNotesWithTimeFrames()

audio = Audio(video.getAudioPathWithName())
audio.sonifyJams(noteframes)

# Initialize the VideoManager object and create the video
videoManager = VideoManager(fretboard, video, Images())
videoManager.saveAsVideoImagesNoSeconds()
videoManager.createVideoWithAudio()