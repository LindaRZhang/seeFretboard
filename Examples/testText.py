import numpy as np

from bokeh.io import curdoc, show
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, Text
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from SeeFretboard import SeeFretboard

fretboard = SeeFretboard("v", 6, 1, 12)
fretboard.drawVerticalFretboard()
fretboard.addNotesAllString("0,0,2,2,0,0")
fretboard.showFretboard()


N = 9
x = np.linspace(-2, 2, N)
y = x**2
a = "abcdefghijklmnopqrstuvwxyz"
text = [a[i*3:i*3+3] for i in range(N)]


plot = Plot(
    title=None, width=300, height=300,
    min_border=0, toolbar_location=None)

glyph = Text(x="x", y="y", text="text", angle=0.3, text_color="#96deb3")
plot.add_glyph(glyph)

# xaxis = LinearAxis()
# plot.add_layout(xaxis, 'below')

axis = LinearAxis()
# plot.add_layout(yaxis, 'left')

# plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
# plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

show(plot)
