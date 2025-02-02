class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        for i in range(len(heights)):
            l, r = i, i
            while l > 0 and heights[l-1] >= heights[i]:
                l -= 1
            while r < len(heights)-1 and heights[r+1] >= heights[i]:
                r+= 1
            res = max((r-l+1)*heights[i], res)
        return res