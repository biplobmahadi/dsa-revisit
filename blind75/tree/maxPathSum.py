def maxPathSum(root):
    res = [root.val]
    def pathSum(root):
        if not root: return 0
        leftSum = pathSum(root.left)
        rightSum = pathSum(root.right)
        res[0] = max(res[0], root.val + leftSum + rightSum)
        return root.val + max(leftSum, rightSum)
    pathSum(root)
    return res[0]
