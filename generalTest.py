#quick test for my purpose
from Styles import *

# tuning = Tuning(midiTuning = [40, 45, 50, 115, 59, 64])
# print(tuning.midiTuning)
# # f = FretboardStyle(tuning = tuning)
# f = FretboardStyle(midiTuning = [40, 45, 50, 115, 59, 64])

# print(f.tuning.midiTuning)

# range = FretboardRange(fretFrom= 1, fretTo=8)
# print(range.fretTo)
# f = FretboardStyle(fretboardRange = FretboardRange)
# # f = FretboardStyle(midiTuning = [40, 45, 50, 115, 59, 64])

# print(f.fretboardRange.fretTo)

# style = FretboardStyle(orientation=FretboardOrientation("horizontal"), tuning=Tuning(letterTuning=['E', 'A', 'D', 'G', 'B', 'E']), fretboardRange=FretboardRange(1, 12), fretboardDesign=FretboardDesign())
# assert isinstance(style.orientation, FretboardOrientation)
# assert isinstance(style.tuning, Tuning)
# assert isinstance(style.fretboardRange, FretboardRange)
# assert isinstance(style.fretboardDesign, FretboardDesign)

# style = FretboardStyle(tuning="invalid")
# print(style.tuning.midiTuning)
# style.tuning.midiTuning = [1,2,3,4,5,6]
# print(style.tuning.midiTuning)


# fretboardStyle = FretboardStyle(orientation="h")
# print(isinstance(fretboardStyle.orientation, FretboardOrientation))
# fretboardStyle.orientation = "v"
# print(fretboardStyle.orientation)

orientation = FretboardOrientation("horizontal")

orientation.orientation = "invalid"