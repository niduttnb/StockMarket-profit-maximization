def greedy(prices):
        # greedy, if today's price greater than yesterday, add the difference
        pr = 0
        i = 1
        while(i<len(prices)):
        #for i in range(1, len(prices)):
          if prices[i]>prices[i-1]:
              pr += prices[i] - prices[i-1]
          i+=1

        return pr
  