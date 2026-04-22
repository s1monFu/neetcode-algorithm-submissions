class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        n = len(intervals)
        for i in range(n):
            l = intervals[i]
            if newInterval[1] < l[0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > l[1]:
                res.append(l)
            else:
                newInterval = [min(newInterval[0], l[0]), max(newInterval[1], l[1])]
        res.append(newInterval)
        return res