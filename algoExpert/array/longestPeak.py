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

def longestPeak(array):
    res, i = 0, 1
    while i < len(array)-1:
        isPeak = array[i-1] < array[i] > array[i+1]
        if not isPeak:
            i+=1
            continue
        l, r = i-1, i+1
        while l> 0 and array[l-1] < array[l]:
            l-=1
        while r<len(array)-1 and array[r+1]<array[r]:
            r+=1
        res = max(res, r-l+1)
        i=r+1
    return res
