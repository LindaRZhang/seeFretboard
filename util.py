import music21 

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
