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


def main():
    # Read frequency changes from input file
    changes = read_input_lines(1)
    
    # Calculate final frequency (Part 1)
    final_frequency = calculate_frequency(changes)
    print(f"Final frequency: {final_frequency}")


if __name__ == "__main__":
    main()
