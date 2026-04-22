class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key= lambda x: x[0])
        n = len(intervals)
        for i in range(n):
            start, end = intervals[i]
            if not res:
                res.append([start, end])
                continue
            # print(f"start: {start}, end: {end}, res[-1][0]: {res[-1][0]}, res[-1][1]: {res[-1][1]}")
            if start > res[-1][1]:
                res.append([start, end])
            elif start <= res[-1][1]:
                res[-1][1] = max(end, res[-1][1])
        return res
                
            