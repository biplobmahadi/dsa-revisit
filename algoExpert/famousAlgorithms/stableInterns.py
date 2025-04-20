def stableInternships(interns, teams):
    rank = []
    for n in teams:
        obj = {}
        for r, intern in enumerate(n):
            obj[intern] = r
        rank.append(obj)
    internChoose = [0]*len(interns)
    internAvail = [i for i in range(len(interns))]
    res = {}
    while internAvail:
        p = internAvail.pop()
        c = internChoose[p]
        t = interns[p][c]
        if t not in res:
            res[t] = p
            continue
        alreadyIntern = res[t]
        if rank[t][p] > rank[t][alreadyIntern]:
            internAvail.append(p)
            internChoose[p]+=1
        else:
            internAvail.append(alreadyIntern)
            internChoose[alreadyIntern]+=1
            res[t] = p
    final = [[v, k] for k, v in res.items()]
    return final
        
