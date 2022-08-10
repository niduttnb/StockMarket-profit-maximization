def brute_one(prices):
  max_value = 0
  i=len(prices)-1

  while(i>0):     
      mv=min(prices[i::-1])
      if max_value<(prices[i]-mv):
          max_value=prices[i]-mv
      i-=1
  return max_value
