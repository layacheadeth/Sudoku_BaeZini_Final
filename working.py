board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


# implement recursive to implement backtracking, backtracking is recursive in nature.
# Base case: when the board is full, we fill in entire board.
# Getting to last element of the board, solution founds.
def solve(bo):


    find = find_empty(bo)
    # base case
    if not find:
        return True
    # recursive case
    else:
        row, col = find
    # Try filling num 1-10 and see if it's valid using valid function, if yes fill it in.
    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            # We recursively trying to finish the solution by calling solve with new board (updated board) and new value added to the updated board.
            # we do this until we find solution, or till when we get pass 1-10 and still none are valid.
            # if can't solve with current number, then backtrack and go with different number.
            if solve(bo):
                return True
            # If solve is not true, the last element we just added, reset it to 0 and perform backtracking
            # go back to previous step, try again with another value or another solutions

            bo[row][col] = 0

    return False


def valid(bo, num, pos):
    # Check row
    # Check every column in the selected row
    # Check if we see a column in the row that we have just inserted some value and has been used, then just ignore that col inside that row.

    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    # opposite from checking row, checking the column mean checking down the vertical direction.
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    # to loop through each box in 0,1,2 index is the reason for //3
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            # check if any element in the box equal to the element we just added, and make sure we're not gonna check the same position we just added in.
            if bo[i][j] == num and (i,j) != pos:
                return False
    # If that column is empty and has no value, and the value is not duplicated in row, col, and boxses, then fill it in.
    return True


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)  # row, col

    return None

print_board(board)
solve(board)
print("___________________")
print_board(board)