# Given an array of integers heights representing the histogram's
# bar height where the width of each bar is 1, return the area 
# of the largest rectangle in the histogram.

# Constraints:
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4

# Example:
# Input: heights = [2,1,5,6,2,3]
# Output: 10

# The key here is to use a monotonically increasing stack.
# The stack will contain the indices of the heights array.
# When we encounter a height that is less than the top of
# the stack, we pop the stack and calculate the area of the
# rectangle with the popped index as the height. We also extend
# current rectangle to the left for each element popped from
# the stack.
class Solution:
   def largestRectangleArea(self, heights: List[int]) -> int:
        #Initialize maxArea variable
        maxArea = 0

        #Initialize an empty stack to keep track of heights
        stack = []

        #Iterate over the list of heights and its indexes
        for i, h in enumerate(heights):
            # Keep track of the start index
            start = i

            # While the stack is not empty and the last element
            # in the stack is greater than the current height
            while stack and stack[-1][1] > h:
                # Pop the last element in the stack and assign
                # the values to index and height
                index, height = stack.pop()

                # Update maxArea with comparison between maxArea
                # and the area of the rectangle
                maxArea = max(maxArea, height * (i - index))

                # Update start with the value of index
                start = index

            # Append the start and current height to the stack
            stack.append([start, h])

        # Iterate over elements remaining in the stack
        for i, h in stack:
            # Update maxArea 
            maxArea = max(maxArea, h * (len(heights) - i))

        # Return the final maxArea
        return maxArea
    # We iterate over the heights array once and the stack
    # will contain at most n elements.
    # Time: O(n), Space: O(n)