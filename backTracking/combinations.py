n1, k1 = 4, 2
res1 = []
def solve1(i, list):
    if len(list) == k1:
        res1.append(list.copy())
        return
    if i > n1:
        return
    list.append(i)
    solve1(i+1, list)
    list.pop()
    solve1(i+1, list)

solve1(1, [])
print(res1)