def dp_one(prices):
  ans = max_val = 0
  i=1
  while(i<len(prices)):
      max_val = max(max_val + prices[i] - prices[i-1],0)
      ans = max(max_val, ans)
      i+=1
  return ans 