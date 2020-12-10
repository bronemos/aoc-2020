from collections import defaultdict

with open('input10.txt', 'r') as f:
    # pt1

    joltages = sorted([int(x.strip()) for x in f.readlines()])
    joltages.insert(0, 0)
    joltages.append(max(joltages))
    one_difference = 0
    three_difference = 0

    for joltage1, joltage2 in zip(joltages, joltages[1:]):
        if joltage2 - joltage1 == 1:
            one_difference += 1
        else:
            three_difference += 1

    print(one_difference * three_difference)

    # pt2

    combinations = defaultdict(lambda: 0)

    combinations[0] = 1

    for joltage in joltages[1:]:
        combinations[joltage] = combinations[joltage - 1] + combinations[joltage - 2] + combinations[joltage - 3]

    print(combinations[max(joltages)])
