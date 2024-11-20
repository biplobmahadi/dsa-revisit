class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i, intvl in enumerate(intervals):
            start, end = intvl[0], intvl[1]
            if newInterval[1] < start:
                res.append(newInterval)
                return res + intervals[i:]
            if end < newInterval[0]:
                res.append(intvl)
            else:
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]
        res.append(newInterval)
        return res