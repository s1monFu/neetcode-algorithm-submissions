"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key= lambda x: x.start)
        n = len(intervals)

        for i in range(1, n):
            s = intervals[i].start
            e = intervals[i].end
            ls = intervals[i-1].start
            le = intervals[i-1].end
            
            if s < le:
                return False
        return True
