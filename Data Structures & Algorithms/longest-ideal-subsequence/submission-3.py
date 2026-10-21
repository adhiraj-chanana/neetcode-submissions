class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        dp={chr(i):0 for i in range(97,123)}
        res=0
        for i in s:
            n=ord(i)
            for m in range(k+1):
                if chr(n+m) in dp:
                    dp[i]=max(dp[i], dp[chr(n+m)]+1)
                if m!=0 and chr(n-m) in dp:
                    dp[i]=max(dp[i], dp[chr(n-m)]+1)
            dp[i]=max(dp[i],1)
            res=max(res, dp[i])
        
        return res
            


        

