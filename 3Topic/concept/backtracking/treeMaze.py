tree = {'val': 4,
        'left': {'val': 0,
            'left': None,
            'right': {'val': 7,
                'left': None,
                'right': None}},
        'right': {'val': 1,
            'left': {'val': 0,
                'left': None,
                'right': None},
            'right':{'val': 0,
                'left': None,
                'right':None } }
        }

path = []

def canReach(root):
    if not root or root['val'] == 0: return False
    path.append(root['val'])
    if not root['left'] and not root['right']: return True
    if (canReach(root['left'])): return True
    if (canReach(root['right'])): return True
    path.pop()
    return False

print(canReach(tree), path)