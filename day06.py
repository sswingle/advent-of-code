from collections import defaultdict, deque

with open("input.txt") as f:
    pairs = [l.strip().split(")") for l in f.readlines()]

objects = set()
parents = {}
connections = defaultdict(list)

for a, b in pairs:
    objects.add(a)
    objects.add(b)
    parents[b] = a
    connections[a].append(b)
    connections[b].append(a)

# part 1
total_orbits = 0
for o in objects:
    while o != "COM":
        total_orbits += 1
        o = parents[o]
print(total_orbits)

start = parents["YOU"]
goal = parents["SAN"]

seen = set()
to_process = deque([(0, start)])
while True:
    transfers, o = to_process.popleft()
    if o == goal:
        print(transfers)
        break
    if o not in seen:
        seen.add(o)
        for o2 in connections[o]:
            to_process.append((transfers + 1, o2))
