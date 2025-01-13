from utils import read_input_lines, Point

# Parse input
paths = [[(s[0], int(s[1:])) for s in line.strip().split(",")] for line in read_input_lines(3)]

# Direction mapping
DIRECTIONS = {
    'R': Point(1, 0),
    'L': Point(-1, 0),
    'U': Point(0, 1),
    'D': Point(0, -1)
}

def get_step_dict(path):
    steps = 0
    step_dict = {}
    pos = Point(0, 0)
    for direction, distance in path:
        delta = DIRECTIONS[direction]
        for _ in range(distance):
            pos = pos + delta
            steps += 1
            step_dict[pos] = steps
    return step_dict

dict1, dict2 = [get_step_dict(p) for p in paths]
intersections = set(dict1.keys()) & set(dict2.keys())

# Part 1: Find closest intersection by Manhattan distance
min_dist = min(pos.manhattan_distance() for pos in intersections)

# Part 2: Find intersection with minimum combined steps
min_steps = min(dict1[pos] + dict2[pos] for pos in intersections)

print(min_dist)
print(min_steps)
