class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        if t=="":
            return ""

        tMap=Counter(t)
        # tlen=len(t)
        l=0 
        charSet=[]
        res=float('inf')
        # while 
        count={}
        resStr=""
        have,need=0, len(tMap)
        for r in range(len(s)):
            charSet.append(s[r])

            if s[r] in tMap:
                count[s[r]]=1+count.get(s[r],0)
                if count[s[r]]==tMap[s[r]]:
                    have+=1

            if have==need:
                while s[l] not in tMap or count.get(s[l],0)>tMap[s[l]]:
                    if s[l] in count:
                        count[s[l]]-=1
                    charSet.pop(0)
                    l+=1
                    
                if len(charSet)<res:
                    res=len(charSet)
                    resStr= ''.join(charSet)
        
        return resStr

                



        
        