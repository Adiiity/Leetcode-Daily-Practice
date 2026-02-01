class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        
        # set prefixskill

        s,m=len(skill),len(mana)

        prefixskill=[0]*(s+1)
        for i in range(s):
            prefixskill[i+1]=prefixskill[i]+skill[i]

        # think as if setting for j potion and have j-1 potion previously done 
        start=0
        for j in range(1,m):
            prev=mana[j-1]
            curr=mana[j]

            gap=0
            for i in range(s):
                need=prev*prefixskill[i+1]-curr*prefixskill[i]
                if need>gap:
                    gap=need
            start+=gap

        
        return start+mana[-1]*prefixskill[s]



        