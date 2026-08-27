class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        curhighest=-float('inf')
        removed=0
        intervals=sorted(intervals, key= lambda x:x[1])
       
        for s,b in intervals:
            if s>=curhighest:
                curhighest=b
                continue
            else:
                removed+=1
        
        return removed


