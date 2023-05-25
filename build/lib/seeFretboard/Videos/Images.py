import os
from seeFretboard.Utilities.Constants import BASE_PATH

class Images():
    def __init__(self):
        #universal, attributes for all images when you create this
        self.outputPathName = os.path.join(BASE_PATH, 'Outputs', 'Images')
        self.name = "default"
        self.meta = ".png"
        self.fileName = os.path.join(
            self.outputPathName, self.name + self.meta)

    @property
    def outputPathName(self):
        return self._outputPathName

    @outputPathName.setter
    def outputPathName(self, path):
        self._outputPathName = path
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def meta(self):
        return self._meta

    @meta.setter
    def meta(self, meta):
        self._meta = meta

    @property
    def fileName(self):
        return os.path.join(self.outputPathName, self.name + self.meta)


    @fileName.setter
    def fileName(self, fileName):
        self._fileName = fileName
