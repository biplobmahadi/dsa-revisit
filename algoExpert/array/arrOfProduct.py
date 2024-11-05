# O(2*n) time | O(n) space
def arrayOfProducts(array):
    prefix, postfix = 1, 1
    res = [0] * len(array)
    for i, num in enumerate(array):
        res[i] = prefix
        prefix *= num
    for i in reversed(range(len(array))):
        res[i] *= postfix
        postfix *= array[i]
    return res
