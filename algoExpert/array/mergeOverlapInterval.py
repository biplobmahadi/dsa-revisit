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
