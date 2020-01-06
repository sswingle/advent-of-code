import heapq
import itertools as it

with open("input.txt") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]

# find start
num_rows = len(grid)
num_cols = len(grid[0])
for r, c in it.product(range(num_rows), range(num_cols)):
    if grid[r][c] == "@":
        start_r = r
        start_c = c
        for (dr, dc), char in zip(it.product(range(3), repeat=2), "#@#####@#"):
            grid[r - 1 + dr][c - 1 + dc] = char
        break

most_keys = 0
seen = set()
start_positions = ((start_r - 1, start_c - 1), (start_r + 1, start_c -1 ), (start_r - 1, start_c + 1), (start_r + 1, start_c + 1 ))
heap = [(0, (start_positions, frozenset()))]
while heap:
    dist, state = heapq.heappop(heap)
    if state in seen:
        continue
    seen.add(state)
    r, c, keys = state
    if len(keys) == 26:
        print(f"Steps: {dist}")
        break
    for robot_index in range()
    for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
        nextr, nextc = r + dr, c + dc
        char = grid[nextr][nextc]
        if char == "#":
            continue
        if char.isupper() and not char.lower() in keys:
            continue
        if char.islower():
            nextkeys = keys.union(char)
        else:
            nextkeys = keys
        new_state = (dist + 1, (nextr, nextc, nextkeys))
        if len(nextkeys) > most_keys:
            most_keys = len(nextkeys)
            print(most_keys, nextkeys)
        if new_state not in seen:
            heapq.heappush(heap, new_state)
