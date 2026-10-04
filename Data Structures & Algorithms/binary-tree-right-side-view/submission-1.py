# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        #  level order, queue-based bfs

        rightSideView = []
        q = collections.deque()
        q.append(root)

        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            # to get the right side view at each level, get the rightmost node from the current level's list that is not null. treat it as a stack: iteratively checking with each element top of the stack
            if level:
                rightSideView.append(level[-1])
            # while level:
            #     if not level[-1]:
            #         level.pop()
            #     else:
            #         rightSideView.append(level[-1])
        return rightSideView





        # queue logic ex:
            # curr level at level 3: [4, 5, null, null]
                # return 5 as the righgt side view of the level 3
                # return any rightmost node in the current level's list that is not null
        
    
        


