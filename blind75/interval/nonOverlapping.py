class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        intervals.sort()
        curr = intervals[0]
        count = 0
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if start < curr[1]:
                count += 1
                if end < curr[1]:
                    curr = intervals[i]
            else:
                curr = intervals[i]
        return count
                