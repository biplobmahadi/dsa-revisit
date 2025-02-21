from collections import defaultdict

# O(n^2) time | O(n^2) space - Average
# O(n^3) time | O(n^2) space - Worst
def fourNumberSum(array, targetSum):
    pairMap = defaultdict(list)
    res = []
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            pair = array[i] + array[j]
            comp = targetSum - pair
            if comp in pairMap:
                for val in pairMap[comp]:
                    res.append(val + [array[i] , array[j]])
        for k in range(0, i):
            total = array[i] + array[k]
            pairMap[total].append([array[i] , array[k]])
    return res


def fourNumberSum(array, targetSum):
    res = []
    pairMap = {}
    for i in range(1, len(array)-1):
        for j in range(i+1, len(array)):
            total = array[i]+array[j]
            diff = targetSum - total
            if diff in pairMap:
                for val in pairMap[diff]:
                    res.append(val + [array[i], array[j]])

        for k in range(0, i):
            total = array[k] + array[i]
            if total in pairMap:
                pairMap[total].append([array[k], array[i]])
            else:
                pairMap[total] = [[array[k], array[i]]]
    return res
