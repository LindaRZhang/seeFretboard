import os
from tqdm import tqdm
from PIL import Image
import re
import ffmpeg
import cv2

from bokeh.io import export_png, export_svg
import glob

class VideoManager():
    """
    The VideoManager class provides functionalities to manage video and image files. 
    It allows the user to save video frames as images, generate a video from saved images,
    create a video with audio, and delete all saved images. It also provides options to 
    display a progress bar while generating images and to set the output file format for 
    images.

    Attributes:
        fretboard (Fretboard): The Fretboard object.
        video (Video): The Video object.
        images (Images): The Images object.
        imageProgressBar (bool): Flag indicating whether to display a progress bar while generating images.
    """
    def __init__(self, fretboard, video, images, imageProgressBar=True):
        self.fretboard = fretboard
        self.video = video
        self.images = images
        self.imageProgressBar = imageProgressBar

    def saveAsVideoImages(self):
        """
        Saves video frames as images.

        This method iterates over the frames of the video and saves each frame as an image.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        oriImgName = self.images.name
        print(oriImgName)
        for k, v in self.video.getFramesItems():
            self.fretboard.updateFretboard(v)
            self.images.name = str(k)+oriImgName
            self.saveImage()
            print("saving"+self.images.name)
        print("done")

    # 
    def saveAsVideoImagesNoSeconds(self):
        """
        Saves video frames as images when the number of seconds is not defined.
        For guitarset and other data where number of second is not defined

        This method saves video frames as images without considering the number of seconds.
        It uses a dictionary to track previously saved frames to avoid duplicate saving.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        oriImgName = self.images.name
        images = {}
        print("IMAGES Generateing")
        for i in tqdm(range(len(self.video.getFrames())), disable=not(self.imageProgressBar)):
            frame = self.video.getFrames()[i]
            self.images.name = str(i)+oriImgName

            if frame in images:
                image = images[frame]
                image.copy().save(os.path.join(
                    self.images.outputPathName, self.images.name + self.images.meta))
            else:
                self.fretboard.updateFretboard(self.video.getFrames()[i])
                self.saveImage()
                image = Image.open(os.path.join(
                    self.images.outputPathName, self.images.name + self.images.meta))
                images[frame] = image.copy()
        print("IMAGES Generate done")

    def saveAsVideo(self):
        """
        Generates a video from saved images.

        This method reads the saved images, orders them based on their filenames, and
        creates a video from the ordered frames.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        images = os.listdir(self.images.outputPathName)
        images = sorted(images, key=lambda s: [
                        int(x) if x.isdigit() else x for x in re.split('(\d+)', s)])

        fourcc = cv2.VideoWriter_fourcc(*self.video.getCodec())
        frameSize = (self.fretboard.fretboardFig.fig.width, self.fretboard.fretboardFig.fig.height)

        videoWriter = cv2.VideoWriter(self.video.getVideoPathWithName(
        )+self.video.getFileExtension(), fourcc, self.video.getFrameRate(), frameSize)

        for image in images:
            frame = cv2.imread(os.path.join(self.images.outputPathName, image))
            videoWriter.write(frame)

        cv2.destroyAllWindows()
        videoWriter.release()

        print("VIDEO " + self.video.getVideoName() +
              " saved at "+self.video.getVideoPathName())

    def createVideoWithAudio(self):
        """
        Creates a video with audio.

        This method combines the video file and audio file into a single video file with audio.

        Raises:
            FileNotFoundError: If the video or audio files specified in the Video object do not exist.
        """
        self.saveAsVideo()

        videoPath = ffmpeg.input(
            self.video.getVideoPathWithName()+self.video.getFileExtension())
        audioPath = ffmpeg.input(self.video.getAudioPathWithName())


        ffmpeg.concat(videoPath, audioPath, v=1, a=1).output(
            self.video.getVideoWAudioPathWithName()).run(overwrite_output=True)
        print("video save with audio done")

    def saveVideoWithAudio(self):
        """
        Saves a video with audio.

        This method combines the video file and audio file into a single video file with audio
        and saves it with a specified name.

        Raises:
            FileNotFoundError: If the video or audio files specified in the Video object do not exist.
        """
        videoPath = ffmpeg.input(
            self.video.getVideoPathWithName()+self.video.getFileExtension())
        audioPath = ffmpeg.input(self.video.getAudioPathWithName())

        ffmpeg.concat(videoPath, audioPath, v=1, a=1).output(
            self.video.getVideoName(
            )+".mp4").run(overwrite_output=True)
        print("video save with audio done")
    
    def saveImage(self):
        """
        Saves the fretboard visualization as an image.

        This method saves the current state of the fretboard visualization as an image file.
        The image format is determined by the file extension specified in the Images object.
        png and svg for now.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        if (self.images.meta.lower() == ".png"):
            export_png(self.fretboard.getFretboardFig().fig, filename=self.images.fileName)

        elif (self.images.meta.lower() == ".svg"):
            export_svg(self.fretboard.getFretboardFig().fig, filename=self.images.fileName)


    def deleteAllImages(self):
        """
        Deletes all saved images.

        This method deletes all image files in the output directory specified in the Images object.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        files = glob.glob(os.path.join(self.images.outputPathName, "*"))
        for f in files:
            os.remove(f)
        print("All Images Delete")

        
    @property
    def imageProgressBar(self):
        """
        bool: Flag indicating whether to display a progress bar while generating images.
        """
        return self._imageProgressBar

    @imageProgressBar.setter
    def imageProgressBar(self, imageProgressBar):
        """
        Setter for the imageProgressBar property.

        Args:
            imageProgressBar (bool): Flag indicating whether to display a progress bar while generating images.
        """
        self._imageProgressBar = imageProgressBar