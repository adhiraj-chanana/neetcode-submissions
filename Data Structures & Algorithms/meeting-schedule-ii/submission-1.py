"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        intervals.sort(key=lambda x:x.start)
        q=[]
        for i in intervals:
            if not q:
                q.append([i.end,i.start])
            else:
                s=q[0]
                if s[0]<=i.start:
                    heapq.heappop(q)
                heapq.heappush(q,[i.end, i.start])
        return len(q)
        