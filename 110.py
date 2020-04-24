# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def deeptree(node):
            if not node:
                return 0, True

            l, flag1 = deeptree(node.left)
            r, flag2 = deeptree(node.right)
            if not (flag1 and flag2):
                return 0, False
            else:
                return max(l, r)+1, (abs(l-r) < 2)
        return deeptree(root)[1]