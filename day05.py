with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]


def run(p):
    def get(offset):
        mode = (instruction // 10 ** (1 + offset)) % 10
        if mode == 0:
            return p[index + offset]
        elif mode == 1:
            return index + offset
        else:
            assert False, f"invalid mode: {mode}"

    index = 0
    while True:
        instruction = p[index]
        opcode = instruction % 100

        if opcode == 1:  # add
            p[get(3)] = p[get(1)] + p[get(2)]
            index += 4
        elif opcode == 2:  # mult
            p[get(3)] = p[get(1)] * p[get(2)]
            index += 4
        elif opcode == 3:  # input
            p[get(1)] = int(input("enter: "))
            index += 2
        elif opcode == 4:  # output
            print(f"output: {p[get(1)]}")
            index += 2
        elif opcode == 5:  # jump nonzero
            if p[get(1)] != 0:
                index = p[get(2)]
            else:
                index += 3
        elif opcode == 6:  # jump zero
            if p[get(1)] == 0:
                index = p[get(2)]
            else:
                index += 3
        elif opcode == 7:  # less than
            p[get(3)] = int(p[get(1)] < p[get(2)])
            index += 4
        elif opcode == 8:  # equals
            p[get(3)] = int(p[get(1)] == p[get(2)])
            index += 4
        elif opcode == 99:  # halt
            print("halt")
            break
        else:
            assert False, f"invalid opcode: {opcode}"


run(inp)
