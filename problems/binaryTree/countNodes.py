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

def countNodesOptimal(root):
    if not root:
        return 0
    height = findHeight(root)
    totalNodeWithoutLastLevel = pow(2, height-1) - 1
    totalInLastLevel = getTotalInLastLevel(root, height)
    return totalInLastLevel + totalNodeWithoutLastLevel

def findHeight(root):
    current = root
    count = 0
    while current:
        count+=1
        current = current.left
    return count

def getTotalInLastLevel(root, height):
    left, right = 0, pow(2, height-1) - 1
    while left <= right:
        mid = (left + right) // 2
        midNode = findAnyNode(mid, root, height)
        if midNode:
            left = mid+1
        else:
            right = mid -1
    return right + 1

def findAnyNode(position, root, height):
    left, right, current = 0, pow(2, height-1) - 1, root
    while left != right:
        mid = (left + right) // 2
        if position <= mid:
            current = current.left
            right = mid
        else:
            current = current.right
            left = mid + 1
    return current
