def dp(prices):
    profit = [0 for i in range(len(prices))]
    i = 1
    while (i < len(prices)):
        profit[i] = profit[i-1] + max(0, prices[i] - prices[i-1])
        i += 1
    return profit[len(prices)-1]
