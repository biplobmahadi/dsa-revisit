def numOfTimes(n, headID, manager: list, informTime: list):
    if n <= 1:
        return 0
    adjacencyList = {}
    for i in range(n):
        if manager[i] != -1:
            key = adjacencyList.get(manager[i])
            if key:
                adjacencyList[manager[i]].append(i)
            else:
                adjacencyList[manager[i]] = [i]
    
    return dfs(adjacencyList, informTime, headID)

def dfs(adjacencyList, informTime, headID):
    if not adjacencyList.get(headID):
        return 0
    compTime = 0
    for i in adjacencyList.get(headID):
        total = dfs(adjacencyList, informTime, i)
        compTime = max(total, compTime)
    return compTime + informTime[headID]

manager = [2, 2, -1, 2, 2, 2, 3, 4]
informTime = [0, 0, 1, 6, 4, 0, 0, 0]
print(numOfTimes(8, 2, manager, informTime))