import sys
from pathlib import Path

# Add parent directory to path so we can import day01
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from day01 import calculate_frequency, find_first_repeat


def test_calculate_frequency():
    """Test frequency calculation with example cases from the problem"""
    # Test case 1: +1, -2, +3, +1 = 3
    assert calculate_frequency(["+1", "-2", "+3", "+1"]) == 3
    
    # Test case 2: +1, +1, +1 = 3
    assert calculate_frequency(["+1", "+1", "+1"]) == 3
    
    # Test case 3: +1, +1, -2 = 0
    assert calculate_frequency(["+1", "+1", "-2"]) == 0
    
    # Test case 4: -1, -2, -3 = -6
    assert calculate_frequency(["-1", "-2", "-3"]) == -6


def test_find_first_repeat():
    """Test finding first repeated frequency with example cases"""
    # Test case from detailed example: +1, -2, +3, +1 reaches 2 twice
    assert find_first_repeat(["+1", "-2", "+3", "+1"]) == 2
    
    # Additional test cases from part 2
    assert find_first_repeat(["+1", "-1"]) == 0
    assert find_first_repeat(["+3", "+3", "+4", "-2", "-4"]) == 10
    assert find_first_repeat(["-6", "+3", "+8", "+5", "-6"]) == 5
    assert find_first_repeat(["+7", "+7", "-2", "-7", "-4"]) == 14


def test_with_input_file(tmp_path):
    """Test with a small input file"""
    # Create a temporary input file
    input_file = tmp_path / "input.txt"
    input_file.write_text("+1\n-2\n+3\n+1\n")
    
    # Run main and capture output
    import day01
    from io import StringIO
    import sys
    
    # Redirect stdout to capture output
    old_stdout = sys.stdout
    sys.stdout = mystdout = StringIO()
    
    # Temporarily set the input file path
    import os
    os.environ["AOC_INPUT_PATH"] = str(input_file)
    
    # Run main
    day01.main()
    
    # Get output and restore stdout
    output = mystdout.getvalue()
    sys.stdout = old_stdout
    
    # Verify output contains both part 1 and part 2 results
    assert "Part 1 - Final frequency: 3" in output
    assert "Part 2 - First repeated frequency: 2" in output
    
    # Clean up
    del os.environ["AOC_INPUT_PATH"]