import heapq
from collections import defaultdict
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # adj={src: [] for src,dst in tickets}

        # tickets.sort()

        # for src, dst in tickets:
        #     adj[src].append(dst)

        # res=["JFK"]
        # def dfs(src):
        #     if len(res)==1+len(tickets):
        #         return True
        #     if src not in adj:
        #         return False

        #     temp=list(adj[src])
        #     for i,v in enumerate(temp):
        #         adj[src].pop(i)
        #         res.append(v)
        #         if dfs(v): return True
        #         res.pop()
        #         adj[src].insert(i,v)
        #     return False

        # dfs("JFK")
        # return res
        adj = defaultdict(list)
        for src,dst in tickets:
            heapq.heappush(adj[src],dst)

        res=[]
        def dfs(src):
            while adj[src]:
                next_dest=heapq.heappop(adj[src])
                dfs(next_dest)
            res.append(src)

        dfs("JFK")

        return res[::-1]

        