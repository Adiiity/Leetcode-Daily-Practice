class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        hi=sum(nums)

        while low<hi:
            mid=(low+hi)//2
            blocks=1
            curr_sum=0

            for n in nums:
                if curr_sum+n>mid:
                    blocks+=1
                    curr_sum=n
                else:
                    curr_sum+=n
            
            if blocks>k:
                low=mid+1
            else:
                hi=mid
        
        return low
