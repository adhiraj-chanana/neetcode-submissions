class Solution:
    def countSeniors(self, details: List[str]) -> int:
        s=0
        for i in details:
            if int(i[11:13])>60:
                s+=1
        return s
                
        