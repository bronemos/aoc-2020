from math import prod

with open('input13.txt', 'r') as f:
    time, bus_nums = int(f.readline()), [int(x) for x in f.readline().split(',') if x != 'x']

# pt1

earliest_time, num = min([((time // num * num + num) % time, num) for num in bus_nums], key=lambda x: x[0])
print(earliest_time * num)

# pt2

with open('input13.txt', 'r') as f:
    _, bus_nums = int(f.readline()), [(int(x), offset) for offset, x in enumerate(f.readline().split(',')) if
                                      x != 'x']
    res = 0
    product = prod([x[0] for x in bus_nums])

    # chinese reminder theorem

    for t, i in bus_nums:
        p = product // t
        res += i * pow(p, -1, t) * p
    print(-res % product)
