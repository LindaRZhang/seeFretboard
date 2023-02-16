from bokeh.plotting import figure, show
from bokeh.models import Circle,Label, Button,Toggle,CustomJS
from bokeh.layouts import layout
from bokeh.events import ButtonClick

import os
from Note import Note

class SeeFretboard():
    
    #default values
    def __init__(self, hv="h", strings=6, frets=12, showTuning=True):
        self.tuning = ['E','A','D','G','B','E']
        self.stringsLength = strings
        self.fretsLength = frets
        
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
        
        self.fig = figure()
        
        #note
        self.note = Note()
        self.notes = []
        
        self.pathName = os.path.expanduser("default")

        #horizontal or vertical fretboard
        self.hv = hv

        self.tuningLabelbutton = Button(label="Toggle Tuning",button_type="success")
        self.fretLabelbutton = Button(label="Toggle Fretboard Number",button_type="success")


    def drawTuningLabel(self, distanceStrings,i,vh):
        if(vh == "h"):
            string_label = Label(x=-2, y=distanceStrings-self.distanceBetweenStrings/2, text=self.tuning[i+1], text_align='center', text_font_size='10pt')
        else:
            string_label = Label(x=distanceStrings, y=self.distanceBetweenFrets*self.fretsLength+1, text=self.tuning[i+1], text_align='center', text_font_size='10pt')

        string_label.visible = self.showTuning
        self.fig.add_layout(string_label)
        
        self.tuningLabelbutton.js_on_event(ButtonClick, CustomJS(args=dict(stringLabel=string_label),code="""stringLabel.visible = !stringLabel.visible"""))

    def drawFretLabel(self, distanceBetweenFrets,j,vh):
        if(vh == "h"):
            fret_label = Label(x=distanceBetweenFrets+self.distanceBetweenFrets-self.distanceBetweenFrets/1.7, y=-self.note.noteRadius, text=str(j+1), text_align='center', text_font_size='10pt')
        else:
            fret_label = Label(x=-self.note.noteRadius*2, y=distanceBetweenFrets+self.distanceBetweenFrets-self.distanceBetweenFrets/1.7, text=str(j), text_align='center', text_font_size='10pt')

        fret_label.visible = self.showFretboardNumber
        self.fig.add_layout(fret_label)
        
        self.fretLabelbutton.js_on_event(ButtonClick, CustomJS(args=dict(fretLabel=fret_label),code="""fretLabel.visible = !fretLabel.visible"""))

        
    #preview
    def drawHorizontalFretboard(self):

        x =[0,self.distanceBetweenFrets*self.fretsLength]
        y=[0,0]

        self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.stringsLength-1):
            x=[0,self.distanceBetweenFrets*self.fretsLength]
            y=[distanceStrings,distanceStrings]

            self.drawTuningLabel(distanceStrings,i,"h")            
            
            distanceStrings+=self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for j in range(0,self.fretsLength+1):
            fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            fy=[distanceBetweenFrets,distanceBetweenFrets]

            if(j!=self.fretsLength):
                self.drawFretLabel(distanceBetweenFrets,j,"h")

            distanceBetweenFrets+=self.distanceBetweenFrets
            self.fig.line(x=fy, y=fx, line_color=self.fretColor, line_alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = self.fig.circle(x=3*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                     y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
                     radius=self.note.noteRadius,
                     fill_color=self.fretboardMarkerColor,
                     line_width=self.note.noteLineWidth,
                     fill_alpha=self.note.noteFill)
        markerFret5 = self.fig.circle(x=5*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                     y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
                     radius=self.note.noteRadius,
                     fill_color=self.fretboardMarkerColor,
                     line_width=self.note.noteLineWidth,
                     fill_alpha=self.note.noteFill)
        markerFret7 = self.fig.circle(x=7*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                     y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
                     radius=self.note.noteRadius,
                     fill_color=self.fretboardMarkerColor,
                     line_width=self.note.noteLineWidth,
                     fill_alpha=self.note.noteFill)
        markerFret9 = self.fig.circle(x=9*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                     y=(self.stringsLength-1)*self.distanceBetweenStrings/2,
                     radius=self.note.noteRadius,
                     fill_color=self.fretboardMarkerColor,
                     line_width=self.note.noteLineWidth,
                     fill_alpha=self.note.noteFill)

        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False

    
    def drawVerticalFretboard(self):
        x =[0,0]
        y=[0,self.distanceBetweenFrets*self.fretsLength]
        
        self.drawTuningLabel(0,-1,"v")            

        self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (vertical line)
        for i in range(0,self.stringsLength-1):
            x=[distanceStrings,distanceStrings]
            y=[0,self.distanceBetweenFrets*self.fretsLength]

            self.drawTuningLabel(distanceStrings,i,"v")

            distanceStrings+=self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor, line_alpha=self.stringsOpactiy)        
        
        distanceBetweenFrets = 0
        fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
        fy=[self.fretsLength*self.distanceBetweenFrets,self.fretsLength*self.distanceBetweenFrets]
        self.fig.line(x=fx, y=fy, line_color=self.fretColor, line_alpha=self.fretOpacity)
            
        #draw frets (horizontal line)
        fretlength = self.fretsLength

        for j in range(0,self.fretsLength):
            fx=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            fy=[distanceBetweenFrets,distanceBetweenFrets]
            
            self.drawFretLabel(distanceBetweenFrets,fretlength,"v")

            fretlength-=1
            distanceBetweenFrets+=self.distanceBetweenFrets
            self.fig.line(x=fx, y=fy, line_color=self.fretColor, line_alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = self.fig.circle(x=(self.stringsLength-1)*self.distanceBetweenStrings/2,
                     y= self.distanceBetweenFrets*self.fretsLength - (3-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2,
                     radius=self.note.noteRadius,
                     fill_color=self.fretboardMarkerColor,
                     line_width=self.note.noteLineWidth,
                     fill_alpha=self.note.noteFill)
        # markerFret3 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (3-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.note.noteRadius, facecolor=self.fretboardMarkerColor,linewidth = self.note.noteLineWidth, fill=self.note.noteFill)
        # markerFret5 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (5-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.note.noteRadius, facecolor=self.fretboardMarkerColor,linewidth = self.note.noteLineWidth, fill=self.note.noteFill)
        # markerFret7 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (7-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.note.noteRadius, facecolor=self.fretboardMarkerColor,linewidth = self.note.noteLineWidth, fill=self.note.noteFill)
        # markerFret9 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (9-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.note.noteRadius, facecolor=self.fretboardMarkerColor,linewidth = self.note.noteLineWidth, fill=self.note.noteFill)


        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False
    
    def showFretboard(self):
        layoutF = layout(self.fig,[self.tuningLabelbutton,self.fretLabelbutton])
        show(layoutF)

    def closeFretboard(self):
        self.fig.close('all')
    
    def clearFretboard(self):
        print(len(self.notes))
        for note in self.notes:
            note.remove()

    def getPathName(self):
        return self.pathName

    def setPathName(self,path):
        self.pathName = path

    #saveAsImg
    def saveAs(self,meta):
        plt.savefig(self.pathName+"."+meta, format=meta)
    
    #user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self,notes):
        notes = [int(x.strip()) for x in notes.split(',')]
        for i in range (1,self.stringsLength+1):
            self.addNote(i,notes[i-1])
    
    def addNote(self, string, fret):
        if(self.hv=="h"):
            circle = plt.Circle(((fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(string-1)*self.distanceBetweenStrings), self.note.noteRadius, facecolor=self.note.noteFaceColor,edgecolor=self.note.noteEdgeColor, linewidth = self.note.noteLineWidth, zorder = 12,fill=self.note.noteFill)
        else:
            circle = plt.Circle(((string-1)*self.distanceBetweenStrings,self.distanceBetweenFrets*self.fretsLength - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.note.noteRadius, facecolor=self.note.noteFaceColor,edgecolor=self.note.noteEdgeColor, linewidth = self.note.noteLineWidth, zorder = 12,fill=self.note.noteFill)
        
        self.ax.add_artist(circle)
        self.notes.append(circle)

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
    
    def getFrets(self):
        return self.fretsLength
    
    def setFrets(self, frets):
        self.fretsLength = frets
        
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