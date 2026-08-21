class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses={i:[] for i in range(numCourses)}
        e={i:0 for i in range(numCourses)}
        for i,j in prerequisites:
            courses[j].append(i)
            e[i]+=1
        q=deque()
        for i in e:
            if e[i]==0:
                q.append(i)
        visited=set()
        while q:
            node=q.popleft()
            visited.add(node)
            for neigh in courses[node]:
                if neigh in visited:
                    return False
                else:
                    e[neigh]-=1
                    if e[neigh]==0:
                        q.append(neigh)
        if numCourses==len(visited):
            return True
        else:
            return False
            
        





        

        





        