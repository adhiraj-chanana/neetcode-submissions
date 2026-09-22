class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        count=len(digits)-1
        while count>=0  and digits[count]==9:
            digits[count]=0
            count-=1
        
        if count ==-1:
            digits.insert(0,1)
            return digits
        else:
            digits[count]+=1
            return digits
        

        