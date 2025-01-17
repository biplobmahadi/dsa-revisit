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