def canFinish(numCourses, prerequisites):
    indegree = [0] * numCourses
    adjList = [[] for _ in range((numCourses))]
    for d, s in prerequisites:
        indegree[d] += 1
        adjList[s].append(d)
    stack = []
    for i, n in enumerate(indegree):
        if not n:
            stack.append(i)
    count = 0
    while stack:
        p = stack.pop()
        count+=1
        for nei in adjList[p]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                stack.append(nei)
    return count == numCourses

print(canFinish(2, [[1,0]]))