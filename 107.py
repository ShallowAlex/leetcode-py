# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        node = [root]
        child = []
        ans = []
        if not root:
            return []
        while node:
            child = []
            val = []
            for n in node:
                val.append(n.val)
                if n.left:
                    child.append(n.left)
                if n.right:
                    child.append(n.right)
            node = child
            ans.insert(0, val)
        return ans