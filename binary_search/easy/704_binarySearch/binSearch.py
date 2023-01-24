# Given an array of integers nums which is sorted
# in ascending order, and an integer target, write
# a function to search target in nums. If target
# exists, then return its index. Otherwise, return -1.

# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4

# Constraints:
# 1 <= nums.length <= 10^4
# -10^4 < nums[i], target < 10^4

# Because the input is sorted in ascending order,
# we can do better than O(n) using binary search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left/right/mid pointers
        L, R = 0, len(nums) - 1

        # While the pointers have not crossed
        while L <= R:
            # Update middle pointer
            M = (L + R) // 2

            # If less, shrink left
            if nums[M] < target:
                L = M + 1

            # If more, shrink right
            elif nums[M] > target:
                R = M - 1

            # If target found, return index
            else:
                return M

        # If target is not present exit gracefully
        return -1
    # Time: O(log n), Space: O(1)