# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # after processing a node's left and right, that's another level
        # queue-based bfs
        # init a queue for enqueue and dequeue operations at each tree level
        # and a level list to store all nodes within a level.
        res = []

        q = collections.deque()
        q.append(root)

        # while we not hitting the end of the binary tree:
        while q:
            level = []
            # process nodes by each level
            for i in range(len(q)):
                node = q.popleft()
                # append all nodes in a level to a list, and enqueue the nodes of the next level into the queue q
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res








