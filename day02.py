with open("input.txt") as f:
    inp = [int(x) for x in f.read().split(",")]


def run(ints, a, b):
    ints = list(ints)
    ints[1] = a
    ints[2] = b
    for i in range(0, len(ints), 4):
        op, a, b, c = ints[i : i + 4]
        if op == 1:
            ints[c] = ints[a] + ints[b]
        elif op == 2:
            ints[c] = ints[a] * ints[b]
        elif op == 99:
            break
        else:
            assert False
    return ints[0]


# part 1
print(run(inp, 12, 2))

# part 2
for a in range(100):
    for b in range(100):
        out = run(list(inp), a, b)
        if out == 19690720:
            print(a, b)
