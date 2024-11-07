# O(n) time | O(n) space
def majorityElement(array):
    count = {}
    for num in array:
        count[num] = count.get(num, 0) + 1
    res = [-1, -1]
    for val, key in count.items():
        if key > res[0]:
            res = [key, val]
    return res[1]
