from collections import defaultdict
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]
        hashmap={}
        for x in nums2:
            while stack and stack[-1]<x:
                val=stack.pop()
                hashmap[val]=x
            stack.append(x)
        
        return [hashmap.get(x,-1) for x in nums1]
        