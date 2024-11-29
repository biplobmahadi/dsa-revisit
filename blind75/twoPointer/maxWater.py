class Solution:
    def maxArea(self, height) -> int:
        l, r, maxWater = 0, len(height)-1, 0
        while r > l:
            maxWater = max(maxWater, (min(height[l], height[r]) * (r-l)))
            if height[r] >= height[l]: l+=1
            else: r-=1
        return maxWater