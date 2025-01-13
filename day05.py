from utils import read_input_int_csv, IntcodeComputer

# Read program from input file
program = read_input_int_csv(5)

# Create computer instance
computer = IntcodeComputer(program)

# Run program with input 1 for part 1
# The computer will print outputs as it runs
outputs = computer.run([1])
print("Final outputs:", outputs)
