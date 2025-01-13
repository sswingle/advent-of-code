import os
from pathlib import Path
from utils import read_input_ints


def calculate_fuel(mass: int) -> int:
    """Calculate fuel required for a given mass."""
    return mass // 3 - 2


def calculate_total_fuel(mass: int) -> int:
    """Calculate total fuel required including fuel for the fuel."""
    total = 0
    while (mass := mass // 3 - 2) > 0:
        total += mass
    return total


def main():
    # Use environment variable for input path if set, otherwise use default
    input_path = os.getenv("AOC_INPUT_PATH", "input/day01.txt")
    masses = read_input_ints(1)

    # Part 1: Calculate basic fuel requirements
    part1_result = sum(calculate_fuel(m) for m in masses)
    print(f"Part 1: {part1_result}")

    # Part 2: Calculate total fuel requirements
    part2_result = sum(calculate_total_fuel(m) for m in masses)
    print(f"Part 2: {part2_result}")


if __name__ == "__main__":
    main()
