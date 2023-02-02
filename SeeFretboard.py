import matplotlib.pyplot as plt

class SeeFretboard():
    
    #default values
    def __init__(self, strings=6, frets=12, showTuning=True):
        self.tuning = ['E','A','D','G','B','E']
        self.strings = strings
        self.frets = frets
        self.showTuning = showTuning
        
        self.distanceBetweenFrets = 2
        self.distanceBetweenStrings = 2
        self.fretColor = "black"
        self.stringsColor = "black"
    
        self.circleRadius = 0.5
        self.circleFaceColor = "blue"
        self.circleEdgeColor = "black"
        self.circleLineWidth = 2
        self.circleFill = True
        
    #preview
    def drawHorizontalImg(self):
        x =[0,self.distanceBetweenFrets*self.frets]
        y=[0,0]
        plt.plot(x,y,color=self.stringsColor)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.strings-1):
            x=[0,self.distanceBetweenFrets*self.frets]
            y=[distanceStrings,distanceStrings]
            
            distanceStrings+=self.distanceBetweenStrings
            plt.plot(x,y,color=self.stringsColor)
        
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for i in range(0,self.frets):
            x=[0,self.distanceBetweenStrings*(self.strings-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            plt.plot(y,x,color=self.fretColor)
        
        plt.axis('off')
        plt.show()
    
    def drawVerticalImg(self):
        x =[0,0]
        y=[0,self.distanceBetweenFrets*self.frets]
        plt.plot(x,y,color=self.stringsColor)

        distanceStrings = self.distanceBetweenStrings
        #draw strings (horizontal line)
        for i in range(0,self.strings-1):
            x=[distanceStrings,distanceStrings]
            y=[0,self.distanceBetweenFrets*self.frets]
            
            distanceStrings+=self.distanceBetweenStrings
            plt.plot(x,y,color=self.stringsColor)
        
        
        distanceBetweenFrets = 0
        #draw frets (vertical line)
        for i in range(0,self.frets+1):
            x=[0,self.distanceBetweenStrings*(self.strings-1)]
            y=[distanceBetweenFrets,distanceBetweenFrets]
            
            distanceBetweenFrets+=self.distanceBetweenFrets
            plt.plot(x,y,color=self.stringsColor)
        
        plt.axis('off')
        plt.show()
    
    #saveAsImg
    def saveImg(self):
        pass
    
    #string123456 = 'E','A','D','G','B','E'
    def addCircle(self, string, fret, hV):
        if(hV=="h"):
            circle = plt.Circle(((fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,(string-1)*self.distanceBetweenStrings), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)
        else:
            circle = plt.Circle(((string-1)*self.distanceBetweenStrings,self.distanceBetweenStrings*self.frets - (fret-1)*self.distanceBetweenFrets - self.distanceBetweenFrets/2), self.circleRadius, facecolor=self.circleFaceColor,edgecolor=self.circleEdgeColor, linewidth = self.circleLineWidth, zorder = 12,fill=self.circleFill)

        plt.gca().add_artist(circle)
    
    
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
        return self.strings
    
    def setStrings(self, strings):
        self.strings = strings
    
    def getFrets(self):
        return self.frets
    
    def setFrets(self, frets):
        self.frets = frets
        
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