class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        maxC=0
        counter=0
        
        for n in nums:
            if n==1:
                counter+=1
                if counter>maxC:
                    maxC=counter
            else:
                counter=0

        return maxC
        