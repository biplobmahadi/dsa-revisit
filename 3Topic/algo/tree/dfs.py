def dfsInorder(root):
    if not root:
        return
    dfsInorder(root.left)
    print(root.value)
    dfsInorder(root.right)
    