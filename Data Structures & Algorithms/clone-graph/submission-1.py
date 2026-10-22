"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        map={}

        def dfs(root):    
            if not root:
                return 
            # print(root.val)
            new_root=Node(root.val)
            map[root]=new_root
            for neigh in root.neighbors:
                if neigh in map:
                    new_root.neighbors.append(map[neigh])
                else:
                    new_root.neighbors.append(dfs(neigh))
            return new_root
        
        return dfs(node)
        

        