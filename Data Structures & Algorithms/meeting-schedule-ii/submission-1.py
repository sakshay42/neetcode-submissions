"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key = lambda x: x.start)
        counter = defaultdict(int)
        for interval in intervals:
            counter[interval.start]+=1
            counter[interval.end] -=1
        counter_sorted = sorted(list(counter.keys()))
        max_rooms = 0
        curr= 0 
        for i in counter_sorted:
            curr += counter[i]
            max_rooms = max(max_rooms, curr)
        return max_rooms