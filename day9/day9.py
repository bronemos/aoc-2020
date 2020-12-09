from itertools import combinations

with open('input9.txt', 'r') as f:

    # pt1

    numbers = [int(x.strip()) for x in f.readlines()]
    for index, number in enumerate(numbers[25:]):
        is_sum = False
        for x, y in combinations(numbers[index:index + 25], 2):
            if x + y == number:
                is_sum = True
                break
        if not is_sum:
            invalid_number = number
            print(number)
            break

    # pt2

    ranges = [numbers[i:j] for i in range(len(numbers)) for j in range(i + 1, len(numbers) + 1) if
              len(numbers[i:j]) > 1]

    for num_range in ranges:
        if sum(num_range) == invalid_number:
            print(min(num_range) + max(num_range))
            break
