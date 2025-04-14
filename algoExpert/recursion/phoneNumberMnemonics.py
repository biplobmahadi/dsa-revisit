obj = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

def phoneNumberMnemonics(phoneNumber):
    res = []
    def solve(i, s):
        if i == len(phoneNumber):
            newS = s.copy()
            res.append(''.join(newS))
            return
        if phoneNumber[i] == '1' or phoneNumber[i] == '0':
            s.append(str(phoneNumber[i]))
            solve(i+1, s)
            s.pop()
        else:
            val = str(phoneNumber[i])
            for n in obj[val]:
                s.append(n)
                solve(i+1, s)
                s.pop()
    solve(0, [])
    return res
