import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html


from seeFretboard import SeeFretboard
from bokeh.layouts import row
from bokeh.io import  curdoc


fretboard1 = SeeFretboard()  
fretboard1.drawHorizontalFretboard()
fretboard1.addScale("c","major")

fretboard1.genereateScriptAndDiv()