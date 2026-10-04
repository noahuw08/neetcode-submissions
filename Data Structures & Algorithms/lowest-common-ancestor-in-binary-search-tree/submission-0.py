# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # return the lowest common ancestor of the two node
        # BST: all left subtree values are smaller than the node value, all right subtree values are larger than node value

        # if both p and q are smaller than node, recursively checking with the left subtrees
        # if both p and q are larger than ndoe, recursively checking with the right subtrees
        # otherwise, (p < node, q > node) or (p > node, q < node), the node is the lca

        # base case,/ exit cond
        if not root or not p or not q:
            return None
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

        






