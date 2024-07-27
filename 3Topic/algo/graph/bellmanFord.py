from math import inf

def bellmanFord(adj: dict, src):
    res = {}
    for key in adj.keys():
        res[key] = inf
    res[src] = 0
    for _ in range(len(adj)-1):
        count = 0
        for k, v in adj.items():
            for des, w in v:
                weight = res[k] + w
                if weight < res[des]:
                    res[des] = weight
                    count += 1
        if count == 0: break

    return res

adj = {
    "A": [('B', -5), ('C', 3)],
    "B": [('D', 10)],
    "C": [('B', 2), ('E', -4), ('D', -1)],
    "D": [('E', 2)],
    "E": [],
}

print(bellmanFord(adj, 'A'))
