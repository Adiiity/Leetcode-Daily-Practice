class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]

        for n in nums:
            heapq.heappush(minHeap,(-1 * n))

        res=0
        for _ in range(k):
            res= -1*heapq.heappop(minHeap)

        return res
