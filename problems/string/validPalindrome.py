def isPalindrome(s:str):
    i, j = 0, len(s) - 1

    while(j>=i):
        if s[i].isalnum() and s[j].isalnum():
            if s[i].upper() != s[j].upper():
                return False
            i+=1
            j-=1
        else:
            if not s[i].isalnum():
                i+=1
            if not s[j].isalnum():
                j-=1
    return True
    
s = "race a car"
print(isPalindrome(s))
