"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        """
        are the intervals non overlapping 
        """
        intervals.sort(key=lambda x: x.start)
        
        n = len(intervals)
        for i in range(1,n):
            prev_start,prev_end = intervals[i-1].start, intervals[i-1].end
            curr_start, curr_end = intervals[i].start, intervals[i].end
            if max(curr_start, prev_start) < min(prev_end,curr_end):
                return False
        return True