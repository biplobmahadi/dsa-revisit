def dfsInorder(root):
    if not root:
        return
    dfsInorder(root.left)
    print(root.value)
    dfsInorder(root.right)

def dfsPreorder(root):
    if not root:
        return
    print(root.value)
    dfsPreorder(root.left)
    dfsPreorder(root.right)

def dfsPostorder(root):
    if not root:
        return
    dfsPostorder(root.left)
    dfsPostorder(root.right)
    print(root.value)
