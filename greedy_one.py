
def greedy_one(prices):
  l = float('inf')
  result = 0
  i=0
  while i<len(prices):
    l = min(l, prices[i])
    result = max(result, prices[i] - l)
    i+=1
  return result