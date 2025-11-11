class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_max=1
        curr_min=1
        res=nums[0]
        for n in nums:
            if n==0:
                curr_max=1
                curr_min=1
            
            temp=n*curr_max
            curr_max=max(n*curr_max,n*curr_min,n)
            curr_min=min(temp,n*curr_min,n)
            res=max(res,curr_max)
        
        return res
        