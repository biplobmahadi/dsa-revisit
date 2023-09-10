from collections import deque

def bfsIn2DArr(arr, initRow, initCol):
    if not (arr and arr[0]):
        return []
    list, queue = [], deque([{'row': initRow, 'col': initCol}])
    visited = [[False]*len(arr[0]) for _ in range(len(arr))]
    bfs(arr, visited, queue, list)
    return list

def bfs(arr, visited, queue: deque, list: list):
    if not queue:
        return
    popped = queue.popleft()
    row = popped.get('row')
    col = popped.get('col')
    if not visited[row][col]:
        list.append(arr[row][col])
        visited[row][col] = True

    pushToQueue(arr, queue, visited, row-1, col)
    pushToQueue(arr, queue, visited, row, col+1)
    pushToQueue(arr, queue, visited, row+1, col)
    pushToQueue(arr, queue, visited, row, col-1)

    bfs(arr, visited, queue, list)

def pushToQueue(arr, queue, visited, row, col):
    if (row>=0 and col>=0 and row<len(arr) and col<len(arr[0])):
        if not visited[row][col]:
            queue.append({'row': row, 'col': col})

arr = [
  [1, 2, 3, 4, 5],
  [6, 7, 8, 9, 10],
  [11, 12, 13, 14, 15],
  [16, 17, 18, 19, 20],
]
print(bfsIn2DArr(arr, 2, 2))