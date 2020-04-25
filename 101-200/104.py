# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        node = [root]
        child = []
        ans = 0
        while node:
            p = node.pop()
            if p.left:
                child.append(p.left)
            if p.right:
                child.append(p.right)
            if not node:
                ans += 1
                node = child
                child = []
        return ans