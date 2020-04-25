# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node):
            nonlocal maxsum
            if not node:
                return 0
            l = max(dfs(node.left), 0)
            r = max(dfs(node.right), 0)
            maxsum = max(maxsum, node.val+l+r)
            return node.val + max(l, r)
        maxsum = float('-inf')
        dfs(root)
        return maxsum