# O(nlog(n)) time | O(n) space
def mergeOverlappingIntervals(intervals):
    intervals.sort()
    nonIntervals = []
    curr = intervals[0]
    for i in range(1, len(intervals)):
        if curr[1] >= intervals[i][0]:
            curr = [min(curr[0], intervals[i][0]), max(intervals[i][1], curr[1])]
        else:
            nonIntervals.append(curr)
            curr = intervals[i]
    nonIntervals.append(curr)
    return nonIntervals

def mergeOverlappingIntervals(intervals):
    intervals.sort()
    res = []
    prev = intervals[0]
    for i in range(1, len(intervals)):
        curr = intervals[i]
        if curr[0] <= prev[1]:
            prev = [min(curr[0], prev[0]), max(curr[1], prev[1])]
        else:
            res.append(prev)
            prev = curr
    res.append(prev)
    return res