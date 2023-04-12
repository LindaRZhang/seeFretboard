from SeeFretboard import SeeFretboard
from Video import Video
from TabSequence import TabSequence
# f = SeeFretboard(7)
# f = SeeFretboard()
# f= SeeFretboard("h", 6, 3, 12)
# f= SeeFretboard("h", 6, 5, 12)


f = SeeFretboard("v", 6, 1, 12)
# f = SeeFretboard("v",6,5,9)


f.addNotesAllString("-1,0,5,5,0,0")
# f.drawHorizontalFretboard()
f.drawVerticalFretboard()


# v = Video(0,30,0,1,30)
# v.addTab(1,"5,0,6,6,0,0")
# v.addTab(1,"0,0,7,7,7,0")
# v.addTab(1,"0,0,7,7,7,5")
# f.setVideo(v)

# 00_BN1-129-Eb_comp

# v = Video(0, 30, 0, 1, 30)
# v.setFrames(guitarSetSongString)
# f.setVideo(v)

tabS = TabSequence(0)
tabS.setFrameType("midi")
tabS.makingFrames()
frame = tabS.getFrames()
# print(frame)
# f.deleteAllImages()
# f.saveAsVideoImagesNoSeconds()
# f.saveAsVideoWithAudio()
f.saveMidi(frame)
f.showFretboard()

# f.addNote(2, 2)
# f.addNote(5, 2)

# f.saveAs("png")

# f.saveAs("svg")
