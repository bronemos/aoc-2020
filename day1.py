from sys import stdin
from itertools import combinations

[print(x*y*z) for x, y, z in combinations([int(x.strip()) for x in stdin.readlines()], 3) if x + y + z == 2020]

