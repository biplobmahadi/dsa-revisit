class Solution:
    @staticmethod
    def validTree(n, edges):
        adj = [[] for _ in range(n)]
        for s, d in edges:
            adj[s].append(d)
            adj[d].append(s)
        
        visited = {}
        def dfs(node, adj, visited, prev):
            if node in visited:
                return visited[node]
            visited[node] = True
            
            for nei in adj[node]:
                if nei != prev:
                    if(dfs(nei, adj, visited, node)): return True
            
        if dfs(0, adj, visited, -1): return False
        return len(visited) == n
    
print(Solution.validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]))
print(Solution.validTree(2, [[0, 1]]))
