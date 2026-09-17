class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        # print(dp)
        for i in range(1,amount+1):
            for coin in coins:
                # print(coin)
                if i-coin<0:
                    continue
                elif i-coin==0:
                    dp[i]=1
                else:
                    dp[i]=min(dp[i],dp[i-coin]+1)
            #print(dp)
        if dp[amount]==float('inf'):
            return -1
        else:
            return dp[amount]


                



                
        
        
        