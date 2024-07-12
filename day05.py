# Read input from "input.txt" and convert it to a list of integers
with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]

def run(p):
    # Helper function to get the parameter based on the mode
    def get(offset):
        mode = (instruction // 10 ** (1 + offset)) % 10
        if mode == 0:
            return p[index + offset]  # Position mode
        elif mode == 1:
            return index + offset  # Immediate mode
        else:
            assert False, f"invalid mode: {mode}"

    index = 0  # Initialize instruction pointer
    while True:
        instruction = p[index]  # Get the current instruction
        opcode = instruction % 100  # Extract the opcode

        if opcode == 1:  # add
            p[get(3)] = p[get(1)] + p[get(2)]  # Perform addition
            index += 4  # Move to the next instruction
        elif opcode == 2:  # mult
            p[get(3)] = p[get(1)] * p[get(2)]  # Perform multiplication
            index += 4  # Move to the next instruction
        elif opcode == 3:  # input
            p[get(1)] = int(input("enter: "))  # Read input from user
            index += 2  # Move to the next instruction
        elif opcode == 4:  # output
            print(f"output: {p[get(1)]}")  # Output the value
            index += 2  # Move to the next instruction
        elif opcode == 5:  # jump nonzero
            if p[get(1)] != 0:
                index = p[get(2)]  # Jump to the address if non-zero
            else:
                index += 3  # Move to the next instruction
        elif opcode == 6:  # jump zero
            if p[get(1)] == 0:
                index = p[get(2)]  # Jump to the address if zero
            else:
                index += 3  # Move to the next instruction
        elif opcode == 7:  # less than
            p[get(3)] = int(p[get(1)] < p[get(2)])  # Perform less-than comparison
            index += 4  # Move to the next instruction
        elif opcode == 8:  # equals
            p[get(3)] = int(p[get(1)] == p[get(2)])  # Perform equality comparison
            index += 4  # Move to the next instruction
        elif opcode == 99:  # halt
            print("halt")  # Halt the program
            break  # Exit the loop
        else:
            assert False, f"invalid opcode: {opcode}"  # Handle invalid opcode

run(inp)  # Execute the program with the input
