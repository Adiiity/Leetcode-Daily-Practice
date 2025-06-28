class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:

        evensum,oddsum=0,0

        for i in range(len(nums)):
            if i%2==0:
                evensum+=nums[i]
            else:
                oddsum+=nums[i]
        
        count=0
        lefteven=0
        leftodd=0

        for i,a in enumerate(nums):
            if i%2 ==0:
                evensum-=a
            else:
                oddsum-=a

            if lefteven+oddsum==leftodd+evensum:
                count+=1
            
            if i%2==0:
                lefteven+=a
            else:
                leftodd+=a
        
        return count