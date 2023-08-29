from heapq import heapify, heappop, heappush

def kthLargest(k, arr):
    heap = []

    for i in range(0, k):
        heappush(heap, arr[i])
    
    for i in range(k, len(arr)):
        top = heap[0]
        if top < arr[i]:
            heappop(heap)
            heappush(heap, arr[i])

    return heap[0]

arr = [2, 32, 23, 35, 65, 76, 45]
print(kthLargest(1, arr=arr))
print(kthLargest(2, arr=arr))
print(kthLargest(3, arr=arr))
print(kthLargest(4, arr=arr))
print(kthLargest(5, arr=arr))
