def dp_one(prices):

    profit = [0 for x in range(len(prices))] # profit
    min_value = prices[0] # minimum values of the stocks on the left
    i = 1     
    
    while(i < len(prices) + 1):
        min_value = min(min_value, prices[i - 1])
        profit.append(max(profit[i - 1], prices[i - 1] - min_value))
        i += 1
        
    return profit[-1]
