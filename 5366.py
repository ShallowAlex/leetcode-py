# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 16:00:42 2020

@author: Alex

code for windows
"""
class Solution:
    def hasValidPath(self, grid):
        Flag=False
        n=len(grid)#行
        m=len(grid[0])#列
        vis=[ [ 0 for _ in range(m)]for _ in range(n)]
        
        stack=[]
        stack.append((0,0))
        vis[0][0]=1
        while stack:
            x,y=stack.pop()
            if x==n-1 and y==m-1:
                return True
            #向左
            if grid[x][y] in [1,3,5] and y-1>=0 and vis[x][y-1]==0 and grid[x][y-1] in [1,4,6]:
                vis[x][y-1]=1
                stack.append((x,y-1))
                
            #向右
            if grid[x][y] in [1,4,6] and y+1<m and vis[x][y+1]==0 and grid[x][y+1] in [1,3,5]:
                vis[x][y+1]=1
                stack.append((x,y+1))

            #向上
            if grid[x][y] in [2,5,6] and x-1>=0 and vis[x-1][y]==0 and grid[x-1][y] in [2,3,4]:
                vis[x-1][y]=1
                stack.append((x-1,y))
                
            #向下
            if grid[x][y] in [2,3,4] and x+1<n and vis[x+1][y]==0 and grid[x+1][y] in [2,5,6]:
                vis[x+1][y]=1
                stack.append((x+1,y))
        
        return False

if __name__ == "__main__":
    s = Solution()
    a1 = [[2],[2],[2],[2],[2],[2],[6]]
    #a2 = 
    print(s.hasValidPath(a1))