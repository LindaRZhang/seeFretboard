from SeeFretboard import SeeFretboard

#f = SeeFretboard(7)
f = SeeFretboard()


'''
f.addCircle(1, 2,"h")
f.addCircle(3, 4,"h")
f.addCircle(6, 2,"h")
f.addCircle(5, 4,"h")
f.addCircle(4, 4,"h")


f.drawHorizontalImg()
'''

# f.addCircle(1, 2,"v")
# f.addCircle(3, 4,"v")
# f.addCircle(6, 2,"v")
# f.addCircle(5, 4,"v")
# f.addCircle(4, 4,"v")

# f.drawVerticalImg()

f.addNotesAllString("1,0,1,1,0,0","h")
f.addCircle(5, 5,"h")

f.drawHorizontalFretboard()

# f.addNotesAllString("1,0,1,1,0,0","v")
# f.drawVerticalImg()
