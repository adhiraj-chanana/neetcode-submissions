class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        l=0
        freq={}
        heap=[]
        nums.sort()
        while l<len(nums):
            curNumber=nums[l]
            freq[curNumber]=0
            while l<len(nums) and nums[l]==curNumber:
                freq[curNumber]+=1
                l+=1
            heapq.heappush(heap, [-freq[curNumber], curNumber])
        result=[]
        for i in range(k):
            c,num=heapq.heappop(heap)
            result.append(num)
        
        return result
            


                


        