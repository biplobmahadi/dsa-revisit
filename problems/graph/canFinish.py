from collections import deque

def canFinish(numCourses, prerequisites: list[list]):
    adjacencyList = {}
    for i in prerequisites:
        if adjacencyList.get(i[1]):
            adjacencyList[i[1]].append(i[0])
        else:
            adjacencyList[i[1]] = [i[0]]
    
    for key in adjacencyList:
        queue = deque([key])
        seen = {}
        while queue:
            popped = queue.popleft()
            if not seen.get(popped):
                seen[popped] = True
                for i in adjacencyList[popped]:
                    if i == key:
                        return False
                    if adjacencyList.get(i) and not seen.get(i):
                        queue.append(i)
    return True

prerequisites = [[0,1], [0, 2], [2, 1], [1,0]]
print(canFinish(3, prerequisites))

def canFinishOptimalWithAdjList(numCourses, prerequisites: list[list]):
    indegree = [0]*numCourses
    adjList = list(map(lambda _: [], indegree))
    for pair in prerequisites:
        indegree[pair[0]]+=1
        adjList[pair[1]].append(pair[0])
    count, stack = 0, []
    for i, x in enumerate(indegree):
        if x == 0: stack.append(i)
    while stack:
        popped = stack.pop()
        count+=1
        for i in adjList[popped]:
            indegree[i]-=1
            if indegree[i] == 0:
                stack.append(i)
    return count == numCourses

print(canFinishOptimalWithAdjList(3, prerequisites))

# def canFinishOptimal(numCourses, prerequisites: list[list]):
#     indegree = [0]*numCourses
#     adjList = list(map(lambda _: [], indegree))
#     for pair in prerequisites:
#         indegree[pair[0]]+=1
#         adjList[pair[1]].append(pair[0])
#     count, stack = 0, []
#     for i, x in enumerate(indegree):
#         if x == 0: stack.append(i)
#     while stack:
#         popped = stack.pop()
#         count+=1
#         for i in adjList[popped]:
#             indegree[i]-=1
#             if indegree[i] == 0:
#                 stack.append(i)
#     return count == numCourses

# print(canFinishOptimal(3, prerequisites))
