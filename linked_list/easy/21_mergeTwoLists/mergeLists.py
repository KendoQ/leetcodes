# Given the heads of two sorted linked lists list1
# and list2. Merge the two lists into one sorted 
# list. The list should be made by splicing together
# the nodes of the first two lists. Return the head 
# of the merged linked list.

# Constraints:
# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# We can use conditional logic to merge the lists
# together by comparing their values. To save a bit
# of extra space, we can use recursion to merge
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Handle the base cases
        if not l1:
            return l2
        elif not l2:
            return l1

        # Compare the values in each list at the head
        # If l1 is least, move head node to next node
        elif l1 < l2:
            l1.next = self.mergeTwoLists(l1.next, l2)

            # Add l1 to the merged list
            return l1

        # Otherwise move l2 to next node
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)

            # Add l2 to merged list
            return l2
    # Time: O(n), Space: O(1)