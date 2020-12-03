from sys import stdin
from itertools import combinations

[print(x*y*z) if x + y + z == 2020 else 0 for x, y, z in combinations([int(x.strip()) for x in stdin.readlines()], 3)]

