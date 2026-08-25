class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)-1
        if nums[0]<nums[n]:
            return nums[0]
        l=0
        r=n
        while l<=r:
            m=l+(r-l)//2
            if nums[m]<nums[r]:
                r=m
            else:
                l=m+1
        return nums[m]








        