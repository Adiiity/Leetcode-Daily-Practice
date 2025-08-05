class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum=0
        maxsum=nums[0]

        for num in nums:
            if currSum < 0:
                currSum=0
            currSum+=num
            maxsum=max(currSum,maxsum)

        return maxsum
        