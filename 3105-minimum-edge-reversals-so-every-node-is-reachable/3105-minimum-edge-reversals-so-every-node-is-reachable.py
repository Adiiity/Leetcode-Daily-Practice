class Solution:
    def minEdgeReversals(self, n: int, edges: List[List[int]]) -> List[int]:
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append((v,0))
            adj[v].append((u,1))

        visited=[False]*n
        visited[0]=True
        stack=[0]        
        res=[0]*n
        total0=0

        while stack:
            u=stack.pop()
            for v,cost in adj[u]:
                if not visited[v]:
                    visited[v]=True
                    total0+=cost
                    stack.append(v)

        res[0]=total0
        stack=[0]
        visited=[False]*n
        visited[0]=True

        while stack:
            u=stack.pop()
            for v,cost in adj[u]:
                if not visited[v]:
                    if cost==1:
                        res[v]=res[u]-1
                    else:
                        res[v]=res[u]+1
                    visited[v]=True
                    stack.append(v)
        return res
            