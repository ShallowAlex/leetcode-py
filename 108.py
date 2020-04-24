# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:23:22 2020

@author: Alex

code for windows
"""
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        def build(start, end):
            if start > end:
                return None
            mid = (start + end + 1) // 2
            root = TreeNode(nums[mid])
            root.left = build(start, mid-1)
            root.right = build(mid+1, end)
            return root
        return build(0, len(nums)-1)
    
if __name__ == "__main__":
    s = Solution()
    a1 = [-10,-3,0,5,9]
    #a2 = 
    ans = s.sortedArrayToBST(a1)
    print(ans)
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
            