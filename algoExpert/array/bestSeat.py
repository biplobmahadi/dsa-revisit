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
    

def bestSeat(seats):
    if len(seats) < 3: return -1
    res, gap = -1, 0
    i = 1
    while i < len(seats)-1:
        if seats[i]:
            i+= 1
            continue
        l = r = i
        while r < len(seats)-1 and seats[r] == 0:
            r+=1
        if r-l > gap:
            gap = r-l
            res = l + ((r-l-1)//2)
        i = r+1
    return res

