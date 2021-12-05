def part1():
    drawn, boards = parse()
    marked_boards = [[[0 for _ in range(len(boards[0][0]))] for _ in range(len(boards[0]))] for _ in range(len(boards))]
    for num in drawn:
        for board_num, board in enumerate(boards):
            for row_num, row in enumerate(board):
                for col_num, elem in enumerate(row):
                    if elem == num:
                        marked_boards[board_num][row_num][col_num] = 1
                        if horiz_bingo(marked_boards[board_num]) or vert_bingo(marked_boards[board_num]) or diag_bingo(marked_boards[board_num]):
                            return board_score(board, marked_boards[board_num], num)
    return -1

def part2():
    drawn, boards = parse()
    marked_boards = [[[0 for _ in range(len(boards[0][0]))] for _ in range(len(boards[0]))] for _ in range(len(boards))]
    bingo_board_indices = set()
    for num in drawn:
        for board_num, board in enumerate(boards):
            for row_num, row in enumerate(board):
                for col_num, elem in enumerate(row):
                    if elem == num:
                        marked_boards[board_num][row_num][col_num] = 1
                        if horiz_bingo(marked_boards[board_num]) or vert_bingo(marked_boards[board_num]) or diag_bingo(marked_boards[board_num]):
                            bingo_board_indices.add(board_num)
                            if len(bingo_board_indices) == len(boards):
                                return board_score(board, marked_boards[board_num], num)
    return -1

def horiz_bingo(marked_board):
    for row in marked_board:
        if sum(row) == len(row):
            return True
    return False

def vert_bingo(marked_board):
    for col in zip(*marked_board):
        if sum(col) == len(col):
            return True
    return False

def diag_bingo(marked_board):
    l_to_r_sum = 0
    r_to_l_sum = 0
    for i in range(len(marked_board)):
        l_to_r_sum += marked_board[i][i]
        r_to_l_sum += marked_board[i][-(i + 1)]
    return l_to_r_sum == len(marked_board) or r_to_l_sum == len(marked_board)

def board_score(board, marked_board, last_called):
    score = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if not marked_board[i][j]:
                score += board[i][j]
    return score * last_called

def parse():
    with open('input/4.txt', 'r') as f:
        raw = f.read().strip().split('\n\n')
        drawn = [int(x) for x in raw[0].strip().split(',')]
        boards = [[[int(x) for x in row.strip().split()] for row in board.strip().split('\n')] for board in raw[1:]]
        return (drawn, boards)

if __name__ == '__main__':
    print(part1())
    print(part2())
