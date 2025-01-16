# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    i = 0
    for n in array:
        if i == len(sequence): 
            return True
        if n == sequence[i]:
            i+=1
    return i == len(sequence)

# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    i, j = 0, 0
    while i < len(array) and j < len(sequence):
        if array[i] == sequence[j]:
            j+=1
        i+=1
    return j == len(sequence)