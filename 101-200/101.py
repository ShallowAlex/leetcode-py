# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        l = [root]
        r = [root]
        while l:
            p1 = l.pop()
            p2 = r.pop()
            if not p1 and not p2:
                continue
            elif not p1 or not p2:
                return False
            if p1.val == p2.val:
                l.append(p1.left)
                r.append(p2.right)
                l.append(p1.right)
                r.append(p2.left)
            else:
                return False
        if r:
            return False
        return True