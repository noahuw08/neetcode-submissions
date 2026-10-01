# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        cnt = 1
        def depthCount(root, cnt):
            if not root.left and not root.right:
                return cnt
            elif root.left and not root.right:
                return depthCount(root.left, cnt + 1)
            elif not root.left and root.right:
                return depthCount(root.right, cnt + 1)
            else:
                left_depth = depthCount(root.left, cnt + 1)
                right_depth = depthCount(root.right, cnt + 1)
            return max(left_depth, right_depth)
        
        return depthCount(root, cnt)