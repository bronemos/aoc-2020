import sys

print(''.join(['a' if (line[1][0] in (line[2][int(line[0].split('-')[0]) - 1], line[2][int(line[0].split('-')[1]) - 1])) and line[2][int(line[0].split('-')[0]) - 1] != line[2][int(line[0].split('-')[1]) - 1] else 'b' for line in [x.strip().split(' ') for x in sys.stdin.readlines()]]).count('a'))

