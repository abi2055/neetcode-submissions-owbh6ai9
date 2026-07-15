# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 789 + 342
        # 1131
        # use the carryover addition 

        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            if l1:
                value1 = l1.val
            else:
                value1 = 0

            if l2:
                value2 = l2.val
            else:
                value2 = 0

            # these checks ensure that None isnt being added to int
            # in the case that the lists are different lengths

            addition = value1 + value2 + carry
            # adding the values together with the carry like typical addition
            carry = addition // 10 
            # the remaining value will either be 1 or 0
            curr.next = ListNode(addition % 10)
            # the next value would be the remainder in the new list
            curr = curr.next

            if l1:
                l1 = l1.next
            else:
                l1 = None
            
            if l2:
                l2 = l2.next
            else:
                l2 = None

            # checks to prevent any unwanted behaviour falling of the list

        return dummy.next

            

            
            
                
