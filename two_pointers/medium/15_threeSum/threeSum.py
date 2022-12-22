# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that 
# i != j, i != k, and j != k, 
# and nums[i] + nums[j] + nums[k] == 0.
# Solution set must not contain duplicate triplets

# Constraints:
# 3 <= len(nums) <= 3000
# -10^5 <= nums[i] <= 10^5

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: The triplets [-1,-1,2] and [-1,0,1] are unique
# and sum to 0.

# The brute force method is not v scalable with time O(n^3)
# We can speed this up significantly by first sorting
# Taking care to avoid duplicate triplets, we can then loop
# through each num[i] solving a sorted two-sum with the
# remainder of the array
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Initialize the result array and sort the input
        res = []
        nums.sort()

        # Loop through each index, number in sorted array
        for i, a in enumerate(nums):

            # Do not create duplicate triplets by starting
            # search with the same number
            if i > 0 and nums[i -1] == a:
                continue

            # Initialize left and right pointers
            L, R = i + 1, len(nums) - 1

            # Solve sorted two sum using a as third digit
            while L < R:
                threeSum = a + nums[L] + nums[R]

                # If sum > 0, move R left
                if threeSum > 0:
                    R -= 1

                # If sum < 0, move L right
                elif threeSum < 0:
                    L += 1

                # If sum == 0, update result and move
                # the pointers for next check
                else:
                    res.append([a, nums[L], nums[R]])
                    L += 1 # R will update above
                    
                    # Do not use same L and dupe the triplet
                    while nums[L - 1] == nums[L] and L < R:
                        L += 1

        # Return result
        return res
    # We sort the array and then loop through it at most
    # twice. We avoid creating a hash so space is constant
    # Time complexity: O(nlogn) + O(n^2) = O(n^2)
    # Space: O(1) or O(n) depending on the sort operation