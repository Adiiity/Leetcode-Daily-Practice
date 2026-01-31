class Solution:
    def firstUniqChar(self, s: str) -> int:
        count={}

        for i in s:
            count[i]=1+count.get(i,0)

        for i,c in enumerate(s):
            if count[c]==1:
                return i
        return -1