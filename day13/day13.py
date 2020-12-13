from math import prod

with open('input13.txt', 'r') as f:
    time, bus_nums = int(f.readline()), [int(x) for x in f.readline().split(',') if x != 'x']

# pt1

earliest_time, num = min([((time // num * num + num) % time, num) for num in bus_nums], key=lambda x: x[0])
print(earliest_time * num)


# pt2

# chinese remainder theorem

def chinese_remainder(n, a):
    p = prod(n)
    total = sum(y * pow(p // x, -1, x) * (p // x) for x, y in zip(n, a))
    return total % p


with open('input13.txt', 'r') as f:
    _, bus_nums = int(f.readline()), [(int(x), int(x) - offset) for offset, x in enumerate(f.readline().split(',')) if
                                      x != 'x']

    print(chinese_remainder([x[0] for x in bus_nums], [x[1] for x in bus_nums]))
