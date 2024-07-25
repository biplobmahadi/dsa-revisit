from collections import deque

def bfs(root):
    if not root: return
    queue = deque()
    queue.append(root)

    while queue:
        popped = queue.popleft()
        print(popped['value'])
        if popped['left']:
            queue.append(popped['left'])
        if popped['right']:
            queue.append(popped['right'])

root = {'value': 4, 
        'left': {'value': 3, 
            'left': 
                {'value': 7, 
                'left': None,
                'right': None},
            'right': 
                {'value': 23, 
                'left': None,
                'right': None}
            },
        'right': 
            {'value': 6, 
            'left': {'value': 41, 
                'left': None,
                'right': None},
            'right': {'value': 14, 
                'left': None,
                'right': None}}
        }

bfs(root)