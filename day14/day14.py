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
        for prod in cart_prod:
            address = (int(match[1]) ^ first_mask) | first_mask
            address = '{:036b}'.format(address)
            mask_copy = mask
            for character in prod:
                i = mask_copy.find('X')
                mask_copy = mask_copy.replace('X', character, 1)
                address = address[:i] + character + address[i + 1:]
            address = int(address, 2)
            memory[address] = int(match[2])

print(sum(memory.values()))
