def generateDocument(characters, document):
    if not document:
        return True
    chMap, docMap = {}, {}
    for s in characters:
        chMap[s] = chMap.get(s, 0)+1
    for s in document:
        docMap[s] = docMap.get(s, 0) + 1
    for k, v in docMap.items():
        if v > chMap.get(k, 0):
            return False
    return True