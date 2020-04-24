# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 17:05:19 2020

@author: Alex

code for windows
"""


if __name__ == "__main__":
    s = Solution()
    a1 = 
    #a2 = 
    print(s(a1))


if __name__ == "__main__":
    s = Solution()
    a1 = [-10,-3,0,5,9]
    #a2 = 
    ans = s.sortedArrayToBST(a1)
    print(ans)
    
#层次遍历tree
    tmplist = []
    treeval = []
    tmplist.append(ans)
    while tmplist:
        for i in range(len(tmplist)):
            p = tmplist.pop(0)
            if p:
                treeval.append(p.val)
                tmplist.append(p.left)
                tmplist.append(p.right)
            else:
                treeval.append(None,)
    while treeval[-1] == None:
        treeval.pop()
    print(treeval)

def buildtree(a1):
    root = TreeNode(a1[0])
    a1 = a1[1:]
    parents = [root]
    i = 0
    child = []
    while parents:
        for p in parents:
            if p:
                p.left = TreeNode(a1[i])
                i += 1
                child.append(p.left)
                if i >= len(a1):
                    break
                p.right = TreeNode(a1[i])
                i += 1
                if i >= len(a1):
                    break
                child.append(p.right)
        a1 = a1[i:]
        parents = child
    return root