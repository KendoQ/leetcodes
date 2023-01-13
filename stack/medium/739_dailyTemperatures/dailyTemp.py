# Given an array of integers temperatures represents the
# daily temperatures, return an array answer such that
# answer[i] is the number of days you have to wait after
# the ith day to get a warmer temperature. If there is no
# future day for which this is possible, answer[i] == 0

# Constraints:
# 1 <= len(temperatures) <= 10^5
# 30 <= temperatures[i] <= 100

# Example:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# The brute force method can be implemented with a
# nested loop in O(n^2) time. We can do better by
# using some extra memory for a stack. We will 
# implement the stack as the indices corresponding
# to the monotonically decreasing temperatures. Then
# we can form the result in linear time
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Initialize the stack and result
        res, stack = [0] * len(temperatures), []

        # Loop over the indices of temperatures
        for i in range(len(temperatures)):
            # If current temp is greature than temp
            # pointed to by top of the stack
            while stack and temperatures[i] > temperatures[stack[-1]]:
                # Pop index from top of stack
                T = stack.pop()

                # Update the result
                res[T] = i - T

            # Add the current index to stack
            stack.append(i)

        # Return the result
        return res
    # We use extra space for a stack of maximum
    # size n, and iterate over the temperatures
    # only once
    # Time: O(n), Space: O(n)