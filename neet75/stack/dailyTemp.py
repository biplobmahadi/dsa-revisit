class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]*len(temperatures)
        stack = []
        for i, n in enumerate(temperatures):
            while stack and stack[-1][1] < n:
                ind, val = stack.pop()
                res[ind] = i - ind
            stack.append([i, n])
        return res