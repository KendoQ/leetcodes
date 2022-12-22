# Given an array of integeres sorted in non decreasing
# order, find two numbers that add up to a specific
# target number and return there indices if the original 
# array is 1-indexed.

# Constraints:
# -1000 <= numbers[i] <= 1000
# There is exactly one solution

# Example:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index 1 and 2 are returned.

# The brute force method involves searching every combination
# of numbers in at worst O(n^2) time. We can achieve better,
# with constant extra space by using two-pointers and 
# exploiting the fact array is sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Initialize the left and right pointers
        L, R = 0, len(numbers) - 1

        while L < R:
            sumLR = numbers[L] + numbers[R]

            # If the sum is larger than target, move R left
            if sumLR > target:
                R -= 1

            # If the sum is less than target, move L right
            elif sumLR < target:
                L += 1

            # We are guaranteed a solution
            else:
                return [L + 1, R + 1]

        # Line never executes, but is needed to compile
        return []
    # We are searching the array one time and using constant space
    # Time: O(n), Space: O(1)