class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if intervals == [[]]:
            return intervals
        intervals.sort(key = lambda i:i[0])
        n = len(intervals)
        i = 0
        while i < n-1:
            if intervals[i][1] >= intervals[i+1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i+1][1])
                intervals.pop(i+1)
                n -= 1
            else:
                i += 1
        return intervals