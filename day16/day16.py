import re
from collections import defaultdict

boundaries = re.compile(r'(\d*)-(\d*)')

with open('input16.txt', 'r') as f:
    tickets = [x.split('\n') for x in f.read().split('\n' * 2)]

range_list = []

for boundary in tickets[0]:
    range_list.extend([tuple(map(int, x)) for x in boundaries.findall(boundary)])

# pt1
nearby_tickets = [tuple(map(int, x.split(','))) for x in tickets[2][1:]]
total = 0
for ticket in list(nearby_tickets):
    for value in ticket:
        if not any([boundary[1] >= value >= boundary[0] for boundary in range_list]):
            total += value
            nearby_tickets.remove(ticket)
print(total)

# pt2

names = re.compile(r'^([a-z]+)[a-z\s]*')
my_ticket = list(map(int, tickets[1][1].split(',')))
boundary_dict = {}
for boundary in tickets[0]:
    boundary_dict[names.match(boundary).group()] = [tuple(map(int, x)) for x in boundaries.findall(boundary)]

field_dict = defaultdict(set)
for boundary_name in boundary_dict:
    for column in range(len(nearby_tickets[0])):
        first_range = boundary_dict[boundary_name][0]
        second_range = boundary_dict[boundary_name][1]
        if all([first_range[0] <= ticket[column] <= first_range[1] or
                second_range[0] <= ticket[column] <= second_range[1] for ticket in nearby_tickets]):
            field_dict[boundary_name].add(column)

while not all([len(x) == 1 for x in field_dict.values()]):
    for columns in field_dict.values():
        if len(columns) == 1:
            for value in field_dict.values():
                if value != columns:
                    value -= columns

total = 1
for k, v in field_dict.items():
    if 'departure' in k:
        total *= my_ticket[v.pop()]

print(total)

