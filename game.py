board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            # every three rows horizontal line
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:  # every 3 printed numbers print the '|'
                print(" | ", end="")
            if j == 8:  # when you're at j = 8 which is last item in column
                print(board[i][j])
            else:
                # end = "" so we stay on the same line
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
