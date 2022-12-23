# Given an integer array height of length n, there are
# n vertical lines drawn such that the two endpoints of 
# the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form
# a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# Constraints:
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4

# Example:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: In this case, the max area of water
# the container can contain is 49. The container formed
# by the lines (1, 8) and (8, 7) is the largest container.

# The brute force method incolves checking each possible
# combination of left and right lines for the maximum area
# We are guaranteed to find a solution this way, but
# the time complexity is at worst O(n^2). We can speed
# this up significantly at no extra space using two pointers
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Initialize the result int
        res = 0

        # Initialize the left and right pointers
        L, R = 0, len(height) - 1

        # While the left and right lines dont meet
        while L < R:
            # Compute the current area
            area = (R - L) * min(height[L], height[R])

            # Update the max area
            res = max(res, area)

            # If left side is lower, move L right
            if height[L] < height[R]:
                L += 1

            # If right side is lower or they are
            # equal, move R left
            else:
                R -= 1

        return res
    # We pass through the area once using two pointers
    # Time: O(n)
    # Space: O(1)