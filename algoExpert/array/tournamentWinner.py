def tournamentWinner(competitions, results):
    res = {}
    for i, (home, away) in enumerate(competitions):
        if results[i] == 0:
            res[away] = res.get(away, 0) + 1
        else:
            res[home] = res.get(home, 0) + 1
    print(res)
    winner = ''
    count = 0
    for key, val in res.items():
        if count < val:
            count = val
            winner = key
    return winner
