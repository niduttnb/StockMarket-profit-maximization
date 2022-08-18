def greedy_one(prices):

  l = float('inf')
  profit = 0
  i = 0
  
  while i < len(prices):
    l = min(l, prices[i])
    profit = max(profit, prices[i] - l)
    i += 1
    
  return profit
