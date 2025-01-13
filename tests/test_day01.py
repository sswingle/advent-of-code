import os
import sys
from pathlib import Path

# Add parent directory to path so we can import day01
sys.path.append(str(Path(__file__).parent.parent))

import pytest
from day01 import calculate_fuel, calculate_total_fuel


def test_calculate_fuel():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583


def test_calculate_total_fuel():
    assert calculate_total_fuel(14) == 2
    assert calculate_total_fuel(1969) == 966
    assert calculate_total_fuel(100756) == 50346


def test_with_input_file(tmp_path):
    # Create a temporary input file
    input_file = tmp_path / "input.txt"
    input_file.write_text("12\n1969\n")
    
    # Temporarily set the input file path
    os.environ["AOC_INPUT_PATH"] = str(input_file)
    
    # Import the module again to use the new input file
    import importlib
    import day01
    importlib.reload(day01)
    
    # Clean up
    del os.environ["AOC_INPUT_PATH"]