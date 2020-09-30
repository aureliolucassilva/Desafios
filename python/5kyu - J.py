# Link -> https://www.codewars.com/kata/525caa5c1bf619d28c000335

def is_solved(board):
    column_1 = [board[0][0], board[1][0], board[2][0]]
    column_2 = [board[0][1], board[1][1], board[2][1]]
    column_3 = [board[0][2], board[1][2], board[2][2]]
    diagonal_1 = [board[0][0], board[1][1], board[2][2]]
    diagonal_2 = [board[0][2], board[1][1], board[2][0]]

    # X
    for index in range(3):
        if board[index] == [1, 1, 1]:
            return 1

    if column_1 == [1, 1, 1]:
        return 1
    elif column_2 == [1, 1, 1]:
        return 1
    elif column_3 == [1, 1, 1]:
        return 1
    elif diagonal_1 == [1, 1, 1]:
        return 1
    elif diagonal_2 == [1, 1, 1]:
        return 1

    # O
    for index in range(3):
        if board[index] == [2, 2, 2]:
            return 2

    if column_1 == [2, 2, 2]:
        return 2
    elif column_2 == [2, 2, 2]:
        return 2
    elif column_3 == [2, 2, 2]:
        return 2
    elif diagonal_1 == [2, 2, 2]:
        return 2
    elif diagonal_2 == [2, 2, 2]:
        return 2

    # Empty spots
    for index in range(3):
        if 0 in board[index]:
            return -1

    # Draw, since the function did not yet return any value
    return 0
