with open('input2.txt', 'r') as f:
    print(len([line for line in [x.strip().split(' ') for x in f.readlines()] if (line[1][0] in (line[2][int(line[0].split('-')[0]) - 1], line[2][int(line[0].split('-')[1]) - 1])) and line[2][int(line[0].split('-')[0]) - 1] != line[2][int(line[0].split('-')[1]) - 1]]))
