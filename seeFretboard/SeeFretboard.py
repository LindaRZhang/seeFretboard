from bokeh.plotting import figure, show
from bokeh.models import Line, Circle, Label, Button, CustomJS, ColumnDataSource, PanTool, BoxSelectTool, Range1d
from bokeh.models.widgets import TextInput
from bokeh.layouts import layout
from bokeh.events import ButtonClick
from bokeh.io import  curdoc
from bokeh.layouts import row
from bokeh.resources import CDN
from bokeh.embed import file_html, components, server_document
from bokeh.application import Application
from bokeh.application.handlers import FunctionHandler

from seeFretboard.Designs.CirlceNote import CircleNote
from seeFretboard.Utilities import Functions
import seeFretboard.Utilities.Constants as Constants
from seeFretboard.PitchCollection import PitchCollection
from seeFretboard.Designs.FretboardStyle import *
from seeFretboard.Designs.FretboardFigure import FretboardFigure
from seeFretboard.NotePosition import NotePositionsOnCurrentFretboard
from seeFretboard.Utilities.PathInfo import EmbedPathInfo
from seeFretboard.Utilities import Constants

from tqdm import tqdm

from music21 import scale, interval, harmony, key
from music21 import pitch as m21Pitch
#manager/master kinda
class SeeFretboard():
    
    # default values
    #fret 0 include open strings
    def __init__(self, orientation = "h",fretFrom=1, fretTo=12, string=6, showTuning=True, theme="", **kwargs):
        # styleing/theme
        self.fretboardTheme = FretboardTheme(theme=theme, orientation=orientation, 
                                    fretFrom =fretFrom, fretTo=fretTo, string=string,
                                    showTuning=showTuning, **kwargs)

        # notes circle
        self.currentNotesPositionOnFretboard = [] #NotePosition
        self.notes = [] #glyph of the current notes more for removeable purposes
        self.labels = []
        
        # figure attribute
        self.fretboardFig = FretboardFigure( self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue(), self.fretboardTheme, orientation)
        
        self.stringSource = ""
        self.fretSource = ""

        # buttons
        self.tuningLabelButton = Button(
            label="Toggle Tuning", button_type="success")
        self.fretLabelButton = Button(
            label="Toggle Fretboard Number", button_type="success")
        self.fretBoardDirectionButton = Button(
            label="Toggle Fretboard Direction", button_type="success")
        self.toggleButtons = row(
            self.fretBoardDirectionButton, self.tuningLabelButton, self.fretLabelButton)
        self.inputChordInput = TextInput(
            value="x,0,2,2,0,0", title="Enter Notes Fret:")
        self.inputChordButton = Button(label="ENTER ", button_type="success")
        self.clearFretboardButton = Button(
            label="Clear Fretboard ", button_type="success")
        self.notesOptions = row(
            self.inputChordInput, self.inputChordButton, self.clearFretboardButton)

        self.inputChordButton.on_click(self.inputChordButtonClicked)
        self.clearFretboardButton.on_click(self.clearFretboard)
        self.fretBoardDirectionButton.on_click(self.toggleFretboardDirection)

        #notes/pitches for scales n arpeggios
        self.pitchCollection = PitchCollection()
        
        self.scaleCustom = False

        self.pathInfo = EmbedPathInfo()

        self.layout = layout([self.fretboardFig.fig,
                         self.toggleButtons, self.notesOptions])

    def getFretboardFig(self):
        return self.fretboardFig
    
    def setFretboardFig(self, fig):
        self.fretboardFig = fig

    def inputChordButtonClicked(self):
        #setting pitch collection let me think think
        self.updateFretboard(self.inputChordInput.value)

    # fretboard relate
    def drawTuningLabel(self, distanceStrings, i):
        if (self.fretboardTheme.orientation.orientation == "h"):
            stringLabel = Label(x=-1, y=distanceStrings-self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                                 text=self.fretboardTheme.tuning.letterTuning[i], text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.tuningLabelFontSize, text_font_style='bold', text_color=self.fretboardTheme.fretboardDesign.tuningLabelColor)
        else:
            stringLabel = Label(x=distanceStrings, y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                self.fretboardTheme.fretboardRange.numOfFrets+1), text=self.fretboardTheme.tuning.letterTuning[i+1], text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.tuningLabelFontSize, text_color=self.fretboardTheme.fretboardDesign.tuningLabelColor, text_font_style='bold')

        stringLabel.visible = self.fretboardTheme.fretboardDesign.showTuning
        
        self.fretboardFig.stringLabel = stringLabel
        self.fretboardFig.addStringLabelLayout()

        self.tuningLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            stringLabel=stringLabel), code="""stringLabel.visible = !stringLabel.visible"""))

    def drawFretLabel(self, distanceBetweenFrets, j):
        if (self.fretboardTheme.orientation.orientation == "h"):
            fretLabel = Label(x=distanceBetweenFrets+self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                               y=-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius*2.5, text=str(j+1), text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.tuningLabelFontSize, text_color=self.fretboardTheme.fretboardDesign.tuningLabelColor,text_font_style='bold')
        else:
            fretLabel = Label(x=-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius*2.5, y=distanceBetweenFrets+self.fretboardTheme.fretboardDesign.distanceBetweenFrets -
                               self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2, text=str(j), text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.tuningLabelFontSize, text_color=self.fretboardTheme.fretboardDesign.tuningLabelColor,text_font_style='bold')

        fretLabel.visible = self.fretboardTheme.fretboardDesign.showFretboardNumber
        
        self.fretboardFig.fretLabel = fretLabel
        self.fretboardFig.addFretLabelLayout()

        self.fretLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            fretLabel=fretLabel), code="""fretLabel.visible = !fretLabel.visible"""))

    def toggleFretboardDirection(self):
        notesPosOnFretboard = self.getCurrentNotesOnFretboard()
        self.removeFigure()

        if(self.fretboardTheme.orientation.orientation in Constants.HORIZONTAL):
            self.setFretboardFig(FretboardFigure(self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue(), self.getTheme(), "v"))
            self.getTheme().orientation.orientation = "v"
            self.drawVerticalFretboard()

        else:
            self.setFretboardFig(FretboardFigure(self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue(), self.getTheme(), "h"))
            self.getTheme().orientation.orientation = "h"
            self.drawHorizontalFretboard()

        self.layout.children.insert(0,self.fretboardFig.fig)

        self.notes = []
        self.labels = []

        # Add the progress bar
        with tqdm(total=len(notesPosOnFretboard)) as pbar:
            for i, notePos in enumerate(notesPosOnFretboard):
                self.pitchCollection.setPitchesIndex(i)
                self.addNote(self.pitchCollection.getStringsAt(i),self.pitchCollection.getFretsAt(i))
                pbar.update(1)  # Update the progress bar
        print("Toggle Fretboard Success")
        
    def drawFretboard(self, orientation):
        if(orientation.lower() in Constants.HORIZONTAL):
            self.fretboardTheme.orientation.orientation = "h"
            self.fretboardFig.switchOrientation("h")
            self.drawHorizontalFretboard()
        elif(orientation.lower() in Constants.VERTICAL):
            self.fretboardTheme.orientation.orientation = "v"
            self.fretboardFig.switchOrientation("v")
            self.drawVerticalFretboard()

    # preview
    def drawHorizontalFretboard(self):
        distanceStrings = 0        
        strings = {
            "x": [],
            "y": []
        }
        frets = {
            "x": [],
            "y": []
        }
        # draw strings (horizontal line)
        for i in range(0, self.fretboardTheme.tuning.numOfStrings):
            strings["x"].append([0, self.fretboardTheme.fretboardDesign.distanceBetweenFrets * (self.fretboardTheme.fretboardRange.fretTo - self.fretboardTheme.fretboardRange.fretFrom + 1)])
            strings["y"].append([distanceStrings, distanceStrings])

            self.drawTuningLabel(distanceStrings + self.fretboardTheme.fretboardDesign.distanceBetweenStrings, i)

            distanceStrings += self.fretboardTheme.fretboardDesign.distanceBetweenStrings
        self.stringSource = ColumnDataSource(data=strings)
        self.fretboardFig.fig.multi_line(xs="x", ys="y", line_color=self.fretboardTheme.fretboardDesign.stringsColor,
                                   line_alpha=self.fretboardTheme.fretboardDesign.stringsOpacity, line_width = self.fretboardTheme.fretboardDesign.stringThinkness, source=self.stringSource)

        distanceBetweenFrets = 0
    
        # draw frets (vertical line)
        for j in range(self.fretboardTheme.fretboardRange.fretFrom - 1, self.fretboardTheme.fretboardRange.fretTo + 1):
            frets["x"].append([distanceBetweenFrets, distanceBetweenFrets])
            frets["y"].append([0, self.fretboardTheme.fretboardDesign.distanceBetweenStrings * (self.fretboardTheme.tuning.numOfStrings - 1)])

            if j != self.fretboardTheme.fretboardRange.fretTo:
                self.drawFretLabel(distanceBetweenFrets, j)

            distanceBetweenFrets += self.fretboardTheme.fretboardDesign.distanceBetweenFrets

        self.fretSource = ColumnDataSource(data=frets)
        self.fretboardFig.fig.multi_line(xs="x", ys="y", line_color=self.fretboardTheme.fretboardDesign.fretColor,
                                        line_alpha=self.fretboardTheme.fretboardDesign.fretOpacity, line_width = self.fretboardTheme.fretboardDesign.fretThinkness, source=self.fretSource)
        self.drawInlay()

        self.fretboardFig.fig.y_range=Range1d(0-self.fretboardTheme.fretboardDesign.distanceBetweenStrings, self.fretboardTheme.fretboardDesign.distanceBetweenStrings*self.fretboardTheme.fretboardRange.numOfStrings,bounds='auto')
        self.fretboardFig.fig.background_fill_color = self.fretboardTheme.fretboardDesign.backgroundColor

    def drawVerticalFretboard(self):
        x = [0, 0]
        y = [0, self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets+1)]

        self.drawTuningLabel(0, -1)

        self.fretboardFig.fig.line(x=x, y=y, line_color=self.fretboardTheme.fretboardDesign.stringsColor,
                      line_alpha=self.fretboardTheme.fretboardDesign.stringsOpacity)

        distanceStrings = self.fretboardTheme.fretboardDesign.distanceBetweenStrings
        # draw strings (vertical line)
        for i in range(0, self.fretboardTheme.tuning.numOfStrings-1):
            x = [distanceStrings, distanceStrings]
            y = [0, self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets+1)]

            self.drawTuningLabel(distanceStrings, i)

            distanceStrings += self.fretboardTheme.fretboardDesign.distanceBetweenStrings
            self.fretboardFig.fig.line(x=x, y=y, line_color=self.fretboardTheme.fretboardDesign.stringsColor,
                          line_alpha=self.fretboardTheme.fretboardDesign.stringsOpacity, line_width = self.fretboardTheme.fretboardDesign.fretThinkness)

        distanceBetweenFrets = (self.fretboardTheme.fretboardRange.numOfFrets+1) * \
            self.fretboardTheme.fretboardDesign.distanceBetweenFrets

        fx = [0, self.fretboardTheme.fretboardDesign.distanceBetweenStrings*(self.fretboardTheme.tuning.numOfStrings-1)]
        fy = [0, 0]
        self.fretboardFig.fig.line(x=fx, y=fy, line_color=self.fretboardTheme.fretboardDesign.fretColor,
                      line_alpha=self.fretboardTheme.fretboardDesign.fretOpacity , line_width = self.fretboardTheme.fretboardDesign.stringThinkness)

        # draw frets (horizontal line)
        fretlength = self.fretboardTheme.fretboardRange.fretFrom-1

        for j in range(self.fretboardTheme.fretboardRange.fretFrom, self.fretboardTheme.fretboardRange.fretTo+1):
            fx = [0, self.fretboardTheme.fretboardDesign.distanceBetweenStrings*(self.fretboardTheme.tuning.numOfStrings-1)]
            fy = [distanceBetweenFrets, distanceBetweenFrets]

            if (j != self.fretboardTheme.fretboardRange.fretFrom):
                self.drawFretLabel(distanceBetweenFrets, fretlength)

            fretlength += 1
            distanceBetweenFrets -= self.fretboardTheme.fretboardDesign.distanceBetweenFrets
            self.fretboardFig.fig.line(x=fx, y=fy, line_color=self.fretboardTheme.fretboardDesign.fretColor,
                          line_alpha=self.fretboardTheme.fretboardDesign.fretOpacity, line_width = self.fretboardTheme.fretboardDesign.fretThinkness,)

        self.drawFretLabel(distanceBetweenFrets, fretlength)

        self.drawInlay()                

        self.fretboardFig.fig.x_range=Range1d(0-self.fretboardTheme.fretboardDesign.distanceBetweenStrings, self.fretboardTheme.fretboardDesign.distanceBetweenStrings*self.fretboardTheme.fretboardRange.numOfStrings,bounds='auto')
        self.fretboardFig.fig.toolbar_location =  self.fretboardTheme.fretboardDesign.toolBar
        
        self.fretboardFig.fig.background_fill_color = self.fretboardTheme.fretboardDesign.backgroundColor

    def drawInlay(self):
        if (self.fretboardTheme.orientation.orientation == "h"):
            # draw 3,5,7,9 marker
            if (self.fretboardTheme.fretboardRange.fretFrom <= 3 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret3 = self.fretboardFig.fig.circle(x=(3-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.fretboardTheme.tuning.numOfStrings-1) *
                                              self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 5 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret5 = self.fretboardFig.fig.circle(x=(5-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.fretboardTheme.tuning.numOfStrings-1) *
                                              self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 7 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret7 = self.fretboardFig.fig.circle(x=(7-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.fretboardTheme.tuning.numOfStrings-1) *
                                              self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 9 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret9 = self.fretboardFig.fig.circle(x=(9-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.fretboardTheme.tuning.numOfStrings-1) *
                                              self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 12 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret12_1 = self.fretboardFig.fig.circle(x=(12-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                                 y=(self.fretboardTheme.tuning.numOfStrings) *
                                                 self.fretboardTheme.fretboardDesign.distanceBetweenStrings/4,
                                                 radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                                 fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                                 fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                                 line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
                markerFret12_2 = self.fretboardFig.fig.circle(x=(12-self.fretboardTheme.fretboardRange.fretFrom+1)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                                 y=(self.fretboardTheme.tuning.numOfStrings) *
                                                 self.fretboardTheme.fretboardDesign.distanceBetweenStrings/1.75,
                                                 radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                                                 fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                                 fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                                 line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)

        else:
            if (self.fretboardTheme.fretboardRange.fretFrom <= 3 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret3 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings-1)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                  3-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 5 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret5 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings-1)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                  5-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 7 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret7 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings-1)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                  7-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 9 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret9 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings-1)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                  9-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                              fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                              fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
            if (self.fretboardTheme.fretboardRange.fretFrom <= 12 <= self.fretboardTheme.fretboardRange.fretTo):
                markerFret12_1 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings*2/3-self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                                 y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                     12-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                                 radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                                 fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                                 fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                                 line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
                markerFret12_2 = self.fretboardFig.fig.circle(x=(self.fretboardTheme.tuning.numOfStrings)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings/3-self.fretboardTheme.fretboardDesign.distanceBetweenStrings/2,
                                                 y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(self.fretboardTheme.fretboardRange.numOfFrets) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets*(
                                                     12-self.fretboardTheme.fretboardRange.fretFrom-1) - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                                                 radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                                 fill_color=self.fretboardTheme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                                                 fill_alpha=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFill,
                                                 line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor)
        # self.notes.append(self.fig.add_glyph(circleNote))

    def showFretboard(self):
        
        curdoc().add_root(self.layout)


    def clearFretboard(self):
        notesCopy = list(self.notes)

        for note in notesCopy:
            self.fretboardFig.fig.renderers.remove(note)
            self.notes.remove(note)
        
        for label in self.labels:
            label.text = ""
        
        self.labels = []
        self.currentNotesPositionOnFretboard = []

    def removeFigure(self):
        self.currentNotesPositionOnFretboard = []
        self.layout.children.remove(self.fretboardFig.fig)
        
    def updateFretboard(self, notes):
        self.clearFretboard()
        self.addNotesAllString(notes)

    # user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self, notes):
        notes = [(x.strip()) for x in notes.split(',')]
        midiNotes = []
        strings = []
        frets = []
        len(notes)
        self.pitchCollection.setAllEmpty()
        for i in range(len(notes)):
            self.pitchCollection.appendPitchesEmpty("")
            strings.append(i)
            frets.append(notes[i])
            midiNotes.append(str(Functions.fretToMidi(self.fretboardTheme.tuning.midiTuning[i],notes[i])))
        self.pitchCollection.setStrings(strings)
        self.pitchCollection.setFrets(frets)
        notesWithOctaveName = Functions.midisToNoteNameWithOctaves(midiNotes)
        print(notesWithOctaveName)
        self.pitchCollection.setPitchWithOctave(notesWithOctaveName)
        
        
        if (len(notes) == self.fretboardTheme.tuning.numOfStrings):
            for i in range(0, self.fretboardTheme.tuning.numOfStrings):
                self.pitchCollection.setPitchesIndex(i)
                self.addNote(i, notes[i])
        else:
            print("ERROR, WRONG FORMAT.")

    # -1 = x
    def addNote(self, string, fret):
        note = ""
        
        textValue = str(self.pitchCollection.getArrayTypeNowAt(self.pitchCollection.getCurrentPitchesIndex()))
        textValue = textValue.replace("-","b")

        notePos = NotePositionsOnCurrentFretboard(string, fret)
        self.appendCurrentNotesOnFretboard(notePos)

        if(fret=="" or fret==''):
            return None

        elif isinstance(fret, str) and fret.lower() == 'x':
            print("")

        elif(int(fret) > self.fretboardTheme.fretboardRange.fretTo or int(fret) < self.fretboardTheme.fretboardRange.fretFrom and (int(fret) != 0)):
            print("fret",fret,"must be within the fretboard range")
            return None

        elif (fret != "0"):
            fret = int(fret)-self.fretboardTheme.fretboardRange.fretFrom+1

        if (self.fretboardTheme.orientation.orientation == "h"):  # edit later
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(fret)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius*2.2,
                              fill_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFaceColor,
                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor,
                              fill_alpha = self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(fret)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/1.5,
                                        text=textValue, text_align='center',text_font_size=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextFont(),text_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextColor())
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
                
            elif (isinstance(fret, str) and fret.lower() == 'x'):
                fret = 0
                xPos = (fret)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2
                yPos = (string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings+self.fretboardTheme.fretboardDesign.distanceBetweenStrings/6
                symbolSize = self.fretboardTheme.fretboardDesign.distanceBetweenStrings/8
                
                xCor = [xPos - symbolSize*4, xPos + symbolSize]
                yCor = [yPos - symbolSize, yPos + symbolSize]
                source = ColumnDataSource(data=dict(x=xCor, y=yCor))

                lineOne = Line(x="x",
                               y="y", line_width=3, line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteFaceColor())
                yCorFlip = yCor[::-1]
                lineTwo = Line(x="x",
                               y="yFlip", line_width=3, line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteFaceColor())

                source.data["yFlip"] = yCorFlip

                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineOne))
                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineTwo))
                    
                
            else:
                fret = int(fret)
                note = Circle(x=(fret)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius*2.2,
                              fill_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFaceColor,
                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor,
                              fill_alpha = self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(fret)*self.fretboardTheme.fretboardDesign.distanceBetweenFrets-self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/1.5,
                                        text=textValue, text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextFont(),text_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextColor())
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
        else:
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets *
                              (self.fretboardTheme.fretboardRange.numOfFrets+1) +
                              self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteRadius()*6,
                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                              fill_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFaceColor,
                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor,
                              fill_alpha = self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteOpactiy,
                              name="circleNote"
                              )
                label = Label(x=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets *
                              (self.fretboardTheme.fretboardRange.numOfFrets+2) - (fret) *
                              self.fretboardTheme.fretboardDesign.distanceBetweenFrets - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/1.7-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                        text=textValue, text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextFont(),text_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextColor())
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)

            elif (isinstance(fret, str) and fret.lower() == 'x'):
                fret = 0
                xPos = (string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings
                yPos = self.fretboardTheme.fretboardDesign.distanceBetweenFrets * \
                    (self.fretboardTheme.fretboardRange.numOfFrets+1)+self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteRadius()*6
                symbolSize = self.fretboardTheme.fretboardDesign.distanceBetweenStrings/8

                xCor = [xPos - symbolSize, xPos + symbolSize]
                yCor = [yPos - symbolSize*4, yPos + symbolSize]
                source = ColumnDataSource(data=dict(x=xCor, y=yCor))

                lineOne = Line(x="x",
                               y="y", line_width=3, line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteFaceColor())
                yCorFlip = yCor[::-1]
                lineTwo = Line(x="x",
                               y="yFlip", line_width=3, line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteFaceColor())

                source.data["yFlip"] = yCorFlip

                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineOne))
                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineTwo))
                
                label = Label(x=xPos,
                              y=yPos,
                                        text="", text_align='center', text_font_size='10pt')
                self.labels.append(label)

                self.fretboardFig.fig.add_layout(label)

            else:
                fret = int(fret)
                note = Circle(x=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets *
                              (self.fretboardTheme.fretboardRange.numOfFrets+2) - (fret) *
                              self.fretboardTheme.fretboardDesign.distanceBetweenFrets - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/2,
                              radius=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius,
                              fill_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteFaceColor,
                              line_width=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeWidth,
                              line_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteEdgeColor,
                              fill_alpha = self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(string)*self.fretboardTheme.fretboardDesign.distanceBetweenStrings,
                              y=self.fretboardTheme.fretboardDesign.distanceBetweenFrets *
                              (self.fretboardTheme.fretboardRange.numOfFrets+2) - (fret) *
                              self.fretboardTheme.fretboardDesign.distanceBetweenFrets - self.fretboardTheme.fretboardDesign.distanceBetweenFrets/1.7-self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().noteRadius/2,
                                        text=textValue, text_align='center', text_font_size=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextFont(),text_color=self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getNoteTextColor())
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
                
        if (note != ""):
            self.notes.append(self.fretboardFig.fig.add_glyph(note))
        
    #drawing fretboard getter n setters
    def getTheme(self):
        return self.fretboardTheme
    
    def setTheme(self, theme):
        self.fretboardTheme = theme

    def getCurrentNotesOnFretboard(self):
        return self.currentNotesPositionOnFretboard

    def appendCurrentNotesOnFretboard(self, value):
        self.currentNotesPositionOnFretboard.append(value)

    def setCurrentNotesOnFretboard(self, notes):
        self.currentNotesPositionOnFretboard = notes
    
    #adding scale, arpeggio, interval, chord
    
    #rootNote = "c", type="major"
    def addScale(self, rootNote, type, intervalsDegrees=None):
        
        if type.lower() == 'major' or type.lower() == 'ionian':
            scaleObj = scale.MajorScale(rootNote)
        elif type.lower() == 'minor' or type.lower() == 'aeolian':
            scaleObj = scale.MinorScale(rootNote)
        elif type.lower() == 'harmonic minor':
            scaleObj = scale.HarmonicMinorScale(rootNote)
        elif type.lower() == 'melodic minor':
            scaleObj = scale.MelodicMinorScale(rootNote)
        elif type.lower() == 'dorian':
            scaleObj = scale.DorianScale(rootNote)
        elif type.lower() == 'phrygian':
            scaleObj = scale.PhrygianScale(rootNote)
        elif type.lower() == 'lydian':
            scaleObj = scale.LydianScale(rootNote)
        elif type.lower() == 'mixolydian':
            scaleObj = scale.MixolydianScale(rootNote)
        elif type.lower() == 'locrian':
            scaleObj = scale.LocrianScale(rootNote)
        elif type.lower() == 'blues':
            scaleObj = scale.BluesScale(rootNote)
        elif type.lower() == 'whole tone':
            scaleObj = scale.WholeToneScale(rootNote)
        elif type.lower() == 'chromatic':
            scaleObj = scale.ChromaticScale(rootNote)
        elif type.lower() == 'hypodorian':
            scaleObj = scale.HypodorianScale(rootNote)
        elif type.lower() == 'hypophrygian':
            scaleObj = scale.HypophrygianScale(rootNote)
        elif type.lower() == 'hypolydian':
            scaleObj = scale.HypolydianScale(rootNote)
        elif type.lower() == 'hypomixolydian':
            scaleObj = scale.HypomixolydianScale(rootNote)
        elif type.lower() == 'hypoaeolian':
            scaleObj = scale.HypoaeolianScale(rootNote)
        elif type.lower() == 'octatonic':
            scaleObj = scale.OctatonicScale(rootNote)
        elif type.lower() == 'octaverepeating':
            scaleObj = scale.OctaveRepeatingScale(rootNote)
        elif type.lower() == 'cyclical':
            scaleObj = scale.CyclicalScale(rootNote)
        elif type.lower() == 'ragasawari':
            scaleObj = scale.RagAsawari(rootNote)
        elif type.lower() == 'ragmarwa':
            scaleObj = scale.RagMarwa(rootNote)
        elif type.lower() == 'weightedhexatonicblues':
            scaleObj = scale.WeightedHexatonicBlues(rootNote)
        elif type.lower() == "minorpentatonic":
            intervals = 'P1 m3 P4 P5 m7'.split()
            intervals.append("P1")
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True

        elif type.lower() == "majorpentatonic":
            intervals = 'P1 M2 M3 P5 M6'.split()
            intervals.append("P1")
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True
        else:
            # assume user-defined scale
            if intervalsDegrees is None:
                raise ValueError("Intervals must be provided for a user-defined scale.")
            
            intervals = intervalsDegrees.split()
            intervals.append("P1")
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True
        
        pitches = scaleObj.getPitches()
        #make the arrays or pitches
        self.addPitchesToFretboard(pitches, scaleObj)

    def addPitchesToFretboard(self, pitches, scaleObj):
        self.arraysForPitchCollection(pitches, scaleObj)
        for i in range(len(self.pitchCollection.getArrayTypeNow())):
            self.pitchCollection.setPitchesIndex(i)
            self.addNote(self.pitchCollection.getStringsAt(i),self.pitchCollection.getFretsAt(i))
            

    def arraysForPitchCollection(self, pitches, scaleObj):
        #Add to Arrays for different options
        self.pitchCollection.setPitchesNames([])
        self.pitchCollection.setPitchWithOctave([])
        self.pitchCollection.setPitchesScaleDegrees([])
        self.pitchCollection.setPitchesEmpty([])

        #add to fretboard and octave name string
        for pitchIndex in range(len(pitches)):
            fretNum = []
            stringNum = []

            #get each note on each string n their fret
            fretNum, stringNum= self.convertPitchesToFretsStringsNum(pitches[pitchIndex])    
            
            #depending on how many octave to display 
            quotient, remainder = divmod(self.fretboardTheme.fretboardRange.fretTo+1, 12)
            for octavesFret in range(quotient):
                for index in range(self.fretboardTheme.tuning.numOfStrings):
                    newFret = fretNum[index]+12  
                    fretNum.append(newFret)
                    stringNum.append(index)
            #check to see if between fret range 
            for i in range(len(fretNum)):
                if (self.fretboardTheme.fretboardRange.fretFrom > fretNum[i] or fretNum[i] >= self.fretboardTheme.fretboardRange.fretTo+1) and not((self.fretboardTheme.fretboardRange.fretFrom == 1) and (fretNum[i] == 0)):                    
                    fretNum[i]=""
            # add the notes to the  octave array
            for i in range(len(fretNum)):
                self.pitchCollection.appendFrets(fretNum[i])
                self.pitchCollection.appendStrings(stringNum[i])
                self.pitchCollection.appendPitchesName(pitches[pitchIndex].name)
                self.pitchCollection.appendPitchesEmpty("")


                if(fretNum[i] != ""):
                    midi = Functions.fretToMidi(self.fretboardTheme.tuning.midiTuning[stringNum[i]],fretNum[i])
                    pitchWithOctave = Functions.midiToNoteNameWithOctave(midi)
                else:
                    pitchWithOctave = ""
        
                self.pitchCollection.appendPitchWithOctave(pitchWithOctave)

                #scale degree
                if(self.scaleCustom == True):
                    self.pitchCollection.appendPitchesScaleDegree(self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().getScaleDegrees()[pitchIndex])
        
                else:
                #for nonConcrete scale
                    if(pitches[pitchIndex].alter == -1.0):
                        self.pitchCollection.appendPitchesScaleDegree("b"+str(scaleObj.getScaleDegreeFromPitch(pitches[pitchIndex])))
                    elif(pitches[pitchIndex].alter == 1.0):
                        self.pitchCollection.appendPitchesScaleDegree("#"+str(scaleObj.getScaleDegreeFromPitch(pitches[pitchIndex])))
                    else:
                        self.pitchCollection.appendPitchesScaleDegree(scaleObj.getScaleDegreeFromPitch(pitches[pitchIndex]))

                
            print("NOTE FINSIH")

    #MAYBE PUT somehwere else
    #given pitch, give me all of the places it is located in fret, string
    def convertPitchesToFretsStringsNum(self, pitch):
        #tuning = TabSequence.getStringMidi()#util later
        frets = []
        strings = []
        
        midiPitch=pitch.midi

        for stringIndex, stringPitch in enumerate(self.fretboardTheme.tuning.midiTuning):
            fret = (midiPitch - stringPitch) % 12

            if fret >= (self.fretboardTheme.fretboardRange.fretFrom - 1) and fret <= self.fretboardTheme.fretboardRange.fretTo or fret == 0:
                frets.append(fret)
                strings.append(stringIndex)

        return frets, strings
    
   
    def getArpeggioPitches(self, rootNote, type="", chordPitches="", bass=""):
            if type != "":
                chordObj = harmony.ChordSymbol(root=rootNote, bass=bass, kind=type)
                chordPitches = chordObj.pitches
                intervals = []
                for i in range(len(chordPitches)):
                    intervalObj = interval.Interval(chordPitches[0],chordPitches[i])
                    intervals.append(intervalObj.directedName)
            else:
                intervals = chordPitches.split()
            type = type.lower()    
            intervals.append("P1")
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.fretboardTheme.fretboardDesign.getCurrentNoteTypeValue().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True
            pitches = scaleObj.getPitches()

            return pitches, scaleObj

    def addArpeggio(self, rootNote, type="", chordPitches="", bass=""):
            pitches, scaleObj = self.getArpeggioPitches(rootNote,type,chordPitches,bass)              

            self.addPitchesToFretboard(pitches, scaleObj)
    
    def getIntervalPitches(self, rootNote, intervalName=""):
        rootNotePitch = m21Pitch.Pitch(rootNote+"2")
        scalePitches = [rootNotePitch.transpose(interval.Interval(intervalName))] 
        scalePitches.insert(0,rootNotePitch)
        scaleObj = scale.ConcreteScale(rootNote,scalePitches)
        pitches = scaleObj.getPitches()
        
        return pitches, scaleObj
    
    def addInterval(self, rootNote, intervalName=""):
            pitches, scaleObj = self.getIntervalPitches(rootNote, intervalName)

            self.addPitchesToFretboard(pitches, scaleObj)


    #there is just so many different ways to think about chord and construct them, a chord works as long as it has the notes of the chord like inversions
    #only work in standard tuning as of now
    #caged dont work well with dim7,aug7 chords, lotta time also just take out 5
    #put in one that is more easier to press
    # Very basic people start with caged
    def addCagedPosChord(self, rootNote, type="", caged="c"):
        chordType = type.lower()
        Functions.checkChordType(chordType)

        Functions.ifInDict(caged, Functions.cagedShapes)

        
        processedShape = Functions.processCAGEDShape(caged.upper(), rootNote, chordType)

        note = processedShape["note"][chordType]
        pos = processedShape["position"][chordType]
        sd = processedShape["scaleDegree"][chordType]

        self.pitchCollection.setFrets(pos)
        self.pitchCollection.setPitchesNames(note)
        self.pitchCollection.setPitchesScaleDegrees(sd)
        self.pitchCollection.setStrings([0,1,2,3,4,5])

        for i in range(len(note)):
            self.pitchCollection.setPitchesIndex(i)
            self.addNote(self.pitchCollection.getStringsAt(i),self.pitchCollection.getFretsAt(i))

    def addDropChord(self, rootNote, type="", drop="Drop2", pos="1", string="6"):
        chordType = type.lower()
        drop = drop.upper()

        Functions.checkChordType(chordType,True)
        Functions.ifInDict(drop, Functions.DROPShapes)

        processedShape = Functions.processDropShape(drop.upper(), rootNote, chordType, string,pos)

        note = processedShape["note"][chordType]
        pos = processedShape["position"][chordType]
        sd = processedShape["scaleDegree"][chordType]

        self.pitchCollection.setFrets(pos)
        self.pitchCollection.setPitchesNames(note)
        self.pitchCollection.setPitchesScaleDegrees(sd)
        self.pitchCollection.setStrings([0,1,2,3,4,5])

        for i in range(len(note)):
            self.pitchCollection.setPitchesIndex(i)
            self.addNote(self.pitchCollection.getStringsAt(i),self.pitchCollection.getFretsAt(i))

    def addCustomShape(self, customShape, name):
        customShape = customShape.getShape(name)
        self.pitchCollection.setFrets(customShape['note'])
        self.pitchCollection.setPitchesNames(customShape['position'])
        self.pitchCollection.setPitchesScaleDegrees(customShape['scaleDegree'])
        self.pitchCollection.setStrings([0,1,2,3,4,5])

        for i in range(len(customShape['note'])):
            self.pitchCollection.setPitchesIndex(i)
            self.addNote(self.pitchCollection.getStringsAt(i),self.pitchCollection.getFretsAt(i))

    def addOctave(self, rootNote):
        self.addArpeggio(rootNote,"","P1")
    
    def getPitchCollection(self):
        return self.pitchCollection
    
    def setPitchCollection(self, pitchCollection):
        self.pitchCollection = pitchCollection

    #Embedding
    def generateStandaloneHtml(self, name="standalone.html"):
        html = file_html(self.getFretboardFig().fig, CDN, "my plot")

        self.pathInfo.name = name
        # Write the HTML to a file
        with open(self.pathInfo.getPathWithName(), "w") as file:
            file.write(html)
    
    def genereateScriptAndDiv(self, scriptName="script.html", divName="div.html"):
        script, div = components(self.fretboardFig.fig)

        self.pathInfo.name = scriptName
        # Write to a file
        with open(self.pathInfo.getPathWithName(), "w") as file:
            file.write(script)
        
        self.pathInfo.name = divName
        with open(self.pathInfo.getPathWithName(), "w") as file:
            file.write(div)

    def generateWithServerHtml(self, name="withServer.html"):
        script = server_document("http://localhost:5006/generalTest")
        
        self.pathInfo.name = name
        with open(self.pathInfo.getPathWithName(), "w") as file:
            file.write(script)

