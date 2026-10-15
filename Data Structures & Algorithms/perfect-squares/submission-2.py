class Solution:
    def numSquares(self, n: int) -> int:
        if (n**(0.5)).is_integer():
            return 1
        a=[1]
        c=1
        while a[-1]<n:
            a.append(a[-1]+c+2)
            c=c+2
        a.pop()
        # print(a)
        a.sort(reverse=True)
        dp=[float('inf')]*(n+1)
        dp[0]=0
        for i in range(1,n+1):
            for s in a:
                # print(i-s)
                if (i-s)>=0:
                    dp[i]=min(dp[i], 1+dp[i-s])
            
            # print(dp)
        
        return dp[-1]


        






        