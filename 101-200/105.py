# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        node = TreeNode(preorder[0])
        n = inorder.index(preorder[0])
        node.left = self.buildTree(preorder[1:n+1], inorder[:n])
        node.right = self.buildTree(preorder[n+1:], inorder[n+1:])
        return node