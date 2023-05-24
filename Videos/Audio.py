import pretty_midi
import tempfile
import sox
import soundfile as sf
import os

class Audio:
    """A class for working with audio files and MIDI data."""

    def __init__(self, audioPath):
        """
        Initialize an Audio object.

        Args:
            audioPath (str): The path to the audio file.
        """
        self.sampleRate = 44100
        self.audioPath = audioPath
    
    def saveMidi(self, frames):
        """
        Convert frames to MIDI and save as a PrettyMIDI object, which would be a MIDI file.

        Args:
            frames (list): List of frames representing audio data. Each frame contains information about the pitch, start, and end time.

        Returns:
            pretty_midi.PrettyMIDI: The generated MIDI object.
        """
        midi = pretty_midi.PrettyMIDI()
        inst = pretty_midi.Instrument(program=25)

        for frame in frames:
            n = pretty_midi.Note(velocity=100,
                                 pitch=frame.getPitch(), start=frame.getStartTime(),
                                 end=frame.getEndTime()
                                 )
            inst.notes.append(n)
        midi.instruments.append(inst)

        return midi

    def sonifyJams(self, frames):
        """
        Convert frames to MIDI, synthesize audio, and save as a WAV file.

        Args:
            frames (list): List of frames representing audio data.

        Returns:
            tuple: A tuple containing the synthesized audio signal and the sample rate.
        """
        midi = self.saveMidi(frames)
        signal_out = midi.fluidsynth(fs=44100.0)
        path = self.audioPath
        self.saveSmallWav(path, signal_out, self.sampleRate)
        return signal_out, self.sampleRate

    def saveSmallWav(self, out_path, y, fs):
        """
        Save the audio signal as a WAV file.

        Args:
            out_path (str): The output file path.
            y (numpy.ndarray): The audio signal.
            fs (int): The sample rate.
        """
        fhandle, tmp_file = tempfile.mkstemp(suffix='.wav')

        sf.write(tmp_file, y, fs)

        tfm = sox.Transformer()
        tfm.convert(bitdepth=16)
        tfm.build(tmp_file, out_path)
        os.close(fhandle)
        os.remove(tmp_file)

    @property
    def sampleRate(self):
        """Get the sample rate."""
        return self._sampleRate

    @sampleRate.setter
    def sampleRate(self, value):
        """Set the sample rate."""
        self._sampleRate = value

    @property
    def audioPath(self):
        """Get the audio path."""
        return self._audioPath

    @audioPath.setter
    def audioPath(self, value):
        """Set the audio path."""
        self._audioPath = value