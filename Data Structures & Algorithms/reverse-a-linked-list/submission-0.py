# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    
        current = head
        prev = None

        while current:
            # the next node after the current head 
            up_next = current.next
            # first iteration references None, second iteration references the one before
            current.next = prev
            # the previous moves to the current node
            prev = current
            # current moves forward one 
            current = up_next

        return prev 

    # head references None
    # current.next references head 