class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count=defaultdict(int)  #prefix hashmap 
        count[0]=1
        curr=0
        ans=0

        for n in nums:
            curr+=n

            ans+=count[curr-k]

            count[curr]+=1

        return ans


        