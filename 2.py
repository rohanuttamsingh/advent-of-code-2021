def part1():
    horiz = 0
    depth = 0
    for dir, val in parse():
        if dir == 'f':
            horiz += val
        elif dir == 'd':
            depth += val
        else:
            depth -= val
    return horiz * depth

def part2():
    aim = 0
    horiz = 0
    depth = 0
    for dir, val in parse():
        if dir == 'd':
            aim += val
        elif dir == 'u':
            aim -= val
        else:
            horiz += val
            depth += aim * val
    return horiz * depth

def parse():
    with open('2_input.txt', 'r') as f:
        return [[line[0], int(line.split(' ')[1])] for line in f.read().strip().split('\n')]

if __name__ == '__main__':
    print(part1())
    print(part2())
