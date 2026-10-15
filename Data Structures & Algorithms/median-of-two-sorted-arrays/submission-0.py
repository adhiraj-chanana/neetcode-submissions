class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        small=[]
        large=[]

        i=0
        while nums1 or nums2:
            if nums1 and nums2:
                if nums1[0]<nums2[0]:
                    n=nums1.pop(0)
                else:
                    n=nums2.pop(0)
            elif nums1:
                
                n=nums1.pop(0)
            else:  
                n=nums2.pop(0)
            # print(n)
            if large and n<=large[0]:
                heapq.heappush(small,-1*n)
            else:
                heapq.heappush(large,n)
            
            if len(large)-len(small)==2:
                heapq.heappush(small,-1*heapq.heappop(large))
            if len(small)-len(large)==2:
                heapq.heappush(large, -1*heapq.heappop(small))
            # print(small, large)
        
        if len(large)>len(small):
            return heapq.heappop(large)
        elif len(small)> len(small):
            return -1*heapq.heappop(small)
        else:
            return (float(heapq.heappop(large)+(-1*heapq.heappop(small)))/2.0)
            
            

            


        