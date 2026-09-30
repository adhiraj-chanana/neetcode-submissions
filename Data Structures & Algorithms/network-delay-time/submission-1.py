class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adjMap={i:[] for i in range(1,n+1)} 
        for u,v,t in times:
            adjMap[u].append([v,t])
        
        distances=[float('inf')]*n
        distances[k-1]=0
        q=deque([(0,k)])

        while q:
            dist, node=q.popleft()
            
            for neigh,new_dist in adjMap[node]:
                if dist+new_dist<distances[neigh-1]:
                    distances[neigh-1]=new_dist+dist
                    q.append((distances[neigh-1], neigh))
            
        result=max(distances)
        if result==float('inf'):
            return -1
        else:
            return result





        