
# Generated by CodiumAI
from seeFretboard.Designs.FretboardStyle import FretboardTheme
from seeFretboard.Designs.FretboardStyle import FretboardOrientation
from seeFretboard.Designs.FretboardStyle import Tuning
from seeFretboard.Designs.FretboardStyle import FretboardRange
from seeFretboard.Designs.FretboardStyle import FretboardDesign
from seeFretboard.Utilities.Constants import STANDARD_TUNING, STANDARD_TUNING_MIDI

import pytest

"""
Code Analysis

Main functionalities:
The FretboardStyle class is responsible for creating a customizable fretboard design. It combines the properties of the FretboardOrientation, Tuning, FretboardRange, and FretboardDesign classes to create a complete fretboard style.

Methods:
The FretboardStyle class does not have any methods of its own. It relies on the methods of the classes it combines to create the fretboard style.

Fields:
- orientation: an instance of the FretboardOrientation class that determines whether the fretboard is displayed horizontally or vertically
- tuning: an instance of the Tuning class that determines the tuning of the strings on the fretboard
- fretboardRange: an instance of the FretboardRange class that determines the range of frets displayed on the fretboard
- fretboardDesign: an instance of the FretboardDesign class that determines the visual design of the fretboard, including the distance between frets and strings, the color of the frets and strings, and whether to display the tuning and fretboard number.
"""

class TestFretboardStyle:
    # Tests that a FretboardStyle object can be created with all valid inputs. 
    def test_create_fretboard_style_with_all_valid_inputs(self):
        style = FretboardTheme(orientation=FretboardOrientation("horizontal"), tuning=Tuning(letterTuning=STANDARD_TUNING), fretboardRange=FretboardRange(1, 12), fretboardDesign=FretboardDesign())
        assert isinstance(style.orientation, FretboardOrientation)
        assert isinstance(style.tuning, Tuning)
        assert isinstance(style.fretboardRange, FretboardRange)
        assert isinstance(style.fretboardDesign, FretboardDesign)

    # Tests that a FretboardStyle object can be created with only some optional inputs. 
    def test_create_fretboard_style_with_some_optional_inputs(self):
        style = FretboardTheme(tuning=Tuning(letterTuning=STANDARD_TUNING), fretboardRange=FretboardRange(1, 12))
        assert isinstance(style.orientation, FretboardOrientation)
        assert isinstance(style.tuning, Tuning)
        assert isinstance(style.fretboardRange, FretboardRange)
        assert isinstance(style.fretboardDesign, FretboardDesign)

    # Tests that a FretboardStyle object cannot be created with an invalid orientation input. 
    def test_create_fretboard_style_with_invalid_orientation_input(self):
        with pytest.raises(ValueError):
            style = FretboardTheme(orientation="invalid")

    # Tests that a FretboardStyle object cannot be created with an invalid tuning input. 
    def test_create_fretboard_style_with_invalid_tuning_input(self):
        with pytest.raises(TypeError):
            style = FretboardTheme(tuning="invalid")

    # Tests that a FretboardStyle object cannot be created with an invalid fretboard range input. 
    def test_create_fretboard_style_with_invalid_fretboard_range_input(self):
        with pytest.raises(ValueError):
            style = FretboardTheme(fretboardRange=FretboardRange(0, 12))

    # Tests that a FretboardStyle object cannot be created with an invalid fretboard design input. 
    def test_create_fretboard_style_with_invalid_fretboard_design_input(self):
        with pytest.raises(TypeError):
            style = FretboardTheme(fretboardDesign="invalid")

    # Tests that a FretboardStyle object has an orientation property.  
    def test_fretboard_style_has_orientation_property(self):
        style = FretboardTheme()
        assert hasattr(style, "orientation")

    # Tests that a FretboardStyle object can set and get properties for each of its components.  
    def test_fretboard_style_can_set_and_get_properties(self):
        style = FretboardTheme(orientation=FretboardOrientation(orientation="v"), tuning=Tuning(numOfStrings=7), fretboardRange=FretboardRange(1, 12), fretboardDesign=FretboardDesign(distanceBetweenFrets=6))
        assert style.orientation.orientation == "v"
        assert style.tuning.numOfStrings == 7
        assert style.fretboardRange.fretFrom == 1
        assert style.fretboardDesign.distanceBetweenFrets == 6

    # Tests the interaction between the FretboardStyle object and its components.  
    def test_fretboard_style_components_interaction(self):
        style = FretboardTheme(orientation="h", tuning=Tuning(numOfStrings=4), fretboardRange=FretboardRange(1, 5), fretboardDesign=FretboardDesign(distanceBetweenFrets=3))
        assert style.orientation.orientation == "h"
        assert style.tuning.numOfStrings == 4
        assert style.fretboardRange.fretFrom == 1
        assert style.fretboardRange.numOfFrets == 4
        assert style.fretboardDesign.distanceBetweenFrets == 3
        assert style.fretboardDesign.showTuning == True

    # Tests the behavior of the Tuning class.   
    def test_tuning_class_behavior(self):
        # Test default values
        tuning = Tuning()
        assert tuning.letterTuning == STANDARD_TUNING
        assert tuning.midiTuning == STANDARD_TUNING_MIDI
        assert tuning.numOfStrings == 6

        # Test custom values
        tuning = Tuning(letterTuning=['D', 'G', 'C', 'F', 'A', 'D'], midiTuning=[38, 43, 48, 53, 57, 62], numOfStrings=6)
        assert tuning.letterTuning == ['D', 'G', 'C', 'F', 'A', 'D']
        assert tuning.midiTuning == [38, 43, 48, 53, 57, 62]
        assert tuning.numOfStrings == 6

    # Tests the behavior of the FretboardRange class.   
    def test_fretboard_range_class_behavior(self):
        # Test valid input
        fretboardRange = FretboardRange(1, 12)
        assert fretboardRange.fretFrom == 1
        assert fretboardRange.fretTo == 12
        assert fretboardRange.numOfFrets == 11

        # Test invalid input
        with pytest.raises(ValueError):
            fretboardRange = FretboardRange(-1, 12)
        with pytest.raises(ValueError):
            fretboardRange = FretboardRange(12, 1)

    # Tests the behavior of the FretboardDesign class.    
    def test_fretboard_design_class_behavior(self):
        design = FretboardDesign()
        assert design.showTuning == True
        assert design.showFretboardNumber == True
        assert design.distanceBetweenFrets == 5
        assert design.distanceBetweenStrings == 2
        assert design.fretColor == "black"
        assert design.stringsColor == "black"
        assert design.fretOpacity == 0.3
        assert design.stringsOpacity == 1
        assert design.fretboardMarkerColor == "#DCDCDC"

    # Tests that the fretboardDesign property getter returns the correct value.    
    def test_fretboard_design_property_getter(self):
        style = FretboardTheme(fretboardDesign=FretboardDesign(showTuning=False))
        assert style.fretboardDesign.showTuning == False