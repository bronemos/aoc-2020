import sys

# pt1
# print(''.join([y[i*3 if i*3 < len(y) else i*3 - (i*3)//len(y)*len(y)] for i, y in enumerate([x.strip() for x in sys.stdin.readlines()])]).count('#'))

# pt2

print([x := (i+1)*num if i == 0 else x*num for i, num in enumerate([[''.join([y[i*r if i*r < len(y) else i*r - (i*r)//len(y)*len(y)] for i, y in enumerate((user_in[::d]))]).count('#') for r, d in ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))] for user_in in [[x.strip() for x in sys.stdin.readlines()]]][0])][-1])