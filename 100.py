# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        nodep = [p]
        nodeq = [q]
        while nodep:
            p = nodep.pop()
            q = nodeq.pop()
            if p and q and p.val == q.val:
                nodep.append(p.left)
                nodep.append(p.right)
                nodeq.append(q.left)
                nodeq.append(q.right)
            elif (not p) and (not q):
                continue
            else:
                return False
        if nodeq:
            return False
        return True