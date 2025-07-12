class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # if not grid:
        #     return 0

        # rows,cols=len(grid),len(grid[0])
        # visited=set()
        # islands=0

        # def bfs(r,c):
        #     q=collections.deque()
        #     visited.add((r,c))
        #     q.append((r,c))
        #     while q:
        #         row,col=q.popleft()

        #         directions=[[1,0],[-1,0],[0,1],[0,-1]]

        #         for dr,dc in directions:
        #             r=dr+row
        #             c=dc+col
        #             if (r in range(rows) and
        #                 c in range(cols) and 
        #                 grid[r][c]=="1" and
        #                 (r,c) not in visited):
        #                 visited.add((r,c))
        #                 q.append((r,c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c]=="1" and (r,c) not in visited:
        #             bfs(r,c)
        #             islands+=1
        # return islands

        if not grid: 
            return 0

        islands=0
        rows,cols=len(grid),len(grid[0])
        
        def dfs(r,c):
            if (r<0 or c<0 or
                r>=rows or c>=cols or 
                grid[r][c]=="0"):
                return

            grid[r][c]="0"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    dfs(r,c)
                    islands+=1

        return islands