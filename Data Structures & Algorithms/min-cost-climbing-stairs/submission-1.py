class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        a=[0]*(len(cost)+1)
        
        for i in range(2, len(cost)+1):
            a[i]=min(a[i-1]+cost[i-1],a[i-2]+cost[i-2])
        
        return a[len(cost)]

        


        