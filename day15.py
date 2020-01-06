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
    def __init__(self):
        # 0 is unknown, 1 is free, 2 is wall, 3 is oxygen
        self.x, self.y = size // 2, size // 2
        self.grid = [["~" for _ in range(size)] for _ in range(size)]

    def update_dist_grid(self, symbol="~"):
        self.dist_grid = [[10000] * size for _ in range(size)]
        level = 0
        to_update = set()
        seen = set()
        for r in range(size):
            for c in range(size):
                if self.grid[r][c] == symbol:
                    to_update.add((r, c))
                    seen.add((r, c))
        while to_update:
            next_to_update = set()
            for r, c in to_update:
                self.dist_grid[r][c] = level
                for dx, dy in d_map.values():
                    dr = r + dx
                    dc = c + dy
                    if dr < 0 or dr >= size or dc < 0 or dc >= size:
                        continue
                    if (dr, dc) in seen:
                        continue
                    if self.grid[dr][dc] == "#":
                        continue
                    next_to_update.add((dr, dc))
                    seen.add((dr, dc))
            level += 1
            to_update = next_to_update

    def status_code(self, code):
        # print("Status Code: ", code)
        # print("Position: ", self.x, self.y)
        dx, dy = d_map[self.last_move]
        if code == 0:
            self.grid[self.x + dx][self.y + dy] = "#"
        else:
            self.x += dx
            self.y += dy
        if code == 1:
            self.grid[self.x][self.y] = " "
        elif code == 2:
            self.grid[self.x][self.y] = "O"
            print("FOUND")

    def display(self):
        last_val = self.grid[self.x][self.y]
        self.grid[self.x][self.y] = "D"
        for row in self.grid:
            print("".join(row))
        self.grid[self.x][self.y] = last_val

    def final(self):
        print("FINAL")
        self.display()
        self.update_dist_grid("O")
        print(self.dist_grid[size // 2][size // 2])
        max_val = -1
        for r in range(size):
            for c in range(size):
                val = self.dist_grid[r][c]
                if val != 10000:
                    max_val = max(max_val, val)
        print(max_val)
        exit()

    def move_command(self, manual=False):
        if manual:
            self.display()
            move = int(input())
        else:
            self.display()
            self.update_dist_grid()
            best_move = -1
            lowest_val = 1000
            for move, (dr, dc) in d_map.items():
                val = self.dist_grid[self.x + dr][self.y + dc]
                if val < lowest_val:
                    lowest_val = val
                    best_move = move
            move = best_move
            if move == -1:
                self.final()
        self.last_move = move
        return move


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
            move_command = robot.move_command()
            p[get(1)] = move_command
            index += 2
        elif opcode == 4:  # output
            status_code = p[get(1)]
            robot.status_code(status_code)
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


robot = Robot()
run(inp, robot)
