import os
from tqdm import tqdm
from PIL import Image
import re
import ffmpeg
import cv2

from bokeh.io import export_png, export_svg
import glob

class VideoManager():
    def __init__(self, fretboard, video, images, imageProgressBar=True):
        self.fretboard = fretboard
        self.video = video
        self.images = images
        self.imageProgressBar = imageProgressBar

    def saveAsVideoImages(self):
        oriImgName = self.images.name
        print(oriImgName)
        for k, v in self.video.getFramesItems():
            self.fretboard.updateFretboard(v)
            self.images.name = str(k)+oriImgName
            self.saveImage()
            print("saving"+self.images.name)
        print("done")

    # for guitarset n other data where num of second is not defined
    def saveAsVideoImagesNoSeconds(self):
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
        self.saveAsVideo()

        videoPath = ffmpeg.input(
            self.video.getVideoPathWithName()+self.video.getFileExtension())
        audioPath = ffmpeg.input(self.video.getAudioPathWithName())


        ffmpeg.concat(videoPath, audioPath, v=1, a=1).output(
            self.video.getVideoWAudioPathWithName()).run(overwrite_output=True)
        print("video save with audio done")

    def saveVideoWithAudio(self):
        videoPath = ffmpeg.input(
            self.video.getVideoPathWithName()+self.video.getFileExtension())
        audioPath = ffmpeg.input(self.video.getAudioPathWithName())

        ffmpeg.concat(videoPath, audioPath, v=1, a=1).output(
            self.video.getVideoName(
            )+".mp4").run(overwrite_output=True)
        print("video save with audio done")
    
    def saveImage(self):
        if (self.images.meta.lower() == ".png"):
            export_png(self.fretboard.getFretboardFig().fig, filename=self.images.fileName)

        elif (self.images.meta.lower() == ".svg"):
            export_svg(self.fretboard.getFretboardFig().fig, filename=self.images.fileName)


    def deleteAllImages(self):
        files = glob.glob(os.path.join(self.images.outputPathName, "*"))
        for f in files:
            os.remove(f)
        print("All Images Delete")

        
    @property
    def imageProgressBar(self):
        return self._imageProgressBar

    @imageProgressBar.setter
    def imageProgressBar(self, imageProgressBar):
        self._imageProgressBar = imageProgressBar