from collections import deque

def levelOrder(root):
    if not root:
        return []
    list = []
    queue = deque()
    queue.append({'node': root, 'level': 1})

    while queue:
        popped = queue.popleft()
        if len(list) < popped.get('level'):
            list.append([popped.get('node').get('val')])
        else:
            list[popped.get('level') - 1].append(popped.get('node').get('val'))
        if popped.get('node').get('left'):
            queue.append({'node': popped.get('node').get('left'), 'level': popped.get('level') + 1})
        if popped.get('node').get('right'):
            queue.append({'node': popped.get('node').get('right'), 'level': popped.get('level') + 1})

    return list
root = {'val': 4,
        'left': {'val': 5,
            'left': None,
            'right': None},
        'right': {'val': 15,
            'left': None,
            'right': None}
        }

def levelOrderGoodCode(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        eachLevel, lenOfQueue = [], len(queue)
        for i in range(0, lenOfQueue):
            popped = queue.popleft()
            eachLevel.append(popped.val)
            if popped.left:
                queue.append(popped.left)
            if popped.right:
                queue.append(popped.right)
        result.append(eachLevel)
    return result

print(levelOrder(root))
print(levelOrderGoodCode(root))