from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np

with open("input.txt") as f:
    inp = [int(x) for x in f.read().strip().split(",")]


def run(p, initial_color):
    painted = set()
    rpos = (0, 0)
    panels = defaultdict(int)
    panels[(0, 0)] = initial_color
    direction = 0 - 1j
    paint_mode = True
    p = defaultdict(int, {i: a for i, a in enumerate(p)})

    def get(offset):
        mode = (instruction // 10 ** (1 + offset)) % 10
        if mode == 0:
            return p[index + offset]
        elif mode == 1:
            return index + offset
        elif mode == 2:
            return p[index + offset] + relative_base
        else:
            assert False, f"invalid mode: {mode}"

    index = 0
    relative_base = 0
    while True:
        instruction = p[index]
        opcode = instruction % 100

        if opcode == 1:  # add
            p[get(3)] = p[get(1)] + p[get(2)]
            index += 4
        elif opcode == 2:  # mult
            p[get(3)] = p[get(1)] * p[get(2)]
            index += 4
        elif opcode == 3:  # input
            p[get(1)] = panels[rpos]
            index += 2
        elif opcode == 4:  # output
            output = p[get(1)]
            if paint_mode:
                panels[rpos] = output
                painted.add(rpos)
                paint_mode = False
            else:
                if output == 0:  # turn left
                    direction /= 1j
                else:
                    direction *= 1j
                paint_mode = True
                rpos = (
                    rpos[0] + int(direction.real),
                    rpos[1] + int(direction.imag),
                )
            index += 2
        elif opcode == 5:  # jump nonzero
            if p[get(1)] != 0:
                index = p[get(2)]
            else:
                index += 3
        elif opcode == 6:  # jump zero
            if p[get(1)] == 0:
                index = p[get(2)]
            else:
                index += 3
        elif opcode == 7:  # less than
            p[get(3)] = int(p[get(1)] < p[get(2)])
            index += 4
        elif opcode == 8:  # equals
            p[get(3)] = int(p[get(1)] == p[get(2)])
            index += 4
        elif opcode == 9:  # update relative base
            relative_base += int(p[get(1)])
            index += 2
        elif opcode == 99:  # halt
            print("halt")
            break
        else:
            assert False, f"invalid opcode: {opcode}"

    return painted, panels


# part 1
print(len(run(inp, 0)[0]))

# part 2
image = np.zeros((20, 50))
for key, value in run(inp, 1)[1].items():
    image[key[1] + 5, key[0] + 5] = value
plt.imshow(image)
plt.show()
