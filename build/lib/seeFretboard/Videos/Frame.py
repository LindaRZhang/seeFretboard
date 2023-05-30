class Frame:
    """
    The Frame class is designed to represent a frame in a video. 
    It stores the frame rate and frame period, which are important parameters
    for determining the timing and smoothness of the animation. 
    The main functionalities of the class are to set and get the frame rate 
    and frame period, which can be used to control the speed and duration of the video.

    Args:
        frameRate (int or float): The frame rate of the frame.

    Attributes:
        frameRate (int or float): The frame rate of the frame.
        framePeriod (float): The time duration of each frame in seconds.
    """

    def __init__(self, frameRate):
        """
        Initializes a Frame object with the specified frame rate.

        Args:
            frameRate (int or float): The frame rate of the frame.
        """
        self.frameRate = frameRate
        self.framePeriod = 1 / self.frameRate

    def getFrameRate(self):
        """
        Returns the frame rate of the frame.

        Returns:
            int or float: The frame rate of the frame.
        """
        return self.frameRate

    def setFrameRate(self, fr):
        """
        Sets the frame rate of the frame.

        Args:
            fr (int or float): The new frame rate for the frame.
        """
        self.frameRate = fr

    def getFramePeriod(self):
        """
        Returns the time duration of each frame.

        Returns:
            float: The time duration of each frame in seconds.
        """
        return 1 / self.frameRate

    def setFramePeriod(self, fp):
        """
        Sets the time duration of each frame.

        Args:
            fp (float): The new frame period for the frame in seconds.
        """
        self.framePeriod = fp
