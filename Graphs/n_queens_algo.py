"""
The N-Queens problem asks you to place N queens on an N×N chessboard so that no two queens attack each other (no two share a row, column, or diagonal)."""

def dfs_n_queens(n:int):
    # if n is less than 1, there is no valid chessboard, so return an empty list.
    if n < 1:
        return []

    # this list will store every valid solution we find.
    #
    # For example, for n = 4, one solution is:
    # [1, 3, 0, 2]
    # this means:
    # row 0 -> queen is in column 1
    # row 1 -> queen is in column 3
    # row 2 -> queen is in column 0
    # row 3 -> queen is in column 2
    solutions = []

    # this list represents the board we are currently building.
    # board[row] = column where the queen is placed.
    # start with an empty board.
    board = []

    # create a set to keep track of columns that already contain a queen.
    used_columns = set()

    # create a set to keep track of "/" diagonals.
    # for a square at (row, column), row + column is the same for every square on one "/" diagonal.
    used_diagonals1 = set()

    # create a set to keep track of "\" diagonals.
    # for a square at (row, column), row - column is the same for every square on one "\" diagonal.
    used_diagonals2 = set()

    # define a recursive helper function that performs the DFS.
    #
    # row tells us which row we are currently trying to place a queen in.
    def dfs(row):

        # if row == n, we have successfully placed a queen in every row.
        if row == n:

            # make a copy of board and add it to solutions.
            #
            # we use board[:] because board will continue changing while DFS searches for other solutions.
            solutions.append(board[:])

            # stop this particular search path.
            return

        # try placing the queen in every possible column.
        for column in range(n):

            # calculate which "/" diagonal this position belongs to.
            diagonal1 = row + column

            # calculate which "\" diagonal this position belongs to.
            diagonal2 = row - column

            # check whether this column is already occupied.
            if column in used_columns:
                continue

            # check whether this "/" diagonal is already occupied.
            if diagonal1 in used_diagonals1:
                continue

            # check whether this "\" diagonal is already occupied.
            if diagonal2 in used_diagonals2:
                continue

            # if we reach this point, the position is safe.
            # add the column to our set of used columns.
            used_columns.add(column)

            # add the "/" diagonal to our used diagonals.
            used_diagonals1.add(diagonal1)

            # add the "\" diagonal to our used diagonals.
            used_diagonals2.add(diagonal2)

            # place the queen in this row and column.
            board.append(column)

            # move to the next row.
            dfs(row + 1)

            # we have finished exploring this choice. remove the queen so we can try another column.
            board.pop()

            # mark the column as available again.
            used_columns.remove(column)

            # mark the "/" diagonal as available again.
            used_diagonals1.remove(diagonal1)

            # mark the "\" diagonal as available again.
            used_diagonals2.remove(diagonal2)

    # start DFS from row 0.
    dfs(0)

    # return every valid solution that DFS found.
    return solutions