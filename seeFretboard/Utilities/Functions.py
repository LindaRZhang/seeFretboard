import music21 
from .Constants import *

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

def calculateHalfSteps(startNote, endNote):
    """
    Calculates the number of half steps between two notes, considering enharmonic equivalents.

    Args:
        startNote (str): The starting note.
        endNote (str): The ending note.

    Returns:
        int: The number of half steps from startNote to endNote. Returns 0 if startNote and endNote are the same.
    """

    noteIndices = {}
    for i, sublist in enumerate(chromaticWEnharmonicScaleFindDistance):
        for note in sublist:
            noteIndices[note.upper()] = i

    startIndex = noteIndices.get(startNote.upper())
    endIndex = noteIndices.get(endNote.upper())

    if startIndex is None or endIndex is None:
        raise ValueError("Invalid startNote or endNote.")

    numNotes = len(chromaticWEnharmonicScaleFindDistance)
    distance = (endIndex - startIndex) % numNotes
    
    if distance < 0:
            distance += numNotes

    return distance

def getNoteFromInterval(note, interval, rootNote):
    """
    Returns a new note that is the given interval away from the input note.

    Args:
        note (str): The starting note.
        interval (int): The interval (number) indicating the distance from the starting note.

    Returns:
        str: The new note that is interval away from the input note. Will be in # unless it is the root note
    """
    print("getnote",note, rootNote, interval)
    for i, sublist in enumerate(chromaticWEnharmonicScaleFindDistance):
        if note.upper() in [sub.upper() for sub in sublist]:
            noteIndex = i
            newIndex = (noteIndex + interval) % len(chromaticWEnharmonicScaleFindDistance)
            newSublist = chromaticWEnharmonicScaleFindDistance[newIndex]
            newNote = newSublist[0]
            if len(newSublist) > 1 and newNote.upper() != rootNote.upper():
                newNote = newSublist[1]

            return newNote

    return None  # Note not found


def processCAGEDShape(caged, rootNote, type="major"):
    """
    Process a CAGED shape for a given root note and type.

    Args:
        caged (str): The CAGED shape to process ('c', 'a', 'g', 'd', etc.).
        rootNote (str): The root note.
        type (str, optional): The type of chord or scale. Defaults to 'major'.

    Raises:
        ValueError: If an invalid CAGED shape is provided.
        ValueError: If the given type does not exist in the shape.

    Returns:
        dict: The processed CAGED shape information.
    """
    shape = cagedShapes[caged]

    if type+"Note" not in shape:
        raise ValueError(f"Invalid type '{type}' provided for CAGED shape '{caged}'")

    interval = calculateHalfSteps(shape["name"], rootNote)
    print(shape["name"], rootNote, "interval", interval)

    processedShape = {
        "name": shape["name"],
        "note": {},
        "position": {},
        "scaleDegree": {}
    }

    processedShape["note"][type] = []
    processedShape["position"][type] = []
    processedShape["scaleDegree"][type] = shape[type + "ScaleDegree"]

    for i in range(len(shape[type + "Note"])):
        newNote = getNoteFromInterval("".join(shape[type + "Note"][i].split()), interval, rootNote)
        print("newNote", newNote)
        pos = shape[type + "Position"][i]
        print(shape[type + "Position"])

        if not(isinstance(pos, str) and pos.lower() == 'x'):
            pos = int(pos) + interval

        processedShape["note"][type].append(newNote)
        processedShape["position"][type].append(str(pos))

    return processedShape
