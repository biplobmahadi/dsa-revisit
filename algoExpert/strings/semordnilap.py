def semordnilap(words):
    wordSet = set(words)
    res = []
    for w in words:
        semord = w[::-1]
        if semord in wordSet and semord != w:
            res.append([w, semord])
            wordSet.remove(w)
    return res