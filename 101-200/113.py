# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sums: int) -> bool:
        def dfs(root, sums):
            if not root:
                return False
            if not root.left and not root.right:
                if sums == root.val:
                    return True
                else:
                    return False
            return dfs(root.left, sums - root.val) or dfs(root.right, sums - root.val)
        # if sums == root.val and (root.left or root.right):
        #     return False
        return dfs(root, sums)