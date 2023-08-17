import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12)
fretboard.drawFretboard("v")#this function can change from h to v

#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

"""
Drop2 String6
"""
fretboard.addDropChord("c","maj7")
fretboard.setNoteType("groundTruth")
fretboard.addDropChord("c", "maj7","Drop2", "2")
fretboard.setNoteType("prediction")
fretboard.addDropChord("c", "maj7","Drop2", "3")
fretboard.setNoteType("groundTruth")
fretboard.addDropChord("c", "maj7","Drop2", "4")

# fretboard.addDropChord("c","dom7")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "2")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dom7","Drop2", "3")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "4")

# fretboard.addDropChord("c","min7")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "2")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7","Drop2", "3")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "4")

# fretboard.addDropChord("c","min7b5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "2")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7b5","Drop2", "3")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "4")

# fretboard.addDropChord("c","dim7")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "2")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dim7","Drop2", "3")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "4")
"""
Drop2 String5
"""
# fretboard.addDropChord("c","maj7","Drop2","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop2", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "maj7","Drop2", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop2", "4","5")

# fretboard.addDropChord("c","dom7","Drop2","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dom7","Drop2", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "4","5")

# fretboard.addDropChord("c","min7","Drop2","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7","Drop2", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "4","5")

# fretboard.addDropChord("c","min7b5","drop2","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7b5","Drop2", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "4","5")

# fretboard.addDropChord("c","dim7","drop2","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dim7","Drop2", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "4","5")


"""
Drop2 String4
"""
# fretboard.addDropChord("c","maj7","Drop2","1","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop2", "2","4")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "maj7","Drop2", "3","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop2", "4","4")

# fretboard.addDropChord("c","dom7","Drop2","1","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "2","4")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dom7","Drop2", "3","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop2", "4","4")

# fretboard.addDropChord("c","min7","Drop2","1","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "2","4")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7","Drop2", "3","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop2", "4","4")

# fretboard.addDropChord("c","min7b5","drop2","1","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "2","4")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7b5","Drop2", "3","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop2", "4","4")

# fretboard.addDropChord("c","dim7","drop2","1","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "2","4")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dim7","Drop2", "3","4")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop2", "4","4")

"""
Drop3 String6
"""
# fretboard.addDropChord("c","maj7","Drop3","1","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop3", "2","6")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "maj7","Drop3", "3","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop3", "4","6")

# fretboard.addDropChord("c","dom7","Drop3","1","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop3", "2","6")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dom7","Drop3", "3","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop3", "4","6")

# fretboard.addDropChord("c","min7","Drop3","1","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop3", "2","6")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7","Drop3", "3","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop3", "4","6")

# fretboard.addDropChord("c","min7b5","Drop3","1","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop3", "2","6")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7b5","Drop3", "3","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop3", "4","6")

# fretboard.addDropChord("c","dim7","Drop3","1","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop3", "2","6")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dim7","Drop3", "3","6")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop3", "4","6")
"""
Drop3 String5
"""
# fretboard.addDropChord("c","maj7","Drop3","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop3", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "maj7","Drop3", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "maj7","Drop3", "4","5")

# fretboard.addDropChord("c","dom7","Drop3","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop3", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "dom7","Drop3", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dom7","Drop3", "4","5")

# fretboard.addDropChord("c","min7","Drop3","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop3", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7","Drop3", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7","Drop3", "4","5")

# fretboard.addDropChord("c","min7b5","Drop3","1","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop3", "2","5")
# fretboard.setNoteType("prediction")
# fretboard.addDropChord("c", "min7b5","Drop3", "3","5")
# fretboard.setNoteType("groundTruth")
# fretboard.addDropChord("c", "min7b5","Drop3", "4","5")

# fretboard.addDropChord("c","dim7","Drop3","1","5")
# fretboard.theme.fretboardDesign.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop3", "2","5")
# fretboard.theme.fretboardDesign.setNoteType("prediction")
# fretboard.addDropChord("c", "dim7","Drop3", "3","5")
# fretboard.theme.fretboardDesign.setNoteType("groundTruth")
# fretboard.addDropChord("c", "dim7","Drop3", "4","5")

fretboard.showFretboard()