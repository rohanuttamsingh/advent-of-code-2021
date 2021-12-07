def part1():
    data = parse()
    min_fuel = float('inf')
    min_val, max_val = min(data), max(data)
    for align in range(min_val, max_val):
        min_fuel = min(min_fuel, sum([abs(x - align) for x in data]))
    return min_fuel

def part2():
    data = parse()
    min_fuel = float('inf')
    min_val, max_val = min(data), max(data)
    for align in range(min_val, max_val):
        min_fuel = min(min_fuel, sum([abs(x - align) * (abs(x - align) + 1) // 2 for x in data]))
    return min_fuel

def parse():
    with open ('input/7.txt', 'r') as f:
        return [int(x) for x in f.read().strip().split(',')]

if __name__ == '__main__':
    print(part1())
    print(part2())
