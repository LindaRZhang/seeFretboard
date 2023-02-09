import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import os

class SeeFretboard():
    
    #default values
    def __init__(self, hv="h", strings=6, frets=12, showTuning=True):
        self.tuning = ['E','A','D','G','B','E']
        self.stringsLength = strings
        self.fretsLength = frets
        
        self.showTuning = showTuning
        self.showFretboardNumber = True
        self.showStringNumber = True
        
       # fretboard parameters
        self.distanceBetweenFrets = 5
        self.distanceBetweenStrings = 2
        self.fretColor = "black"
        self.stringsColor = "black"
        self.fretOpacity = 0.3
        self.stringsOpactiy=1

        self.fretboardMarkerColor = "#DCDCDC"
        
        self.fig, self.ax = plt.subplots()

        #note sparameter
        self.circles = []
        self.circleRadius = 0.5
        self.circleFaceColor = "blue"
        self.circleEdgeColor = "black"
        self.circleLineWidth = 2
        self.circleFill = True
        
        self.pathName = os.path.expanduser("default")

        #horizontal or vertical fretboard
        self.hv = hv

    #preview
    def drawHorizontalFretboard(self):
        x =[0,self.distanceBetweenFrets*self.fretsLength]
        y=[0,0]
        self.ax.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.stringsLength-1):
            x=[0,self.distanceBetweenFrets*self.fretsLength]
            y=[distanceStrings,distanceStrings]
            
            distanceStrings+=self.distanceBetweenStrings
            self.ax.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)
        
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for i in range(0,self.fretsLength):
            x=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            self.ax.plot(y,x,color=self.fretColor, alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = plt.Circle(((3)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret5 = plt.Circle(((5)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret7 = plt.Circle(((7)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret9 = plt.Circle(((9)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)

        self.ax.add_artist(markerFret3)
        self.ax.add_artist(markerFret5)
        self.ax.add_artist(markerFret7)
        self.ax.add_artist(markerFret9)
        
        #draw circles/notes
        for circle in self.circles:
            self.ax.add_artist(circle)

        plt.axis('off')
        
        self.fig.set_figwidth(self.distanceBetweenFrets*2)
        self.fig.set_figheight(self.distanceBetweenStrings*3/2)
        
        self.ax.margins(x=0,y=self.circleRadius/5)
        self.ax.set_aspect("equal")
    
    def drawVerticalFretboard(self):
        x =[0,0]
        y=[0,self.distanceBetweenFrets*self.fretsLength]
        self.ax.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (vertical line)
        for i in range(0,self.stringsLength-1):
            x=[distanceStrings,distanceStrings]
            y=[0,self.distanceBetweenFrets*self.fretsLength]
            
            distanceStrings+=self.distanceBetweenStrings
            self.ax.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)
        
        
        distanceBetweenFrets = 0
        #draw frets (horizontal line)
        for i in range(0,self.fretsLength+1):
            x=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            self.ax.plot(x,y,color=self.fretColor,alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (3-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret5 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (5-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret7 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (7-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret9 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (9-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)

        self.ax.add_artist(markerFret3)
        self.ax.add_artist(markerFret5)
        self.ax.add_artist(markerFret7)
        self.ax.add_artist(markerFret9)

        #draw circles/notes
        for circle in self.circles:
            self.ax.add_artist(circle)

        plt.axis('off')

        self.fig.set_figwidth(3)
        self.fig.set_figheight(8)

        self.ax.margins(y=0,x=self.circleRadius/5)
        self.ax.set_aspect("equal")
    
    def showFretboard(self):
        plt.show()

    def closeFretboard(self):
        plt.close('all')
    
    def clearFretboard(self):
        self.circles = []

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
            self.addCircle(i,notes[i-1])

    def addCircle(self, string, fret):
        if(self.hv=="h"):
            circle = plt.Circle(((fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(string-1)*self.distanceBetweenStrings), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)
        else:
            circle = plt.Circle(((string-1)*self.distanceBetweenStrings,self.distanceBetweenFrets*self.fretsLength - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)
        
        self.ax.add_artist(circle)
        self.circles.append(circle)
        

    def removeCircle(self):
        pass    
    
    def getCircleRadius(self):
        return self.circleRadius
    
    def setCircleRadius(self,radius):
        self.circleRadius = radius
        
    def getCircleFaceColor(self):
        return self.circleFaceColor
    
    def setCircleFaceColor(self,color):
        self.circleFaceColor = color
        
    def getCircleEdgeColor(self):
        return self.circleEdgeColor
    
    def setCircleEdgeColor(self,color):
        self.circleEdgeColor = color
        
    def getCircleLineWidth(self):
        return self.circleLineWidth
    
    def setCircleLineWidth(self,lw):
        self.circleLineWidth = lw
        
    def getCircleFill(self):
        return self.circleFill
    
    def set(self,circleFill):
        self.circleFill = circleFill
        
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