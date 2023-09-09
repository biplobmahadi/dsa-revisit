def dfs(root, list):
    if root.left:
        dfs(root.left, list)
    list.append(root.val)
    if root.right:
        dfs(root.right, list)

def isValidBST(root):
    if not root:
        return True
    list = []
    dfs(root, list)
    i, j = 0, 1
    while j < len(list):
        if list[i] >= list[j]:
            return False
        i+=1
        j+=1
    return True