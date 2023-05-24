class NotePosition():
    def __init__(self, string, fret):
        self.string = string
        self.fret = fret
    
    def getFret(self):
        return self.fret
    
    def setFret(self, fret):
        self.fret = fret
    
    def getString(self):
        return self.string
    
    def setString(self, string):
        self.string = string