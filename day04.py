from collections import Counter


def check1(s):
    return list(s) == sorted(s) and len(set(s)) < len(s)


def check2(s):
    return list(s) == sorted(s) and 2 in Counter(s).values()


print(sum(check1(str(x)) for x in range(138307, 654505)))
print(sum(check2(str(x)) for x in range(138307, 654505)))
