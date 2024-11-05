# O(n) time | O(1) space
def bestSeat(seats):
    if len(seats) == 1:
        return -1 if seats[0] else 0
    gap, res, left = 0, -1, 1
    while left < len(seats)-1:
        while left < len(seats)-1 and seats[left]:
            left+=1
            continue
        right = left
        while not seats[right]:
            right+=1
        distance = right - left
        if gap < distance:
            gap = distance
            res = (right+left-1)//2
        left = right
    return res
    
    
