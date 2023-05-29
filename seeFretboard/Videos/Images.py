import os
from seeFretboard.Utilities.Constants import BASE_PATH

class Images():
    '''
    The Images class is designed to create and manage image files. 
    It allows the user to set the output path, name, and file type 
    of the image, and automatically generates a file name based on 
    these parameters. The class also includes getter and setter methods 
    for each attribute, allowing for easy modification of the image properties.
    
    Attributes:
        outputPathName (str): The output path name where the image will be saved.
        name (str): The name of the image.
        meta (str): The file extension or meta information of the image.
        fileName (str): The full file path and name of the image.
    '''
    def __init__(self):
        """
        Initializes an Images object with default attribute values.
        """
        self.outputPathName = os.path.join(BASE_PATH, 'Outputs', 'Images')
        self.name = "default"
        self.meta = ".png"
        self.fileName = os.path.join(self.outputPathName, self.name + self.meta)

    @property
    def outputPathName(self):
        """
        Gets or sets the output path name where the image will be saved.

        Returns:
            str: The output path name.
        """
        return self._outputPathName

    @outputPathName.setter
    def outputPathName(self, path):
        """
        Sets the output path name where the image will be saved.

        Args:
            path (str): The output path name.
        """
        self._outputPathName = path
    
    @property
    def name(self):
        """
        Gets or sets the name of the image.

        Returns:
            str: The name of the image.
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of the image.

        Args:
            name (str): The name of the image.
        """
        self._name = name

    @property
    def meta(self):
        """
        Gets or sets the file extension or meta information of the image.

        Returns:
            str: The file extension or meta information.
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """
        Sets the file extension or meta information of the image.

        Args:
            meta (str): The file extension or meta information.
        """
        self._meta = meta

    @property
    def fileName(self):
        """
        Gets or sets the full file path and name of the image.

        Returns:
            str: The full file path and name.
        """
        return os.path.join(self.outputPathName, self.name + self.meta)

    @fileName.setter
    def fileName(self, fileName):
        """
        Sets the full file path and name of the image.

        Args:
            fileName (str): The full file path and name.
        """
        self._fileName = fileName