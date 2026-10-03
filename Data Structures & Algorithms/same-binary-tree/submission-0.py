# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # same exact structure, and same values at every node of that structure
        # at current node, check if it's the same across p and q
        # so if current node p and q both exist, and their values are also the same, we continue recursively checking with both their children to the left and right
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        # if in one case, either node p or q not exist, or if their val dont' match, false immediately
        else:
            return False

            