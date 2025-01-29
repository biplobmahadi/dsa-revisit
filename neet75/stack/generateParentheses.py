class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def generate(openN, closeN):
            if openN == closeN == n:
                res.append(''.join(stack))
                return
            if openN < n: 
                stack.append('(')
                generate(openN+1, closeN)
                stack.pop()
            if openN>closeN:
                stack.append(')')
                generate(openN, closeN+1)
                stack.pop()
        generate(0, 0)
        return res