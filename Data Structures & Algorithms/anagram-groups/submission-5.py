class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        visited={}
        for s in strs:
            a={chr(i):0 for i in range(97,123)}
            for i in s:
                a[i]+=1
            
            res=''
            for i in range(97,123):
                res+=(chr(i)*a[chr(i)])
            
            if res in visited:
                visited[res].append(s)
            else:
                visited[res]=[s]
        result=[]
        for i in visited:
            result.append(visited[i])
        return result
            






        