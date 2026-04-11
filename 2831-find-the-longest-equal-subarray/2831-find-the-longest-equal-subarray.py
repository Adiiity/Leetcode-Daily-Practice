class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        maxf=0
        count=Counter()
        i=0
        
        for j in range(len(nums)):
            count[nums[j]]=1+count.get(nums[j],0)
            maxf=max(maxf,count[nums[j]])
            if (j-i+1)-maxf>k:
                count[nums[i]]-=1
                i+=1
        return maxf