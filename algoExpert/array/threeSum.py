def threeNumberSum(array, targetSum):
    array.sort()
    triplets = []

    for i, num in enumerate(array):
        left, right = i+1, len(array)-1
        while left<right:
            total = num + array[left] + array[right]
            if total > targetSum:
                right -= 1
            elif total < targetSum:
                left += 1
            else:
                triplets.append([num, array[left], array[right]])
                left += 1
                right -= 1
    return triplets

def threeNumberSum2(array, targetSum):
    res = []
    array.sort()
    for i in range(len(array)-2):
        l, r = i+1, len(array)-1
        while r > l:
            total = array[i] + array[l] + array[r]
            if total > targetSum:
                r -= 1
            elif total < targetSum:
                l += 1
            else:
                res.append([array[i], array[l], array[r]])
                l+=1
                r-=1
    return res
            
