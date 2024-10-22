class Solution:
    def countComponents(self, n, edges):
        adjList = [[] for _ in range(n)]
        for s, d in edges:
            adjList[s].append(d)
            adjList[d].append(s)

        visit = {}
        def dfs(node, visit, adjList):
            if node in visit:
                return 0
            visit[node] = True
            for nei in adjList[node]:
                dfs(nei, visit, adjList)
            return 1
        
        count = 0
        for node in range(n):
            count += dfs(node, visit, adjList)
        return count