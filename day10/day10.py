with open('input10.txt', 'r') as f:

    # pt1

    joltages = sorted([int(x.strip()) for x in f.readlines()])
    joltages.insert(0, 0)
    joltages.append(max(joltages))
    one_difference = 0
    three_difference = 0

    for i, joltage in enumerate(joltages[1:]):
        if joltage - joltages[i] == 1:
            one_difference += 1
        else:
            three_difference += 1

    print(one_difference * three_difference)

    # pt2


