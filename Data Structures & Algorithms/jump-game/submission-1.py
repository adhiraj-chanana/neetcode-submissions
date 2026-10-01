class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp=[False]*len(nums)
        dp[0]=True

        for i in range(len(nums)):
            if not dp[i]==True:
                continue
            if nums[i]==0:
                continue
            if (i+nums[i])>=(len(nums)-1):
                return True
            else:
                for j in range(i,i+nums[i]+1):
                    dp[j]=True
        
        return dp[len(nums)-1]
            
                
