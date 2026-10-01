# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # index is not given as param,
        # we know there's a cycle if the next of a current node is pointing to the prev node

        seen = set()
        if not head:
            return False

        while head.next:
            if head.val in seen:
                return True
            else:
                seen.add(head.val)
                head = head.next
        return False

        # [1,2,2,2,2], index = 2
