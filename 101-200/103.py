# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        node = [root]
        ans = []
        flag = 1
        if not root:
            return ans
        while node:
            child = []
            value = []
            for p in node:
                value.append(p.val)
                if p.left:
                    child.append(p.left)
                if p.right:
                    child.append(p.right)
            ans.append(value[::flag])
            node = child
            flag = -1 * flag
        return ans