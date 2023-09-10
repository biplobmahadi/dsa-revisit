def dfs2DArr(arr):
    if not (arr and arr[0]):
        return []
    list, visited = [], [[False]*len(arr[0]) for _ in range(len(arr))]
    dfs(arr, list, visited, 0, 0)
    return list

def dfs(arr, list, visited, row, col):
    if (row<0 or col<0 or row>=len(arr) or col>=len(arr[0]) or visited[row][col]):
        return
    
    list.append(arr[row][col])
    visited[row][col] = True

    dfs(arr, list, visited, row-1, col)
    dfs(arr, list, visited, row, col+1)
    dfs(arr, list, visited, row+1, col)
    dfs(arr, list, visited, row, col-1)

arr = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
]

print(dfs2DArr(arr))
