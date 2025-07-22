class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board=[["."]* n for _ in range(n)]

        cols=set()
        negdia=set()
        posdia=set()

        res=[]

        def backtrack(r):
            if r==n:
                copy=["".join(row) for row in board]
                res.append(copy)
                return

            for c in range(n):
                if c in cols or (r+c) in posdia or (r-c) in negdia:
                    continue
                
                cols.add(c)
                posdia.add(r+c)
                negdia.add(r-c)
                board[r][c]="Q"
                backtrack(r+1)

                cols.remove(c)
                posdia.remove(r+c)
                negdia.remove(r-c)
                board[r][c]="."

        backtrack(0)

        return res



                