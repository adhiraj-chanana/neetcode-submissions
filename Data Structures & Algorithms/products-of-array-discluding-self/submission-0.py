class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        for i in range(len(nums)):
            if i==0:
                continue
            else:
                prefix[i]=nums[i-1]*prefix[i-1]

        for j in range(len(nums)-1,-1,-1):
            if j==len(nums)-1:
                continue
            else:
                suffix[j]=(nums[j+1]*suffix[j+1])
        
        res=[1]*len(nums)
        for i in range(len(nums)):
            res[i]=prefix[i]*suffix[i]
        return res
            
            



        