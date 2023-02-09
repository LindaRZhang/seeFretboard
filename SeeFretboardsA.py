from SeeFretboards import SeeFretboards

f = SeeFretboards()
f.addNotesAllString("1,0,1,1,0,0")
f.drawHorizontalFretboard()
f.addCircle(5, 5,"h")
f.updateFretboard()
f.clearFretboard()
f.addCircle(3, 4,"b")
f.updateFretboard()
