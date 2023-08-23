def recurringChar(arr):
    visited = {}
    for el in arr:
        if visited.get(el) is not None: return visited[el]
        visited[el] = el
    return None

arr = [2, 4, 6, 2, 5, 4, 8]
arr2 = [2, 1, 1, 2, 5, 4, 8]
arr3 = [0, 1, 2, 0, 4]

print(recurringChar(arr3))

