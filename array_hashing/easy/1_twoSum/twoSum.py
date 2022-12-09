# Given an array nums and an integer target, return
# the indices of two numbers in nums that sum to target
# Guaranteed to have one solution

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]

# Ignoring the brute force method, we can use a hashmap to store the
# difference between the target and the current number.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a hash map
        diffMap = {}

        # Iterate through the array and indices
        for i, num in enumerate(nums):

            # If the number matches a difference, return both indices
            if num in diffMap:
                return [diffMap[num], i]

            # Compute the difference with target
            diff = target - num

            # Add the difference and its array index to map
            diffMap[diff] = i
        # We are iterating through array at most once and creating a map
        # Time complexity is O(n)
        # Space: O(n)

    # Brute force method compares every pair of integer sums to the target
    def twoSum1(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
    # Time complexity: O(n^2)
    # Space complexity: O(1)