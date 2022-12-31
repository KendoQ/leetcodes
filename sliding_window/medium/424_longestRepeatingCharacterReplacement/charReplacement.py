# Given a string s and integer k, you can choose any
# character of the string and change it to any other
# uppercase English character. You can perform this
# operation at most k times. Return the length of the
# longest substring containing the same letter you can
# get after performing the above operations.

# Constraints:
# 1 <= s.length <= 10^5
# s consists of only uppercase English letters.

# Example:
# Input: s = "AABABBA", k = 1
# Output: 4 
# Explanation: Replace the one 'A' in the middle with
# 'B' and form "AABBBBA". The substring "BBBB" has the
# longest repeating letters, which is 4. We can also
# replace the first 'B' with 'A' and get "AAAABBA" 

# The brute force solution involves checking every
# substring i O(n^2) time. We can improve this by
# using a sliding window to check for duplicates in
# O(n) time. There are two possible solutions, one
# is more optimal but requires more explanation.
class Solution:
    def characterReplacement2(self, s: str, k: int) -> int:
        # Initialize the result and left pointer
        res, L = 0, 0

        # Hashmap to store the count of each alpha
        counts = {}

        # Iterate over right pointer
        for R in range(len(s)):

            # Increase count of current char in map 
            counts[s[R]] = counts.get(s[R], 0) + 1

            # The window is valid if size of window
            # minus count of most repeating char in 
            # window is less than k or == k, since
            # we have enough replacements
            while R - L + 1 - max(counts.values()) > k: # window is invalid

                # Shrink the window from left and update
                # the map
                counts[s[L]] -= 1
                L += 1

            # Update the result
            res = max(res, R - L + 1)
        
        # Return the result
        return res
    # Searching through the map each iteration
    # for the max value is O(26), so worst time is O(26n)
    # or O(n). Space: O(26) or O(1).

    # This solution is not bad and actually acceptable,
    # but it turns out we can do even better with a small
    # adjustment
    def characterReplacement(self, s: str, k: int) -> int:
        # Initialize the result and left pointers, and an
        # extra value to track the count of the maximum
        # occuring character
        res, L, maxCount = 0, 0, 0 

        # Map to store the counts of characters
        counts = collections.defaultdict(int)

        # Iterate over the right pointer
        for R in range(len(s)):

            # Increase count of current char
            counts[s[R]] += 1

            # Update the max count
            maxCount = max(maxCount, counts[s[R]])

            # Shrink the window if it is invalid
            while R - L + 1 - maxCount > k:
                counts[s[L]] -= 1
                L += 1
            
            # Update the result
            res = max(res, R - L + 1)

        # Return the result
        return res
    # By not searching for a the maximum value
    # each time the map is updated and just
    # keeping the global maximum, we save a 
    # bit of time. Note we dont neet to decrement
    # since it would not change the result
    # Time: O(n), Space: O(1)