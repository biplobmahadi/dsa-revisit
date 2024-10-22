# O(n) time | O(1) space
def isValidSubsequence(array, sequence):
    i = 0
    for n in array:
        if i == len(sequence): 
            return True
        if n == sequence[i]:
            i+=1
    return i == len(sequence)
