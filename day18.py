import heapq
import itertools as it

import more_itertools as mit
import networkx as nx

with open("input.txt") as f:
    grid = [[c for c in line.strip()] for line in f.readlines()]
SIZE = len(grid)
MID = SIZE // 2


def solve(grid):
    # keymap = dict()
    start_positions = []
    graph = nx.Graph()
    quad_lists = [[] for _ in range(4)]
    for r, c in it.product(range(SIZE), repeat=2):
        if (char := grid[r][c]) == "#":
            continue
        pos = (r, c)
        if char == "@":
            start_positions.append(pos)
        if char.isupper():
            pos = char
        if char.islower():
            # keymap[char] = pos
            pos = char
            quadrant = 2 * (r // (MID + 1)) + (c // (MID + 1))
            quad_lists[quadrant].append(char)
        for nextr, nextc in [(r, c + 1), (r + 1, c)]:
            other_char = grid[nextr][nextc]
            if other_char != "#":
                graph.add_edge(
                    pos, other_char if other_char.isalpha() else (nextr, nextc)
                )

    """
    quad_start_names = [f"quad_start_{i}" for i in range(4)]
    for quad_start_name, quad_start_pos in zip(
        quad_start_names, start_positions
    ):
        keymap[quad_start_name] = quad_start_pos
    """

    for ql in quad_lists:
        print(len(ql), ql)
    print(start_positions)

    paths = {}
    for quad in range(4):
        for key1, key2 in it.product(
            [start_positions[quad]] + quad_lists[quad], repeat=2
        ):
            if key1 == key2:
                continue
            if (path := paths.get((key2, key1))) is None:
                path = nx.shortest_path(graph, key1, key2)
            paths[(key1, key2)] = path

    dists_and_blockers = {}
    for (k1, k2), path in paths.items():
        door_blocks = set()
        key_blocks = set()
        for t in path[1:-1]:
            if isinstance(t, tuple):
                char = grid[t[0]][t[1]]
            (door_blocks if char.isupper() else key_blocks).add(char.lower())
        else:
            dists_and_blockers[(k1, k2)] = (
                len(path) - 1,
                door_blocks,
                key_blocks,
            )

    # positions_list, keys_needed_sets, keys_got_set
    initial_state = (
        tuple(quad_start_names),
        tuple(
            frozenset(quad_lists[i]) - frozenset(quad_start_names)
            for i in range(4)
        ),
        frozenset(),
    )
    heap = [(0, initial_state)]
    print(initial_state)

    max_keys = 0
    seen = set()
    while heap:
        dist, state = heapq.heappop(heap)
        if state in seen:
            continue
        seen.add(state)
        start_positions, keys_needed, keys_have = state
        if len(keys_have) > max_keys:
            max_keys = len(keys_have)
            print(max_keys, keys_have)
        if len(keys_have) == 26:
            return dist
        for robot in range(4):
            for key in keys_needed[robot]:
                path_dist, door_blocks, key_blocks = dists_and_blockers[
                    (start_positions[robot], key)
                ]
                if not keys_have.issuperset(door_blocks):
                    continue
                if keys_needed[robot].intersection(key_blocks):
                    continue
                new_positions = list(start_positions)
                new_positions[robot] = key
                new_positions = tuple(new_positions)
                new_keys_needed = list(keys_needed)
                new_keys_needed[robot] = keys_needed[robot].difference([key])
                new_keys_needed = tuple(new_keys_needed)
                new_keys_have = keys_have.union([key])
                new_state = (new_positions, new_keys_needed, new_keys_have)
                if new_state not in seen:
                    heapq.heappush(heap, (dist + path_dist, new_state))


# part 1
# print(solve(grid))

# part 2
for (dr, dc), char in zip(it.product(range(3), repeat=2), "@#@###@#@"):
    grid[MID - 1 + dr][MID - 1 + dc] = char
for row in grid:
    print("".join(row))
print(grid[39][39])
print(solve(grid))


# # find start and keys
# num_rows = len(grid)
# num_cols = len(grid[0])
# keymap = dict()
# for r, c in it.product(range(num_rows), range(num_cols)):
#     if grid[r][c] == "@":
#         grid[r][c] = "."
#         start_r = r
#         start_c = c
#     elif grid[r][c].islower():
#         keymap[grid[r][c]] = (r, c)


# part 1
# most_keys = 0
# seen = set()
# heap = [(0, (start_r, start_c, frozenset()), [])]
# while heap:
#     dist, state, order = heapq.heappop(heap)
#     if state in seen:
#         continue
#     seen.add(state)
#     r, c, keys = state
#     if len(keys) == 26:
#         print(f"Steps: {dist}")
#         break
#     for dr, dc in [(1, 0), (-1, 0), (0, -1), (0, 1)]:
#         nextr, nextc = r + dr, c + dc
#         char = grid[nextr][nextc]
#         if char == "#":
#             continue
#         if char.isupper() and not char.lower() in keys:
#             continue
#         if char.islower() and char not in keys:
#             keys = keys.union(char)
#             order = order + [char]
#         new_state = (nextr, nextc, keys)
#         if len(keys) > most_keys:
#             most_keys = len(keys)
#             print(most_keys, order)
#         if new_state not in seen:
#             heapq.heappush(heap, (dist + 1, new_state, order))
