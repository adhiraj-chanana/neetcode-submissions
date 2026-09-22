class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=0
        for i in range(len(nums)+1):
            l^=i
        
        for n in nums:
            l^=n
        
        return l

        