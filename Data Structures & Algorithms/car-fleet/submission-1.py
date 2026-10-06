class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        arr=[]
        for i in range(len(position)):
            arr.append([position[i], speed[i]])
        
        arr.sort(reverse=True)
        stack=[]

        for p,s in arr:
            time=(target-p)/s
            while stack and stack[-1]>=time:
                a=stack.pop()
                time=max(time,a)
            stack.append(time)
        
        return len(stack)

                

        