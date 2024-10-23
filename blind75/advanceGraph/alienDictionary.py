class Solution:
    def foreignDictionary(self, words) -> str:
        adj = {}
        for word in words:
            for c in word:
                adj[c] = []
        for i in range(1, len(words)):
            one = words[i-1]
            two = words[i]
            minL = min(len(one), len(two))
            if one[:minL] == two[:minL] and len(one) > len(two):
                return ''
            for j in range(minL):
                if one[j] != two[j]:
                    adj[one[j]].append(two[j])
                    break
        visit = {}
        res = []
        
        def dfs(node):
            if node in visit:
                return visit[node]
            visit[node] = True
            for nei in adj[node]:
                if dfs(nei):
                    return True
            res.append(node)
            visit[node] = False
            return False
        
        for key in adj:
            if dfs(key):
                return ''
        res.reverse()
        return ''.join(res)