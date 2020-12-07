with open('input7.txt', 'r') as f:

    # pt1

    bags = {k[:-5]: [' '.join(bag.split(' ')[1:3]) for bag in v[:-1].split(', ')] for k, v in
            [x.strip().split(' contain ') for x in f.readlines()]}
    eligible = set([x for x in bags if 'shiny gold' in bags[x]])
    while True:
        new_eligible = set()
        for bag in eligible:
            for k in bags:
                if bag in bags[k]:
                    new_eligible.add(k)
        if new_eligible <= eligible:
            print(len(eligible))
            break
        else:
            eligible |= new_eligible

    f.seek(0)

    # pt2


    def count_bags(bags: dict, bag_to_count: str) -> int:
        total = 1
        for bag in bags[bag_to_count]:
            if bag == 'no other bags':
                return total
            else:
                total += count_bags(bags, bag[2:]) * int(bag[0])
        return total


    bags = {k[:-5]: [' '.join(bag.split(' ')[0:3]) for bag in v[:-1].split(', ')] for k, v in
            [x.strip().split(' contain ') for x in f.readlines()]}

    print(count_bags(bags, 'shiny gold') - 1)
