def longestPeak(array):
    lenOfLongestPeak = 0
    i = 1
    while i < len(array)-1:
        if array[i-1] < array[i] > array[i+1]:
            left, right = i-1, i+1
            while (left-1>=0 and array[left-1] < array[left]) or (right+1<len(array) and array[right+1] < array[right]):
                if left-1>=0 and array[left-1] < array[left]:
                    left -= 1
                if right+1<len(array) and array[right+1] < array[right]:
                    right += 1
            lenOfLongestPeak = max(lenOfLongestPeak, right-left+1)
            i = right
        i += 1
    return lenOfLongestPeak

