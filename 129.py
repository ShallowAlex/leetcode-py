# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def Numbers(node, s):
            if not node:
                return 0
            s = s*10 + node.val
            if node.left or node.right:
                return Numbers(node.left, s) + Numbers(node.right, s)
            else:
                return s
        return Numbers(root, 0)