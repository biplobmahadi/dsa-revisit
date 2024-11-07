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

# O(n) time | O(1) space
def majorityElementOptimal(array):
    res = array[0]
    count = 1

    for i in range(1, len(array)):
        if count == 0:
            res = array[i]
            
        if res == array[i]:
            count += 1
        else:
            count -= 1
    return res
