with open('input15.txt', 'r') as f:
    nums = [int(x) for x in f.readline().split(',')]

# pt1 & pt2

for part in (2020, 30000000):
    spoken = {num: [turn, ] for turn, num in enumerate(nums, 1)}
    last = nums[-1]
    for turn in range(len(spoken) + 1, part + 1):
        if last in spoken:
            if len(spoken[last]) == 1:
                last = 0
            else:
                last = spoken[last][-1] - spoken[last][-2]

            if last in spoken:
                spoken[last].append(turn)
            else:
                spoken[last] = [turn, ]

        else:
            spoken[last] = [turn, ]

    print(last)
