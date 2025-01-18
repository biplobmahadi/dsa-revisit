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


HOME_TEAM_WIN = 1

def tournamentWinner2(competitions, results):
    currentBestTeam = ''
    scores = {}

    for i, (homeTeam, awayTeam) in enumerate(competitions):
        result = results[i]
        winningTeam = homeTeam if HOME_TEAM_WIN == result else awayTeam
        scores[winningTeam] = scores.get(winningTeam, 0) + 3
        if scores[winningTeam] > scores.get(currentBestTeam, 0):
            currentBestTeam = winningTeam
            
    return currentBestTeam


def tournamentWinner2(competitions, results):
    res = {}
    for i in range(len(results)):
        home = competitions[i][0]
        away = competitions[i][1]
        if results[i]:
            res[home] = res.get(home, 0) + 3
        else:
            res[away] = res.get(away, 0) + 3
    final, total = '', 0
    for k, v in res.items():
        if total < v:
            final = k
            total = v
    return final
