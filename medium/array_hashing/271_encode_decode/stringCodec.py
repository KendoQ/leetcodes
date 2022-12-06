# Design an algorithm to encode a list of strings to a string.
# The encoded string is then sent over the network and is decoded 
# back to the original list of strings.

# Example 1:
# Input: ["Hello", "World"]
# Output: ["Hello", "World"]

# Since we have to pass through the entire string twice, the time complexity is O(n)
# where n is the length of the string. The space complexity is O(n) as well.

class Codec:
    def encode(self, strs: List[str]) -> str:
        # Encodes a list of strings to a single string.
        res = ""
        for s in strs:
            # The length of the string is added to the front of the string
            # with a semicolon separating the two.
            res += str(len(s)) + ";" + s
        return res
        

    def decode(self, s: str) -> List[str]:
        # Decodes a single string to a list of strings.
        res, i = [], 0

        # Iterate through the string and add the strings to the list.
        while i < len(s):
            j = i

            # The length of each substring is found by iterating through the string
            # until the first semicolon is found.
            while s[j] != ";":
                j += 1
            length = int(s[i:j])

            # The substring is added to the list.
            res.append(s[j + 1:j + 1 + length])

            # The index is updated to the next substring.
            i = j + 1 + length
        return res