class Solution:
    def isHappy(self, n: int) -> bool:
        visited=set()
        def dfs(i):
            visited.add(i)
            s=0
            while i>0:
                d=i%10
                s+=d**2
                i=i//10
           
            if s==1:
                return True
            elif s in visited:
                
                return False
            else:
                return dfs(s)
        
        return dfs(n)