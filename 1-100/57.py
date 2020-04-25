# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:11:10 2020

@author: Alex

code for windows
"""

class Solution:
    def insert(self, intervals, newInterval):
        import bisect
        if not intervals:
            return [newInterval]
        index0 = bisect.bisect(intervals,newInterval)
#        tmp = []
#        for i in intervals:#这里可以用二分优化
#            tmp.append(i[1])
#        index1 = bisect.bisect(tmp,newInterval[1])
        left = 0
        right = len(intervals) - 1
        while left < right:
            mid = (left + right) // 2
            if intervals[mid][1] < newInterval[1]:
                left = mid + 1
            else:
                right = mid
        index1 = left
        if newInterval[1] > intervals[left][1]:
            index1 += 1
        print(left,index1)
        if index0 - 1 >= 0 and newInterval[0] <= intervals[index0 - 1][1]:
            newInterval[0] = intervals[index0 - 1][0]
            index0 -= 1
        if index1 < len(intervals) and newInterval[1] >= intervals[index1][0]:
            newInterval[1] = intervals[index1][1]
            index1 += 1
        return (intervals[:index0] + [newInterval] + intervals[index1:])

if __name__ == "__main__":
    s = Solution()
    a1 = []
    a2 = [2,5]
    print(s.insert(a1,a2))