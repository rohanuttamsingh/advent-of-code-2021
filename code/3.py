import numpy as np

def part1():
    gamma_list, epsilon_list = get_most_and_least_common_bit_lists()
    gamma = int(''.join([str(x) for x in gamma_list]), 2)
    epsilon = int(''.join([str(x) for x in epsilon_list]), 2)
    return gamma * epsilon

def part2():
    remaining_nums_ox = np.array(parse())
    curr_idx = 0
    while len(remaining_nums_ox) > 1:
        bits = [int(num[curr_idx]) for num in remaining_nums_ox]
        bit_avg = sum(bits) / len(bits)
        most_common_bit = int(bit_avg >= 0.5)
        remaining_nums_ox = np.array([num for num in remaining_nums_ox if int(num[curr_idx]) == most_common_bit])
        curr_idx += 1
    remaining_nums_co2 = np.array(parse())
    curr_idx = 0
    while len(remaining_nums_co2) > 1:
        bits = [int(num[curr_idx]) for num in remaining_nums_co2]
        bit_avg = sum(bits) / len(bits)
        least_common_bit = 1 - int(bit_avg >= 0.5)
        remaining_nums_co2 = np.array([num for num in remaining_nums_co2 if int(num[curr_idx]) == least_common_bit])
        curr_idx += 1
    return int(''.join([str(x) for x in remaining_nums_ox[0]]), 2) * int(''.join([str(x) for x in remaining_nums_co2[0]]), 2)

def get_most_and_least_common_bit_lists():
    data = parse()
    sums = np.zeros(len(data[0]))
    for num in data:
        for i, bit in enumerate(num):
            sums[i] += int(bit)
    bool_list = sums / len(data) > 0.5
    gamma_list = bool_list.astype('int')
    epsilon_list = (~bool_list).astype('int')
    return (gamma_list, epsilon_list)

def parse():
    with open('input/3.txt', 'r') as f:
        return [line for line in f.read().strip().split('\n')]
    
if __name__ == '__main__':
    print(part1())
    print(part2())
