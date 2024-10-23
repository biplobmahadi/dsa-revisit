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
