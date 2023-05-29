import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard

fretboard = SeeFretboard("h", 1, 12)
fretboard.drawFretboard("v")#this function can change from h to v

#fretboard.getPitchCollection().setPitchesType("pitchesScaleDegrees")

# fretboard.addCagedPosChord("c","maj", "c")
# fretboard.addCagedPosChord("c", "maj", "a")
# fretboard.addCagedPosChord("c", "maj", "g")
# fretboard.addCagedPosChord("c", "maj", "e")
# fretboard.addCagedPosChord("c", "maj", "d")

# fretboard.addCagedPosChord("c","min", "c")
# fretboard.addCagedPosChord("c", "min", "a")
# fretboard.addCagedPosChord("c", "min", "g")
# fretboard.addCagedPosChord("c", "min", "e")
# fretboard.addCagedPosChord("c", "min", "d")

# fretboard.addCagedPosChord("c","dim", "c")
# fretboard.addCagedPosChord("c", "dim", "a")
# fretboard.addCagedPosChord("c", "dim", "g")
# fretboard.addCagedPosChord("c", "dim", "e")
# fretboard.addCagedPosChord("c", "dim", "d")

# fretboard.addCagedPosChord("c","aug", "c")
# fretboard.addCagedPosChord("c", "aug", "a")
# fretboard.addCagedPosChord("c", "aug", "g")
# fretboard.addCagedPosChord("c", "aug", "e")
# fretboard.addCagedPosChord("b", "aug", "d")

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
# fretboard.addCagedPosChord("c","dim7", "d")

#flat
#fretboard.addCagedPosChord("Db","maj", "c")
# fretboard.addCagedPosChord("Db", "maj", "a")
# fretboard.addCagedPosChord("Db", "maj", "g")
# fretboard.addCagedPosChord("Db", "maj", "e")
# fretboard.addCagedPosChord("bb", "maj", "d")

# fretboard.addCagedPosChord("Db","min", "c")
# fretboard.addCagedPosChord("Db", "min", "a")
# fretboard.addCagedPosChord("Db", "min", "g")
# fretboard.addCagedPosChord("Db", "min", "e")
# fretboard.addCagedPosChord("Db", "min", "d")

# fretboard.addCagedPosChord("Db","dim", "c")
# fretboard.addCagedPosChord("Db", "dim", "a")
# fretboard.addCagedPosChord("Db", "dim", "g")
# fretboard.addCagedPosChord("Db", "dim", "e")
# fretboard.addCagedPosChord("Db", "dim", "d")

# fretboard.addCagedPosChord("Db","aug", "c")
# fretboard.addCagedPosChord("Db", "aug", "a")
# fretboard.addCagedPosChord("Db", "aug", "g")
# fretboard.addCagedPosChord("Db", "aug", "e")
# fretboard.addCagedPosChord("Db", "aug", "d")

#sharp
# fretboard.addCagedPosChord("Db","maj7", "c")
# fretboard.addCagedPosChord("Db","dom7", "c")
# fretboard.addCagedPosChord("Db","min7", "c")
# fretboard.addCagedPosChord("Db","min7b5", "c")
# fretboard.addCagedPosChord("Db","dim7", "c")

# fretboard.addCagedPosChord("Db","maj7", "a")
# fretboard.addCagedPosChord("Db","dom7", "a")
# fretboard.addCagedPosChord("Db","min7", "a")
# fretboard.addCagedPosChord("Db","min7b5", "a")
# fretboard.addCagedPosChord("Db","dim7", "a")

#g 7th shape cant really with caged, hand cant stretch

# fretboard.addCagedPosChord("Db","maj7", "e")
# fretboard.addCagedPosChord("Db","dom7", "e")
# fretboard.addCagedPosChord("Db","min7", "e")
# fretboard.addCagedPosChord("Db","min7b5", "e")
# fretboard.addCagedPosChord("Db","dim7", "e")

# fretboard.addCagedPosChord("Db","maj7", "d")
# fretboard.addCagedPosChord("Db","dom7", "d")
# fretboard.addCagedPosChord("Db","min7", "d")
# fretboard.addCagedPosChord("Db","min7b5", "d")
# fretboard.addCagedPosChord("Db","dim7", "d")

#SHARP
# fretboard.addCagedPosChord("c#","maj", "c")
# fretboard.addCagedPosChord("c#", "maj", "a")
# fretboard.addCagedPosChord("c#", "maj", "g")
# fretboard.addCagedPosChord("c#", "maj", "e")
fretboard.addCagedPosChord("a#", "maj", "d")

# fretboard.addCagedPosChord("c#","min", "c")
# fretboard.addCagedPosChord("c#", "min", "a")
# fretboard.addCagedPosChord("c#", "min", "g")
# fretboard.addCagedPosChord("c#", "min", "e")
# fretboard.addCagedPosChord("c#", "min", "d")

# fretboard.addCagedPosChord("c#","dim", "c")
# fretboard.addCagedPosChord("c#", "dim", "a")
# fretboard.addCagedPosChord("c#", "dim", "g")
# fretboard.addCagedPosChord("c#", "dim", "e")
# fretboard.addCagedPosChord("c#", "dim", "d")

# fretboard.addCagedPosChord("c#","aug", "c")
# fretboard.addCagedPosChord("c#", "aug", "a")
# fretboard.addCagedPosChord("c#", "aug", "g")
# fretboard.addCagedPosChord("c#", "aug", "e")
# fretboard.addCagedPosChord("c#", "aug", "d")

# fretboard.addCagedPosChord("c#","maj7", "c")
# fretboard.addCagedPosChord("c#","dom7", "c")
# fretboard.addCagedPosChord("c#","min7", "c")
# fretboard.addCagedPosChord("c#","min7b5", "c")
# fretboard.addCagedPosChord("c#","dim7", "c")

# fretboard.addCagedPosChord("c#","maj7", "a")
# fretboard.addCagedPosChord("c#","dom7", "a")
# fretboard.addCagedPosChord("c#","min7", "a")
# fretboard.addCagedPosChord("c#","min7b5", "a")
# fretboard.addCagedPosChord("c#","dim7", "a")

#g 7th shape cant really with caged, hand cant stretch

# fretboard.addCagedPosChord("c#","maj7", "e")
# fretboard.addCagedPosChord("c#","dom7", "e")
# fretboard.addCagedPosChord("c#","min7", "e")
# fretboard.addCagedPosChord("c#","min7b5", "e")
# fretboard.addCagedPosChord("c#","dim7", "e")

# fretboard.addCagedPosChord("c#","maj7", "d")
# fretboard.addCagedPosChord("c#","dom7", "d")
# fretboard.addCagedPosChord("c#","min7", "d")
# fretboard.addCagedPosChord("c#","min7b5", "d")
# fretboard.addCagedPosChord("c#","dim7", "d")
fretboard.showFretboard()