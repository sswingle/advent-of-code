from utils import read_input_ints

masses = read_input_ints(1)

# part 1
print(sum(m // 3 - 2 for m in masses))

# part 2
total = 0
for m in masses:
    while (m := m // 3 - 2) > 0:
        total += m
print(total)
