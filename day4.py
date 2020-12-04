import sys
import re

# pt1

# print(len([z for z in [re.split(':|\\s', y) for y in [x.replace('\n', ' ') for x in ''.join(sys.stdin.readlines()).split('\n'*2)]] if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0]))

# pt2
#print([print(x, y) for x, y in [zip(z[::2], z[1::2]) for z in [re.split(':|\\s', y) for y in [x.replace('\n', ' ') for x in ''.join(sys.stdin.readlines()).split('\n'*2)]] if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0]])
re_dict = dict()
print([z for z in [re.split(':|\\s', y) for y in [x.replace('\n', ' ') for x in ''.join(sys.stdin.readlines()).split('\n'*2)]] if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0])
b = [[1, 'a', 2, 'b'], [3, 'c', 4, 'd']]
print([zip(a[::2], a[1::2]) for a in b])
[print(x, y, sep='\n') for x, y in [zip(a[::2], a[1::2]) for a in b]]
