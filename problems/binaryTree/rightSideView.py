from collections import deque

def rightSideView(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        lenghtOfQueue = len(queue)
        for i in range(0, lenghtOfQueue):
            popped = queue.popleft()
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
            if (i == lenghtOfQueue-1):
                result.append(popped.val)
    return result

def dfs(root, list, level):
    if not root:
        return list
    if len(list) == level:
        list.append(root.val)
    if root.right:
        dfs(root.right, list, level+1)
    if root.left:
        dfs(root.left, list, level+1)
    return list

def righSideViewDfs(root):
    return dfs(root, [], 0)

