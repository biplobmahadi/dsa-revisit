# given sorted arr, val could be negative
# return 2 indeces of 2 element which sum is equal to target
# there is exactly one soln

arr = [-1, 2, 3, 4, 7, 9]

def targetSum(arr, target):
    l, r = 0, len(arr) - 1
    while r>l:
        total = arr[r] + arr[l]
        if total>target:
            r-=1
        elif total<target:
            l+=1
        else:
            return [l, r]

print(targetSum(arr, 7))