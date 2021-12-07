from collections import Counter

def part1():
    return solve(80)

def part2():
    return solve(256)

def solve(days):
    counter = Counter(parse())
    for _ in range(days):
        hit_zero = counter[0]
        for i in range(8):
            counter[i] = counter[i + 1]
        counter[8] = hit_zero
        counter[6] += hit_zero
    return sum([counter[i] for i in range(9)])

def parse():
    with open('input/6.txt', 'r') as f:
        raw = f.read().strip().split(',')
        timers = [int(x) for x in raw]
        return timers

if __name__ == '__main__':
    print(part1())
    print(part2())
