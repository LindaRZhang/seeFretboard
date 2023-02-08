import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

class SeeFretboard():
    
    #default values
    def __init__(self, strings=6, frets=12, showTuning=True):
        self.tuning = ['E','A','D','G','B','E']
        self.stringsLength = strings
        self.fretsLength = frets
        
        self.showTuning = showTuning
        self.showFretboardNumber = True
        self.showStringNumber = True
        
        self.distanceBetweenFrets = 5
        self.distanceBetweenStrings = 2
        self.fretColor = "black"
        self.stringsColor = "black"
        self.fretOpacity = 0.3
        self.stringsOpactiy=1

        self.fretboardMarkerColor = "#DCDCDC"
        
        self.circles = []
        self.circleRadius = 0.5
        self.circleFaceColor = "blue"
        self.circleEdgeColor = "black"
        self.circleLineWidth = 2
        self.circleFill = True
        
    #preview
    def drawHorizontalFretboard(self):
        x =[0,self.distanceBetweenFrets*self.fretsLength]
        y=[0,0]
        plt.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.stringsLength-1):
            x=[0,self.distanceBetweenFrets*self.fretsLength]
            y=[distanceStrings,distanceStrings]
            
            distanceStrings+=self.distanceBetweenStrings
            plt.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)
        
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for i in range(0,self.fretsLength):
            x=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            plt.plot(y,x,color=self.fretColor, alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = plt.Circle(((3)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret5 = plt.Circle(((5)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret7 = plt.Circle(((7)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret9 = plt.Circle(((9)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(self.stringsLength-1)*self.distanceBetweenStrings/2), self.circleRadius, facecolor=self.fretboardMarkerColor, linewidth = self.circleLineWidth, fill=self.circleFill)

        plt.gca().add_artist(markerFret3)
        plt.gca().add_artist(markerFret5)
        plt.gca().add_artist(markerFret7)
        plt.gca().add_artist(markerFret9)
        
        #draw circles/notes
        for circle in self.circles:
            plt.gca().add_artist(circle)

        plt.axis('off')
        figureWin = plt.gcf()
        figureWin.set_figwidth(self.distanceBetweenFrets*2)
        figureWin.set_figheight(self.distanceBetweenStrings*3/2)
        ax = plt.gca()
        ax.margins(x=0,y=self.circleRadius/5)
        ax.set_aspect("equal")
        plt.show()
    
    def drawVerticalFretboard(self):
        x =[0,0]
        y=[0,self.distanceBetweenFrets*self.fretsLength]
        plt.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (vertical line)
        for i in range(0,self.stringsLength-1):
            x=[distanceStrings,distanceStrings]
            y=[0,self.distanceBetweenFrets*self.fretsLength]
            
            distanceStrings+=self.distanceBetweenStrings
            plt.plot(x,y,color=self.stringsColor,alpha=self.stringsOpactiy)
        
        
        distanceBetweenFrets = 0
        #draw frets (horizontal line)
        for i in range(0,self.fretsLength+1):
            x=[0,self.distanceBetweenStrings*(self.stringsLength-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            plt.plot(x,y,color=self.fretColor,alpha=self.fretOpacity)
        
        #draw 3,5,7,9 marker
        markerFret3 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (3-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret5 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (5-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret7 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (7-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)
        markerFret9 = plt.Circle(((self.stringsLength-1)*self.distanceBetweenStrings/2, self.distanceBetweenFrets*self.fretsLength - (9-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.fretboardMarkerColor,linewidth = self.circleLineWidth, fill=self.circleFill)

        plt.gca().add_artist(markerFret3)
        plt.gca().add_artist(markerFret5)
        plt.gca().add_artist(markerFret7)
        plt.gca().add_artist(markerFret9)

        #draw circles/notes
        for circle in self.circles:
            plt.gca().add_artist(circle)

        plt.axis('off')
        figureWin = plt.gcf()
        figureWin.set_figwidth(3)
        figureWin.set_figheight(8)
        ax = plt.gca()
        ax.margins(y=0,x=self.circleRadius/5)
        ax.set_aspect("equal")
        plt.show()
        
    def clearFretboard(self):
        # plt.clf()
        pass

    #saveAsImg
    def saveImg(self):
        pass
    
    #user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self,notes,hv):
        notes = [int(x.strip()) for x in notes.split(',')]
        for i in range (1,self.stringsLength+1):
            self.addCircle(i,notes[i-1],hv)

    def addCircle(self, string, fret, hV):
        if(hV=="h"):
            circle = plt.Circle(((fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(string-1)*self.distanceBetweenStrings), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)
        else:
            circle = plt.Circle(((string-1)*self.distanceBetweenStrings,self.distanceBetweenFrets*self.fretsLength - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)
        
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