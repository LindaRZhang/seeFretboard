class CircleNote():
    def __init__(self, noteFaceColor = "blue", noteEdgeColor = "black", noteLineWidth=2, noteFill = True, noteRadius = 0.5):
        
        self.noteFaceColor = noteFaceColor
        self.noteEdgeColor = noteEdgeColor
        self.noteLineWidth = noteLineWidth
        self.noteFill = noteFill
        self.noteRadius = noteRadius
    
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
        