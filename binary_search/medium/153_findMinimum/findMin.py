# An n sized array sorted in ascending order has been right
# rotated between 1 and n times. Find the minimum value in
# the array in O(log n) time.

# Constraints:
# All elements in array are unique
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000

# Example:
# Input: nums = [4,5,6,7,0,1,2]
# Output: 0

# To do better than linear time, we can explit the sorted
# array using a binary serch algorithm. To update the
# pointers, we evaluate if we are on the "left" or "right"
# portion of the rotated array. Numbers in the right part
# of the array should always be less than numbers in the
# left part. So we can use the number pointed to by the 
# left pointer to figure out which part we are in. When
# the search becomes restricted to one contiguous part 
# of the array, we can stop. 
class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Initialize left and right pointers
        L, R = 0, len(nums) - 1

        # Initialize the result
        res = float("inf")

        # While non-contiguous, binary search
        while nums[L] > nums[R]:
            # Update middle pointers
            M = (L + R) // 2

            # Update result
            res = min(res, nums[M])

            # If we are in left part, search right
            if nums[L] <= nums[M]:
                L = M + 1

            # If we are in right part, search left
            else:
                R = M - 1

        # Return updated result
        return min(res, nums[L])
    # Time: O(log n), Space: O(1)