# Given an integer array nums and an integer k, there
# is a sliding window of size k which is moving from
# the very left of the array to the very right. Return
# the local max sliding window.

# Constrains:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length

# Example:
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation:
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

# We can take every window of size k and find the max
# in O(k) time. This would take O(nk) to pass through
# nums. We can do better by using a deque. We can
# store the indices of the current window in the deque
# such that the deque is monotonically decreasing
# in value. Then the value at the left of deque
# is the current maximum
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # k==1 is included in our constrainsts, so
        # handle this edge case first
        if k == 1: return nums

        # Initialize the window deque
        W = collections.deque()

        # Initialize left pointer
        L = 0

        # Initialize the result
        res = []

        # Iterate over the right pointer
        for R in range(len(nums)):
            # While deque is not empty and smaller
            # values exist on the left
            while W and nums[R] > nums[W[-1]]:
                # Pop from right
                W.pop()

            # Add current index to deque
            W.append(R)

            # As left pointer moves, indices fall
            # from the deque
            if L > W[0]:
                W.popleft()

            # If the window is at k length
            if R + 1 >= k:

                # Update the result
                res.append(nums[W[0]])

                # Move left pointer right
                L += 1

        # Return the result
        return res
    # We pass through the nums array once only
    # and use additonal space on for deque window
    # and the result
    # Time: O(n), Space: O(n)