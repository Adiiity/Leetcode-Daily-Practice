class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid),len(grid[0])
        visit=set()
        area=0

        def bfs(r,c):
            q=collections.deque()
            q.append((r,c))
            visit.add((r,c))
            res=1

            while q:
                row,col=q.popleft()
                directions=[[1,0],[-1,0],[0,1],[0,-1]]

                for dr,dc in directions:
                    r,c=dr+row,dc+col
                    if (r<0 or c<0 or r>=rows or c>=cols or grid[r][c]==0 or (r,c) in visit):
                        continue
                    q.append((r,c))
                    visit.add((r,c))
                    res+=1
            return res

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] ==1 and (r,c) not in visit:
                    area=max(area,bfs(r,c))

        return area

