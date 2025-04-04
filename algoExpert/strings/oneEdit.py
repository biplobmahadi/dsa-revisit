def oneEdit(stringOne, stringTwo):
    l1, l2 = len(stringOne), len(stringTwo)
    if abs(l1-l2) > 1: return False
    i1, i2 = 0, 0
    madeEdit = False
    while i1<l1 and i2<l2:
        if stringOne[i1] != stringTwo[i2]:
            if madeEdit:
                return False
            madeEdit = True
            if l1>l2:
                i1+=1
            elif l2>l1:
                i2+=1
            else:
                i1+=1
                i2+=1
        else:
            i1+=1
            i2+=1
    return True