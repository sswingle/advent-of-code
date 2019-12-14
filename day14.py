from collections import Counter as C
from math import ceil as c

with open("input.txt") as f:
    r = dict()
    for i, o in [l.strip().split(" => ") for l in f.readlines()]:
        r[(o := o.split())[1]] = {
            t: -int(q) if t != "ORE" else int(q)
            for q, t in [s.split() for s in i.split(", ")]
        }
        r[o[1]][o[1]] = int(o[0])


def o(f):
    n = C({"FUEL": f})
    while (m := n.most_common(1)[0])[1] > 0:
        n.subtract({t: c(m[1] / r[m[0]][m[0]]) * r[m[0]][t] for t in r[m[0]]})
    return -n["ORE"]


# part 1
print(o(1))

# part 2
b = [1, m := 10 ** 12, m]
while b[0] + 1 < b[1]:
    b[o(mid) > b[2]] = (mid := sum(b[:2]) // 2)
print(b[0])
