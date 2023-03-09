from SeeFretboard import SeeFretboard
from Video import Video
#f = SeeFretboard(7)
#f = SeeFretboard()
#f= SeeFretboard("h", 6, 3, 12)
f= SeeFretboard("h", 6, 3, 7)


# f = SeeFretboard("v",6,3,12)
# f = SeeFretboard("v",6,5,9)


f.addNotesAllString("x,0,5,5,0,0")
f.drawHorizontalFretboard()
# f.drawVerticalFretboard()


# v = Video(0,30,0,1,30)
# v.addTab(1,"5,0,6,6,0,0")
# v.addTab(1,"0,0,7,7,7,0")
# v.addTab(1,"0,0,7,7,7,5")
# f.setVideo(v)

# f.deleteAllImages()
# f.saveAsVideoImages()
# f.saveAsVideo()

f.showFretboard()

#f.addNote(2, 2)
#f.addNote(5, 2)

#f.saveAs("png")

#f.saveAs("svg")


