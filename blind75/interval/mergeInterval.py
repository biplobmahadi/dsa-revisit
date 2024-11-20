class Solution:
    def merge(self, intervals):
        intervals.sort()
        curr = intervals[0]
        res = []
        for i in range(1, len(intervals)):
            start, end = intervals[i][0], intervals[i][1]
            if curr[1] < start:
                res.append(curr)
                curr = intervals[i]
            else:
                curr = [min(start, curr[0]), max(end, curr[1])]
        res.append(curr)
        return res