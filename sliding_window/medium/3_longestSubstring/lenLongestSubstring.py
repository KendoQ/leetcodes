# Given a string s, find the length of the longest substring
# without repeating characters.

# Constraints:
# 0 <= s.length <= 5 * 10^4

# Example:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# The brute force solution involves checking every 
# contiguous substring for duplicates in O(n^3) time.
# We can improve this by using a sliding window to
# check for duplicates in O(n) time.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Initialize left pointer and result
        L, res = 0, 0

        # Initialize set to store substring
        mySet = set()

        # Loop over the string index
        for R in range(len(s)):

            # If we encouner a duplicate char, shrink
            # the window by moving pointer to right until
            # duplicate is removed from set
            while s[R] in mySet:
                mySet.remove(s[L])
                L += 1

            # Add char to the substring and update the
            # max length
            mySet.add(s[R])
            res = max(res, R - L + 1) #len(mySet)

        # Return result
        return res
    # Function passes over the string one time and the 
    # set is at most the size of the input
    # Time: O(n), Space: O(n)