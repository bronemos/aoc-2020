import sys

# pt1

def calculate(characters: str, interval: tuple, lower: str, upper: str) -> int:
    for idx, character in enumerate(characters):
        if idx != len(characters) - 1:
            if character == lower:
                interval = (interval[0], interval[1] - (interval[1] - interval[0]) // 2 - 1)
            else:
                interval = (interval[0] + (interval[1] - interval[0]) // 2 + 1, interval[1])
        else:
            if character == lower:
                return interval[0]
            else:
                return interval[1]


def calculate_id(characters: str) -> int:
    return calculate(characters[:7], (0, 127), 'F', 'B') * 8 + calculate(characters[7:], (0, 7), 'L', 'R')

print(max(seats := [calculate_id(x.strip()) for x in sys.stdin.readlines()]))

#pt 2

print((set(range(min(seats), max(seats))) - set(seats)).pop())
