class Solution:
    def numberOfMatches(self, n: int) -> int:
        c=0
        while n>1:
            if n%2==0:
                n=n//2
                c+=n
            else:
                n=n//2
               
                c+=n
                n=n+1
                


        return c
