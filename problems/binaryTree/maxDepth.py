def dfs(root, count, map):
    if root.left:
        dfs(root.left, count+1, map)
    if root.right:
        dfs(root.right, count+1, map)
    if count > map.get('maxCount'):
        map['maxCount'] = count

def maxDepth(root):
    if root == None:
        return 0
    count = 1
    map = {'maxCount': 1}
    dfs(root, count, map)
    return map.get('maxCount')

def dfsOptimal(root, count):
    if root == None: return count
    return max(dfsOptimal(root.left, count+1), dfsOptimal(root.right, count+1))

def maxDepthOptimal(root):
    return dfsOptimal(root, 0)