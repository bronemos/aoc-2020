with open('input5.txt', 'r') as f:
    # pt1

    print(max(seats := [int(x.strip().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2) for x in f.readlines()]))

    # pt 2

    print((set(range(min(seats), max(seats))) - set(seats)).pop())
