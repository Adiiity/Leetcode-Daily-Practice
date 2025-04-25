class Solution(object):
    def numSplits(self, s):
        """
        :type s: str
        :rtype: int
        """
        # split_counter=0
        # for i in range(len(s)):
        #     countA={}
        #     countB={}
        #     for j in range(0,i):
        #         countA[s[j]]=1+countA.get(s[j],0)
        #     for k in range(i,len(s)):
        #         countB[s[k]]=1+countB.get(s[k],0)
        #     if len(countA)==len(countB):
        #         split_counter+=1

        # return split_counter
        n=len(s)
        left_set=set()
        right_set=set()
        right_count=[0]*n

        for i in range(n-1,-1,-1):
            right_set.add(s[i])
            right_count[i]=len(right_set)

        good_splits=0

        for i in range(n-1):
            left_set.add(s[i])
            if len(left_set)==right_count[i+1]:
                good_splits+=1
        
        return  good_splits