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

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapWater(height))


def trapWaterOptimal(height: list):
    i, j, maxLeft, maxRight, total = 0, len(height) - 1, 0, 0, 0

    while j > i:
        if height[j] >= height[i]:
            maxLeft = max(maxLeft, height[i])
            total += maxLeft - height[i]
            i += 1
        else:
            maxRight = max(maxRight, height[j])
            total += maxRight - height[j]
            j -= 1
    return total

print(trapWaterOptimal(height))
