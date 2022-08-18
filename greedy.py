def greedy(prices):

    # greedy, if today's price greater than yesterday, add the difference
    profit = 0
    i = 1
    
    while(i < len(prices)):
      if prices[i] > prices[i-1]:
          profit += prices[i] - prices[i-1]
      i += 1

    return profit
