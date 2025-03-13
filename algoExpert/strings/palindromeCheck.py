def isPalindrome(string):
    i, j = 0, len(string)-1
    while j>i:
        if string[j] == string[i]:
            i+=1
            j-=1
        else: 
            return False
    return True
