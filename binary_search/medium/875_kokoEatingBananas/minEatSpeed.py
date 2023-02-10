# There are n piles of bananas, the ith pile has piles[i]
# bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k.
# Each hour, she chooses some pile of bananas and eats k 
# bananas from that pile. If the pile has less than k bananas,
# she eats all of them instead and will not eat any more
# bananas during this hour. Return the minimum integer k
# such that Koko can eat all the bananas within h hours.

# Constraints:
# 1 <= piles.length <= 10^4
# piles.length <= h <= 10^9
# 1 <= piles[i] <= 10^9

# Example: 
# Input: piles = [3,6,7,11], h = 8
# Output: 4

# Since we are looking for a mininum value, we can first
# consider the upper bound of the search space. The upper
# bound is the maximum number of bananas that Koko can eat
# in one hour. This is the maximum number of bananas in any
# pile. The lower bound is 1 banana per hour. We can then 
# search this range for the minimum value that satisfies
# the constraint that Koko can eat all the bananas in h hours.
# We can do this either iteratively or recursively. We can use
# a binary search patter to speed up the process.
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Initialize the left and right pointers
        L, R = 1, max(piles) # max in linear time

        # Initialize the result to the upper bound
        res = R

        # Binary search
        while L <= R:
            # Choose how many bananas to eat per hour
            k = (L + R) // 2

            # Reset count
            hours = 0

            # Count the hours to eat all bananas
            for p in piles:
                hours += math.ceil(p / k)

            # If we ate all bananas in time
            if hours <= h:
                # Update the result
                res = min(res, k)

                # Search lower values of k
                R = k - 1

            # If we did not eat all bananas in time
            else:
                # Search higher values of k
                L = k + 1

        # Return result
        return res
    # The max amount of bananas in a pile is m. There are
    # n piles of bananas. We are searching the range [1,m]
    # for a value of k. We evaluate each value n times, once
    # for each pile. This makes a brute force search of
    # O(m*n) complexity. Using binary search, we achieve
    # Time: O(log(m)*n), Space: O(1)
