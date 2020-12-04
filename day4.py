import sys
import re

#pt 1

print(''.join(['a' if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0 else 'b' for z in [re.split(':|\\s', y)[::2] for y in [x.replace('\n', ' ') for x in ''.join(sys.stdin.readlines()).split('\n\n')]]]).count('a'))

#pt2


