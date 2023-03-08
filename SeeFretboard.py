from bokeh.plotting import figure, show
from bokeh.models import Text, Circle,Label, Button,CustomJS, Slider
from bokeh.models.widgets import TextInput
from bokeh.layouts import layout
from bokeh.events import ButtonClick
from bokeh.io import export_png, export_svg, curdoc
from bokeh.layouts import row
from bokeh.document import without_document_lock

import os
import time
import glob
import re

import cv2

from Note import Note
from Video import Video


class SeeFretboard():
    
    #default values
    def __init__(self, hv="h", strings=6, fretFrom=0, fretsTo=12, showTuning=True):
        #horizontal or vertical fretboard
        self.hv = hv

        self.tuning = ['E','A','D','G','B','E']
        self.stringsLength = strings
        self.fretFrom = fretFrom
        self.fretTo = fretsTo
        self.fretLength = self.fretTo - self.fretFrom
        
        self.showTuning = showTuning
        self.showFretboardNumber = True
        
       # fretboard parameters
        self.distanceBetweenFrets = 5
        self.distanceBetweenStrings = 2
        self.fretColor = "black"
        self.stringsColor = "black"
        self.fretOpacity = 0.3
        self.stringsOpactiy=1

        self.fretboardMarkerColor = "#DCDCDC"
        
        #figure attribute
        self.fig = figure()
        if(self.hv == "h"):
            self.fig.width = 800
            self.fig.height = 400
        else:
            self.fig.width = 400
            self.fig.height = 800

        #note
        self.note = Note()
        self.notes = []
        
        self.imagePathName = os.path.join(os.getcwd(), 'Image')
        print(self.imagePathName)
        self.videoPathName = os.getcwd()
        self.imageName = "default"

        #buttons
        self.tuningLabelButton = Button(label="Toggle Tuning",button_type="success")
        self.fretLabelButton = Button(label="Toggle Fretboard Number",button_type="success")
        self.fretBoardDirectionButton = Button(label="Toggle Fretboard Direction",button_type="success")
        self.toggleButtons = row(self.fretBoardDirectionButton, self.tuningLabelButton,self.fretLabelButton)
        self.inputChordInput = TextInput(value="X,0,5,5,0,0", title="Enter Notes Fret:")
        self.inputChordButton = Button(label="ENTER ",button_type="success")
        self.clearFretboardButton = Button(label="Clear Fretboard ",button_type="success")
        self.notesOptions =row(self.inputChordInput,self.inputChordButton,self.clearFretboardButton)

        self.inputChordButton.on_click(self.inputChordButtonClicked)
        self.clearFretboardButton.on_click(self.clearFretboard) 

        #video parameter
        self.video = Video(0,10,0,0.1,30)
        self.videoFrames = self.video.frames

        self.timeslider = Slider(start=self.video.startTime, end=self.video.endTime, value=self.video.currentFrame, step=self.video.frameStep, title="Time")
        #self.timeslider.on_change('value', self.sliderTimeCallback)
        
        self.playButton = Button(label="Play")
        self.playButton.on_click(self.playButtonClicked)
        self.playing = False

    def inputChordButtonClicked(self):
        self.updateFretboard(self.inputChordInput.value)

    #video related
    def playButtonClicked(self):
        if(self.playing):
            self.playButton.label = "Play"
            self.playing = False
        else:
            self.playButton.label = "Pause"
            self.playing = True
            while(self.playing != False):
                self.updatingFretboardAnimation()
    
    @without_document_lock
    def updatingFretboardAnimation(self):
        
        if (self.video.currentFrame >= self.video.endTime):
            self.playButton.label = "Play"
            self.playing = False
            self.video.currentFrame = 0
            
            self.updateFretboard(str(list(self.video.frames.values())[0]))
            return

        #if in the frame there is a chord draw chord
        if(self.video.getCurrentFrame() in self.video.frames.keys()):
            currentChord = self.video.frames[self.video.currentFrame]
            self.updateFretboard(currentChord)

        newCurrentFrame = self.video.getCurrentFrame()+self.video.getFrameStep()
        self.video.setCurrentFrame(newCurrentFrame)

        self.timeslider.update(start=0, end=3, value=self.video.getCurrentSecond(), step=self.video.frameStep)

    # def sliderTimeCallback(self, attr, old, new):
    #     self.video.setCurrentFrame(self.timeslider.value)
    #     for i in range(self.video.getFramesLength):
    #         key1, key2 = list(self.video.getFramesKeys)[i:i+2]
    #         if (self.timeslider.value > key1 and self.timeslider.value < key2 ):
    #             self.updateFretboard(self.video.getFrame(key1))

    def setVideo(self, video):
        self.video = video
        self.timeslider.update(start=self.video.getStartTime(), end=self.video.getEndTime(), value=self.video.getCurrentFrame(), step=self.video.getFrameStep())
    
    def getVideo(self):
        return self.video
    
    def saveAsVideoImages(self):
        oriImgName = self.imageName
        print(oriImgName)
        for k, v in self.video.getFramesItems():
            self.updateFretboard(v)
            self.setImageName(str(k)+oriImgName)
            self.saveAs("png")
            print("saving"+self.getImageName())
        print("done")

    def deleteAllImages(self):
        files = glob.glob(self.imagePathName)
        for f in files:
            os.remove(f)
        print("All Images Delete")

    def saveAsVideoImagesFromCurrentFrame(self):
        pass

    def saveAsVideoImagesFrom(self,frameFrom,frameTo):
        pass
    
    def saveAsVideo(self):
        images = os.listdir(self.imagePathName)
        images = sorted(images, key=lambda s: [int(x) if x.isdigit() else x for x in re.split('(\d+)', s)])

        fourcc = cv2.VideoWriter_fourcc(*self.video.getCodec())
        frameSize = (self.fig.width,self.fig.height)

        videoWriter = cv2.VideoWriter(os.path.join(self.getVideoPathName()+self.video.getName()), fourcc, self.video.getFrameRate(), frameSize)

        for image in images:
            print(os.path.join(self.getImagePathName(),image))
            frame = cv2.imread(os.path.join(self.getImagePathName(),image))
            videoWriter.write(frame)
            
        cv2.destroyAllWindows()
        videoWriter.release()

        print("video saved at "+self.videoPathName)
        
    #fretboard relate
    def drawTuningLabel(self, distanceStrings,i):
        if(self.hv == "h"):
            string_label = Label(x=-1, y=distanceStrings-self.distanceBetweenStrings, text=self.tuning[i+1], text_align='center', text_font_size='10pt')
        else:
            string_label = Label(x=distanceStrings, y=self.distanceBetweenFrets*self.fretTo+1, text=self.tuning[i+1], text_align='center', text_font_size='10pt')

        string_label.visible = self.showTuning
        self.fig.add_layout(string_label)
        
        self.tuningLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(stringLabel=string_label),code="""stringLabel.visible = !stringLabel.visible"""))

    def drawFretLabel(self, distanceBetweenFrets,j):
        if(self.hv == "h"):
            fret_label = Label(x=distanceBetweenFrets+self.distanceBetweenFrets-self.distanceBetweenFrets/2, y=-self.note.noteRadius*1.5, text=str(j+1), text_align='center', text_font_size='10pt')
        else:
            fret_label = Label(x=-self.note.noteRadius*1.5, y=distanceBetweenFrets+self.distanceBetweenFrets-self.distanceBetweenFrets/2, text=str(j), text_align='center', text_font_size='10pt')

        fret_label.visible = self.showFretboardNumber
        self.fig.add_layout(fret_label)
        
        self.fretLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(fretLabel=fret_label),code="""fretLabel.visible = !fretLabel.visible"""))

    def drawToggleFretboardDirection(self):
        pass
        # self.clearFretboard()
        # self.fretBoardDirectionButton.js_on_event(ButtonClick, CustomJS(args=dict(hv=self.hv, drawV = self.drawVerticalFretboard, drawH = self.drawHorizontalFretboard),code="""if (hv=="h"){  drawV()} else{ drawH()}"""))
        
    #preview
    def drawHorizontalFretboard(self):

        x =[0,self.distanceBetweenFrets*(self.fretTo-self.fretFrom+1)]
        y=[0,0]

        self.drawTuningLabel(self.distanceBetweenStrings,-1)            

        self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.stringsLength-1):
            x=[0,self.distanceBetweenFrets*(self.fretTo-self.fretFrom+1)]
            y=[distanceStrings,distanceStrings]

            self.drawTuningLabel(distanceStrings+self.distanceBetweenStrings,i)            
            
            distanceStrings+=self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for j in range(self.fretFrom-1,self.fretTo+1):
            fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            fy=[distanceBetweenFrets,distanceBetweenFrets]

            if(j!=self.fretTo):
                self.drawFretLabel(distanceBetweenFrets,j)

            distanceBetweenFrets+=self.distanceBetweenFrets
            self.fig.line(x=fy, y=fx, line_color=self.fretColor, line_alpha=self.fretOpacity)
        
        self.drawInlay()

        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False

    
    def drawVerticalFretboard(self):
        x =[0,0]
        y=[self.distanceBetweenFrets*self.fretFrom-self.distanceBetweenFrets,self.distanceBetweenFrets*(self.fretTo)]
        
        self.drawTuningLabel(0,-1)            

        self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (vertical line)
        for i in range(0,self.stringsLength-1):
            x=[distanceStrings,distanceStrings]
            y=[self.distanceBetweenFrets*self.fretFrom-self.distanceBetweenFrets,self.distanceBetweenFrets*(self.fretTo)]

            self.drawTuningLabel(distanceStrings,i)

            distanceStrings+=self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)        
        
        distanceBetweenFrets = self.fretTo*self.distanceBetweenFrets
        fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
        fy=[self.fretTo*self.distanceBetweenFrets,self.fretTo*self.distanceBetweenFrets]
        self.fig.line(x=fx, y=fy, line_color=self.fretColor, line_alpha=self.fretOpacity)
            
        #draw frets (horizontal line)
        fretlength = self.fretFrom-1

        for j in range(self.fretFrom,self.fretTo+2):
            fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            fy=[distanceBetweenFrets,distanceBetweenFrets]
            
            if(j!=self.fretFrom):
                self.drawFretLabel(distanceBetweenFrets,fretlength)

            fretlength+=1
            distanceBetweenFrets-=self.distanceBetweenFrets
            self.fig.line(x=fx, y=fy, line_color=self.fretColor, line_alpha=self.fretOpacity)
        
        self.drawInlay()

        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False
    
    def drawInlay(self):
        pass
        # if(self.hv == "h"):
        # #draw 3,5,7,9 marker
        #     markerFret3 = self.fig.circle(x=3*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
        #                 y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 radius=self.note.noteRadius,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret5 = self.fig.circle(x=5*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
        #                 y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 radius=self.note.noteRadius,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret7 = self.fig.circle(x=7*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
        #                 y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 radius=self.note.noteRadius,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret9 = self.fig.circle(x=9*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
        #                 y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 radius=self.note.noteRadius,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        # else:
        #     markerFret3 = self.fig.circle(x=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 y= self.distanceBetweenFrets*self.fretsLength - (3-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
        #                 radius=self.note.noteRadius/2,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret5 = self.fig.circle(x=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 y= self.distanceBetweenFrets*self.fretsLength - (5-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
        #                 radius=self.note.noteRadius/2,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret7 = self.fig.circle(x=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 y= self.distanceBetweenFrets*self.fretsLength - (7-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
        #                 radius=self.note.noteRadius/2,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)
        #     markerFret9 = self.fig.circle(x=(self.stringsLength-1)*self.distanceBetweenStrings/2,
        #                 y= self.distanceBetweenFrets*self.fretsLength - (9-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
        #                 radius=self.note.noteRadius/2,
        #                 fill_color=self.fretboardMarkerColor,
        #                 line_width=self.note.noteLineWidth,
        #                 fill_alpha=self.note.noteFill,
        #                 line_color=self.note.noteEdgeColor)

    def showFretboard(self):
        layoutF = layout(self.fig,self.timeslider, self.playButton, self.toggleButtons, self.notesOptions)
        curdoc().add_root(layoutF)
        #show(layoutF)

    def closeFretboard(self):
        pass
    
    def clearFretboard(self):        
        notesCopy = list(self.notes)
        
        for note in notesCopy:
            self.fig.renderers.remove(note)
            self.notes.remove(note)
        
        for r in self.fig.renderers:
            if isinstance(r, Label) and r.name == "xNote":
                self.fig.remove(r)

    def updateFretboard(self, notes):
        self.clearFretboard()
        self.addNotesAllString(notes)

    def getImagePathName(self):
        return self.imagePathName

    def setImagePathName(self,path):
        self.imagePathName = path

    def getVideoPathName(self):
        return self.videoPathName

    def setVideoPathName(self,path):
        self.videoPathName = path

    #saveAsImg
    def saveAs(self,meta):
        fileName = os.path.join(self.imagePathName, self.getImageName() +"."+meta)
        if(meta.lower()=="png"):
            export_png(self.fig, filename=fileName)

        elif(meta.lower()=="svg"):
            export_svg(self.fig, filename=fileName)
    
    def getImageName(self):
        return self.imageName
    
    def setImageName(self,name):
        self.imageName = name

    def setNoteObject(self,note):
        self.note = note

    #user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self,notes):
        notes = [(x.strip()) for x in notes.split(',')]
        if(len(notes) == self.stringsLength):
            for i in range (1,self.stringsLength+1):
                self.addNote(i,notes[i-1])
        else:
            print("ERROR, WRONG FORMAT.")    
        
    def addNote(self, string, fret):
        textX = ""
        circleNote = ""
        
        if(fret != "0" and fret.lower() != "x"):
            fret = int(fret)-self.fretFrom+1

        if(self.hv=="h"):
            if(fret == "0"):
               fret = int(fret)
               circleNote = Circle(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2, 
                            y=(string-1)*self.distanceBetweenStrings,
                     radius=self.note.noteRadius,
                     line_width=self.note.noteLineWidth,
                     line_color=self.note.noteEdgeColor,
                     fill_alpha=0,
                     name="circleNote"
                     )
            elif(fret == "x" or fret == "X"):
                fret = 0
                textX = Label(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2, 
                            y=(string-1)*self.distanceBetweenStrings, text='X', text_color="#000000",name="xNote")
                self.fig.add_layout(textX)
            else:
                fret = int(fret)
                circleNote = Circle(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2, 
                            y=(string-1)*self.distanceBetweenStrings,
                     radius=self.note.noteRadius,
                     fill_color=self.note.noteFaceColor,
                     line_width=self.note.noteLineWidth,
                     line_color=self.note.noteEdgeColor,
                     name="circleNote"
                     )
        else:
            if(fret == "0"):
                fret = int(fret)
                circleNote = Circle(x=(string-1)*self.distanceBetweenStrings, 
                                y=self.distanceBetweenFrets*self.fretTo - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
                        radius=self.note.noteRadius/2,
                        line_width=self.note.noteLineWidth,
                        line_color=self.note.noteEdgeColor,
                        fill_alpha=0,
                        name="circleNote"
                        )
            elif(fret == "x" or fret == "X"):
                fret = 0
                textX = Label(x=(string-1)*self.distanceBetweenStrings, 
                                y=self.distanceBetweenFrets*self.fretTo - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2, text='X', text_color="#000000",name="circleNote")
                self.fig.add_layout(textX)
            else:
                fret = int(fret)
                circleNote = Circle(x=(string-1)*self.distanceBetweenStrings, 
                                y=self.distanceBetweenFrets*self.fretTo - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
                        radius=self.note.noteRadius/2,
                        fill_color=self.note.noteFaceColor,
                        line_width=self.note.noteLineWidth,
                        line_color=self.note.noteEdgeColor,
                        name="circleNote"
                        )
        if(textX == ""):
            self.notes.append(self.fig.add_glyph(circleNote))
    
    def removeNote(self):
        pass    
    
    def getTuning(self):
        return self.tuning
    
    def setTuning(self, tuning):
        self.tuning = tuning
    
    def getStrings(self):
        return self.stringsLength
    
    def setStrings(self, strings):
        self.stringsLength = strings
    
    def getFretFrom(self):
        return self.fretFrom
    
    def setFretFrom(self, frets):
        self.fretFrom = frets
    
    def getFretTo(self):
        return self.fretTo
    
    def setFretTo(self, frets):
        self.fretTo = frets

    def getFretLength(self):
        return self.fretLength
    
    def setFretLength(self, l):
        self.fretTo = l
        
    def getShowTuning(self):
        return self.showTuning
    
    def setShowTuning(self, showTuning):
        self.showTuning = showTuning
        
    def getDistanceBetweenFrets(self):
        return self.distanceBetweenFrets
    
    def setDistanceBetweenFrets(self, distanceBetweenFrets):
        self.distanceBetweenFrets = distanceBetweenFrets
        
    def getDistanceBetweenStrings(self):
        return self.distanceBetweenStrings
    
    def setDistanceBetweenStrings(self, distanceBetweenStrings):
        self.distanceBetweenStrings = distanceBetweenStrings
        
    def getFretColor(self):
        return self.fretColor
    
    def setFretColor(self, fretColor):
        self.fretColor = fretColor
        
    def getStringsColor(self):
        return self.stringsColor
    
    def setStringsColor(self, stringsColor):
        self.stringsColor = stringsColor
    
    def getFretOpacity(self):
        return self.fretOpacity
    
    def setFretOpacity(self, fretOpacity):
        self.fretOpacity = fretOpacity
    
    def getStringsOpactiy(self):  
        return self.stringsOpactiy
    
    def setStringsOpacity(self, stringsOpactiy):
        self.stringsOpactiy = stringsOpactiy

    def getFigWidth(self):  
        return self.fig.width
    
    def setFigWidth(self, width):
        self.fig.width = width

    def getFigHeight(self):  
        return self.fig.height
    
    def setFigHeight(self, height):
        self.fig.height = height