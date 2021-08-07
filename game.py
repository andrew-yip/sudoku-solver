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


def solve(board):
    find = find_empty(board)  # to find the next empty spot on the board
    if not find:
        return True
    else:
        # if we find an empty space we set a tuple to that location and search that row and column
        row, column = find  # the location of the 0 that was found

    # filling the board with possible solutions
    for i in range(1, 10):
        if valid(board, i, (row, column)):
            board[row][column] = i

            # recursive calls
            if solve(board):
                return True

            # backtracking process
            board[row][column] = 0

    return False


def valid(board, number, position):
    # check row by going through each column (left to right)
    # we are checking to see if any of the numbers in the current row are the same to the one we just added in
    for i in range(len(board[0])):  # always will be 9
        # as long as this isn't the column we just input
        if board[position[0]][i] == number and position[1] != i:
            return False

    # check column by going through each row (up to down)
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # check 3x3 box to see if it is valid
    box_x = position[1] // 3
    box_y = position[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


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
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, col (y, x)
    return None


# Driver Code
print("------------------------")
print("Pre Solved Board: ")
print("------------------------")
print_board(board)
solve(board)
print("------------------------")
print("Solved Board: ")
print("------------------------")
print_board(board)
print("------------------------")
