"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        starts, ends = [], []
        for intvl in intervals:
            starts.append(intvl.start)
            ends.append(intvl.end)
        res = count = s = e = 0
        starts.sort()
        ends.sort()
        while s<len(starts): 
            if starts[s] < ends[e]:
                s+=1
                count+=1
            else: 
                e+=1
                count-=1
            res = max(res, count)
        return res