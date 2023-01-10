# Design a stack that supports push, pop, top,
# and retrieving the minimum element in constant time.
# Implement the stack as the MinStack class with 
# class methods push(), pop(), top(), and getMin()
# Implement each method in O(1) time.

# Constraints:
# -2^31 <= val <= 2^31 - 1
# At most 3*10^4 call will be made to methods
# Methods pop(), top(), getMin() are always called
# on nonempty stacks.

# Example:
# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]
# Output
# [null,null,null,null,-3,null,0,-2]

# The challenge here is to implement the getMin()
# method for the stack. The best way to accomplish
# is to track the minimum at each position.
# Intuitively, we may want to use a single
# variable to track the minimum value. However,
# this will not work because the minimum value
# may change as we push and pop values. We can get
# we want by using a separate stack that has the min
# value and push/pop to both stacks
class MinStack:
    def __init__(self):
        # Initialize the stack and minStack
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # Push to the stack
        self.stack.append(val)

        # Update the min value
        val = min(val, self.minStack[-1]) if self.minStack else val

        # Push to the minStack
        self.minStack.append(val)

    def pop(self) -> None:
        # Pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # Return the top of the stack
        return self.stack[-1]

    def getMin(self) -> int:
        # Return the top of the minStack
        return self.minStack[-1]
# Each method is implemented in O(1) tima and
# we use an additional O(n) space to store the
# minStack.
# Time: O(1), Space: O(n)