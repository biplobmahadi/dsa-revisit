def maxArea(height: list):
    n = len(height)
    max = 0
    for i in range(0, n):
        for j in range(i+1, n):
            width = j - i
            minVertex = height[i]
            if height[j] < height[i]:
                minVertex = height[j]
            area = width * minVertex
            if area > max:
                max = area
    return max

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

# def maxAreaOptimal(height):
#     i, j, max = 0, len(height) - 1, 0

#     while i < j:
#         width = j - i
#         area = 0
#         if height[i] < height[j]:
#             area = height[i] * width
#             i += 1
#         else:
#             area = height[j] * width
#             j -= 1
#         if area > max:
#             max = area
#     return max

# print(maxAreaOptimal(height))
