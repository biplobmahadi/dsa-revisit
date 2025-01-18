class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax, rightMax, res = [0]* len(height), [0]* len(height), 0
        maxVal = height[0]
        for i in range(1, len(height)):
            maxVal = max(maxVal, height[i-1])
            leftMax[i] = maxVal
        maxVal = height[len(height)-1]
        for i in range(len(height)-2, -1, -1):
            maxVal = max(maxVal, height[i+1])
            rightMax[i] = maxVal
        for i in range(len(height)):
            low = min(rightMax[i], leftMax[i])
            if low > height[i]:
                res += low - height[i]
        return res
    
class Solution2:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        maxLeft, maxRight = height[0], height[len(height)-1]
        l, r = 0, len(height)-1
        total = 0
        while r > l:
            if height[l] < height[r]:
                diff = min(maxLeft, maxRight)
                if diff > height[l]:
                    total += diff - height[l]
                l+= 1
                maxLeft = max(maxLeft, height[l])
            else:
                diff = min(maxLeft, maxRight)
                if diff > height[r]:
                    total += diff - height[r]
                r-= 1
                maxRight = max(maxRight, height[r])
        return total