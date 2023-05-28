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
from seeFretboard.NotePosition import NotePosition
from seeFretboard.PathInfo import EmbedPathInfo
from seeFretboard.Utilities import Constants

from tqdm import tqdm

from music21 import scale, interval, harmony, key
from music21 import pitch as m21Pitch
#manager/master kinda
class SeeFretboard():
    
    # default values
    #fret 0 include open strings
    def __init__(self, orientation = "h",fretFrom=1, fretTo=12, string=6, showTuning=True, **kwargs):
        # styleing/theme
        self.theme = FretboardTheme(theme="light", orientation=orientation, 
                                    fretFrom =fretFrom, fretTo=fretTo, string=string,
                                    showTuning=showTuning, **kwargs)

        # notes circle
        self.currentNotesPositionOnFretboard = [] #NotePosition
        self.notes = [] #glyph of the current notes more for removeable purposes
        self.labels = []
        self.noteTypes = {
            'prediction': CircleNote(), #default using that
            'groundTruth': CircleNote(noteFaceColor="red"),
        }
        self.noteType = "prediction"
        
        # figure attribute
        self.fretboardFig = FretboardFigure(self.getCurrentNoteType(), self.theme, orientation)
        
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
            value="'x',0,2,2,0,0", title="Enter Notes Fret:")
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
        self.updateFretboard(self.inputChordInput.value)

    # fretboard relate
    def drawTuningLabel(self, distanceStrings, i):
        if (self.theme.orientation.orientation == "h"):
            stringLabel = Label(x=-1, y=distanceStrings-self.theme.fretboardDesign.distanceBetweenStrings,
                                 text=self.theme.tuning.letterTuning[i], text_align='center', text_font_size='10pt')
        else:
            stringLabel = Label(x=distanceStrings, y=self.theme.fretboardDesign.distanceBetweenFrets*(
                                self.theme.fretboardRange.numOfFrets+1), text=self.theme.tuning.letterTuning[i+1], text_align='center', text_font_size='10pt')

        stringLabel.visible = self.theme.fretboardDesign.showTuning
        
        self.fretboardFig.stringLabel = stringLabel
        self.fretboardFig.addStringLabelLayout()

        self.tuningLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            stringLabel=stringLabel), code="""stringLabel.visible = !stringLabel.visible"""))

    def drawFretLabel(self, distanceBetweenFrets, j):
        if (self.theme.orientation.orientation == "h"):
            fretLabel = Label(x=distanceBetweenFrets+self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                               y=-self.getCurrentNoteType().noteRadius*2.5, text=str(j+1), text_align='center', text_font_size='10pt')
        else:
            fretLabel = Label(x=-self.getCurrentNoteType().noteRadius*2.5, y=distanceBetweenFrets+self.theme.fretboardDesign.distanceBetweenFrets -
                               self.theme.fretboardDesign.distanceBetweenFrets/2, text=str(j), text_align='center', text_font_size='10pt')

        fretLabel.visible = self.theme.fretboardDesign.showFretboardNumber
        
        self.fretboardFig.fretLabel = fretLabel
        self.fretboardFig.addFretLabelLayout()

        self.fretLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            fretLabel=fretLabel), code="""fretLabel.visible = !fretLabel.visible"""))

    def toggleFretboardDirection(self):
        notesPosOnFretboard = self.getCurrentNotesOnFretboard()
        pitchCollectionOnFretboard = self.getPitchCollection()

        self.removeFigure()

        if(self.theme.orientation.orientation in Constants.HORIZONTAL):
            self.setFretboardFig(FretboardFigure(self.getCurrentNoteType(), self.getTheme(), "v"))
            self.getTheme().orientation.orientation = "v"
            self.drawVerticalFretboard()

        else:
            self.setFretboardFig(FretboardFigure(self.getCurrentNoteType(), self.getTheme(), "h"))
            self.getTheme().orientation.orientation = "h"
            self.drawHorizontalFretboard()
            
        self.layout.children.insert(0,self.fretboardFig.fig)

        self.setPitchCollection(pitchCollectionOnFretboard)
        # Add the progress bar
        with tqdm(total=len(notesPosOnFretboard)) as pbar:
            for notePos in notesPosOnFretboard:
                self.addNote(notePos.getString(), notePos.getFret(), False)
                pbar.update(1)  # Update the progress bar
        
        print("Toggle Fretboard Success")
        
    def drawFretboard(self, orientation):
        if(orientation.lower() in Constants.HORIZONTAL):
            self.theme.orientation.orientation = "h"
            self.fretboardFig.switchOrientation("h")
            self.drawHorizontalFretboard()
        elif(orientation.lower() in Constants.VERTICAL):
            self.theme.orientation.orientation = "v"
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
        for i in range(0, self.theme.tuning.numOfStrings):
            strings["x"].append([0, self.theme.fretboardDesign.distanceBetweenFrets * (self.theme.fretboardRange.fretTo - self.theme.fretboardRange.fretFrom + 1)])
            strings["y"].append([distanceStrings, distanceStrings])

            self.drawTuningLabel(distanceStrings + self.theme.fretboardDesign.distanceBetweenStrings, i)

            distanceStrings += self.theme.fretboardDesign.distanceBetweenStrings
        self.stringSource = ColumnDataSource(data=strings)
        self.fretboardFig.fig.multi_line(xs="x", ys="y", line_color=self.theme.fretboardDesign.stringsColor,
                                   line_alpha=self.theme.fretboardDesign.stringsOpacity, source=self.stringSource)

        distanceBetweenFrets = 0
    
        # draw frets (vertical line)
        for j in range(self.theme.fretboardRange.fretFrom - 1, self.theme.fretboardRange.fretTo + 1):
            frets["x"].append([distanceBetweenFrets, distanceBetweenFrets])
            frets["y"].append([0, self.theme.fretboardDesign.distanceBetweenStrings * (self.theme.tuning.numOfStrings - 1)])

            if j != self.theme.fretboardRange.fretTo:
                self.drawFretLabel(distanceBetweenFrets, j)

            distanceBetweenFrets += self.theme.fretboardDesign.distanceBetweenFrets
            print(frets)

        self.fretSource = ColumnDataSource(data=frets)
        self.fretboardFig.fig.multi_line(xs="x", ys="y", line_color=self.theme.fretboardDesign.fretColor,
                                        line_alpha=self.theme.fretboardDesign.fretOpacity, source=self.fretSource)
        self.drawInlay()

        self.fretboardFig.fig.y_range=Range1d(0-self.theme.fretboardDesign.distanceBetweenStrings, self.theme.fretboardDesign.distanceBetweenStrings*self.theme.fretboardRange.numOfStrings,bounds='auto')
        # self.fretboardFig.fig.axis.visible = False
        # self.fretboardFig.fig.xgrid.visible = False
        # self.fretboardFig.fig.ygrid.visible = False

        self.drawInlay()
        self.fretboardFig.fig.y_range=Range1d(0-self.theme.fretboardDesign.distanceBetweenStrings, self.theme.fretboardDesign.distanceBetweenStrings*self.theme.fretboardRange.numOfStrings,bounds='auto')
        self.fretboardFig.fig.axis.visible = self.theme.fretboardDesign.toolBar
        # self.fretboardFig.fig.xgrid.visible = False
        # self.fretboardFig.fig.ygrid.visible = False

    def drawVerticalFretboard(self):
        x = [0, 0]
        y = [0, self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets+1)]

        self.drawTuningLabel(0, -1)

        self.fretboardFig.fig.line(x=x, y=y, line_color=self.theme.fretboardDesign.stringsColor,
                      line_alpha=self.theme.fretboardDesign.stringsOpacity)

        distanceStrings = self.theme.fretboardDesign.distanceBetweenStrings
        # draw strings (vertical line)
        for i in range(0, self.theme.tuning.numOfStrings-1):
            x = [distanceStrings, distanceStrings]
            y = [0, self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets+1)]

            self.drawTuningLabel(distanceStrings, i)

            distanceStrings += self.theme.fretboardDesign.distanceBetweenStrings
            self.fretboardFig.fig.line(x=x, y=y, line_color=self.theme.fretboardDesign.stringsColor,
                          line_alpha=self.theme.fretboardDesign.stringsOpacity)

        distanceBetweenFrets = (self.theme.fretboardRange.numOfFrets+1) * \
            self.theme.fretboardDesign.distanceBetweenFrets

        fx = [0, self.theme.fretboardDesign.distanceBetweenStrings*(self.theme.tuning.numOfStrings-1)]
        fy = [0, 0]
        self.fretboardFig.fig.line(x=fx, y=fy, line_color=self.theme.fretboardDesign.fretColor,
                      line_alpha=self.theme.fretboardDesign.fretOpacity)

        # draw frets (horizontal line)
        fretlength = self.theme.fretboardRange.fretFrom-1

        for j in range(self.theme.fretboardRange.fretFrom, self.theme.fretboardRange.fretTo+1):
            fx = [0, self.theme.fretboardDesign.distanceBetweenStrings*(self.theme.tuning.numOfStrings-1)]
            fy = [distanceBetweenFrets, distanceBetweenFrets]

            if (j != self.theme.fretboardRange.fretFrom):
                self.drawFretLabel(distanceBetweenFrets, fretlength)

            fretlength += 1
            distanceBetweenFrets -= self.theme.fretboardDesign.distanceBetweenFrets
            self.fretboardFig.fig.line(x=fx, y=fy, line_color=self.theme.fretboardDesign.fretColor,
                          line_alpha=self.theme.fretboardDesign.fretOpacity)

        self.drawFretLabel(distanceBetweenFrets, fretlength)

        self.drawInlay()                

        self.fretboardFig.fig.x_range=Range1d(0-self.theme.fretboardDesign.distanceBetweenStrings, self.theme.fretboardDesign.distanceBetweenStrings*self.theme.fretboardRange.numOfStrings,bounds='auto')
        self.fretboardFig.fig.axis.visible = self.theme.fretboardDesign.toolBar
        self.fretboardFig.fig.xgrid.visible = False
        self.fretboardFig.fig.ygrid.visible = False

    def drawInlay(self):
        # I think I still need to work more on the math for layout on 12th fret
        # vertical note radius is /2, should fix or check up on it later
        if (self.theme.orientation.orientation == "h"):
            # draw 3,5,7,9 marker
            if (self.theme.fretboardRange.fretFrom <= 3 <= self.theme.fretboardRange.fretTo):
                markerFret3 = self.fretboardFig.fig.circle(x=(3-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.theme.tuning.numOfStrings-1) *
                                              self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.getCurrentNoteType().noteRadius,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 5 <= self.theme.fretboardRange.fretTo):
                markerFret5 = self.fretboardFig.fig.circle(x=(5-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.theme.tuning.numOfStrings-1) *
                                              self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.getCurrentNoteType().noteRadius,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 7 <= self.theme.fretboardRange.fretTo):
                markerFret7 = self.fretboardFig.fig.circle(x=(7-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.theme.tuning.numOfStrings-1) *
                                              self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.getCurrentNoteType().noteRadius,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 9 <= self.theme.fretboardRange.fretTo):
                markerFret9 = self.fretboardFig.fig.circle(x=(9-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              y=(self.theme.tuning.numOfStrings-1) *
                                              self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              radius=self.getCurrentNoteType().noteRadius,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 12 <= self.theme.fretboardRange.fretTo):
                markerFret12_1 = self.fretboardFig.fig.circle(x=(12-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                                 y=(self.theme.tuning.numOfStrings) *
                                                 self.theme.fretboardDesign.distanceBetweenStrings/4,
                                                 radius=self.getCurrentNoteType().noteRadius,
                                                 fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.getCurrentNoteType().noteEdgeWidth,
                                                 fill_alpha=self.getCurrentNoteType().noteFill,
                                                 line_color=self.getCurrentNoteType().noteEdgeColor)
                markerFret12_2 = self.fretboardFig.fig.circle(x=(12-self.theme.fretboardRange.fretFrom+1)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                                                 y=(self.theme.tuning.numOfStrings) *
                                                 self.theme.fretboardDesign.distanceBetweenStrings/1.75,
                                                 radius=self.getCurrentNoteType().noteRadius,
                                                 fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.getCurrentNoteType().noteEdgeWidth,
                                                 fill_alpha=self.getCurrentNoteType().noteFill,
                                                 line_color=self.getCurrentNoteType().noteEdgeColor)

        else:
            if (self.theme.fretboardRange.fretFrom <= 3 <= self.theme.fretboardRange.fretTo):
                markerFret3 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings-1)*self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                  3-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.getCurrentNoteType().noteRadius/2,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 5 <= self.theme.fretboardRange.fretTo):
                markerFret5 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings-1)*self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                  5-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.getCurrentNoteType().noteRadius/2,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 7 <= self.theme.fretboardRange.fretTo):
                markerFret7 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings-1)*self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                  7-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.getCurrentNoteType().noteRadius/2,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 9 <= self.theme.fretboardRange.fretTo):
                markerFret9 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings-1)*self.theme.fretboardDesign.distanceBetweenStrings/2,
                                              y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                  9-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                              radius=self.getCurrentNoteType().noteRadius/2,
                                              fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                                              fill_alpha=self.getCurrentNoteType().noteFill,
                                              line_color=self.getCurrentNoteType().noteEdgeColor)
            if (self.theme.fretboardRange.fretFrom <= 12 <= self.theme.fretboardRange.fretTo):
                markerFret12_1 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings)*self.theme.fretboardDesign.distanceBetweenStrings*2/3-self.theme.fretboardDesign.distanceBetweenStrings/2,
                                                 y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                     12-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                                 radius=self.getCurrentNoteType().noteRadius/2,
                                                 fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.getCurrentNoteType().noteEdgeWidth,
                                                 fill_alpha=self.getCurrentNoteType().noteFill,
                                                 line_color=self.getCurrentNoteType().noteEdgeColor)
                markerFret12_2 = self.fretboardFig.fig.circle(x=(self.theme.tuning.numOfStrings)*self.theme.fretboardDesign.distanceBetweenStrings/3-self.theme.fretboardDesign.distanceBetweenStrings/2,
                                                 y=self.theme.fretboardDesign.distanceBetweenFrets*(self.theme.fretboardRange.numOfFrets) - self.theme.fretboardDesign.distanceBetweenFrets*(
                                                     12-self.theme.fretboardRange.fretFrom-1) - self.theme.fretboardDesign.distanceBetweenFrets/2,
                                                 radius=self.getCurrentNoteType().noteRadius/2,
                                                 fill_color=self.theme.fretboardDesign.fretboardMarkerColor,
                                                 line_width=self.getCurrentNoteType().noteEdgeWidth,
                                                 fill_alpha=self.getCurrentNoteType().noteFill,
                                                 line_color=self.getCurrentNoteType().noteEdgeColor)
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

    def removeFigure(self):
        self.layout.children.remove(self.fretboardFig.fig)
        
    def updateFretboard(self, notes):
        self.clearFretboard()
        self.addNotesAllString(notes)

    # user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self, notes):
        notes = [(x.strip()) for x in notes.split(',')]
        if (len(notes) == self.theme.tuning.numOfStrings):
            for i in range(0, self.theme.tuning.numOfStrings):
                self.addNote(i, notes[i])
        else:
            print("ERROR, WRONG FORMAT.")

    # -1 = x
    def addNote(self, string, fret, appendPos=True):
        note = ""
        textValue = str(self.pitchCollection.getArrayTypeNowAt(self.pitchCollection.getCurrentPitchesIndex()))
        textValue = textValue.replace("-","b")

        if isinstance(fret, str) and fret.lower() == 'x':
            print("")
        
        elif(int(fret) > self.theme.fretboardRange.fretTo or int(fret) < self.theme.fretboardRange.fretFrom and (int(fret) != 0)):
            print("fret",fret,"must be within the fretboard range")
            return None

        elif (fret != "0"):
            fret = int(fret)-self.theme.fretboardRange.fretFrom+1

        if (self.theme.orientation.orientation == "h"):  # edit later
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(fret)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              radius=self.getCurrentNoteType().noteRadius,
                              fill_color=self.getCurrentNoteType().noteFaceColor,
                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                              line_color=self.getCurrentNoteType().noteEdgeColor,
                              fill_alpha = self.getCurrentNoteType().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(fret)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.theme.fretboardDesign.distanceBetweenStrings-self.theme.fretboardDesign.distanceBetweenStrings/12-self.getCurrentNoteType().noteRadius/1.5,
                                        text=textValue, text_align='center', text_font_size='10pt',text_color='white')
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
                
            elif (isinstance(fret, str) and fret.lower() == 'x'):
                fret = 0
                xPos = (fret)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2
                yPos = (string)*self.theme.fretboardDesign.distanceBetweenStrings+self.theme.fretboardDesign.distanceBetweenStrings/6
                symbolSize = self.theme.fretboardDesign.distanceBetweenStrings/8
                
                xCor = [xPos - symbolSize*4, xPos + symbolSize]
                yCor = [yPos - symbolSize, yPos + symbolSize]
                source = ColumnDataSource(data=dict(x=xCor, y=yCor))

                lineOne = Line(x="x",
                               y="y", line_width=3, line_color=self.getCurrentNoteType().getNoteFaceColor())
                yCorFlip = yCor[::-1]
                lineTwo = Line(x="x",
                               y="yFlip", line_width=3, line_color=self.getCurrentNoteType().getNoteFaceColor())

                source.data["yFlip"] = yCorFlip

                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineOne))
                self.notes.append(self.fretboardFig.fig.add_glyph(
                    source, lineTwo))
                
            else:
                fret = int(fret)
                note = Circle(x=(fret)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              radius=self.getCurrentNoteType().noteRadius,
                              fill_color=self.getCurrentNoteType().noteFaceColor,
                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                              line_color=self.getCurrentNoteType().noteEdgeColor,
                              fill_alpha = self.getCurrentNoteType().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(fret)*self.theme.fretboardDesign.distanceBetweenFrets-self.theme.fretboardDesign.distanceBetweenFrets/2,
                              y=(string)*self.theme.fretboardDesign.distanceBetweenStrings-self.getCurrentNoteType().noteRadius/1.5,
                                        text=textValue, text_align='center', text_font_size='10pt',text_color='white')
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
        else:
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              y=self.theme.fretboardDesign.distanceBetweenFrets *
                              (self.theme.fretboardRange.numOfFrets+1) +
                              self.getCurrentNoteType().getNoteRadius()*6,
                              radius=self.getCurrentNoteType().noteRadius,
                              fill_color=self.getCurrentNoteType().noteFaceColor,
                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                              line_color=self.getCurrentNoteType().noteEdgeColor,
                              fill_alpha = self.getCurrentNoteType().noteOpactiy,
                              name="circleNote"
                              )
                label = Label(x=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              y=self.theme.fretboardDesign.distanceBetweenFrets *
                              (self.theme.fretboardRange.numOfFrets+2) - (fret) *
                              self.theme.fretboardDesign.distanceBetweenFrets - self.theme.fretboardDesign.distanceBetweenFrets/1.7-self.getCurrentNoteType().noteRadius/2,
                                        text=textValue, text_align='center', text_font_size='10pt',text_color='white')
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)

            elif (isinstance(fret, str) and fret.lower() == 'x'):
                fret = 0
                xPos = (string)*self.theme.fretboardDesign.distanceBetweenStrings
                yPos = self.theme.fretboardDesign.distanceBetweenFrets * \
                    (self.theme.fretboardRange.numOfFrets+1)+self.getCurrentNoteType().getNoteRadius()*6
                symbolSize = self.theme.fretboardDesign.distanceBetweenStrings/8

                xCor = [xPos - symbolSize, xPos + symbolSize]
                yCor = [yPos - symbolSize*4, yPos + symbolSize]
                source = ColumnDataSource(data=dict(x=xCor, y=yCor))

                lineOne = Line(x="x",
                               y="y", line_width=3, line_color=self.getCurrentNoteType().getNoteFaceColor())
                yCorFlip = yCor[::-1]
                lineTwo = Line(x="x",
                               y="yFlip", line_width=3, line_color=self.getCurrentNoteType().getNoteFaceColor())

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
                note = Circle(x=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              y=self.theme.fretboardDesign.distanceBetweenFrets *
                              (self.theme.fretboardRange.numOfFrets+2) - (fret) *
                              self.theme.fretboardDesign.distanceBetweenFrets - self.theme.fretboardDesign.distanceBetweenFrets/2,
                              radius=self.getCurrentNoteType().noteRadius,
                              fill_color=self.getCurrentNoteType().noteFaceColor,
                              line_width=self.getCurrentNoteType().noteEdgeWidth,
                              line_color=self.getCurrentNoteType().noteEdgeColor,
                              fill_alpha = self.getCurrentNoteType().noteOpactiy,
                              name="circleNote"
                              )
                
                label = Label(x=(string)*self.theme.fretboardDesign.distanceBetweenStrings,
                              y=self.theme.fretboardDesign.distanceBetweenFrets *
                              (self.theme.fretboardRange.numOfFrets+2) - (fret) *
                              self.theme.fretboardDesign.distanceBetweenFrets - self.theme.fretboardDesign.distanceBetweenFrets/1.7-self.getCurrentNoteType().noteRadius/2,
                                        text=textValue, text_align='center', text_font_size='10pt',text_color='white')
                self.labels.append(label)
                self.fretboardFig.fig.add_layout(label)
                
        if (note != ""):
            self.notes.append(self.fretboardFig.fig.add_glyph(note))
            if(appendPos):
                notePos = NotePosition(string, fret)
                self.appendCurrentNotesOnFretboard(notePos)

    #drawing fretboard getter n setters
    def getTheme(self):
        return self.theme
    
    def setTheme(self, theme):
        self.theme = theme

    def getNoteTypes(self, key):
        return self.noteTypes.get(key)

    def setNoteTypes(self, key, value):
        self.noteTypes[key] = value

    def getNoteType(self):
        return self.noteType 

    def setNoteType(self, type):
        self.noteType = type

    def getCurrentNoteType(self):
        return self.getNoteTypes(self.getNoteType())

    def getCurrentNotesOnFretboard(self):
        return self.currentNotesPositionOnFretboard

    def appendCurrentNotesOnFretboard(self, value):
        self.currentNotesPositionOnFretboard.append(value)

    def setCurrentNotesOnFretboard(self, notes):
        self.currentNotesPositionOnFretboard = notes
    
    #adding scale, arpeggio, interval, chord
    
    '''
    Availible/builtin scales
        Major
        NaturalMinor
        HarmonicMinor
        MelodicMinor
        PentatonicMajor
        PentatonicMinor
        Blues
        WholeTone
        Octatonic
        BebopDominant
        BebopDorian
        BebopMajor
        BebopMelodicMinor
        BebopMinor
        Dorian
        Mixolydian
        Lydian
        Locrian
        Phrygian
    '''
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
            self.getCurrentNoteType().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.getCurrentNoteType().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True

        elif type.lower() == "majorpentatonic":
            intervals = 'P1 M2 M3 P5 M6'.split()
            intervals.append("P1")
            self.getCurrentNoteType().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.getCurrentNoteType().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True
        else:
            # assume user-defined scale
            if intervalsDegrees is None:
                raise ValueError("Intervals must be provided for a user-defined scale.")
            
            intervals = intervalsDegrees.split()
            intervals.append("P1")
            self.getCurrentNoteType().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.getCurrentNoteType().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
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

        #add to fretboard and octave name string
        for pitchIndex in range(len(pitches)):
            fretNum = []
            stringNum = []

            #get each note on each string n their fret
            fretNum, stringNum= self.convertPitchesToFretsStringsNum(pitches[pitchIndex])    
            
            #depending on how many octave to display 
            quotient, remainder = divmod(self.theme.fretboardRange.fretTo+1, 12)
            for octavesFret in range(quotient):
                for index in range(self.theme.tuning.numOfStrings):
                    newFret = fretNum[index]+12  
                    fretNum.append(newFret)
                    stringNum.append(index)
            #check to see if between fret range 
            for i in range(len(fretNum)):
                if (self.theme.fretboardRange.fretFrom > fretNum[i] or fretNum[i] >= self.theme.fretboardRange.fretTo+1) and not((self.theme.fretboardRange.fretFrom == 1) and (fretNum[i] == 0)):                    
                    fretNum[i]=""
            # add the notes to the  octave array
            for i in range(len(fretNum)):
                self.pitchCollection.appendFrets(fretNum[i])
                self.pitchCollection.appendStrings(stringNum[i])
                self.pitchCollection.appendPitchesName(pitches[pitchIndex].name)

                if(fretNum[i] != ""):
                    midi = Functions.fretToMidi(self.theme.tuning.midiTuning[stringNum[i]],fretNum[i])
                    pitchWithOctave = Functions.midiToNoteNameWithOctave(midi)
                else:
                    pitchWithOctave = ""
        
                self.pitchCollection.appendPitchWithOctave(pitchWithOctave)

                #scale degree
                if(self.scaleCustom == True):
                    self.pitchCollection.appendPitchesScaleDegree(self.getCurrentNoteType().getScaleDegrees()[pitchIndex])
        
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

        for stringIndex, stringPitch in enumerate(self.theme.tuning.midiTuning):
            fret = (midiPitch - stringPitch) % 12

            if fret >= (self.theme.fretboardRange.fretFrom - 1) and fret <= self.theme.fretboardRange.fretTo or fret == 0:
                frets.append(fret)
                strings.append(stringIndex)

        return frets, strings
    
    '''
    ('major', ['1,3,5', ['', 'M', 'maj']]), 
    ('minor', ['1,-3,5', ['m', 'min']]),  
    ('augmented', ['1,3,#5', ['+', 'aug']]),  
    ('diminished', ['1,-3,-5', ['dim', 'o']]),

    # sevenths
    ('dominant-seventh', ['1,3,5,-7', ['7', 'dom7', ]]),  
    ('major-seventh', ['1,3,5,7', ['maj7', 'M7']]), 
    ('minor-major-seventh', ['1,-3,5,7', ['mM7', 'm#7', 'minmaj7']]),  
    ('minor-seventh', ['1,-3,5,-7', ['m7', 'min7']]), 
    ('augmented-major-seventh', ['1,3,#5,7', ['+M7', 'augmaj7']]),  
    ('augmented-seventh', ['1,3,#5,-7', ['7+', '+7', 'aug7']]), 
    ('half-diminished-seventh', ['1,-3,-5,-7', ['ø7', 'm7b5']]),  
    ('diminished-seventh', ['1,-3,-5,--7', ['o7', 'dim7']]), 
    ('seventh-flat-five', ['1,3,-5,-7', ['dom7dim5']]),  

    # sixths
    ('major-sixth', ['1,3,5,6', ['6']]),  
    ('minor-sixth', ['1,-3,5,6', ['m6', 'min6']]),  

    # ninths
    ('major-ninth', ['1,3,5,7,9', ['M9', 'Maj9']]),  
    ('dominant-ninth', ['1,3,5,-7,9', ['9', 'dom9']]),  
    ('minor-major-ninth', ['1,-3,5,7,9', ['mM9', 'minmaj9']]),  
    ('minor-ninth', ['1,-3,5,-7,9', ['m9', 'min9']]),  
    ('augmented-major-ninth', ['1,3,#5,7,9', ['+M9', 'augmaj9']]),  
    ('augmented-dominant-ninth', ['1,3,#5,-7,9', ['9#5', '+9', 'aug9']]),  
    ('half-diminished-ninth', ['1,-3,-5,-7,9', ['ø9']]),  
    ('half-diminished-minor-ninth', ['1,-3,-5,-7,-9', ['øb9']]),  
    ('diminished-ninth', ['1,-3,-5,--7,9', ['o9', 'dim9']]),  
    ('diminished-minor-ninth', ['1,-3,-5,--7,-9', ['ob9', 'dimb9']]),  

    # elevenths
    ('dominant-11th', ['1,3,5,-7,9,11', ['11', 'dom11']]),  
    ('major-11th', ['1,3,5,7,9,11', ['M11', 'Maj11']]),  
    ('minor-major-11th', ['1,-3,5,7,9,11', ['mM11', 'minmaj11']]),  
    ('minor-11th', ['1,-3,5,-7,9,11', ['m11', 'min11']]),  
    ('augmented-major-11th', ['1,3,#5,7,9,11', ['+M11', 'augmaj11']]),  
    ('augmented-11th', ['1,3,#5,-7,9,11', ['+11', 'aug11']]),  
    ('half-diminished-11th', ['1,-3,-5,-7,9,11', ['ø11']]),  
    ('diminished-11th', ['1,-3,-5,--7,9,11', ['o11', 'dim11']]),  

    # thirteenths
    ('major-13th', ['1,3,5,7,9,11,13', ['M13', 'Maj13']]),  
    ('dominant-13th', ['1,3,5,-7,9,11,13', ['13', 'dom13']]),  
    ('minor-major-13th', ['1,-3,5,7,9,11,13', ['mM13', 'minmaj13']]),  
    ('minor-13th', ['1,-3,5,-7,9,11,13', ['m13', 'min13']]),  
    ('augmented-major-13th', ['1,3,#5,7,9,11,13', ['+M13', 'augmaj13']]),  
    ('augmented-dominant-13th', ['1,3,#5,-7,9,11,13', ['+13', 'aug13']]),  
    ('half-diminished-13th', ['1,-3,-5,-7,9,11,13', ['ø13']]),  

    # other
    ('suspended-second', ['1,2,5', ['sus2']]),  
    ('suspended-fourth', ['1,4,5', ['sus', 'sus4']]),  
    ('suspended-fourth-seventh', ['1,4,5,-7', ['7sus', '7sus4']]),  
    ('Neapolitan', ['1,2-,3,5-', ['N6']]),  
    ('Italian', ['1,#4,-6', ['It+6', 'It']]),  
    ('French', ['1,2,#4,-6', ['Fr+6', 'Fr']]),  
    ('German', ['1,-3,#4,-6', ['Gr+6', 'Ger']]),  
    ('pedal', ['1', ['pedal']]),  
    ('power', ['1,5', ['power']]),  
    ('Tristan', ['1,#4,#6,#9', ['tristan']]),  
    '''
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
                
            intervals.append("P1")
            self.getCurrentNoteType().setIntervals(intervals)
            scalePitches = [m21Pitch.Pitch(rootNote).transpose(interval) for interval in intervals]
            self.getCurrentNoteType().setScaleDegrees(Functions.intervalsToScaleDegrees(intervals))
            scaleObj = scale.ConcreteScale(rootNote,scalePitches)
            self.scaleCustom = True
            pitches = scaleObj.getPitches()

            return pitches, scaleObj

    def addArpeggio(self, rootNote, type="", chordPitches="", bass=""):
            pitches, scaleObj = self.getArpeggioPitches()              

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
        #what fret to start on and then interval
        #ditch the octave
        #positions
        # Define the CAGED system shapes

        chordType = type.lower()
        #m7b5?
        if chordType not in ["maj", "min", "dim", "aug", "dom7", "dim7", "maj7", "min7","min7b5"]:
            raise ValueError("Invalid chord type provided.")
        
        if caged.upper() not in Constants.cagedShapes.keys():
            raise ValueError("Invalid CAGED SHAPE")
        
        processedShape = Functions.processCAGEDShape(caged.upper(), rootNote, chordType)
        print(processedShape)
        note = processedShape["note"][chordType]
        pos = processedShape["position"][chordType]
        sd = processedShape["scaleDegree"][chordType]
        print(pos)
        self.pitchCollection.setFrets(pos)
        self.pitchCollection.setPitchesNames(note)
        self.pitchCollection.setPitchesScaleDegrees(sd)
        self.pitchCollection.setStrings([0,1,2,3,4,5])

        for i in range(len(note)):
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

