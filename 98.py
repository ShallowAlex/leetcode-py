# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        p = root
        stack = []
        pre = float('-inf')
        while stack or p:
            while p:
                stack.append(p)
                p = p.left
            p = stack.pop()
            if p.val <= pre:
                return False
            pre = p.val
            p = p.right
        return True

            