class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        
        positions=defaultdict(list)

        for i,n in enumerate(nums):
            positions[n].append(i)

        ans=0

        for pos in positions.values():
            left=0
            for right in range(len(pos)):
                while pos[right]-pos[left]-(right-left)>k:
                    left+=1

                ans=max(ans, right-left+1) 
        
        return ans
