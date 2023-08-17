import music21 
from .Constants import *
from bokeh.io import export_png, export_svg

#helper functions

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

def fretToMidi(stringMidi, fret):
    """Converts a fret number on a string to a MIDI note number.
    
    Args:
        string (int): The string number, is the midi string corresponding to that string the fret is on.
        fret (int): The fret number on the string. 
        
    Returns:
        midi (int): The MIDI note number corresponding to the fret on the string.
    """
    print(fret,"fret")
    if(isinstance(fret, str) and fret.lower() == "x"):
        return "x"
    else:
        return int(stringMidi) + int(fret)
    
def midisToNoteNameWithOctaves(midiNote):
    """Converts a list of MIDI note number to a list of note name with octave.
    
    Args:
        midiNote (list): The list of MIDI note number.
        
    Returns:
        noteNameWithOctave (list): The list of note name and octave (e.g. "C4", "F#5") corresponding to the MIDI note number.
    """
    nameOctaves = []
    for midiNote in midiNote:
        octave = midiToNoteNameWithOctave(midiNote)
        nameOctaves.append(octave)

    return nameOctaves

def noteNameToMidi(noteName):
    """Converts a note name to a MIDI note number.
    
    Args:
        noteName (str): The note name (e.g. "C", "F#").
        
    Returns:
        midiNote (int): The MIDI note number corresponding to the note name.
    """
    octave = 2  # Assuming standard guitar tuning starting from the 2nd octave
    note = music21.note.Note()
    note.pitch.nameWithOctave = noteName + str(octave)
    midiNote = note.pitch.midi
    return midiNote


def noteNamesToMidis(noteNames):
    """Converts a list of note names to a list of corresponding MIDI note numbers.
    
    Args:
        noteNames (list): The list of note names (e.g. ["C", "F#"]).
        
    Returns:
        midiNotes (list): The list of MIDI note numbers corresponding to the note names.
    """
    midiNotes = []
    for noteName in noteNames:
        midiNote = noteNameToMidi(noteName)
        midiNotes.append(midiNote)

    return midiNotes

def midiToNoteNameWithOctave(midiNote):
    """Converts a MIDI note number to a note name with octave.
    
    Args:
        midiNote (int): The MIDI note number.
        
    Returns:
        noteNameWithOctave (str): The note name and octave (e.g. "C4", "F#5") corresponding to the MIDI note number.
    """
    if(isinstance(midiNote, str) and midiNote.lower() == "x"):
        nameWithOctave = "x"
    else:
        note = music21.note.Note()
        note.pitch.midi = float(midiNote)
        nameWithOctave = note.nameWithOctave
    return nameWithOctave

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
        pos = shape[type + "Position"][i]

        if not(isinstance(pos, str) and pos.lower() == 'x'):
            pos = int(pos) + interval

        processedShape["note"][type].append(newNote)
        processedShape["position"][type].append(str(pos))

    return processedShape

def processDropShape(drop, rootNote, type, string, shapePos):
    """
    Processes a drop shape by calculating the corresponding notes, positions, and scale degrees.

    Args:
        drop (str): The drop shape name.
        rootNote (str): The root note of the shape.
        type (str): The type of the chord: maj7, dom7, min7, min7b5, dim7
        string (str): The string of the shape.
        shapePos (str): The position of the shape.

    Returns:
        processedShape (dict): A dictionary containing the processed shape information. It has the following structure:
        {
            "note": {
                type: [list of notes]
            },
            "position": {
                type: [list of positions]
            },
            "scaleDegree": {
                type: [list of scale degrees]
            }
        }
    """
    shape = DROPShapes[drop]

    interval = calculateHalfSteps("c", rootNote)

    processedShape = {
        "note": {},
        "position": {},
        "scaleDegree": {}
    }

    processedShape["note"][type] = []
    processedShape["position"][type] = []
    processedShape["scaleDegree"][type] = shape[drop+"String"+string][type + "ScaleDegree"+shapePos]
    for i in range(len(processedShape["scaleDegree"][type])):
        note = shape[drop+"String"+string][type + "Note" + str(shapePos)][i]
        newNote = getNoteFromInterval(note, interval, rootNote)
        pos = shape[drop+"String"+string][type + "Position"+shapePos][i]

        if not(isinstance(pos, str) and pos.lower() == 'x'):
            pos = int(pos) + interval

        processedShape["note"][type].append(newNote)
        processedShape["position"][type].append(str(pos))

    return processedShape

