# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    def solve(el, lv):
        if not isinstance(el, list):
            return el
        res = 0
        for n in el:
            res += solve(n, lv+1)
        return res*lv
    return solve(array, 1)
