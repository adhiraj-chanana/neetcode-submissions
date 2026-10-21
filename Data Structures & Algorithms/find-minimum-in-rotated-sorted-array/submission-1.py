class Solution:
    def findMin(self, nums: List[int]) -> int:

        l=0
        r=len(nums)-1

        while l<r:
            m=l+(r-l)//2
         
            if nums[r]<nums[m]:
                l=m+1
            else:
                r=m
        return nums[l]



        