class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        nums.sort()
        l=0
        r=0
        replace=0
        while r<len(nums):
            if nums[l]<nums[r]:
                replace+=1
                l+=1
            r+=1
        return replace