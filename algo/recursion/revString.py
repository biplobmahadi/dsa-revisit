def revStr(str):
    if str == '': return ''
    return revStr(str[1:]) + str[0]

print(revStr('Hi Can I call you?'))