def part1():
    num_increased = 0
    with open('1_input.txt', 'r') as f:
        last = None
        while True:
            line = f.readline()
            if not line:
                break
            if last and int(line) > last:
                num_increased += 1
            last = int(line)
    return num_increased

def part2():
    num_increased = 0
    with open('1_input.txt', 'r') as f:
        last3 = [int(f.readline()), int(f.readline()), int(f.readline())]
        last_sum = sum(last3)
        while True:
            line = f.readline()
            if not line:
                break
            curr_sum = last_sum - last3[0] + int(line)
            if curr_sum > last_sum:
                num_increased += 1
            last_sum = curr_sum
            last3.pop(0)
            last3.append(int(line))
    return num_increased

if __name__ == '__main__':
    print(part1())
    print(part2())