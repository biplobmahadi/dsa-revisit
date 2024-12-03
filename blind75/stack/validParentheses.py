class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {')': '(', '}': '{', ']': '['}
        for n in s:
            if n in brackets:
                if len(stack) == 0 or stack.pop() != brackets[n]:
                    return False
            else:
                stack.append(n)
        return len(stack) == 0