class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # valid combos in any order - Backtracking 
        output=[]

        def backtrack(i, dots, curIP):
            # base cases
            if dots==4 and i==len(s):
                return output.append(curIP[:-1])
            if dots>4:
                return 
            
            for j in range(i,min(i+3,len(s))):
                if int(s[i:j+1]) <256 and (i==j or s[i]!="0"):
                    backtrack(j+1,dots+1, curIP+s[i:j+1]+'.')
            
        
        backtrack(0,0,"")
        return output
            
            

        