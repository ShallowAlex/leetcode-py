# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def backtrack(p):
            if p.left:
                backtrack(p.left)
            ans.append(p.val)
            if p.right:
                backtrack(p.right)
            
        ans = []
        if root:
            backtrack(root)
        return ans