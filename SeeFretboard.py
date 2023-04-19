from bokeh.plotting import figure, show
from bokeh.models import Line, Circle, Label, Button, CustomJS, Slider, Range1d, ColumnDataSource
from bokeh.models.widgets import TextInput
from bokeh.layouts import layout
from bokeh.events import ButtonClick
from bokeh.io import export_png, export_svg, curdoc
from bokeh.layouts import row
from bokeh.document import without_document_lock

import pretty_midi
import tempfile
import sox
import soundfile as sf

import os
import glob
import re

import ffmpeg
import cv2

from Note import Note
from Video import Video


class SeeFretboard():

    # default values
    def __init__(self, hv="h", strings=6, fretFrom=1, fretsTo=12, showTuning=True):
        # horizontal or vertical fretboard
        self.hv = hv

        self.tuning = ['E', 'A', 'D', 'G', 'B', 'E']
        self.numOfStrings = strings
        self.fretFrom = fretFrom
        self.fretTo = fretsTo
        self.numOfFrets = self.fretTo - self.fretFrom

        self.showTuning = showTuning
        self.showFretboardNumber = True

       # fretboard parameters
        self.distanceBetweenFrets = 5
        self.distanceBetweenStrings = 2
        self.fretColor = "black"
        self.stringsColor = "black"
        self.fretOpacity = 0.3
        self.stringsOpactiy = 1

        self.fretboardMarkerColor = "#DCDCDC"
        # note
        self.note = Note()
        self.notes = []

        # figure attribute
        self.fig = figure()
        self.figHorXRange = Range1d(-8*self.note.getNoteRadius(),
                                    (self.getNumOfFrets()+1.3)*self.distanceBetweenFrets)
        self.figHorYRange = Range1d(-3*self.note.getNoteRadius(),
                                    self.distanceBetweenStrings*self.numOfStrings)
        self.figVerXRange = Range1d(-3*self.note.getNoteRadius(),
                                    self.distanceBetweenStrings*self.numOfStrings)
        self.figVerYRange = Range1d(-8*self.note.getNoteRadius(),
                                    (self.getNumOfFrets()+2)*self.distanceBetweenFrets)

        if (self.hv == "h"):
            self.fig.width = 800
            self.fig.height = 400
            self.fig.x_range = self.figHorXRange
            self.fig.y_range = self.figHorYRange

        else:
            self.fig.width = 400
            self.fig.height = 800
            self.fig.x_range = self.figVerXRange
            self.fig.y_range = self.figVerYRange

        self.imagePathName = os.path.join(os.getcwd(), 'Image')

        self.imageName = "default"

        # buttons
        self.tuningLabelButton = Button(
            label="Toggle Tuning", button_type="success")
        self.fretLabelButton = Button(
            label="Toggle Fretboard Number", button_type="success")
        self.fretBoardDirectionButton = Button(
            label="Toggle Fretboard Direction", button_type="success")
        self.toggleButtons = row(
            self.fretBoardDirectionButton, self.tuningLabelButton, self.fretLabelButton)
        self.inputChordInput = TextInput(
            value="-1,0,5,5,0,0", title="Enter Notes Fret:")
        self.inputChordButton = Button(label="ENTER ", button_type="success")
        self.clearFretboardButton = Button(
            label="Clear Fretboard ", button_type="success")
        self.notesOptions = row(
            self.inputChordInput, self.inputChordButton, self.clearFretboardButton)

        self.inputChordButton.on_click(self.inputChordButtonClicked)
        self.clearFretboardButton.on_click(self.clearFretboard)

        # video parameter
        self.video = Video(0, 10, 0, 0.1)
        self.videoFrames = self.video.frames

        self.timeslider = Slider(start=self.video.startTime, end=self.video.endTime,
                                 value=self.video.currentFrame, step=self.video.frameStep, title="Time")
        # self.timeslider.on_change('value', self.sliderTimeCallback)

        self.playButton = Button(label="Play")
        self.playButton.on_click(self.playButtonClicked)
        self.playing = False

    def inputChordButtonClicked(self):
        self.updateFretboard(self.inputChordInput.value)

    # video related
    def playButtonClicked(self):
        if (self.playing):
            self.playButton.label = "Play"
            self.playing = False
        else:
            self.playButton.label = "Pause"
            self.playing = True
            while (self.playing != False):
                self.updatingFretboardAnimation()

    @without_document_lock
    def updatingFretboardAnimation(self):

        if (self.video.currentFrame >= self.video.endTime):
            self.playButton.label = "Play"
            self.playing = False
            self.video.currentFrame = 0

            self.updateFretboard(str(list(self.video.frames.values())[0]))
            return

        # if in the frame there is a chord draw chord
        if (self.video.getCurrentFrame() in self.video.frames.keys()):
            currentChord = self.video.frames[self.video.currentFrame]
            self.updateFretboard(currentChord)

        newCurrentFrame = self.video.getCurrentFrame()+self.video.getFrameStep()
        self.video.setCurrentFrame(newCurrentFrame)

        self.timeslider.update(
            start=0, end=3, value=self.video.getCurrentSecond(), step=self.video.frameStep)

    # def sliderTimeCallback(self, attr, old, new):
    #     self.video.setCurrentFrame(self.timeslider.value)
    #     for i in range(self.video.getFramesLength):
    #         key1, key2 = list(self.video.getFramesKeys)[i:i+2]
    #         if (self.timeslider.value > key1 and self.timeslider.value < key2 ):
    #             self.updateFretboard(self.video.getFrame(key1))

    def setVideo(self, video):
        self.video = video
        self.timeslider.update(start=self.video.getStartTime(), end=self.video.getEndTime(
        ), value=self.video.getCurrentFrame(), step=self.video.getFrameStep())

    def getVideo(self):
        return self.video

    # the frames are in frets
    def saveMidi(self, frames):
        midi = pretty_midi.PrettyMIDI()
        inst = pretty_midi.Instrument(program=25)
        time = 0

        for frame in frames:
            for i, note in enumerate(frame):
                if (note != -1):
                    n = pretty_midi.Note(velocity=100,
                                         pitch=note, start=time,
                                         end=time + self.video.getFramePeriod()
                                         )

                    inst.notes.append(n)
            time += self.video.getFramePeriod()
        midi.instruments.append(inst)

        return midi

    def sonifyJams(self, frames):
        midi = self.saveMidi(frames)
        signal_out = midi.fluidsynth(fs=44100.0)
        path = os.path.join(
            os.getcwd(), "testmidiAudio.wav")
        self.saveSmallWav(path, signal_out, 44100)
        return signal_out, 44100

    def saveSmallWav(self, out_path, y, fs):
        fhandle, tmp_file = tempfile.mkstemp(suffix='.wav')

        sf.write(tmp_file, y, fs)

        tfm = sox.Transformer()
        tfm.convert(bitdepth=16)
        tfm.build(tmp_file, out_path)
        os.close(fhandle)
        os.remove(tmp_file)

    def saveAsVideoImages(self):
        oriImgName = self.imageName
        print(oriImgName)
        for k, v in self.video.getFramesItems():
            self.updateFretboard(v)
            self.setImageName(str(k)+oriImgName)
            self.saveAs("png")
            print("saving"+self.getImageName())
        print("done")

    # for guitarset n other data where num of second is not defined
    def saveAsVideoImagesNoSeconds(self):
        oriImgName = self.imageName
        for i in range(len(self.video.getFrames())):
            self.updateFretboard(self.video.getFrames()[i])
            self.setImageName(str(i)+oriImgName)
            self.saveAs("png")
            print("saving"+self.getImageName())
        print("done")

    def deleteAllImages(self):
        files = glob.glob(self.imagePathName)
        for f in files:
            os.remove(f)
        print("All Images Delete")

    def saveAsVideoImagesFromCurrentFrame(self):
        pass

    def saveAsVideoImagesFrom(self, frameFrom, frameTo):
        pass

    def saveAsVideo(self):
        images = os.listdir(self.imagePathName)
        images = sorted(images, key=lambda s: [
                        int(x) if x.isdigit() else x for x in re.split('(\d+)', s)])

        fourcc = cv2.VideoWriter_fourcc(*self.video.getCodec())
        frameSize = (self.fig.width, self.fig.height)
        print(self.video.getFrameRate())
        print("self.video.getFrameRate()")
        videoWriter = cv2.VideoWriter(os.path.join(self.video.getVideoPathName(), self.video.getName(
        )+"."+self.video.getFileExtension()), fourcc, self.video.getFrameRate(), frameSize)

        for image in images:
            frame = cv2.imread(os.path.join(self.getImagePathName(), image))
            videoWriter.write(frame)

        cv2.destroyAllWindows()
        videoWriter.release()

        print("video saved at "+self.video.getVideoPathName())

    def saveAsVideoWithAudio(self):
        self.saveAsVideo()

        videoPath = ffmpeg.input(os.path.join(self.video.getVideoPathName(
        ), self.video.getName()+"."+self.video.getFileExtension()))
        audioPath = ffmpeg.input(self.video.getAudioPathName())

        ffmpeg.concat(videoPath, audioPath, v=1, a=1).output(
            "defaultWithAudio.mp4").run(overwrite_output=True)
        print("video save with audio done")

    # fretboard relate
    def drawTuningLabel(self, distanceStrings, i):
        if (self.hv == "h"):
            string_label = Label(x=-1, y=distanceStrings-self.distanceBetweenStrings,
                                 text=self.tuning[i+1], text_align='center', text_font_size='10pt')
        else:
            string_label = Label(x=distanceStrings, y=self.distanceBetweenFrets*(
                self.getNumOfFrets()+1), text=self.tuning[i+1], text_align='center', text_font_size='10pt')

        string_label.visible = self.showTuning
        self.fig.add_layout(string_label)

        self.tuningLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            stringLabel=string_label), code="""stringLabel.visible = !stringLabel.visible"""))

    def drawFretLabel(self, distanceBetweenFrets, j):
        if (self.hv == "h"):
            fret_label = Label(x=distanceBetweenFrets+self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                               y=-self.note.noteRadius*1.5, text=str(j+1), text_align='center', text_font_size='10pt')
        else:
            fret_label = Label(x=-self.note.noteRadius*1.5, y=distanceBetweenFrets+self.distanceBetweenFrets -
                               self.distanceBetweenFrets/2, text=str(j), text_align='center', text_font_size='10pt')

        fret_label.visible = self.showFretboardNumber
        self.fig.add_layout(fret_label)

        self.fretLabelButton.js_on_event(ButtonClick, CustomJS(args=dict(
            fretLabel=fret_label), code="""fretLabel.visible = !fretLabel.visible"""))

    def drawToggleFretboardDirection(self):
        pass
        # self.clearFretboard()
        # self.fretBoardDirectionButton.js_on_event(ButtonClick, CustomJS(args=dict(hv=self.hv, drawV = self.drawVerticalFretboard, drawH = self.drawHorizontalFretboard),code="""if (hv=="h"){  drawV()} else{ drawH()}"""))

    # preview
    def drawHorizontalFretboard(self):

        x = [0, self.distanceBetweenFrets*(self.fretTo-self.fretFrom+1)]
        y = [0, 0]

        self.drawTuningLabel(self.distanceBetweenStrings, -1)

        self.fig.line(x=x, y=y, line_color=self.stringsColor,
                      line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        # draw strings (horizontal line)
        for i in range(0, self.numOfStrings-1):
            x = [0, self.distanceBetweenFrets*(self.fretTo-self.fretFrom+1)]
            y = [distanceStrings, distanceStrings]

            self.drawTuningLabel(
                distanceStrings+self.distanceBetweenStrings, i)

            distanceStrings += self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor,
                          line_alpha=self.stringsOpactiy)

        distanceBetweenFrets = 0
        # draw frets (vertical line)
        for j in range(self.fretFrom-1, self.fretTo+1):
            fx = [0, self.distanceBetweenStrings*(self.numOfStrings-1)]
            fy = [distanceBetweenFrets, distanceBetweenFrets]

            if (j != self.fretTo):
                self.drawFretLabel(distanceBetweenFrets, j)

            distanceBetweenFrets += self.distanceBetweenFrets
            self.fig.line(x=fy, y=fx, line_color=self.fretColor,
                          line_alpha=self.fretOpacity)

        self.drawInlay()

        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False

    def drawVerticalFretboard(self):
        x = [0, 0]
        y = [0, self.distanceBetweenFrets*(self.getNumOfFrets()+1)]

        self.drawTuningLabel(0, -1)

        self.fig.line(x=x, y=y, line_color=self.stringsColor,
                      line_alpha=self.stringsOpactiy)

        distanceStrings = self.distanceBetweenStrings
        # draw strings (vertical line)
        for i in range(0, self.numOfStrings-1):
            x = [distanceStrings, distanceStrings]
            y = [0, self.distanceBetweenFrets*(self.getNumOfFrets()+1)]

            self.drawTuningLabel(distanceStrings, i)

            distanceStrings += self.distanceBetweenStrings
            self.fig.line(x=x, y=y, line_color=self.stringsColor,
                          line_alpha=self.stringsOpactiy)

        distanceBetweenFrets = (self.getNumOfFrets()+1) * \
            self.distanceBetweenFrets

        fx = [0, self.distanceBetweenStrings*(self.numOfStrings-1)]
        fy = [0, 0]
        self.fig.line(x=fx, y=fy, line_color=self.fretColor,
                      line_alpha=self.fretOpacity)

        # draw frets (horizontal line)
        fretlength = self.fretFrom-1

        for j in range(self.fretFrom, self.fretTo+1):
            fx = [0, self.distanceBetweenStrings*(self.numOfStrings-1)]
            fy = [distanceBetweenFrets, distanceBetweenFrets]

            if (j != self.fretFrom):
                self.drawFretLabel(distanceBetweenFrets, fretlength)

            fretlength += 1
            distanceBetweenFrets -= self.distanceBetweenFrets
            self.fig.line(x=fx, y=fy, line_color=self.fretColor,
                          line_alpha=self.fretOpacity)

        self.drawFretLabel(distanceBetweenFrets, fretlength)

        self.drawInlay()

        self.fig.axis.visible = False
        self.fig.xgrid.visible = False
        self.fig.ygrid.visible = False

    def drawInlay(self):
        # I think I still need to work more on the math for layout on 12th fret
        # vertical note radius is /2, should fix or check up on it later
        if (self.hv == "h"):
            # draw 3,5,7,9 marker
            if (self.fretFrom <= 3 <= self.fretTo):
                markerFret3 = self.fig.circle(x=(3-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                              y=(self.numOfStrings-1) *
                                              self.distanceBetweenStrings/2,
                                              radius=self.note.noteRadius,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 5 <= self.fretTo):
                markerFret5 = self.fig.circle(x=(5-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                              y=(self.numOfStrings-1) *
                                              self.distanceBetweenStrings/2,
                                              radius=self.note.noteRadius,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 7 <= self.fretTo):
                markerFret7 = self.fig.circle(x=(7-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                              y=(self.numOfStrings-1) *
                                              self.distanceBetweenStrings/2,
                                              radius=self.note.noteRadius,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 9 <= self.fretTo):
                markerFret9 = self.fig.circle(x=(9-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                              y=(self.numOfStrings-1) *
                                              self.distanceBetweenStrings/2,
                                              radius=self.note.noteRadius,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 12 <= self.fretTo):
                markerFret12_1 = self.fig.circle(x=(12-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                                 y=(self.numOfStrings) *
                                                 self.distanceBetweenStrings/4,
                                                 radius=self.note.noteRadius,
                                                 fill_color=self.fretboardMarkerColor,
                                                 line_width=self.note.noteLineWidth,
                                                 fill_alpha=self.note.noteFill,
                                                 line_color=self.note.noteEdgeColor)
                markerFret12_2 = self.fig.circle(x=(12-self.fretFrom+1)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                                                 y=(self.numOfStrings) *
                                                 self.distanceBetweenStrings/1.75,
                                                 radius=self.note.noteRadius,
                                                 fill_color=self.fretboardMarkerColor,
                                                 line_width=self.note.noteLineWidth,
                                                 fill_alpha=self.note.noteFill,
                                                 line_color=self.note.noteEdgeColor)

        else:
            if (self.fretFrom <= 3 <= self.fretTo):
                markerFret3 = self.fig.circle(x=(self.numOfStrings-1)*self.distanceBetweenStrings/2,
                                              y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                  3-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                              radius=self.note.noteRadius/2,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 5 <= self.fretTo):
                markerFret5 = self.fig.circle(x=(self.numOfStrings-1)*self.distanceBetweenStrings/2,
                                              y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                  5-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                              radius=self.note.noteRadius/2,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 7 <= self.fretTo):
                markerFret7 = self.fig.circle(x=(self.numOfStrings-1)*self.distanceBetweenStrings/2,
                                              y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                  7-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                              radius=self.note.noteRadius/2,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 9 <= self.fretTo):
                markerFret9 = self.fig.circle(x=(self.numOfStrings-1)*self.distanceBetweenStrings/2,
                                              y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                  9-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                              radius=self.note.noteRadius/2,
                                              fill_color=self.fretboardMarkerColor,
                                              line_width=self.note.noteLineWidth,
                                              fill_alpha=self.note.noteFill,
                                              line_color=self.note.noteEdgeColor)
            if (self.fretFrom <= 12 <= self.fretTo):
                markerFret12_1 = self.fig.circle(x=(self.numOfStrings)*self.distanceBetweenStrings*2/3-self.distanceBetweenStrings/2,
                                                 y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                     12-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                                 radius=self.note.noteRadius/2,
                                                 fill_color=self.fretboardMarkerColor,
                                                 line_width=self.note.noteLineWidth,
                                                 fill_alpha=self.note.noteFill,
                                                 line_color=self.note.noteEdgeColor)
                markerFret12_2 = self.fig.circle(x=(self.numOfStrings)*self.distanceBetweenStrings/3-self.distanceBetweenStrings/2,
                                                 y=self.distanceBetweenFrets*(self.getNumOfFrets()) - self.distanceBetweenFrets*(
                                                     12-self.getFretFrom()-1) - self.distanceBetweenFrets/2,
                                                 radius=self.note.noteRadius/2,
                                                 fill_color=self.fretboardMarkerColor,
                                                 line_width=self.note.noteLineWidth,
                                                 fill_alpha=self.note.noteFill,
                                                 line_color=self.note.noteEdgeColor)
        # self.notes.append(self.fig.add_glyph(circleNote))

    def showFretboard(self):
        layoutF = layout(self.fig, self.timeslider, self.playButton,
                         self.toggleButtons, self.notesOptions)
        curdoc().add_root(layoutF)
        # show(layoutF)

    def closeFretboard(self):
        pass

    def clearFretboard(self):
        notesCopy = list(self.notes)

        for note in notesCopy:
            self.fig.renderers.remove(note)
            self.notes.remove(note)

    def updateFretboard(self, notes):
        self.clearFretboard()
        self.addNotesAllString(notes)

    def getImagePathName(self):
        return self.imagePathName

    def setImagePathName(self, path):
        self.imagePathName = path

    # saveAsImg
    def saveAs(self, meta):
        fileName = os.path.join(
            self.imagePathName, self.getImageName() + "."+meta)
        if (meta.lower() == "png"):
            export_png(self.fig, filename=fileName)

        elif (meta.lower() == "svg"):
            export_svg(self.fig, filename=fileName)

    def getImageName(self):
        return self.imageName

    def setImageName(self, name):
        self.imageName = name

    def setNoteObject(self, note):
        self.note = note

    # user input = string like "1,0,1,1,0,0" which correspond to standard tuning "E,A,D,G,B,E"
    def addNotesAllString(self, notes):
        notes = [(x.strip()) for x in notes.split(',')]
        if (len(notes) == self.numOfStrings):
            for i in range(1, self.numOfStrings+1):
                self.addNote(i, notes[i-1])
        else:
            print("ERROR, WRONG FORMAT.")

    # -1 = x
    def addNote(self, string, fret):
        note = ""

        if (fret != "0" and fret != "-1"):
            fret = int(fret)-self.fretFrom+1

        if (self.hv == "h"):
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                              y=(string-1)*self.distanceBetweenStrings,
                              radius=self.note.noteRadius,
                              fill_color=self.note.noteFaceColor,
                              line_width=self.note.noteLineWidth,
                              line_color=self.note.noteEdgeColor,
                              name="circleNote"
                              )
            elif (fret == "-1"):
                fret = 0
                textX = Label(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                              y=(string-1)*self.distanceBetweenStrings, text='X', text_color="#000000", name="xNote")
                self.fig.add_layout(textX)
            else:
                fret = int(fret)
                note = Circle(x=(fret)*self.distanceBetweenFrets-self.distanceBetweenFrets/2,
                              y=(string-1)*self.distanceBetweenStrings,
                              radius=self.note.noteRadius,
                              fill_color=self.note.noteFaceColor,
                              line_width=self.note.noteLineWidth,
                              line_color=self.note.noteEdgeColor,
                              name="circleNote"
                              )
        else:
            if (fret == "0"):
                fret = int(fret)
                note = Circle(x=(string-1)*self.distanceBetweenStrings,
                              y=self.distanceBetweenFrets *
                              (self.getNumOfFrets()+1) +
                              self.note.getNoteRadius()*4,
                              radius=self.note.noteRadius/2,
                              fill_color=self.note.noteFaceColor,
                              line_width=self.note.noteLineWidth,
                              line_color=self.note.noteEdgeColor,
                              name="circleNote"
                              )
            elif (fret == "-1"):
                fret = 0
                xPos = (string-1)*self.distanceBetweenStrings
                yPos = self.distanceBetweenFrets * \
                    (self.getNumOfFrets()+1)+self.note.getNoteRadius()*5
                symbolSize = self.distanceBetweenStrings/8

                xCor = [xPos - symbolSize, xPos + symbolSize]
                yCor = [yPos - symbolSize*4, yPos + symbolSize]
                source = ColumnDataSource(data=dict(x=xCor, y=yCor))

                lineOne = Line(x="x",
                               y="y", line_width=3)
                yCorFlip = yCor[::-1]
                lineTwo = Line(x="x",
                               y="yFlip", line_width=3)

                source.data["yFlip"] = yCorFlip

                self.notes.append(self.fig.add_glyph(
                    source, lineOne))
                self.notes.append(self.fig.add_glyph(
                    source, lineTwo))
            else:
                fret = int(fret)
                note = Circle(x=(string-1)*self.distanceBetweenStrings,
                              y=self.distanceBetweenFrets *
                              (self.getNumOfFrets()+2) - (fret) *
                              self.distanceBetweenFrets - self.distanceBetweenFrets/2,
                              radius=self.note.noteRadius/2,
                              fill_color=self.note.noteFaceColor,
                              line_width=self.note.noteLineWidth,
                              line_color=self.note.noteEdgeColor,
                              name="circleNote"
                              )
        if (note != ""):
            self.notes.append(self.fig.add_glyph(note))

    def removeNote(self):
        pass

    def getTuning(self):
        return self.tuning

    def setTuning(self, tuning):
        self.tuning = tuning

    def getNumOfStrings(self):
        return self.numOfStrings

    def setNumOfStrings(self, strings):
        self.numOfStrings = strings

    def getFretFrom(self):
        return self.fretFrom

    def setFretFrom(self, frets):
        self.fretFrom = frets

    def getFretTo(self):
        return self.fretTo

    def setFretTo(self, frets):
        self.fretTo = frets

    def getNumOfFrets(self):
        return self.fretTo-self.fretFrom

    def setNumOfFrets(self, l):
        self.numOfFrets = l

    def getShowTuning(self):
        return self.showTuning

    def setShowTuning(self, showTuning):
        self.showTuning = showTuning

    def getDistanceBetweenFrets(self):
        return self.distanceBetweenFrets

    def setDistanceBetweenFrets(self, distanceBetweenFrets):
        self.distanceBetweenFrets = distanceBetweenFrets

    def getDistanceBetweenStrings(self):
        return self.distanceBetweenStrings

    def setDistanceBetweenStrings(self, distanceBetweenStrings):
        self.distanceBetweenStrings = distanceBetweenStrings

    def getFretColor(self):
        return self.fretColor

    def setFretColor(self, fretColor):
        self.fretColor = fretColor

    def getStringsColor(self):
        return self.stringsColor

    def setStringsColor(self, stringsColor):
        self.stringsColor = stringsColor

    def getFretOpacity(self):
        return self.fretOpacity

    def setFretOpacity(self, fretOpacity):
        self.fretOpacity = fretOpacity

    def getStringsOpactiy(self):
        return self.stringsOpactiy

    def setStringsOpacity(self, stringsOpactiy):
        self.stringsOpactiy = stringsOpactiy

    def getFigWidth(self):
        return self.fig.width

    def setFigWidth(self, width):
        self.fig.width = width

    def getFigHeight(self):
        return self.fig.height

    def setFigHeight(self, height):
        self.fig.height = height

    def getFigHorXRange(self):
        return self.figHorXRange

    def setFigHorXRange(self, v1, v2):
        self.figHorXRange = Range1d(v1, v2)

    def getFigHorYRange(self):
        return self.figHorYRange

    def setFigHorYRange(self, v1, v2):
        self.figHorYRange = Range1d(v1, v2)

    def getFigVerXRange(self):
        return self.figVerXRange

    def setFigVerXRange(self, v1, v2):
        self.figVerXRange = Range1d(v1, v2)

    def getFigVerYRange(self):
        return self.figVerYRange

    def setFigVerYRange(self, v1, v2):
        self.figVerYRange = Range1d(v1, v2)
