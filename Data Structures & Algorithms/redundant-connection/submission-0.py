class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjMap={i:[] for i in range(1,len(edges)+1)}
        incoming={i:0 for i in range(1,len(edges)+1)}
        c=0
        for u,v in edges:
            if c==0:
                stack=[(u,-1)]
                c=1
            adjMap[u].append(v)
            adjMap[v].append(u)
            incoming[v]+=1
            incoming[u]+=1
        visited=set()
        q=deque()
        for i in range(1, len(edges)+1):
            if incoming[i]==1:
                q.append(i)
       

        while q:
            node=q.popleft()
            for neigh in adjMap[node]:
                incoming[neigh]-=1
                if incoming[neigh]==1:
                    q.append(neigh)
        
        for u,v in reversed(edges):
            if incoming[u]==2 and incoming[v]==2:
                return [u,v]
        
        return []
                
            
        


        