class Solution:
    def canMakeEqual(self, nums: List[int], k: int) -> bool:

        def possible(x):
            num_copy=nums.copy()
            op=0
            for i in range(len(nums)-1):
                if num_copy[i]!=x:
                    num_copy[i]*= -1
                    num_copy[i+1]*= -1
                    op+=1
                    if op>k:
                        return False
            return num_copy.count(x)==len(nums)

        return possible(1) or possible(-1)


                
                    
        