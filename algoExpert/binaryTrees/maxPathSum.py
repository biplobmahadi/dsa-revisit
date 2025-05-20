def maxPathSum(tree):
    res = [float('-inf')]
    def solve(tree):
        if not tree: return 0
        l = solve(tree.left)
        r = solve(tree.right)
        curr = tree.value
        if l > 0: curr+=l
        if r > 0: curr+=r
        if curr > res[0]:
            res[0] = curr
        return l+tree.value if l>r else r+tree.value
    solve(tree)
    return res[0]
