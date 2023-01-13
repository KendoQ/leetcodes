# Given n pairs of parentheses, make a function to
# generate all combinations of valid parentheses, and
# return these combinations in a list of strings

# Constraints:
# 1 <= n <= 8

# Example:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Since each parentheses can be evaluated in a linear
# structure, we can use a stack. To generate all possible
# combinations, we can use recursion/backtracking while
# tracking the amount of open and closed parentheses 
# currently in the stack
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # Initialize the stack for the parentheses
        # and the list for the resulting combinations
        stack, res = [], []

        # Define recursive function to expand all
        # combinations of parentheses
        def recur(open: int, closed: int):
            # If we have a full combination of n pairs
            # update result with combo and back out
            if open == closed == n:
                res.append("".join(stack))
                return

            # If we can add an open parenthese, do so
            if open < n:
                stack.append("(")

                # Recur to finish the combo, increase
                # count of open parentheses
                recur(open + 1, closed)

                # Clean up by popping from stack
                stack.pop()

            # If we can add a closed parenthese, do it
            if closed < open:
                stack.append(")")

                # Finish the combination
                recur(open, closed + 1)

                # Clean up
                stack.pop()
        
        # Call the function with an empty count
        recur(0, 0)

        # Return the resulting combinations
        return res
    # We expand the combinations recursively in
    # linear time, and use a stack to store the 
    # n pairs of parentheses
    # Time: O(n), Space: O(2n) => O(n)