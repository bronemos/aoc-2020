import re
from itertools import product

mask_pattern = re.compile(r'^mask\s=\s([X10]+)$')
value_pattern = re.compile(r'^mem\[(\d+)]\s=\s(\d+)$')

with open('input14.txt', 'r') as f:
    entries = f.read().splitlines()

# pt1

memory = {}
for entry in entries:
    if match := mask_pattern.match(entry):
        first_mask = int(match[1].replace('X', '0'), 2)
        second_mask = int(match[1].replace('X', '1'), 2)
    elif match := value_pattern.match(entry):
        memory[match[1]] = (int(match[2]) | first_mask) & second_mask

print(sum(memory.values()))

# pt2

memory = {}
for entry in entries:
    if match := mask_pattern.match(entry):
        mask = match[1]
        first_mask = int(mask.replace('X', '0'), 2)
        second_mask = int(mask.replace('X', '1'), 2)
    elif match := value_pattern.match(entry):
        cart_prod = product(['0', '1'], repeat=mask.count('X'))
        address = (int(match[1]) | first_mask) & second_mask
        print(bin(address))
        for prod in cart_prod:
            floating = mask.replace('1', '0')
            for character in prod:
                floating = floating.replace('X', character, 1)
            floating = int(floating, 2)
            print(address | floating)
            memory[address] = int(match[2])

print(sum(memory.values()))
