class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjMap={i:[] for i in range(n)}

        for u,v in edges:
            adjMap[u].append(v)
            adjMap[v].append(u)
        
        stack=[(0,-1)]
        visited=set()
        c=0
        while stack:
            c+=1
            node,par=stack.pop()
            visited.add(node)
            for neigh in adjMap[node]:
                if neigh ==par:
                    continue
                if neigh in visited:
                    return False
                else:
                    stack.append((neigh,node))
        if c!=n:
            return False
        return True



        