with open('input6.txt', 'r') as f:
    # pt1

    print(sum([len(set(group)) for group in ''.join([x.strip() if x != '\n' else x for x in f.readlines()]).split('\n')]))

    f.seek(0)
    # pt2

    print(sum([len(set(group[0].intersection(*group[1:]))) for group in [[set(answer) for answer in y.split('\n')] for y in ''.join([x for x in f.readlines()]).split('\n' * 2)]]))
