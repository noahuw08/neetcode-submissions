# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # true if a subtree of root contains the same structure and node values of subroot, otherwise false

        # think about: does subroot exist anywhere inside the tree rooted at the curr root?
        # does it exist somewhere in the left subtree? right subtree?
            # left -> self.isSubtree(root.left, subRoot)
            # right -> self.isSubtree(root.right, subRoot)
        
        # we also need to check if the subroot tree is exaclty the same as the one starting at the current root we're looking at? (example 2 shows this detail)


        # if the subRoot is empty, simply return true
        if not subRoot:
            return True
        # if root is empty but subroot is not, its not a subtree
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True
        # otherwise keep checking for its left and right, whether either of them has sametree
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))

        

    # helper to check if two trees matches exactly
    def sameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # sameTree returns True if the trees rooted at root and subRoot are identical
        if not root and not subRoot:
            return True
        if root and subRoot and root.val == subRoot.val:
            # if both nodes exist, and their values are also the same, recursively check with its left and right subtrees
            return self.sameTree(root.left, subRoot.left) and self.sameTree(root.right, subRoot.right)
        


