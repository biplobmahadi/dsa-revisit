# class Interval(object):
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end


class Solution:
    def canAttendMeetings(self, intervals) -> bool:
        intervals.sort(key=lambda a: a.start)
        for i in range(len(intervals)-1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True