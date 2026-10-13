class Solution:
    def longestPalindrome(self, s: str) -> str:
        m=len(s)//2
        result=0
        track=''
        def expand(l,r):
            track=''       
            while l>=0 and r<len(s) and s[l]==s[r]:
                track=s[l:r+1]
                l-=1
                r+=1
            return track
        
        for i in range(len(s)):
            track1=expand(i,i)
            if len(track1)>result:
                result=len(track1)
                track=track1
            track2=expand(i,i+1)
            if len(track2)>result:
                result=len(track2)
                track=track2
        return track


                


        