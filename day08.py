import functools

import matplotlib.pyplot as plt
import numpy as np

with open("input.txt") as f:
    img = np.fromiter(f.read().strip(), int).reshape(-1, 6, 25)

# part 1
print(min(((l == 0).sum(), (l == 1).sum() * (l == 2).sum()) for l in img)[1])

# part 2
decoded = functools.reduce(lambda a, b: np.where(a < 2, a, b), img)
plt.imshow(decoded)
plt.show()
