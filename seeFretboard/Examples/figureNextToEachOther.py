import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard
from bokeh.layouts import row
from bokeh.io import  curdoc


fretboard1 = SeeFretboard()  
fretboard1.drawHorizontalFretboard()
fretboard2 = SeeFretboard("v")  
fretboard2.drawVerticalFretboard()

layout = row(fretboard1.layout, fretboard2.layout)  
curdoc().add_root(layout)
