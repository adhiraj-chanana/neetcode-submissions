class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        coins.sort(reverse=True)
        a=set(coins)
        dp[0]=0
        for i in range(amount+1):
            if i in a:
                dp[i]=1
                continue
            for c in coins:
                if c>i:
                    continue
                dp[i]=min(1+dp[i-c],dp[i])
            
        if dp[-1]==float('inf'):
            return -1
        else:
            return dp[-1]

            



                



                
        
        
        