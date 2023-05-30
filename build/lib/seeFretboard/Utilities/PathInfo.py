import os
from seeFretboard.Utilities.Constants import BASE_PATH

class PathInfo():
    def __init__(self, name, path):
        """
        Initializes a PathInfo object with the specified name and path.

        Args:
            name (str): The name of the path.
            path (str): The path.
        """
        self.path = path
        self.name = name
        self.pathWithName = os.path.join(self.path, self.name)

    @property
    def path(self):
        """
        The path.

        Returns:
            str: The path.
        """
        return self._path

    @path.setter
    def path(self, value):
        """
        Sets the path.

        Args:
            value (str): The path.
        """
        self._path = value

    @property
    def name(self):
        """
        The name of the path.

        Returns:
            str: The name of the path.
        """
        return self._name

    @name.setter
    def name(self, value):
        """
        Sets the name of the path.

        Args:
            value (str): The name of the path.
        """
        self._name = value

    def getPathWithName(self):
        """
        Returns the path concatenated with the name.

        Returns:
            str: The path concatenated with the name.
        """
        return os.path.join(self._path, self._name)

    def setPathWithName(self, value):
        """
        Sets the path and name based on the provided value.

        Args:
            value (str): The value representing the path and name.
        """
        # Split the provided value to separate path and name
        directory, filename = os.path.split(value)
        self._path = directory
        self._name = filename


class EmbedPathInfo(PathInfo):
    def __init__(self, name="default.html"):
        """
        Initializes an EmbedPathInfo object with the specified name and default path.

        Args:
            name (str): The name of the embed path (default is 'default.html').
        """
        self.path = os.path.join(BASE_PATH, 'Outputs', 'Embeds')
        self.name = name
        self.pathWithName = os.path.join(self.path, self.name)
