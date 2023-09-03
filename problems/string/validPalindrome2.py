def isValidPalindrome(s, i, j):
    while j>i:
        if s[i] != s[j]:
            return False
        i+=1
        j-=1
    return True

def almostPalindrome(s):
    i, j = 0, len(s) - 1
    while j>i:
        if s[i] != s[j]:
            return isValidPalindrome(s, i+1, j) or isValidPalindrome(s, i, j-1)
        i+=1
        j-=1
    return True

s = "ebcbbececabbacecbbcbe"
print(almostPalindrome(s))