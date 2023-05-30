from bokeh.plotting import figure
from bokeh.models import Range1d
import seeFretboard.Utilities.Constants as Constants

class FretboardFigure():
    '''
    The FretboardFigure class is responsible for creating a Bokeh figure object that represents a guitar fretboard. 
    It allows for customization of the figure's orientation, size, and range, as well as the addition of string and fret labels. 
    The class also includes methods for switching the orientation of the figure and getting/setting the x and y ranges.
    
    Attributes:
    - fig (figure): The Bokeh figure object.
    - figHorXRange (Range1d): The x-range for the horizontal orientation.
    - figHorYRange (Range1d): The y-range for the horizontal orientation.
    - figVerXRange (Range1d): The x-range for the vertical orientation.
    - figVerYRange (Range1d): The y-range for the vertical orientation.
    - orientation (str): The orientation of the fretboard figure ('h' for horizontal, 'v' for vertical).
    - stringLabel (str): The string label layout.
    - fretLabel (str): The fret label layout.
    - width (int): The width of the figure.
    - height (int): The height of the figure.
    '''
    def __init__(self, note, theme, orientation="h", width = None, height=None):
        '''
        Initializes a FretboardFigure object with the specified parameters.

        Parameters:
        - note (CircleNote): The CircleNote object.
        - theme (Theme): The Theme object.
        - orientation (str): The orientation of the fretboard figure ('h' for horizontal, 'v' for vertical). Default is 'h'.
        - width (int): The width of the figure. Default is None.
        - height (int): The height of the figure. Default is None.
        '''

        self.fig = figure()
        self.figHorXRange = Range1d(-8*note.getNoteRadius(),
                                        (theme.fretboardRange.numOfFrets+1.3)*theme.fretboardDesign.distanceBetweenFrets)
        self.figHorYRange = Range1d(-3*note.getNoteRadius(),
                                        theme.fretboardDesign.distanceBetweenStrings*theme.tuning.numOfStrings)
        self.figVerXRange = Range1d(-3*note.getNoteRadius(),
                                        theme.fretboardDesign.distanceBetweenStrings*theme.tuning.numOfStrings)
        self.figVerYRange = Range1d(-8*note.getNoteRadius(),
                                        (theme.fretboardRange.numOfFrets+2)*theme.fretboardDesign.distanceBetweenFrets)

        self.orientation = orientation
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
    
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False
        self.fig.axis.visible=False 


    @property
    def stringLabel(self):
        return self._stringLabel

    @stringLabel.setter
    def stringLabel(self, stringLabel):
        self._stringLabel = stringLabel

    def addStringLabelLayout(self):
        '''
        Adds the string label layout to the figure.
        '''
        self.fig.add_layout(self.stringLabel)

    @property
    def fretLabel(self):
        return self._fretLabel

    @fretLabel.setter
    def fretLabel(self, fretLabel):
        self._fretLabel = fretLabel

    def addFretLabelLayout(self):
        '''
        Adds the fret label layout to the figure.
        '''
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
        '''
        Returns the x-range for the horizontal orientation.

        Returns:
        - Range1d: The x-range for the horizontal orientation.
        '''
        return self.figHorXRange

    def setFigHorXRange(self, v1, v2):
        '''
        Sets the x-range for the horizontal orientation.

        Parameters:
        - v1: The starting value of the x-range.
        - v2: The ending value of the x-range.
        '''
        self.figHorXRange = Range1d(v1, v2)

    def getFigHorYRange(self):
        '''
        Returns the y-range for the horizontal orientation.

        Returns:
        - Range1d: The y-range for the horizontal orientation.
        '''
        return self.figHorYRange

    def setFigHorYRange(self, v1, v2):
        '''
        Sets the y-range for the horizontal orientation.

        Parameters:
        - v1: The starting value of the y-range.
        - v2: The ending value of the y-range.
        '''
        self.figHorYRange = Range1d(v1, v2)

    def getFigVerXRange(self):
        '''
        Returns the x-range for the vertical orientation.

        Returns:
        - Range1d: The x-range for the vertical orientation.
        '''
        return self.figVerXRange

    def setFigVerXRange(self, v1, v2):
        '''
        Sets the x-range for the vertical orientation.

        Parameters:
        - v1: The starting value of the x-range.
        - v2: The ending value of the x-range.
        '''
        self.figVerXRange = Range1d(v1, v2)

    def getFigVerYRange(self):
        '''
        Returns the y-range for the vertical orientation.

        Returns:
        - Range1d: The y-range for the vertical orientation.
        '''
        return self.figVerYRange

    def setFigVerYRange(self, v1, v2):
        '''
        Sets the y-range for the vertical orientation.

        Parameters:
        - v1: The starting value of the y-range.
        - v2: The ending value of the y-range.
        '''
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

    def switchOrientation(self, orientation):
        '''
        Switches the orientation of the fretboard figure.

        Parameters:
        - orientation (str): The new orientation ('h' for horizontal, 'v' for vertical).
        '''
        if self.orientation != orientation:
            newH = self.width
            newW = self.height
            self.width = newW
            self.height = newH
        if orientation in Constants.VERTICAL:
            self.fig_x_range = self.getFigVerXRange()
            self.fig_y_range = self.getFigVerYRange()
        else:
            self.fig_x_range = self.getFigHorXRange()
            self.fig_y_range = self.getFigVerYRange()