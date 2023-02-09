from SeeFretboard import SeeFretboard

#f = SeeFretboard(7)
f = SeeFretboard()

#f = SeeFretboard("v")


f.addNotesAllString("1,0,1,1,0,0")
f.addCircle(2, 2)

f.drawHorizontalFretboard()
#f.saveImg("png")

#f.drawVerticalFretboard()
#f.showFretboard()

