from itertools import combinations

with open('input1.txt', 'r') as f:
    [print(x*y*z) for x, y, z in combinations([int(x.strip()) for x in f.readlines()], 3) if x + y + z == 2020]

