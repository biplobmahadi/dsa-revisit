arr = [2, 4, 6]
res = []

def distinctInput(i, list):
    if i == len(arr):
        res.append(list.copy())
        return
    list.append(arr[i])
    distinctInput(i+1, list)
    list.pop()
    distinctInput(i+1, list)

distinctInput(0, [])
print(res)

# arr2 = [2, 1, 2, 3]
# res2 = []
# arr2.sort()
# def notDistinctInput(i, list):
#     if i == len(arr2):
#         res2.append(list.copy())
#         return
#     list.append(arr2[i])
#     notDistinctInput(i+1, list)
#     list.pop()
#     while i+1 < len(arr2) and arr2[i] == arr2[i+1]:
#         i+=1
#     notDistinctInput(i+1, list)

# notDistinctInput(0, [])
# print(res2)