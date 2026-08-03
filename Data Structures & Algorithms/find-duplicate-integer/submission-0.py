class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        a=set()
        for i in nums:
            if i in a:
                return i
            else:
                a.add(i)
        


        