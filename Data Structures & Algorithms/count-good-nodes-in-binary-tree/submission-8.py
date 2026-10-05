# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # bfs, dfs
        # return the number of "good" nodes within the tree
            # "good": the path from root to a node contains no nodes with value > node x
            # meaning along the path, 

        # good nodes along the path is determined separately by left and right because of the root separation
            # queue for eacah left and right, starting from root

        goodNodesCount = 0
        q = collections.deque()
        q.append([root, root.val])
        while q:
            node, pathMax = q.popleft()
            if node:
                if node.val >= pathMax:
                    goodNodesCount += 1
                pathMax = max(pathMax, node.val)
                if node.left:
                    q.append([node.left, pathMax])
                if node.right:
                    q.append([node.right, pathMax])
        return goodNodesCount



        # goodNodesCount = 1

        # leftPath = []
        # rightPath = []
        # leftQ = collections.deque()
        # rightQ = collections.deque()

        # leftQ.append(root.left)
        # rightQ.append(root.right)

        # leftPath.append(root.val)
        # rightPath.append(root.val)

        # # left trees from root:
        # while leftQ:
        #     # at each subtree level
        #     level = []
        #     for _ in range(len(leftQ)):
        #         node = leftQ.popleft()
        #         if node:
        #             level.append(node.val)
        #             leftQ.append(node.left)
        #             leftQ.append(node.right)
        #             if node.val >= max(leftPath):
        #                 goodNodesCount += 1
        #             else:
        #                 continue
        #     if level:
        #         leftPath.extend(level)


        # # right trees from root:
        # while rightQ:
        #     level = []
        #     for _ in range(len(rightQ)):
        #         node = rightQ.popleft()
        #         if node:
        #             level.append(node.val)
        #             rightQ.append(node.left)
        #             rightQ.append(node.right)
        #             if node.val >= max(rightPath):
        #                 goodNodesCount += 1
        #             else:
        #                 continue
        #     if level:
        #         rightPath.extend(level)
            
        # return goodNodesCount







        # think abt how to use queue to compare the current node with all previous nodes along a path so far
        # compare the current node with all previous levels' nodes , either left or right
        # keep appending nodes from previous levels to the left and right queue

        # at a level, keep track of the max of all previous levels. if invalid, don't append to the queue of that level

        # treat this problem as bfs , but separate the problem between left and right subtrees from the root
