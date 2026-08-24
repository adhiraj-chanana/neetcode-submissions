class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0]<temperatures[i]:
                temp,ind=stack.pop()
                res[ind]=i-ind
            stack.append([temperatures[i],i])
        return res



        
        