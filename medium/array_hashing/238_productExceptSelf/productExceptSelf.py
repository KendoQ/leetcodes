# Given an integer array nums, return an answer array answer such that
# answer[i] is equal to the product of all the elements of nums except
# nums[i]. The product of any prefix or suffix of nums is guaranteed to
# fit in a 32-bit integer.

# Constraints:
# 2 <= nums.length <= 10^5
# -30 <= nums[i] <= 30

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # create an array to store the result
        result = [1] * len(nums)

        # compute the prefix product vector, padding with 1
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]

        # compute the suffix product vector, padding with 1
        suffix = 1
        for i in range(len(nums) -1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
# Notes:
# Time complexity: O(N)
# Space complexity: O(1)
# We avoid creating prefix and suffix arrays, space would be O(N)