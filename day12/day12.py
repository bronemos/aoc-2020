with open('input12.txt', 'r') as f:
    # pt1

    instructions = [(instruction.strip()[0], int(instruction.strip()[1:])) for instruction in f.readlines()]
    directions = {'N': (0, 1),
                  0: (0, 1),
                  'S': (0, -1),
                  180: (0, -1),
                  'E': (1, 0),
                  90: (1, 0),
                  'W': (-1, 0),
                  270: (-1, 0)}

    x = 0
    y = 0
    angle = 90

    for direction, amount in instructions:
        if direction in 'NESW':
            i, j = directions[direction]
            x += i * amount
            y += j * amount
        elif direction == 'R':
            angle += amount
            angle %= 360
        elif direction == 'L':
            angle -= amount
            angle %= 360
        else:
            i, j = directions[angle]
            x += i * amount
            y += j * amount
    print(abs(x) + abs(y))

    # pt2

    ferry = 0 + 0j
    waypoint = 10 + 1j

    for direction, amount in instructions:
        if direction == 'N':
            waypoint += amount * 1j
        elif direction == 'S':
            waypoint -= amount * 1j
        elif direction == 'W':
            waypoint -= amount
        elif direction == 'E':
            waypoint += amount
        elif direction == 'R':
            waypoint *= (-1j) ** (amount // 90)
        elif direction == 'L':
            waypoint *= 1j ** (amount // 90)
        else:
            ferry += waypoint * amount

    print(round(abs(ferry.real) + abs(ferry.imag)))
