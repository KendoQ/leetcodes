# Given an integer array, determine the length of the longest
# consecutive sequence that can be made from the array elements

# Constraints:
# Algoritihm must run in O(n) time

# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4

# The constraint of O(n) time means that we can't sort the array
# There are two ways I solve this problem that each invole using
# the set data structure which has fast lookup times
class Solution:
    def longestConsecutive1(self, nums: List[int]) -> int:
        # The first method is very compact programmatically, but
        # it is a bit slower
        numSet = set(nums)
        longest = 0

        # Iterate through each element in the array
        for n in nums:
            # If element is start of a sequence
            if (n - 1) not in numSet:

                # Find length of sequence
                length = 0
                while (n + length) in numSet:
                    length += 1
                
                # Update the longest sequence length
                longest = max(longest, length)

        return longest
    # This method ensures that we consider each element max twice
    # Time is O(n)

    def longestConsecutive2(self, nums: List[int]) -> int:
        # The second solution is a bit more complex and a bit faster
        numSet = set(nums)
        longest = 0

        # Iterate through each element in the array
        for n in nums:
            # If element has been visited, skip
            if n not in numSet:
                continue

            # Initialize lenth and left/right pointers
            length = 1
            left = n - 1
            right = n + 1

            # Check for left sequence
            while left in numSet:
                length += 1
                numSet.remove(left)
                left -= 1

            # Check for right sequence
            while right in numSet:
                length += 1
                numSet.remove(right)
                right += 1

            # Update the longest sequence length
            longest = max(longest, length)

        return longest
        # This two-pointer method ensures we consider each element once,
        # so the time complexity is O(n) and a bit faster than the first method