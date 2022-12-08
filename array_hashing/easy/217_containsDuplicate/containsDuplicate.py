# Given an integer array, return true if any value appears 
# at least twice in the array, and return false if every value is unique

# Example:
# Input: [1,2,3,1]
# Output: true

# There are many solutions. We can trade off space for time complexity
class Solution:
    # Method uses a hashset optimized for fast lookups
    def containsDuplicate(self, nums):
        seen = set()

        # Iterate over entire array
        for n in nums:

            # If we have seen the number before, return True
            if n in seen:
                return True

            seen.add(n)

        return False
    # This method finds the first duplicate in the array
    # Time complexity is O(n) and space is O(n)

    # Single-line method converts entire input array to a set
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
    # Finds all duplicates in the array (can be used to count them)
    # Time complexity is O(n) and space is O(n)
    # Is a bit faster than the previous method

    # The brute force method compares every element to every other element
    def containsDuplicate(self, nums):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):

                if nums[i] == nums[j]:
                    return True
                    
        return False
    # Time complexity is O(n^2) and space is O(1)