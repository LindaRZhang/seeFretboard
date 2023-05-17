from bokeh.plotting import figure
from bokeh.models import Range1d

class fretboardFigure():
    def __init__(self, note, theme, orientation="h", width = None, height=None):
        self.fig = figure()
        self.figHorXRange = Range1d(-8*note.getNoteRadius(),
                                        (theme.fretboardRange.numOfFrets+1.3)*theme.fretboardDesign.distanceBetweenFrets)
        self.figHorYRange = Range1d(-3*note.getNoteRadius(),
                                        theme.fretboardDesign.distanceBetweenStrings*theme.tuning.numOfStrings)
        self.figVerXRange = Range1d(-3*note.getNoteRadius(),
                                        theme.fretboardDesign.distanceBetweenStrings*theme.tuning.numOfStrings)
        self.figVerYRange = Range1d(-8*note.getNoteRadius(),
                                        (theme.fretboardRange.numOfFrets+2)*theme.fretboardDesign.distanceBetweenFrets)

        if (orientation == "h"):
            if(width == None or height == None):
                self.fig.width = 800
                self.fig.height = 400
            else:
                self.fig.width = width
                self.fig.height = height
            self.fig.x_range = self.figHorXRange
            self.fig.y_range = self.figHorYRange
        
        else:
            if(width == None or height == None):
                self.fig.width = 400
                self.fig.height = 800
            else:
                self.fig.width = width
                self.fig.height = height
            self.fig.x_range = self.figVerXRange
            self.fig.y_range = self.figVerYRange
    
    @property
    def fig(self):
        return self._fig

    @fig.setter
    def fig(self, fig):
        self._fig = fig

    @property
    def width(self):
        return self.fig.width

    @width.setter
    def width(self, width):
        self.fig.width = width

    @property
    def height(self):
        return self.fig.height
    
    @height.setter
    def height(self, height):
        self.fig.height = height

    def getFigHorXRange(self):
        return self.figHorXRange

    def setFigHorXRange(self, v1, v2):
        self.figHorXRange = Range1d(v1, v2)

    def getFigHorYRange(self):
        return self.figHorYRange

    def setFigHorYRange(self, v1, v2):
        self.figHorYRange = Range1d(v1, v2)

    def getFigVerXRange(self):
        return self.figVerXRange

    def setFigVerXRange(self, v1, v2):
        self.figVerXRange = Range1d(v1, v2)

    def getFigVerYRange(self):
        return self.figVerYRange

    def setFigVerYRange(self, v1, v2):
        self.figVerYRange = Range1d(v1, v2)
        