from collections import defaultdict

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

with open("input.txt") as f:
    inp = [int(x) for x in f.read().strip().split(",")]


class Game:
    def __init__(self):
        self.blocks = 0
        self.image = np.zeros((26, 37))
        self.ball_x = -1
        self.paddle_x = -1
        self.score = -1
        self.images = []

    def output(self, x, y, t):
        if x == -1 and y == 0:
            self.score = t
        elif t == 4:
            self.ball_x = x
        elif t == 3:
            self.paddle_x = x
        elif t == 2:
            self.blocks += 1
        self.image[y, x] = t

    def get_input(self):
        self.images.append(Image.fromarray(50 * np.array(self.image)))

        if self.paddle_x < self.ball_x:
            return 1
        elif self.paddle_x > self.ball_x:
            return -1
        else:
            return 0


def run(p, game):
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
            p[get(1)] = game.get_input()
            index += 2
        elif opcode == 4:  # output
            outputs.append(p[get(1)])
            if len(outputs) == 3:
                game.output(*outputs)
                outputs = []
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


inp[0] = 2
run(inp, game := Game())
print(game.blocks)  # part 1
print(game.score)  # part 2

# save animated GIF of the gameplay:
game.images[0].save(
    "game.gif",
    format="GIF",
    append_images=game.images[1:],
    save_all=True,
    duration=100,
    loop=0,
)
