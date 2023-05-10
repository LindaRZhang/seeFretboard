class CircleNote():
    def __init__(self, **kwargs):
        
        #more for drawing part
        self.noteFaceColor = kwargs.get('noteFaceColor', 'blue')
        self.noteEdgeColor = kwargs.get('noteEdgeColor', 'black')
        self.noteLineWidth = kwargs.get('noteLineWidth', 2)
        self.noteFill = kwargs.get('noteFill', True)
        self.noteRadius = kwargs.get('noteRadius', 0.4)
        
        #text part
        self.intervals = kwargs.get('interval', None)
        self.scaleDegrees = kwargs.get('scaleDegree', None)
        self.name = kwargs.get('name', None)
        self.nameWithOctave = kwargs.get('nameWithOctave', None)
    
    def getNoteRadius(self):
        return self.noteRadius
    
    def setNoteRadius(self,radius):
        self.noteRadius = radius
        
    def getNoteFaceColor(self):
        return self.noteFaceColor
    
    def setNoteFaceColor(self,color):
        self.noteFaceColor = color
        
    def getNoteEdgeColor(self):
        return self.noteEdgeColor
    
    def setNoteEdgeColor(self,color):
        self.noteEdgeColor = color
        
    def getNoteLineWidth(self):
        return self.noteLineWidth
    
    def setNoteLineWidth(self,lw):
        self.noteLineWidth = lw
        
    def getNoteFill(self):
        return self.noteFill
    
    def setNoteFill(self,noteFill):
        self.noteFill = noteFill
    
    def getIntervals(self):
        return self.intervals
    
    def setIntervals(self, interval):
        self.intervals = interval
    
    def getScaleDegrees(self):
        return self.scaleDegrees
    
    def setScaleDegrees(self, scaleDegree):
        self.scaleDegrees = scaleDegree
    
    def getName(self):
        return self.name
    
    def setName(self, name):
        self.name = name
    
    def getNameWithOctave(self):
        return self.nameWithOctave
    
    def setNameWithOctave(self, nameWithOctave):
        self.nameWithOctave = nameWithOctave

    