def brute_force(prices):
        pro = dict()
            
        while prices[-1] == 0:
            prices.pop()
        
    
        def get_Max_Profit(s, sell):
            if s == len(prices):
                return 0
            
            if sell * s in pro:
                return pro[sell * s]
            
            max_Profit = 0
            for j in range(s, len(prices)):
                next = j + 1
                
                if sell == -1:
                    while next < len(prices) and prices[next] <= prices[j]: next += 1

                profit =  get_Max_Profit(next, -1 * sell) +  sell * prices[j]
                
                if profit > max_Profit:
                    max_Profit = profit
                    
            pro[sell * s] = max_Profit
            
            return max_Profit
        
        return get_Max_Profit(0, -1)