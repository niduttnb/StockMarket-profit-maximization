def brute_force(prices):
    return calculate(prices, 0)
        
def calculate(prices, n):
    if n >= len(prices):
        return 0

    max_profit = 0
    for i in range(n, len(prices)):
        max_value = 0
        for j in range(i+1, len(prices)):
            if prices[i] < prices[j]:
                profit = calculate(prices, j + 1) + prices[j] /
                         - prices[i]
                if profit > max_value:
                    max_value = profit
        if max_value > max_profit:
            max_profit = max_value

    return max_profit
