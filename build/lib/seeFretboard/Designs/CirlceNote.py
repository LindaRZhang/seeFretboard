class CircleNote():
    '''
    CircleNote is for displaying notes, universal
    '''
    def __init__(self, **kwargs):
        
        #more for drawing part
        self.noteFaceColor = kwargs.get('noteFaceColor', 'blue')
        self.noteEdgeColor = kwargs.get('noteEdgeColor', 'black')
        self.noteFill = kwargs.get('noteFill', True)
        self.noteEdgeWidth = kwargs.get('noteEdgeWidth', 2)
        self.noteRadius = kwargs.get('noteRadius', 0.4)
        
        #text part
        self.intervals = kwargs.get('interval', None)
        self.scaleDegrees = kwargs.get('scaleDegree', None)
        self.name = kwargs.get('name', None)
        self.nameWithOctave = kwargs.get('nameWithOctave', None)

        #current note string and fret
        self.fret = kwargs.get('fret', None)
        self.string = kwargs.get('string', None)
    
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
        
    def getnoteEdgeWidth(self):
        return self.noteEdgeWidth
    
    def setnoteEdgeWidth(self,lw):
        self.noteEdgeWidth = lw
        
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

    