def checkChordType(type,seve=False):
    """
    Checks if the provided chord type is valid.

    Args:
        type (str): The chord type to check.
        seve (bool): If True, check for valid chord types for seventh chords.

    Raises:
        ValueError: If the provided chord type is not valid.
    """
    type = type.lower()
    if seve:
        if type not in ["dom7", "dim7", "maj7", "min7","min7b5"]:
            raise ValueError("Invalid chord type provided.")
    
    if type not in ["maj", "min", "dim", "aug", "dom7", "dim7", "maj7", "min7","min7b5"]:
        raise ValueError("Invalid chord type provided.")

def ifInDict(value, dictionary):
    """
    Checks if a value is present in a dictionary.

    Args:
        value: The value to check.
        dictionary (dict): The dictionary to check.

    Raises:
        ValueError: If the value is not present in the dictionary.
    """
    if value.upper() not in dictionary.keys():
        raise ValueError("Invalid "+value+" in "+getDictionaryName(dictionary))

def getDictionaryName(dictionary):
    """
    Returns the name of a dictionary.

    Args:
        dictionary (dict): The dictionary.

    Returns:
        name (str): The name of the dictionary.
    """
    for name, value in globals().items():
        if value is dictionary:
            return name
    return None

def saveImage(fretboardFig, fileName, meta):
        """
        Saves the fretboard visualization as an image.

        This method saves the current state of the fretboard visualization as an image file.
        The image format is determined by the file extension specified in the Images object.
        png and svg for now.

        Raises:
            FileNotFoundError: If the output directory specified in the Images object does not exist.
        """
        if (meta.lower() == "png"):
            export_png(fretboardFig, filename=fileName)

        elif (meta.lower() == "svg"):
            export_svg(fretboardFig, filename=fileName)
        
        print("IMAGE SAVED")

class customShapes():
    """
    A class representing a collection of custom shapes.

    Custom shapes can be added to the collection and retrieved based on their shape name.

    Attributes:
        customShapes (dict): A dictionary containing custom guitar shapes.
            The dictionary structure should be as follows:
            {
                shapeName1: {
                    note: [list of notes],
                    position: [list of positions],
                    scaleDegree: [list of scale degrees]
                },
                shapeName2: {
                    note: [list of notes],
                    position: [list of positions],
                    scaleDegree: [list of scale degrees]
                },
                ...
            }
    """
    def __init__(self):
        """
        Initializes a new instance of the CustomShape class.
        """
        self.customShapes = {

        }
        
    def addShape(self, shapeName, notes, positions, scaleDegrees):
        """Add a custom guitar shape to the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.
            notes (list): A list of notes for the custom shape.
            positions (list): A list of positions for the custom shape.
            scale_degrees (list): A list of scale degrees for the custom shape.

        Returns:
            None
        """
        self.customShapes[shapeName] = {
            'note': notes,
            'position': positions,
            'scaleDegree': scaleDegrees
        }

    def getShape(self, shapeName):
        """Retrieve a custom guitar shape from the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.

        Returns:
            dict: A dictionary representing the custom shape, containing the following keys:
                - 'note': List of notes
                - 'position': List of positions
                - 'scaleDegree': List of scale degrees
        """
        return self.customShapes.get(shapeName, None)

    def removeShape(self, shapeName):
        """Remove a custom guitar shape from the customShapes dictionary.

        Args:
            shape_name (str): The name of the custom shape.

        Returns:
            bool: True if the shape was successfully removed, False otherwise.
        """
        if shapeName in self.customShapes:
            del self.customShapes[shapeName]
            return True
        else:
            return False
        
    