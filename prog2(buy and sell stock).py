def maxProfit(self, prices: List[int]) -> int:

        prof = 0
        curr = prices[-1]
        
        for i in range(len(prices)-1,0,-1):
            
            if prices[i-1]>=curr:
                curr = prices[i-1]
            else:
                prof = max(prof,curr-prices[i-1])    
                
        return (prof)       