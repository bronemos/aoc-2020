with open('input11.txt', 'r') as f:
    # pt1

    seats = [row.strip() for row in f.readlines()]
    while True:
        new_seats = []
        for i, row in enumerate(seats):
            new_row = ''
            for j, seat in enumerate(row):
                if seat == '.':
                    new_row += '.'
                else:
                    occupied_seats = ''.join(
                        [row[j + 1] if j < len(row) - 1 else '',
                         row[j - 1] if j > 0 else '',
                         seats[i - 1][max(0, j - 1): min(len(row), j + 2)] if i > 0 else '',
                         seats[i + 1][max(0, j - 1): min(len(row), j + 2)] if i < len(seats) - 1 else '']).count('#')
                    if seat == '#' and occupied_seats >= 4:
                        new_row += 'L'
                    elif seat == 'L' and occupied_seats == 0:
                        new_row += '#'
                    else:
                        new_row += seat
            new_seats.append(new_row)

        if new_seats == seats:
            print(sum([row.count('#') for row in seats]))
            break
        seats = new_seats

    f.seek(0)
    # pt2

    seats = [row.strip() for row in f.readlines()]
    while True:
        new_seats = []
        for i, row in enumerate(seats):
            new_row = ''
            for j, seat in enumerate(row):
                if seat == '.':
                    new_row += '.'
                else:
                    occupied_seats = ''.join(
                        [row[j + 1] if j < len(row) - 1 else '',
                         row[j - 1] if j > 0 else '',
                         seats[i - 1][max(0, j - 1): min(len(row), j + 2)] if i > 0 else '',
                         seats[i + 1][max(0, j - 1): min(len(row), j + 2)] if i < len(seats) - 1 else '']).count('#')
                    if seat == '#' and occupied_seats >= 4:
                        new_row += 'L'
                    elif seat == 'L' and occupied_seats == 0:
                        new_row += '#'
                    else:
                        new_row += seat
            new_seats.append(new_row)

        if new_seats == seats:
            print(sum([row.count('#') for row in seats]))
            break
        seats = new_seats
