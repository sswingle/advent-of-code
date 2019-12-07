import itertools as it

with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]


def run(p, phase, next_input):
    def get(offset):
        mode = (instruction // 10 ** (1 + offset)) % 10
        if mode == 0:
            return p[index + offset]
        elif mode == 1:
            return index + offset
        else:
            assert False, f"invalid mode: {mode}"

    p = list(p)
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
            if phase is None:
                p[get(1)] = next_input
            else:
                p[get(1)] = phase
                phase = None
            index += 2
        elif opcode == 4:  # output
            to_yield = p[get(1)]
            next_input = yield to_yield
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
            break
        else:
            assert False, f"invalid opcode: {opcode}"


def run_phases(phases, feedback):
    gens = []
    out = 0
    for amp in it.cycle(range(5)):
        if len(gens) < amp + 1:
            gens.append(run(inp, phases[amp], out))
            out = next(gens[amp])
        else:
            try:
                out = gens[amp].send(out)
            except StopIteration:
                return out
        if amp == 4 and not feedback:
            return out


print(max(run_phases(perm, False) for perm in it.permutations(range(5))))
print(max(run_phases(perm, True) for perm in it.permutations(range(5, 10))))

# 34686
# 36384144
