import re

def part1():
    coords = parse()
    board = [[0 for _ in range(1000)] for _ in range(1000)]
    for coord in coords:
        if coord[0] == coord[2]:
            if coord[1] <= coord[3]:
                start, end = coord[1], coord[3] + 1
            else:
                start, end = coord[3], coord[1] + 1
            for y in range(start, end):
                board[y][coord[0]] += 1
        elif coord[1] == coord[3]:
            if coord[0] <= coord[2]:
                start, end = coord[0], coord[2] + 1
            else:
                start, end = coord[2], coord[0] + 1
            for x in range(start, end):
                board[coord[1]][x] += 1
    num_overlapping = 0
    for row in board:
        for elem in row:
            num_overlapping += 1 if elem >= 2 else 0
    return num_overlapping

def part2():
    coords = parse()
    board = [[0 for _ in range(1000)] for _ in range(1000)]
    for coord in coords:
        if coord[0] == coord[2]:
            if coord[1] <= coord[3]:
                start, end = coord[1], coord[3] + 1
            else:
                start, end = coord[3], coord[1] + 1
            for y in range(start, end):
                board[y][coord[0]] += 1
        elif coord[1] == coord[3]:
            if coord[0] <= coord[2]:
                start, end = coord[0], coord[2] + 1
            else:
                start, end = coord[2], coord[0] + 1
            for x in range(start, end):
                board[coord[1]][x] += 1
        else:
            if coord[1] <= coord[3]:
                start_y, end_y = coord[1], coord[3] + 1
                start_x = coord[0]
                x_inc = 1 if coord[0] <= coord[2] else -1
            else:
                start_y, end_y = coord[3], coord[1] + 1
                start_x = coord[2]
                x_inc = 1 if coord[2] <= coord[0] else -1
            x_off = 0
            for y in range(start_y, end_y):
                board[y][start_x + x_off] += 1
                x_off += x_inc
    num_overlapping = 0
    for row in board:
        for elem in row:
            num_overlapping += 1 if elem >= 2 else 0
    return num_overlapping

def parse():
    with open('input/5.txt', 'r') as f:
        raw = f.read().strip().split('\n')
        pattern = r'(\d+),(\d+) -> (\d+),(\d+)'
        coords = []
        for line in raw:
            match = re.search(pattern, line)
            coords.append([int(match.group(1)), int(match.group(2)), int(match.group(3)), int(match.group(4))])
        return coords

if __name__ == '__main__':
    print(part1())
    print(part2())
