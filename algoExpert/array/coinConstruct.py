def nonConstructibleChange(coins):
    coins.sort()

    amount = 0
    for coin in coins:
        if amount + 1 < coin:
            return amount + 1
        amount += coin
    return amount+1

def nonConstructibleChange2(coins):
    if not coins: return 1
    coins.sort()
    curr = 0
    for n in coins:
        if curr+1 < n:
            return curr+1
        curr += n
    return curr+1