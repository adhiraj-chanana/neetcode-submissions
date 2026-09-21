class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited=set()
        adjMap={i:[] for i in range(n)}
        for u,v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for i in adjMap[node]:
                dfs(i)
        c=0
        for i in range(n):
            if i not in visited:
                dfs(i)
                c+=1
        
        return c
            
        
        

        