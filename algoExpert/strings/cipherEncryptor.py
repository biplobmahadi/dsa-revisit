def caesarCipherEncryptor(string, key):
    res = ''
    newKey = key%26
    for s in string:
        p = ord(s)+newKey
        if p <= 122:
            res += chr(p)
        else:
            np = p - 122 + 96
            res+=chr(np)
    return res
        
