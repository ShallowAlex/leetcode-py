# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def trees(head, tail):
            if head > tail:
                return [None,]
            ans = []
            for i in range(head, tail+1):
                tree_left = trees(head, i-1)
                tree_right = trees(i+1, tail)
                for l in tree_left:
                    for r in tree_right:
                        node = TreeNode(i)
                        node.left = l
                        node.right = r
                        ans.append(node)
            return ans
                
        return trees(1,n) if n else []