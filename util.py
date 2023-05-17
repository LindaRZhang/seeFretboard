import music21 

#scale degree, later can add b or #
scaleDegrees = ["1", "b2", "2", "b3", "3", "4", "b5", "5", "b6", "6", "b7", "7","1"]

#notes
chromaticNotes = ["A","A#/Bb","B","C","C#/Db","D","D#/Eb","E","F","F#/Gb","G","G#/Ab"]

#solfeges
chromaticSolfeges = ["do","di","re","ri","mi","fa","fi","sol","si","la","li","ti"]

#intervals
allInterval = ["P1", "m2", "M2", "m3", "M3", "P4", "#4", "P5", "m6", "M6", "m7", "M7", "P8", "m9", "M9", "m10", "M10", "P11", "#11", "P12", "m13", "M13", "m14", "M14", "m15", "M15", "P16"]

#common tunings in notes
STANDARD_TUNING = ['E', 'A', 'D', 'G', 'B', 'E']
DROP_D_TUNING = ['D', 'A', 'D', 'G', 'B', 'E']
OPEN_G_TUNING = ['D', 'G', 'D', 'G', 'B', 'D']
DADGAD_TUNING = ['D', 'A', 'D', 'G', 'A', 'D']
EBEEBE_TUNING = ['E', 'B', 'E', 'E', 'B', 'E']
OPEN_D_TUNING = ['D', 'A', 'D', 'F#', 'A', 'D']
OPEN_E_TUNING = ['E', 'B', 'E', 'G#', 'B', 'E']
OPEN_A_TUNING = ['E', 'A', 'E', 'A', 'C#', 'E']
OPEN_C_TUNING = ['C', 'G', 'C', 'G', 'C', 'E']
DROP_C_TUNING = ['C', 'G', 'C', 'F', 'A', 'D']
OPEN_B_TUNING = ['B', 'F#', 'B', 'F#', 'B', 'D#']
#in midi
STANDARD_TUNING_MIDI = [40, 45, 50, 55, 59, 64]
DROP_D_TUNING_MIDI = [38, 45, 50, 55, 59, 64]
OPEN_G_TUNING_MIDI = [38, 43, 47, 55, 59, 62]
DADGAD_TUNING_MIDI = [38, 45, 50, 55, 57, 62]
EBEEBE_TUNING_MIDI = [40, 47, 50, 50, 47, 50]
OPEN_D_TUNING_MIDI = [38, 45, 50, 54, 57, 62]
OPEN_E_TUNING_MIDI = [40, 47, 50, 56, 59, 64]
OPEN_A_TUNING_MIDI = [40, 45, 40, 45, 49, 52]
OPEN_C_TUNING_MIDI = [36, 43, 36, 43, 36, 40]
DROP_C_TUNING_MIDI = [36, 43, 36, 41, 45, 50]
OPEN_B_TUNING_MIDI = [35, 42, 35, 42, 35, 39]

def intervalsToScaleDegrees(intervals):
    """Converts a list of intervals to scale degrees.
    
    Args:
        intervals (list): A list of interval names (e.g. "M3", "P5")
        
    Returns: 
        scaleDegrees (list): The list of scale degrees (e.g. "3", "5") corresponding to the intervals.
    """
    scaleDegrees = []
    for i in intervals:
        scaleDegrees.append(intervalToScaleDegree(i))
    return scaleDegrees

def scaleDegreesToIntervals(degrees):
    """Converts a list of scale degrees to intervals.
    
    Args:
        degrees (list): A list of scale degree numbers (e.g. "3", "5") 
        
    Returns:
        intervals (list): The list of interval names (e.g. "M3", "P5") corresponding to the scale degrees.
    """
    intervals = []
    for i in degrees:
        intervals.append(scaleDegreeToInterval(i))
    return intervals

def intervalToScaleDegree(interval):
    """Converts an interval name to a scale degree.
    
    Args:
        interval (str): The interval name (e.g. "M3", "P5")
        
    Returns:
        degree (str): The scale degree (e.g. "3", "5") corresponding to the interval.
    """
    index = allInterval.index(interval)
    scaleDegree = scaleDegrees[index % 12] 
    
    return scaleDegree

def scaleDegreeToInterval(degree):
    """Converts a scale degree to an interval name.
    
    Args:
        degree (str): The scale degree (e.g. "3", "5")
        
    Returns:
        interval (str): The interval name (e.g. "M3", "P5") corresponding to the scale degree.
    """
    return allInterval[scaleDegrees.index(degree)]

def midiToFret(string, midiNotes):
        """Converts a MIDI note number to a fret number for a given string.
    
        Args:
            string (int): The string number, where 1 is the highest pitch string.
            midiNotes (list): The list of MIDI note numbers for each string, from lowest to highest pitch.
            
        Returns:
            fret (int): The fret number corresponding to the MIDI note on the given string.
        """
        notes = []
        for m in midiNotes:
            fret = round(abs(int(string) - int(m)))
            notes.append(fret)

        return notes

def fretsToMidi(string, frets):
    """Converts a list of frets on a string to MIDI note numbers.
    
    Args:
        string (int): The string number, where 1 is the highest pitch string.
        frets (list): The list of fret numbers on the string.
        
    Returns:
        midiNotes (list): The list of MIDI note numbers corresponding to the frets.
    """
    midiNotes = []
    for fret in frets:
        midi = fretToMidi(string,fret)
        midiNotes.append(midi)

    return midiNotes

def fretToMidi(string, fret):
    """Converts a fret number on a string to a MIDI note number.
    
    Args:
        string (int): The string number, where 1 is the highest pitch string.
        fret (int): The fret number on the string. 
        
    Returns:
        midi (int): The MIDI note number corresponding to the fret on the string.
    """
    midi = int(string) + int(fret)
    
    return midi

def midiToNoteNameWithOctave(midiNote):
    """Converts a MIDI note number to a note name with octave.
    
    Args:
        midiNote (int): The MIDI note number.
        
    Returns:
        noteNameWithOctave (str): The note name and octave (e.g. "C4", "F#5") corresponding to the MIDI note number.
    """
    note = music21.note.Note()
    note.pitch.midi = midiNote
    return note.nameWithOctave
