from collections import Counter
from typing import List


def check1(s: str) -> bool:
    """Check if password meets criteria for part 1:
    - Digits never decrease from left to right
    - At least two adjacent digits are the same
    """
    return list(s) == sorted(s) and len(set(s)) < len(s)


def check2(s: str) -> bool:
    """Check if password meets criteria for part 2:
    - Digits never decrease from left to right
    - Contains at least one pair of digits that appears exactly twice
    """
    return list(s) == sorted(s) and 2 in Counter(s).values()


# Input range
START = 138307
END = 654505

# Part 1: Count passwords meeting first criteria
print(sum(check1(str(x)) for x in range(START, END + 1)))

# Part 2: Count passwords meeting second criteria
print(sum(check2(str(x)) for x in range(START, END + 1)))
