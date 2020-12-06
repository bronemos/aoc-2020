with open('input5.txt', 'r') as f:
    # pt1

    print(max(seats := [([interval := (0, 63) if i == 0 and character == 'F' else (64, 127) if i == 0 and character == 'B' else (interval[0], interval[1] - (interval[1] - interval[0]) // 2 - 1) if character == 'F' else (interval[0] + (interval[1] - interval[0]) // 2 + 1, interval[1]) for i, character in enumerate(row)][-1][0 if row[-1] == 'F' else 1] * 8 + [interval := (0, 3) if i == 0 and character == 'L' else (4, 7) if i == 0 and character == 'R' else (interval[0], interval[1] - (interval[1] - interval[0]) // 2 - 1) if character == 'L' else (interval[0] + (interval[1] - interval[0]) // 2 + 1, interval[1]) for i, character in enumerate(column)][-1][0 if column[-1] == 'L' else 1]) for row, column in [(y[:7], y[7:]) for y in [x.strip() for x in f.readlines()]]]))

    # pt 2

    print((set(range(min(seats), max(seats))) - set(seats)).pop())
