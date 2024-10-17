class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node: return None
    map = {}
    def dfs(node):
        if node.val in map:
            return map[node.val]
        newNode = Node(node.val)
        map[node.val] = newNode
        for nei in node.neighbors:
            neiNode = dfs(nei)
            newNode.neighbors.append(neiNode)
        return newNode
    res = dfs(node)
    return res

