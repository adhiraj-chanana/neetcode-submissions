class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        b=set(nums)
        res=0
        for i in nums:
            if i-1 in b:
                continue
            k=i
            c=0
            while k in b:
                k+=1
                c+=1
            res=max(res,c)
        return res


                


        