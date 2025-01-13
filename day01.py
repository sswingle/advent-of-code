from utils import read_input_lines


def calculate_frequency(changes: list[str]) -> int:
    """Calculate the final frequency after applying all changes.
    
    Args:
        changes: List of strings with format "+N" or "-N" where N is an integer
        
    Returns:
        The final frequency after applying all changes
    """
    frequency = 0
    for change in changes:
        # Remove any leading '+' and convert to int
        frequency += int(change)
    return frequency


def find_first_repeat(changes: list[str]) -> int:
    """Find the first frequency that's reached twice.
    
    Args:
        changes: List of strings with format "+N" or "-N" where N is an integer
        
    Returns:
        The first frequency that's reached twice
    """
    seen = {0}  # Set of frequencies we've seen, starting with 0
    frequency = 0
    
    while True:  # Keep repeating the list until we find a duplicate
        for change in changes:
            frequency += int(change)
            if frequency in seen:
                return frequency
            seen.add(frequency)


def main():
    # Read frequency changes from input file
    changes = read_input_lines(1)
    
    # Part 1: Calculate final frequency
    final_frequency = calculate_frequency(changes)
    print(f"Part 1 - Final frequency: {final_frequency}")
    
    # Part 2: Find first repeated frequency
    first_repeat = find_first_repeat(changes)
    print(f"Part 2 - First repeated frequency: {first_repeat}")


if __name__ == "__main__":
    main()
