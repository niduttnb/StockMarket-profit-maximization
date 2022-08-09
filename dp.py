def dp(prices):
  curr = prices[0]
  profit = 0

  j = 1
  while j<len(prices):
  #for i in range(1, len(prices)):
    if prices[j]<curr:
      curr = prices[j]
      continue
    profit += prices[j]-curr
    curr = prices[j]
    j+=1
  return profit
