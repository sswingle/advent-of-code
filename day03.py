with open("input.txt") as f:
    paths = [[(s[0], int(s[1:])) for s in l.split(",")] for l in f.readlines()]


def get_step_dict(path):
    steps = 0
    step_dict = {}
    x, y = 0, 0
    for d, n in path:
        for _ in range(n):
            if d == "R":
                x += 1
            elif d == "L":
                x -= 1
            elif d == "U":
                y += 1
            elif d == "D":
                y -= 1
            steps += 1
            step_dict[(x, y)] = steps
    return step_dict


dict1, dict2 = [get_step_dict(p) for p in paths]
min_dist = float("inf")
min_steps = float("inf")
for pos in dict1.keys() & dict2.keys():
    min_dist = min(abs(pos[0]) + abs(pos[1]), min_dist)
    min_steps = min(dict1[pos] + dict2[pos], min_steps)

print(min_dist)
print(min_steps)
