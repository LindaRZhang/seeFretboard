import os
from Utilities.Constants import BASE_PATH

class PathInfo():
    def __init__(self, name, path):
        self.path = path
        self.name = name
        self.pathWithName = os.path.join(self.path, self.name)

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def getPathWithName(self):
        return os.path.join(self._path, self._name)

    def setPathWithName(self, value):
        # Split the provided value to separate path and name
        directory, filename = os.path.split(value)
        self._path = directory
        self._name = filename

class EmbedPathInfo(PathInfo):
    def __init__(self, name="default.html"):
     self.path = os.path.join(BASE_PATH, 'Outputs', 'Embeds')
     self.name = name
     self.pathWithName = os.path.join(self.path, self.name)