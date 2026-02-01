class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # O based index, also assumed for 1 player f(1)=0th index=winner

        winner=0
        for i in range(2,n+1):
            winner = ( winner + k ) % i # here f(2)..f(n) computes and so n+1 
        return winner+1
