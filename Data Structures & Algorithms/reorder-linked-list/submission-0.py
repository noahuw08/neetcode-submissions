# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reorderNodes(root, curr):
            # base case for when recursion hits the exit cond.
            if not curr:
                return root

            # recursive logic
            root = reorderNodes(root, curr.next)
            if not root:
                return None
            tmp = None
            # base case for when the "swap" between forward and unwinding ends:
            # root == curr: (odd length), root.next == curr: even length
                # when all swaps are done, set the next for the current node to be null
            if root == curr or root.next == curr:
                curr.next = None
            else:
                tmp = root.next
                root.next = curr
                curr.next = tmp
            return tmp
        head = reorderNodes(head, head.next)
        






            



            
            

            












