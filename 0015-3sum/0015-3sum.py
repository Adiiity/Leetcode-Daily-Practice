class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            
            l,r=i+1,len(nums)-1
            while l<r:
                finSum=a+nums[l]+nums[r]

                if finSum<0:
                    l+=1
                elif finSum>0:
                    r-=1
                else:
                    result.append([a,nums[l],nums[r]])
                    l+=1
                    while nums[l]==nums[l-1] and l<r:
                        l+=1
                
        return result
