from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

with open("input.txt") as f:
    inp = [int(x) for x in f.read().strip().split(",")]

d_map = {
    1: (-1, 0),
    2: (1, 0),
    3: (0, -1),
    4: (0, 1),
}

size = 50


class Robot:
    def __init__(self, rinput=""):
        # 0 is unknown, 1 is free, 2 is wall, 3 is oxygen
        self.grid = []
        self.current_line = []
        self.rinput = rinput
        self.index = 0

    def output(self, output):
        if output > 200:
            print(output)
            exit()
        if output == 10:
            self.grid.append(self.current_line)
            self.current_line = []
        else:
            self.current_line.append(chr(output))

    def display(self):
        for row in self.grid:
            print("".join(row))

    def get_input(self):
        ascii_char = ord(self.rinput[self.index])
        self.index += 1
        return ascii_char


def run(p, robot):
    outputs = []
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
            move_command = robot.get_input()
            p[get(1)] = move_command
            index += 2
        elif opcode == 4:  # output
            status_code = p[get(1)]
            robot.output(status_code)
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

    return outputs


def left(dr, dc):
    d = (dr + dc * 1j) * 1j
    return int(d.real), int(d.imag)


def right(dr, dc):
    d = (dr + dc * 1j) / 1j
    return int(d.real), int(d.imag)


def out(r, c):
    if r < 0 or r + 1 > sr:
        return True
    if c < 0 or c + 1 > sc:
        return True
    return False


sr, sc = 51, 57


def plan(grid):
    pr, pc = 10, 36
    path = ["R", 0]
    dr, dc = 0, 1
    while True:
        # print(path)
        nr, nc = pr + dr, pc + dc
        if not out(nr, nc) and grid[nr][nc] == "#":
            path[-1] += 1
            pr, pc = nr, nc
        else:
            # try left
            dl = left(dr, dc)
            nr, nc = pr + dl[0], pc + dl[1]
            if not out(nr, nc) and grid[nr][nc] == "#":
                path.append("L")
                path.append(0)
                dr, dc = dl
                continue
            # try right
            dright = right(dr, dc)
            nr, nc = pr + dright[0], pc + dright[1]
            if not out(nr, nc) and grid[nr][nc] == "#":
                path.append("R")
                path.append(0)
                dr, dc = dright
                continue
            # we done
            # print(pr, pc, dr, dc, nr, nc, out2(nr, nc))
            break
    return path


robot = Robot()
run(list(inp), robot)
robot.display()

total = 0
grid = robot.grid
print(len(grid), len(grid[0]))
for r in range(1, len(grid) - 2):
    for c in range(1, len(grid[0]) - 2):
        if (
            grid[r][c] == "#"
            and grid[r - 1][c] == "#"
            and grid[r + 1][c] == "#"
            and grid[r][c - 1] == "#"
            and grid[r][c + 1] == "#"
        ):
            total += r * c
print(total)

for r in range(51):
    for c in range(57):
        if grid[r][c] == "^":
            print(r, c)

path = plan(grid)
print("".join([str(x) for x in path]))

rinput = """A,C,A,C,B,A,C,B,A,B
R,6,L,10,R,8
L,10,R,6,R,6,L,8
R,8,R,12,L,8,L,8
n
"""

robot = Robot(rinput)
inp[0] = 2
run(list(inp), robot)
robot.display()

"""
A R6L10R8R8
C R12L8L8
A R6L10R8R8
C R12L8L8
B L10R6R6L8
A R6L10R8R8
C R12L8L8
B L10R6R6L8
R6L10R8L10R6R6L8

A = R6L10R8R8
B = L10R6R6L8
C = R12L8L8
"""

"""
R6L10R8
R8R12L8L8
R6L10R8
R8R12L8L8
L10R6R6L8
R6L10R8
R8R12L8L8
L10R6R6L8
R6L10R8
L10R6R6L8
"""
