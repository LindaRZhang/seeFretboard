class Note():
    def __init__(self):
        
        self.noteRadius = 0.5
        self.noteFaceColor = "blue"
        self.noteEdgeColor = "black"
        self.noteLineWidth = 2
        self.noteFill = True
    
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
        