# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # idea: for each node keep track of its diameter.
        diameter = 0
        def dfs(root):
            nonlocal diameter
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            # this line because we need to keep track of the max diameter across all nodes
            # the max diameter could be found at any node
            diameter = max(diameter, left + right)
            # at the end return the max height of the child(s) (either left or right) for its parent.
            return 1 + max(left, right)
        dfs(root)
        return diameter




        




            