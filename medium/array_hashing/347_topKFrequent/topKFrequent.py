# Given an integer array nums and an integer k, return the 
# k most frequent elements. You may return the answer in any order.

# Constraints:
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# 1 <= k <= nums.length
# Answer is unique

# Example 1:    
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:
# Input: nums = [1], k = 1
# Output: [1]

# Example 3:
# Input: nums = [1, 3, 3, 2, 5, 5, 5], k = 2
# Output: [5, 3]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dictionary to store the frequency of each number
        # create empty frequency bins 
        counts = {}
        freq = [[] for i in range(len(nums) + 1)]

        # Count the occurence of each number in nums
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
        
        # Place each number in the appropriate frequency bin
        for n, c in counts.items():
            freq[c].append(n)

        # Return the top k numbers
        # Lopp through the frequency bins in reverse order
        # at each bin, add the numbers to the result list
        # until we have k numbers, then return the result list
        res = []
        for i in range(len(nums), 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Time complexity: O(N)
# Space complexity: O(N)
# We avoid using a heap and sorting, which would be O(NlogN)