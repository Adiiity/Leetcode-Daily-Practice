class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # brute force
        # s1=sorted(s1)

        # for i in range(len(s2)):
        #     for j in range(i,len(s2)):
        #         substring=s2[i:j+1]
        #         substring=sorted(substring)
        #         if s1==substring:
        #             return True

        # return False

        # Hash map
        # count1={}
        # for s in s1:
        #     count1[s]=1+count1.get(s,0)
        
        # lens1=len(count1)
        # for i in range(len(s2)):
        #     curr=0
        #     count2={}
        #     for j in range(i,len(s2)):
        #         count2[s2[j]]=1+count2.get(s2[j],0)

        #         if count1.get(s2[j],0)<count2[s2[j]]:
        #             break
        #         if count1.get(s2[j],0)==count2[s2[j]]:
        #             curr+=1
        #         if curr==lens1: 
        #             return True
        # return False

        # Sliding window
        from collections import Counter
        len1,len2=len(s1),len(s2)

        if len1>len2:
            return False
        
        count1=Counter(s1)
        count2=Counter(s2[:len1])

        if count1==count2:
            return True

        l=0
        for r in range(len1,len2):
            count2[s2[r]]+=1
            count2[s2[l]]-=1

            if count2[s2[l]]==0:
                del count2[s2[l]]
            
            if count1==count2:
                return True
            
            l+=1
        
        return False



