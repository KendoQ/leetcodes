# Given n non-negative integers representing an elevation
# map where the width of each bar is 1, compute how much
# water it can trap after raining.

# Constraints:
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5

# Example:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6

# The optimal solution is to use two pointers at each
# end of the array and two variables to keep track of
# the maximum height of the left and right sides. Then
# we can compute the wate stored at each index in linear
# time.
class Solution:
    def trapWater(self, height: List[int]) -> int:
        # Initialize left and right pointers as well as the
        # left and right maximums
        L, R = 0, len(height) - 1
        lmax, rmax = height[L], height[R]

        # Initialize a result sum
        res = 0 

        # While the pointers have not met
        while L < R:

            # If left height is lower, move left pointer
            # Note we cannot store water at the two ends
            if lmax < rmax:
                L += 1

                # Update lmax
                lmax = max(lmax, height[L])

                # Update result with the amount of water stored
                # at the current index
                res += lmax - height[L]
            
            # In all other cases move right pointer
            else:
                R -= 1

                # Update rmax and result
                rmax = max(rmax, height[R])
                res += rmax - height[R]

        # Return the result
        return res
    # We avoid creating arrays to store each lmax, rmax
    # and pass through the array a single time
    # Time: O(n)
    # Space: O(1)
