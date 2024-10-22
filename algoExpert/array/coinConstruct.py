def nonConstructibleChange(coins):
    coins.sort()

    amount = 0
    for coin in coins:
        if amount + 1 < coin:
            return amount + 1
        amount += coin
    return amount+1