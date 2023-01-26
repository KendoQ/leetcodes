# Given the head of a singly-linked list, reverse
# the list and return the head of the reversed
# list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# We can approach the problem using recursion,
# but the simplest and most optimal solution
# is usually to use two-pointers. One pointer
# will track the current head node and the 
# other will store the previous node.
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize the current and previous pointers
        curr, prev = head, None

        # While we have not reached terminal node
        while curr:
            # Save the next pointer
            foo = curr.next

            # Reverse the current node
            curr.next = prev

            # Update prev pointer
            prev = curr

            # Next pointer
            curr = foo

        # Return the reversed list head node
        return prev
    # Time: O(n), Space: O(1)

