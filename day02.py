# This script processes an input list of integers according to specific rules and finds specific outputs.

# Read the input file and convert it to a list of integers.
with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]

# Function to process the list of integers with given parameters a and b.
def run(ints, a, b):
    # Create a copy of the list to avoid modifying the original input.
    ints = list(ints)
    # Set the value at position 1 to parameter a.
    ints[1] = a
    # Set the value at position 2 to parameter b.
    ints[2] = b
    # Process the list in chunks of 4 elements.
    for i in range(0, len(ints), 4):
        # Unpack the operation and positions from the current chunk.
        op, a, b, c = ints[i : i + 4]
        # If the operation is 1, perform addition.
        if op == 1:
            ints[c] = ints[a] + ints[b]
        # If the operation is 2, perform multiplication.
        elif op == 2:
            ints[c] = ints[a] * ints[b]
        # If the operation is 99, halt the processing.
        elif op == 99:
            break
        # If the operation is unknown, raise an assertion error.
        else:
            assert False
    # Return the value at position 0 after processing.
    return ints[0]

# Part 1: Run the function with fixed parameters and print the result.
print(run(inp, 12, 2))

# Part 2: Find the parameters a and b that produce the output 19690720.
for a in range(100):
    # Iterate over possible values for parameter a.
    for b in range(100):
        # Iterate over possible values for parameter b.
        # Run the function with the current parameters a and b.
        out = run(list(inp), a, b)
        # Check if the output matches the target value.
        if out == 19690720:
            # If the output matches, print the parameters a and b.
            print(a, b)
