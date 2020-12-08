from copy import deepcopy

with open('input8.txt', 'r') as f:

    # pt1

    instructions = [[ins, int(value)] for ins, value in [x.strip().split(' ') for x in f.readlines()]]
    lines_run = set()
    curr_line = 0
    accumulator = 0
    while curr_line not in lines_run:
        lines_run.add(curr_line)
        if instructions[curr_line][0] == 'nop':
            curr_line +=1
        elif instructions[curr_line][0] == 'jmp':
            curr_line += instructions[curr_line][1]
        else:
            accumulator += instructions[curr_line][1]
            curr_line += 1
    print(accumulator)

    # pt2

    for line_idx in range(len(instructions)):
        updated_instructions = deepcopy(instructions)
        if updated_instructions[line_idx][0] == 'nop':
            updated_instructions[line_idx][0] = 'jmp'
        elif updated_instructions[line_idx][0] == 'jmp':
            updated_instructions[line_idx][0] = 'nop'
        lines_run = set()
        curr_line = 0
        accumulator = 0
        infinite_loop = False
        while curr_line not in lines_run:
            lines_run.add(curr_line)
            try:
                if updated_instructions[curr_line][0] == 'nop':
                    curr_line += 1
                elif instructions[curr_line][0] == 'jmp':
                    curr_line += updated_instructions[curr_line][1]
                else:
                    accumulator += updated_instructions[curr_line][1]
                    curr_line += 1
            except IndexError:
                print(accumulator)
                exit(0)
