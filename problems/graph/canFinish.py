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

prerequisite = [[0,1], [0, 2], [2, 1], [1, 0]]
print(canFinish(3, prerequisite))