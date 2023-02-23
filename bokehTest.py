from SeeFretboard import SeeFretboard
from Video import Video
#f = SeeFretboard(7)
#f = SeeFretboard()
#f= SeeFretboard("h", 6, 3, 12)
f= SeeFretboard("h", 6, 5, 9)


#f = SeeFretboard("v",6,3,9)
#f = SeeFretboard("v",6,5,9)


f.addNotesAllString("5,0,5,5,0,0")
f.drawHorizontalFretboard()
f.updateFretboard("5,0,9,9,9,0")
v = Video(0,2,0,0.1)
v.addFrame(0,"7,0,5,5,0,0")
v.addFrame(1,"0,0,7,7,7,0")
v.addFrame(2,"0,0,7,7,7,5")
f.setVideo(v)

f.showFretboard()

#f.addNote(2, 2)
#f.addNote(5, 2)

#f.saveAs("png")
#f.drawVerticalFretboard()

#f.saveAs("svg")


