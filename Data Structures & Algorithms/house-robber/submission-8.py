class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        a=[0]*(len(nums))
        a[0]=nums[0]
        a[1]=max(nums[0], nums[1])
        for i in range(2,len(nums)):
            a[i]=max(a[i-2]+nums[i], a[i-1])
        return a[len(nums)-1]
        