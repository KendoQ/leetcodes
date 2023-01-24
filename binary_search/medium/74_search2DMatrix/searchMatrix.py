# You are given an m x n integer matrix. Each row
# is in non-decreasing order, the first element of
# each row is greater than the last element of the
# previous row. Determine whether a given integer 
# target is in the matrix. If so, return true.

# Example:
# Input: matrix = [[1,3,5,7],
#                  [10,11,16,20],
#                  [23,30,34,60]], target = 3
# Output: true

# Constraints:
# m == len(matrix)
# n == len(matrix[i])
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4

# A brute force method can be carried out in
# O(m * n) time. We can speed this up greatly
# by doing a binary search through the rows
# and then a second binary search through a
# single row to find the target. A simpler 
# implementation however is to use a linear
# index for the matrix to perform a single
# binary search. 
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Get the size of matrix
        m, n = len(matrix), len(matrix[0])

        # Initialize left and right pointers
        L, R = 0, (m * n) - 1

        # While pointers have not crossed
        while L <= R:
            # Update middle pointer
            M = (L + R) // 2

            # Convert linear index to 2D coordinate
            row, col = M // n, M % n

            # If less, shrink left
            if matrix[row][col] < target:
                L = M + 1

            # If more shrink right
            elif matrix[row][col] > target:
                R = M - 1

            # If target found return True
            else:
                return True

        # If target not found, return False
        return False
    # Time: O(log m*n), Space: O(1)
