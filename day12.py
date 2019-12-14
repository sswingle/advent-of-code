from functools import reduce
from math import gcd

import numpy as np

with open("input.txt") as f:
    pss = [
        [int(s.split("=")[1]) for s in line[:-1].split(",")]
        for line in f.read().splitlines()
    ]

pss = np.array(pss).T
vss, cycles = np.zeros_like(pss), np.zeros(3, int)
energy = i = 0
while not cycles.all():
    i += 1
    vss += np.clip(pss[:, None] - pss[:, :, None], -1, 1).sum(2)
    pss += vss
    cycles += (cycles == 0) * (np.abs(vss).sum(1) == 0) * 2 * i
    energy += (i == 1000) * (np.abs(pss).sum(0) * np.abs(vss).sum(0)).sum()
print(energy, reduce(lambda a, b: a * b // gcd(a, b), cycles))
