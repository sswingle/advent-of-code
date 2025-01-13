from utils import read_input_int_csv, IntcodeComputer


def run_with_inputs(program, noun, verb):
    computer = IntcodeComputer(program)
    computer.memory[1] = noun
    computer.memory[2] = verb
    computer.run()
    return computer.memory[0]


program = read_input_int_csv(2)

# part 1
print(run_with_inputs(program, 12, 2))

# part 2
for noun in range(100):
    for verb in range(100):
        if run_with_inputs(program, noun, verb) == 19690720:
            print(noun, verb)
            break
