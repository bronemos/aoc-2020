import sys
import re

# pt1

# print(sum([len(set(group)) for group in ''.join([x.strip() if x != '\n' else x for x in sys.stdin.readlines()]).split('\n')]))

# pt2

print(sum([len(set(group[0].intersection(*group[1:]))) for group in [[set(answer) for answer in y.split('\n')] for y in ''.join([x for x in sys.stdin.readlines()]).split('\n' * 2)]]))
