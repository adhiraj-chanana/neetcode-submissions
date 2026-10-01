class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjMap={i:[] for i in range(numCourses)}
        incoming={i:0 for i in range(numCourses)}
        for u,v in prerequisites:
            adjMap[v].append(u)
            incoming[u]+=1
        q=deque()
        for i in range(numCourses):
            if incoming[i]==0:
                q.append(i)
        
        visited=set()
        while q:
            node=q.popleft()
            if node in visited:
                return False
            visited.add(node)
            for neigh in adjMap[node]:
                if neigh not in visited:
                    incoming[neigh]-=1
                    if incoming[neigh]==0:
                        q.append(neigh)
        
        if len(visited)==numCourses:
            return True
        else:
            return False


        
        