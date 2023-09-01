def trapWater(height: list):
    n = len(height)
    res = 0

    for i in range(0, n):
        leftMax, rightMax = 0, 0
        for j in range(i-1, -1, -1):
            if height[j] > leftMax:
                leftMax = height[j]
        for k in range(i+1, n):
            if height[k] > rightMax:
                rightMax = height[k]
        minVal = min(leftMax, rightMax)
        if minVal > height[i]:
            h = minVal - height[i]
            res += h
    
    return res

height = [4,2,0,3,2,5]
print(trapWater(height))

