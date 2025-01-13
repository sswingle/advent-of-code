import sys
from pathlib import Path

# Add parent directory to path so we can import day01
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from day01 import calculate_frequency


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
    
    # Verify output
    assert "Final frequency: 3" in output
    
    # Clean up
    del os.environ["AOC_INPUT_PATH"]