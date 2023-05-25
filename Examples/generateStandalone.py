import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from seeFretboard import SeeFretboard


fretboard1 = SeeFretboard()  
fretboard1.drawHorizontalFretboard()
fretboard1.addScale("c","major")

fretboard1.generateWithServerHtml()