import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12)
fretboard.drawFretboard("v")#this function can change from h to v

#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

#fretboard.addCagedPosChord("c","maj", "c")
#fretboard.addCagedPosChord("bb", "maj", "a")
#fretboard.addCagedPosChord("bb", "maj", "g")
#fretboard.addCagedPosChord("bb", "maj", "e")
#fretboard.addCagedPosChord("a#", "maj", "d")

# fretboard.addCagedPosChord("c","min", "c")
# fretboard.addCagedPosChord("bb", "min", "a")
# fretboard.addCagedPosChord("bb", "min", "g")
# fretboard.addCagedPosChord("bb", "min", "e")
# fretboard.addCagedPosChord("bb", "min", "d")

# fretboard.addCagedPosChord("c","dim", "c")
# fretboard.addCagedPosChord("bb", "dim", "a")
# fretboard.addCagedPosChord("bb", "dim", "g")
# fretboard.addCagedPosChord("bb", "dim", "e")
# fretboard.addCagedPosChord("bb", "dim", "d")

# fretboard.addCagedPosChord("c","aug", "c")
# fretboard.addCagedPosChord("c", "aug", "a")
# fretboard.addCagedPosChord("bb", "aug", "g")
# fretboard.addCagedPosChord("a#", "aug", "e")
# fretboard.addCagedPosChord("bb", "aug", "d")

# fretboard.addCagedPosChord("c","maj7", "c")
# fretboard.addCagedPosChord("c","dom7", "c")
# fretboard.addCagedPosChord("c","min7", "c")
# fretboard.addCagedPosChord("c","min7b5", "c")
# fretboard.addCagedPosChord("c","dim7", "c")

# fretboard.addCagedPosChord("c","maj7", "a")
# fretboard.addCagedPosChord("c","dom7", "a")
# fretboard.addCagedPosChord("c","min7", "a")
# fretboard.addCagedPosChord("c","min7b5", "a")
# fretboard.addCagedPosChord("c","dim7", "a")

#g 7th shape cant really with caged, hand cant stretch

# fretboard.addCagedPosChord("c","maj7", "e")
# fretboard.addCagedPosChord("c","dom7", "e")
# fretboard.addCagedPosChord("c","min7", "e")
# fretboard.addCagedPosChord("c","min7b5", "e")
# fretboard.addCagedPosChord("c","dim7", "e")

# fretboard.addCagedPosChord("c","maj7", "d")
# fretboard.addCagedPosChord("c","dom7", "d")
# fretboard.addCagedPosChord("c","min7", "d")
# fretboard.addCagedPosChord("c","min7b5", "d")
fretboard.addCagedPosChord("c","dim7", "d")

fretboard.showFretboard()