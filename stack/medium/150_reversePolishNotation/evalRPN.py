# Given an array of strings tokens that represents
# a reverse Polish notation expression, evaluate the
# expression and return the value as an integer.
# Valid operators are +, -, *, and /. Division between
# two integers should truncate toward zero. There is no
# division by zero operation in tokens. 

# Constraints: 
# 1 <= tokens.length <= 10^4
# tokens[i] is either an operator: "+", "-", "*",
# or "/", or an integer in the range [-200, 200].

# Example:
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# Since RPN notation is written and evaluated as
# a linear structure, we can use a stack to store
# and update the mathematical value resulting from
# the expression in linear time. 
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Initialize the stack
        stack = []

        # Iterate over the character list
        for c in tokens:

            # If the operation is addition, pop two
            # values from stack and sum them. Then add
            # sum to the stack
            if c == "+":
                stack.append(stack.pop() + stack.pop())

            # If the operation is multiplication, pop
            # two values from stack and take product,
            # add product to the stack
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            
            # If the operation is subtraction, pop
            # two values from stack and subtract top
            # number from number below
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)

            # If the operation is division, pop two
            # from stack and divide bottom number by
            # the top number
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))

            # If it is a number, add it to stack
            else:
                stack.append(int(c))

        # return the value in stack
        return stack[0]
    # We iterate over the stack at most twice.
    # once to add every input char to the stack
    # once to evaluate each number in an expression.
    # Time: O(2n) => O(n), Space: O(n)