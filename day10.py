import itertools as it
from math import atan2, gcd, pi

with open("input.txt") as f:
    rows = [[c == "#" for c in row.strip()] for row in f.readlines()]


def iter_positions():
    return it.product(range(len(rows)), range(len(rows[0])))


def get_astroids_from(r, c):
    astroids = []
    for r2, c2 in iter_positions():
        if not rows[r2][c2] or (r2, c2) == (r, c):
            continue
        dr, dc = r2 - r, c2 - c
        d = gcd(dr, dc)
        num_blocking = sum(
            rows[r + k * dr // d][c + k * dc // d] for k in range(1, d)
        )
        astroids.append((r2, c2, num_blocking))
    return astroids


# part 1
max_seen, base = sorted(
    [
        (sum(x[2] == 0 for x in get_astroids_from(r, c)), (r, c))
        for r, c in iter_positions()
        if rows[r][c]
    ]
)[-1]
print(max_seen)

# part 2
r, c, _ = sorted(
    get_astroids_from(*base),
    key=lambda t: (t[2], atan2(t[1] - base[1], -t[0] + base[0]) % (2 * pi),),
)[199]
print(r * 100 + c)
