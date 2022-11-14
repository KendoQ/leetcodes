""" Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters 
of a different word or phrase, typically using all the original letters exactly once. """

# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Example 2:
# Input: strs = [""]
# Output: [[""]]

from collections import defaultdict
class Solution:
    # The obvious solution involves sorting each string
    # to determine if it is an anagram
    def groupAnagrams2(self, strs):
        counts = defaultdict(list)
        for r in strs:
            # add the string to hashmap using its sorted form as the key
            # Sorted() returns a list which cannot be a key, so
            # we cast as a tuple
            counts[tuple(sorted(r))].append(r)
        return counts.values()
    # Time complexity is O(nlogn) because of the sorting

    # The optimal soltion also uses a hashmap, but
    # we avoid sorting and instead count the occurence
    # of each alpha character, this count tuple(list) is 
    # used as the key for the hashmap
    def groupAnagrams(self, strs):
        counts = defaultdict(list)
        # There are 26 letters in alpha, so the tuple(list)
        # key will be this size
        for s in strs:
            count = [0] * 26
        # Iterate through characters
            for c in s:
                # Return ascii code of each characted, zeroed at 'a'
                count[ord(c) - ord('a')] += 1
        # Add the count to the counts dict
            counts[tuple(count)].append(s)
        return counts.values()