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

def arrayOfProducts(array):
    res = [1]*len(array)
    pre, post = 1, 1
    for i, n in enumerate(array):
        res[i] = pre
        pre *= n
    for i in reversed(range(len(array))):
        res[i] *= post
        post *= array[i]
    return res
