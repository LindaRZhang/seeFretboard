from bokeh.plotting import figure
from bokeh.models import Range1d
import seeFretboard.Utilities.Constants as Constants

class FretboardFigure():
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

        self.oreintation = orientation
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

        self.stringLabel = ""
        self.fretLabel = ""
        self.fig.sizing_mode = "fixed"


    @property
    def stringLabel(self):
        return self._stringLabel

    @stringLabel.setter
    def stringLabel(self, stringLabel):
        self._stringLabel = stringLabel

    def addStringLabelLayout(self):
        self.fig.add_layout(self.stringLabel)

    @property
    def fretLabel(self):
        return self._fretLabel

    @fretLabel.setter
    def fretLabel(self, fretLabel):
        self._fretLabel = fretLabel
    
    def addFretLabelLayout(self):
        self.fig.add_layout(self.fretLabel)

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
    
    @property
    def fig_x_range(self):
        return self.fig.x_range

    @fig_x_range.setter
    def fig_x_range(self, value):
        self.fig.x_range = value

    @property
    def fig_y_range(self):
        return self.fig.y_range

    @fig_y_range.setter
    def fig_y_range(self, value):
        self.fig.y_range = value

    def switchOrientation(self,oreientation):
        if(self.oreintation != oreientation):
            newH = self.width
            newW = self.height
            self.width = newW
            self.height = newH
        if(oreientation in Constants.VERTICAL):
            self.fig_x_range = self.getFigVerXRange()
            self.fig_y_range = self.getFigVerYRange()
        else:    
            self.fig_x_range = self.getFigHorXRange()
            self.fig_y_range = self.getFigVerYRange()
        