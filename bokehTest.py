from SeeFretboard import SeeFretboard

#f = SeeFretboard(7)
#f = SeeFretboard()
#f= SeeFretboard("h", 6, 3, 12)
f= SeeFretboard("h", 6, 5, 9)


#f = SeeFretboard("v",6,3,9)
#f = SeeFretboard("v",6,5,9)


f.addNotesAllString("5,0,5,5,0,0")
#f.addNote(2, 2)
#f.addNote(5, 2)

f.drawHorizontalFretboard()
#f.saveAs("png")
#f.drawVerticalFretboard()

f.showFretboard()
#f.saveAs("svg")


