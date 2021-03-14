from pprint import pprint

board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

stack = []
run = True


def find_next():
    for y, row in enumerate(board):
        for x, col in enumerate(row):
            if col == 0:
                return (x, y)
    return (0, 0)


def get_list_1(x, y):
    return board[y]


def get_list_2(x, y):
    result = []
    for row in board:
        result.append(row[x])
    return result


def get_list_3(x, y):
    result = []
    x_offset = 3 * (x // 3)
    y_offset = 3 * (y // 3)
    result.append(board[y_offset][x_offset])
    result.append(board[y_offset][x_offset + 1])
    result.append(board[y_offset][x_offset + 2])
    result.append(board[y_offset + 1][x_offset])
    result.append(board[y_offset + 1][x_offset + 1])
    result.append(board[y_offset + 1][x_offset + 2])
    result.append(board[y_offset + 2][x_offset])
    result.append(board[y_offset + 2][x_offset + 1])
    result.append(board[y_offset + 2][x_offset + 2])
    return result


def Diff(li1, li2):
    return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))


def guess(x, y):
    if x == 0 and y == 0:
        pprint(board)
        quit()
    possible = get_possible_guesses(x, y)
    if len(possible) > 0:
        board[y][x] = possible[-1]
        stack.append([x, y, possible, possible[-1]])
    else:
        backtrack()


def backtrack():
    possible = []
    while True:
        if len(possible) < 2:
            x, y, possible, guess = stack.pop()
            board[y][x] = 0
        else:
            possible = list(set(possible) - set([guess]))
            board[y][x] = possible[-1]
            stack.append([x, y, possible, possible[-1]])
            break


def get_possible_guesses(x, y):
    base = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    across = get_list_1(x, y)
    down = get_list_2(x, y)
    box = get_list_3(x, y)
    row_col_common = list(set(base) - set(down) & set(base) - set(across))
    row_col_box_common = list(set(row_col_common) & set(base) - set(box))

    return row_col_box_common


pprint(board)

while True:
    x, y = find_next()  # find next blank (technically 0)
    guess(x, y)
