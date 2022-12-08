# Determine if a 9 x 9 Sudoku board is valid. 
# Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain
# the digits 1-9 without repetition.

# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.

# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],
#                 ["6",".",".","1","9","5",".",".","."],
#                 [".","9","8",".",".",".",".","6","."],
#                 ["8",".",".",".","6",".",".",".","3"],
#                 ["4",".",".","8",".","3",".",".","1"],
#                 ["7",".",".",".","2",".",".",".","6"],
#                 [".","6",".",".",".",".","2","8","."],
#                 [".",".",".","4","1","9",".",".","5"],
#                 [".",".",".",".","8",".",".","7","9"]]
# Output: true

# We have to iterate through the entire board, so time
# time complexity will be O(n^2)

# We need to check for duplicates in 3 groups:
# Rows, columns, and 3x3 squares

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        # We check for duplicates in 3 groups we will store
        # as hashsets
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        # We iterate through the entire board indices
        for r in range(9):
            for c in range(9):

                # If the value is empty, skip
                if board[r][c] == ".":
                    continue

                # If duplicate is detected in a group, return F
                if(board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                    return False

                # If no duplicate is dectected, update sets
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[(r//3, c//3)].add(board[r][c])
        # If we reach the end of the loop, return True
        return True