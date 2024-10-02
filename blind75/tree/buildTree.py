class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    if not preorder or not inorder: return None
    root = TreeNode(preorder[0])
    p = inorder.index(preorder[0])
    root.left = buildTree(preorder[1: p+1], inorder[0:p])
    root.right = buildTree(preorder[p+1:len(preorder)], inorder[p+1: len(inorder)])
    return root
