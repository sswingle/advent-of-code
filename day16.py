import itertools as it

import numpy as np

with open("input.txt") as f:
    data = list(map(int, f.read().strip()))


def p(i):
    ms = it.cycle(it.chain(*[it.repeat(a, i + 1) for a in [0, 1, 0, -1]]))
    next(ms)
    return ms


# part 1
d = list(data)
for _ in range(100):
    d = [abs(sum(a * b for a, b in zip(d, p(i)))) % 10 for i in range(len(d))]
print("".join(map(str, d[:8])))

# part 2
offset = int("".join(map(str, data[:7])))
d2 = np.array((data * (10000 - offset // len(data)))[offset % len(data) :])
for _ in range(100):
    d2 = (d2 + d2.sum() - d2.cumsum()) % 10
print("".join(map(str, d2[:8])))
