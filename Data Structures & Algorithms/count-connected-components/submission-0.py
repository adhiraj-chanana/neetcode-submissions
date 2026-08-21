class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        g={i:[] for i in range(n)}
        visited={i:False for i in range(n)}
        for a,b in edges:
            g[a].append(b)
            g[b].append(a)
        def dfs(node):
            if visited[node]==True:
                return
            visited[node]=True
            for neigh in g[node]:
                dfs(neigh)
        res=0
        for i in range(n):
            if visited[i]==False:
                dfs(i)
                res+=1
        
        return res
    
                