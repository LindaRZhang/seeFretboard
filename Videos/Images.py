import os
from bokeh.io import export_png, export_svg
from Utilities.Constants import BASE_PATH

class Images():
    def __init__(self, figure):
        #universal, attributes for all images when you create this
        self.outputPathName = os.path.join(BASE_PATH, 'Outputs', 'Images')
        self.name = "default"
        self.meta = ".png"
        self.imageProgressBar = True
        self.fileName = os.path.join(
            self.outputPathName, self.name + self.meta)

        #Fretboard Figure
        self.figure = figure
    
    # def saveImage(self):#save 1 image
    #     fileName = os.path.join(
    #         self.imagePathName, self.getImageName() + self.getImageMeta())
    #     if (self.getImageMeta().lower() == ".png"):
    #         export_png(self.fretboardFig.fig, filename=fileName)

    #     elif (self.getImageMeta().lower() == ".svg"):
    #         export_svg(self.fretboardFig.fig, filename=fileName)

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
    def imageProgressBar(self):
        return self._imageProgressBar

    @imageProgressBar.setter
    def imageProgressBar(self, imageProgressBar):
        self._imageProgressBar = imageProgressBar

    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, fileName):
        self._fileName = fileName
