# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # put values in an array and then reorder values

        # store = []
        # re_array = []
        # current = head 
         
        # while current:
        #     store.append(current.val)
        #     current = current.next

        # print(store)

        # p1 = 0
        # p2 = len(store) - 1

        # while p2 > p1:
        #     re_array.append(store[p1])
        #     re_array.append(store[p2])
        #     p1 += 1
        #     p2 -= 1
        
        # print(re_array)

        # start with fast and slow pointer 
        # fast is x2 of slow
        # then reverse the links of the lists, slow pointer is the end of list 1
        # fast pointer is the end of list 2
        # then merge the nodes in the reordered format 

        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # getting positions needed

        # reverse the links of list 2 
        list2 = slow.next 
        # this is the head 
        prev = None
        slow.next = None
        # with the reversion the head will reference null

        while list2:
            temp = list2.next
            list2.next = prev
            prev = list2
            list2 = temp

        # the merge
        first_list = head
        second_list = prev
        while second_list:
            temp1 = first_list.next
            temp2 = second_list.next
            first_list.next = second_list
            second_list.next = temp1
            first_list = temp1
            second_list = temp2





            



