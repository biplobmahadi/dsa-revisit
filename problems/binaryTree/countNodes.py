from collections import deque

def countNodes(root):
    if not root:
        return 0
    queue, count = deque([root]), 0
    while queue:
        popped = queue.popleft()
        count += 1
        if popped.left:
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
    return count