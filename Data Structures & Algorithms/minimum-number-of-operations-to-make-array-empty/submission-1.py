class Solution:
    def minOperations(self, nums: List[int]) -> int:

        s={}
        for i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]]+=1
            else:
                s[nums[i]]=1
        
        steps=0

        for k,v in s.items():
            if v==1:
                return -1
            a=v/3
            a=math.floor(a)
            div=a*3
            # print(k,v,a)
            if v-div==0:
                steps+=a
            elif v-div==1:
                steps+=(v-4)//3+2
            else:
                steps+=a+1
            # print(steps)
        
        return steps
            
                





            


        