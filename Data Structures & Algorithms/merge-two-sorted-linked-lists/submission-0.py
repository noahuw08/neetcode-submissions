# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # the idea is that we want a one pass traversal through both linked list at the same time. Create two pointers. Fix one pointer, the other pointer moves if it currently points at a smaller value. Because we want to keep traversing through that list to see if the next node's value of that list is also smaller than the value that the current pointer is at.
            # intuitively, we move whichever pointer that currently points at a smaller value during comparison betwen two sorted linked list.
            # the procedure ends when both pointers are at the end of both lists.

        # at each node of both linked list, compare their value
            # if the value of a list is smaller than the other, update the current head to the node of the smaller value.
        
        # list1.val < list2.val , then recursively merge the remaining of list1
        # list2.val < list1.val, then recursively merge the remaining of list2
        
        # edge case: if either list is empty, return the other
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2




        

        


        