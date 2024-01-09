def lcm(s1, s2):
    return rec(s1, s2, 0, 0)

def rec(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    if s1[i] == s2[j]: 
        return 1 + rec(s1, s2, i+1, j+1)
    else:
        return max(rec(s1, s2, i, j+1),
                   rec(s1, s2, i+1, j))
    
print(lcm('ADCB', 'ABC'))

def lcmTopDown(s1, s2):
    cache = [[-1] * len(s2) for _ in range(len(s1))]
    return recTopDown(s1, s2, 0, 0, cache)

def recTopDown(s1, s2, i, j, cache):
    if i == len(s1) or j == len(s2):
        return 0
    
    if cache[i][j] != -1:
        return cache[i][j]
    
    if s1[i] == s2[j]: 
        cache[i][j] = 1 + recTopDown(s1, s2, i+1, j+1, cache)
    else:
        cache[i][j] = max(recTopDown(s1, s2, i, j+1, cache),
                   recTopDown(s1, s2, i+1, j, cache))
    return cache[i][j]
    
print(lcmTopDown('ADCB', 'ABC'))

def bottomUp(s1, s2):
    M, N = len(s1), len(s2)
    dp = [[0]*(N+1) for _ in range(M+1)]
    for i in range(M):
        for j in range(N):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = 1 + dp[i][j]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
    return dp[M][N]

print(bottomUp('ADCB', 'ABC'))

def bottomUpMemo(s1, s2):
    M, N = len(s1), len(s2)
    dp = [0]*(N+1) 
    for i in range(M):
        curr = [0]*(N+1) 
        for j in range(N):
            if s1[i] == s2[j]:
                curr[j+1] = 1 + dp[j]
            else:
                curr[j+1] = max(curr[j], dp[j+1])
        dp = curr
    return dp[N]

print(bottomUpMemo('ADCB', 'ABC'))
