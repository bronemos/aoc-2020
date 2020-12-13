with open('input13.txt', 'r') as f:
    time, bus_nums = int(f.readline()), [int(x) for x in f.readline().split(',') if x != 'x']

# pt1

min_time, num = min([((time // num * num + num) % time, num) for num in bus_nums], key=lambda x: x[0])
print(min_time * num)

# pt2

with open('input13.txt', 'r') as f:
    _, bus_nums = int(f.readline()), [int(x) if x != 'x' else x for x in f.readline().split(',')]



