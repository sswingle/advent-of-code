# Read the input file and parse the wire paths
with open("input.txt") as f:
    wire_paths = [[(s[0], int(s[1:])) for s in l.split(",")] for l in f.readlines()]

# Function to calculate the steps taken to each point in the path
def calculate_steps(path):
    total_steps = 0
    steps_dict = {}
    x, y = 0, 0
    # Loop over each direction and number of steps
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

def main():
    # Create dictionaries of steps for each wire path
    wire1_steps, wire2_steps = [calculate_steps(p) for p in wire_paths]
    min_dist = float("inf")
    min_steps = float("inf")
    # Calculate the minimum distance and steps to the intersection
    for intersection in wire1_steps.keys() & wire2_steps.keys():
        min_dist = min(abs(intersection[0]) + abs(intersection[1]), min_dist)
        min_steps = min(wire1_steps[intersection] + wire2_steps[intersection], min_steps)

    # Print the results
    print(min_dist)
    print(min_steps)

if __name__ == "__main__":
    main()
