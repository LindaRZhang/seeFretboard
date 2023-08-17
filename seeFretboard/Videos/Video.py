import os
from .Frame import Frame
from seeFretboard.Utilities.Constants import BASE_PATH, FRAMERATE

class Video(Frame):
    """
    The Video class is designed to represent a video and inherits from the Frame class. 
    It stores information about the video such as the start and end times, current frame,
    frame step, video name, file extension, codec, and audio name. The main functionalities
    of the class are to add frames to the video, set and get the video properties, and save the video.
    
    Attributes:
        frames (dict): A dictionary of frames with their corresponding time frames.
        currentAddTabFrames (int): The number of frames added through the `addTab` method.
        fileExtension (str): The file extension of the video.
        codec (str): The video codec.
        videoPath (str): The path to the video directory.
        videoName (str): The name of the video.
        videoPathWithName (str): The path to the video file.
        audioPath (str): The path to the audio directory.
        audioName (str): The name of the audio file.
        audioPathWithName (str): The path to the audio file.
        videoWAudioPath (str): The path to the video with audio directory.
        videoWAudioName (str): The name of the video with audio.
        videoWAudioPathWithName (str): The path to the video with audio file.
    """
    def __init__(self, frameRate=FRAMERATE, videoName="defaultVid", fileExtension=".mp4", codec="mp4v", videoWAudioName="defaultVideoWAudio"):
        super().__init__(frameRate)

        # format = {{frameNumber:chordString},{0:"5,0,5,5,0,0"},{1:"5,0,5,5,0,0"}}
        self.frames = {}

        self.currentAddTabFrames = 0
        self.fileExtension = fileExtension
        self.codec = codec

        # paths
        self.videoPath = os.path.join(BASE_PATH, 'Outputs', 'Videos')
        self.videoName = videoName
        self.videoPathWithName = os.path.join(self.videoPath, self.videoName)
        
        self.audioPath = os.path.join(BASE_PATH, 'GuitarSet',"audio_mono-pickup_mix")
        self.audioName = ""
        self.audioPathWithName = os.path.join(self.audioPath, self.audioName)

        self.videoWAudioPath = os.path.join(BASE_PATH, 'Outputs', 'Videos')
        self.videoWAudioName = videoWAudioName
        self.videoWAudioPathWithName = os.path.join(self.videoWAudioPath, self.videoWAudioName+fileExtension)

    def getVideoPathName(self):
        """
        Get the path of the video file.

        Returns:
            str: The video path.
        """
        return self.videoPath

    def setVideoPathName(self, path):
        """
        Set the path of the video file.

        Args:
            path (str): The video path.
        """
        self.videoPath = path

    def getAudioPathName(self):
        """
        Get the path of the audio file.

        Returns:
            str: The audio path.
        """
        return self.audioPath

    def setAudioPathName(self, path):
        """
        Set the path of the audio file.

        Args:
            path (str): The audio path.
        """
        self.audioPath = path

    def getVideoWAudioPathName(self):
        """
        Get the path of the video file with audio.

        Returns:
            str: The video path with audio.
        """
        return self.videoWAudioPath

    def setVideoWAudioPathName(self, path):
        """
        Set the path of the video file with audio.

        Args:
            path (str): The video path with audio.
        """
        self.videoWAudioPath = path

    def getCurrentSecond(self):
        """
        Get the current second of the video based on the current frame and frame rate.

        Returns:
            float: The current second.
        """
        return self.currentFrame / self.frameRate

    def addFrame(self, timeFrame, notes):
        """
        Add a frame with notes to the video.

        Args:
            timeFrame (float): The time frame of the frame.
            notes: The notes associated with the frame.
        """
        timeFrame = round(timeFrame, 2)
        self.frames[timeFrame] = notes

    def removeFrame(self, timeFrame):
        """
        Remove a frame from the video.

        Args:
            timeFrame (float): The time frame of the frame to remove.
        """
        del self.frames[timeFrame]

    def getFrame(self, frame):
        """
        Get the notes associated with a specific frame.

        Args:
            frame (float): The frame to get the notes for.

        Returns:
            object: The notes associated with the frame.
        """
        return self.frames[frame]

    def getFrames(self):
        """
        Get all the frames of the video.

        Returns:
            dict: A dictionary of frames with their associated notes.
        """
        return self.frames

    def setFrames(self, frames):
        """
        Set the frames of the video.

        Args:
            frames (dict): A dictionary of frames with their associated notes.
        """
        self.frames = frames

    def getFramesItems(self):
        """
        Get the frames as (timeFrame, notes) pairs.

        Returns:
            dict_items: The frames as (timeFrame, notes) pairs.
        """
        return self.frames.items()

    def getFramesLength(self):
        """
        Get the number of frames in the video.

        Returns:
            int: The number of frames.
        """
        return len(self.frames)

    def getFramesKeys(self):
        """
        Get the time frames of all the frames.

        Returns:
            list: A list of time frames.
        """
        return self.frames.keys()

    def getFramesValues(self):
        """
        Get the notes of all the frames.

        Returns:
            list: A list of notes.
        """
        return self.frames.values()

    def getCodec(self):
        """
        Get the video codec.

        Returns:
            str: The video codec.
        """
        return self.codec

    def setCodec(self, codec):
        """
        Set the video codec.

        Args:
            codec (str): The video codec.
        """
        self.codec = codec

    def getFileExtension(self):
        """
        Get the file extension of the video.

        Returns:
            str: The file extension.
        """
        return self.fileExtension

    def setFileExtension(self, ext):
        """
        Set the file extension of the video.

        Args:
            ext (str): The file extension.
        """
        self.fileExtension = ext

    def getVideoName(self):
        """
        Get the name of the video file.

        Returns:
            str: The video name.
        """
        return self.videoName

    def setVideoName(self, name):
        """
        Set the name of the video file.

        Args:
            name (str): The video name.
        """
        self.videoName = name

    def getAudioName(self):
        """
        Get the name of the audio file.

        Returns:
            str: The audio name.
        """
        return self.audioName

    def setAudioName(self, name):
        """
        Set the name of the audio file.

        Args:
            name (str): The audio name.
        """
        self.audioName = name

    def getVideoWAudioName(self):
        """
        Get the name of the video file with audio.

        Returns:
            str: The video name with audio.
        """
        return self.videoWAudioName

    def setVideoWAudioName(self, name):
        """
        Set the name of the video file with audio.

        Args:
            name (str): The video name with audio.
        """
        self.videoWAudioName = name

    def getVideoPathWithName(self):
        """
        Get the full path of the video file.

        Returns:
            str: The full video path.
        """
        return os.path.join(self.videoPath, self.videoName)

    def setVideoPathWithName(self, path):
        """
        Set the full path of the video file.

        Args:
            path (str): The full video path.
        """
        self.videoPathWithName = path

    def getAudioPathWithName(self):
        """
        Get the full path of the audio file.

        Returns:
            str: The full audio path.
        """
        return os.path.join(self.audioPath, self.audioName)

    def setAudioPathWithName(self, path):
        """
        Set the full path of the audio file.

        Args:
            path (str): The full audio path.
        """
        self.audioPathWithName = path

    def getVideoWAudioPathWithName(self):
        """
        Get the full path of the video file with audio.

        Returns:
            str: The full video path with audio.
        """
        return os.path.join(self.videoWAudioPath, self.videoWAudioName+self.fileExtension)

    def setVideoWAudioPathWithName(self, path):
        """
        Set the full path of the video file with audio.

        Args:
            path (str): The full video path with audio.
        """
        self.videoWAudioPath = path

