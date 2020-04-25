# -*- coding: utf-8 -*-
"""
Created on Fri Mar 20 23:37:42 2020

@author: Alex

code for windows
"""
from typing import List
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
         
class Solution:
    def postorderTraversal(self, root: Node) -> List[int]:
        if not root:
            return root
        stack1 = stack2 = []
        stack1.append(root)
        while stack1:
            print(stack1)
            root = stack1.pop()
            print(stack1)
            print('-',root)
            print('--',root.val)
            #stack2.append(root.val)
            if root.left:
                stack1.append(root.left)
                print('*',root.left)
            if root.right:
                stack1.append(root.right)
                print('***',root.right)
            print(stack1)
        return stack2[::-1]
        
def buildtree(a1):
    root = Node(a1[0])
    a1 = a1[1:]
    parents = [root]
    i = 0
    child = []
    while parents:
        for p in parents:
            if p and i < len(a1):
                p.left = Node(a1[i])
                i += 1
                child.append(p.left)
                if i >= len(a1):
                    break
                p.right = Node(a1[i])
                i += 1
                child.append(p.right)
                if i >= len(a1):
                    break              
        #print(i, a1,[_.val for _ in parents], [ch.val for ch in child])
        parents = child
        child = []
    return root      
if __name__ == "__main__":
    s = Solution()
    a1 = [1,2,3]
    #ans = buildtree(a1)
    #a2 = 
    ans = s.postorderTraversal(buildtree(a1))
    print(ans)
    
# =============================================================================
# #层次遍历tree
#     tmplist = []
#     treeval = []
#     tmplist.append(ans)
#     while tmplist:
#         for i in range(len(tmplist)):
#             p = tmplist.pop(0)
#             if p:
#                 treeval.append(p.val)
#                 tmplist.append(p.left)
#                 tmplist.append(p.right)
#             else:
#                 treeval.append(None,)
#     while treeval[-1] == None:
#         treeval.pop()
#     print(treeval)
# =============================================================================

