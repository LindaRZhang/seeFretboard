from bokeh.plotting import figure
from bokeh.io import curdoc, show


# create a figure object
p = figure(width=400, height=400)

# set the x and y position for the symbol (use the same values as the Text glyph)
x = 100
y = 200

# set the size of the symbol
symbol_size = 10

# add two lines to create the 'x' symbol
p.line([x - symbol_size, x + symbol_size],
       [y - symbol_size, y + symbol_size], line_width=2)
p.line([x - symbol_size, x + symbol_size],
       [y + symbol_size, y - symbol_size], line_width=2)

curdoc().add_root(p)

# show the figure
show(p)
