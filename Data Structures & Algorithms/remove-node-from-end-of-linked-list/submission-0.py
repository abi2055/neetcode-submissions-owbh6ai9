# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # simplest approach i can think of 
        # keep an ongoing count 
        # when you get to the ith index just do a reconnection with the node removed
        # not the most clever solution that is with fast and slow pointers 

        linked_len = 0
        curr = head 
        while curr:
            linked_len += 1
            curr = curr.next

        target_index = linked_len - n

        prev = None
        curr = head 

        for i in range(target_index):
            print(i)
            prev = curr
            curr = curr.next

        if prev is None:
            return head.next
        prev.next = curr.next

        return head
