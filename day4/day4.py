import re


with open('input4.txt', 'r') as f:

    # pt1

    print(len([z for z in [re.split(':|\\s', y) for y in [x.replace('\n', ' ') for x in ''.join(f.readlines()).split('\n'*2)]] if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0]))
    f.seek(0)

    # pt2

    # re_dict ={'byr': re.compile(r'(19[2-9][0-9]|200[0-2])'), 'iyr': re.compile(r'20(1[0-9]|20)'), 'eyr': re.compile(r'20(2[0-9]|30)'), 'hgt': re.compile(r'((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)'), 'hcl': re.compile(r'#[0-9a-f]{6}'), 'ecl': re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)'), 'pid': re.compile(r'^\d{9,9}$'), 'cid': re.compile(r'.*')}
    print(len([passport for passport in [[(x, y) for x, y in zip(z[::2], z[1::2])] for z in [re.split(':|\\s', y) for y in [x.replace('\n', ' ') for x in ''.join(f.readlines()).split('\n' * 2)]] if len({'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'} - set(z)) == 0] if all([{'byr': re.compile(r'(19[2-9][0-9]|200[0-2])'), 'iyr': re.compile(r'20(1[0-9]|20)'), 'eyr': re.compile(r'20(2[0-9]|30)'), 'hgt': re.compile(r'((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)'), 'hcl': re.compile(r'#[0-9a-f]{6}'), 'ecl': re.compile(r'(amb|blu|brn|gry|grn|hzl|oth)'), 'pid': re.compile(r'^\d{9,9}$'), 'cid': re.compile(r'.*')}
    [data_type].match(data) for data_type, data in passport])]))
