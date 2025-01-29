class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        exp = {'+', '-', '*', '/'}
        stack = []
        for n in tokens:
            if n in exp:
                p2 = stack.pop()
                p1 = stack.pop()
                if n == '/':
                    stack.append(math.trunc(p1/p2))
                elif n == '+':
                    stack.append(p1 + p2)
                elif n == '-':
                    stack.append(p1 - p2)
                else:
                    stack.append(p1 * p2)
            else:
                stack.append(int(n))
        return stack[-1]
