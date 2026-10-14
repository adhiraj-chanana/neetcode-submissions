class Solution:
    def jump(self, nums: List[int]) -> int:
        
        dp=[float('inf')]*len(nums)
        dp[0]=0

        for i in range(len(nums)):
            for j in range(i,min(len(nums), i+nums[i]+1)):

                dp[j]=min(dp[j], dp[i]+1)

        return dp[-1]