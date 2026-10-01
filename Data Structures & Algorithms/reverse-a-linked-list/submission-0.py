# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Intuition: create 3 pointers. a prev node, curr node, and next node

        # solve with recursion: think about this example: 1 -> 2 -> 3 -> 4
            # same intuition with Fibonacci qs. at start you at node 1, you want to reverse 1->2->3->4, but first you'd need to reverse 2->3->4, but you'd also need to reverse 3->4, and then 4. so after recursively going until 4 (last node), this should become the new head in order to reverse the list.
            # after the recursion exits, it returns back to its call stack and pop one recurive call at a time.
            # meaning that after we recursively go to end of list (recursion exits), 4 must be the new head, then 3, then 2, and then 1. We can achieve this by performing this reverse logic when the recurive calls from the call stack getting popped one by one:
            # LOGIC: at head.next being 4 (the base case we're at), the head is currently 3. We need to point the next node to 3 to have a reversal of 4->3.
                # since head.next is 4, and when we assign head.next.next = head (since head is currently 3), we've successfully pointed the next node of head.next to be current head, which is essentially 4->3.
                # as the recursive calls getting popped out of stack one by one, it'll eventually be 4->3->2->1 and all recurive calls have been alled popped out of stack!
        
        # edge case: if the list is null
        if not head:
            return None
        
        # recurisvely traverse through the linked list. at each node we update the head, then point next to the next node of the list
        curr = head
        # base case: if the next node is null, we've reached the end of the list and recursion exits. otherwise keep recurisvely traversing through the list
        if head.next:
            curr = self.reverseList(head.next)
        # after recursion exits, it returns back to reverseList(3) (start getting popped out of call stack). at reverseList(3), the head is 3, and head.next is 4. since we wnat to reverse the order from 3->4 to 4->3, we update the next node of 4 to be 3, meaning:
            head.next.next = head
        # and as each earlier recursive call is popped out of call stack one at a time (reverseList(2), then reverseList(1)), repeat this same reversal logic until every call has been popped out of the call stack, then we return the new linked list that's reversed.
        
        # this is when head.next points to null (None), when the recursion reaches end, before it exits and the earlier recursive calls are popped out of stack one by one.
        head.next = None
        return curr



        







