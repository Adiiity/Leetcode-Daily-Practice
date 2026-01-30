class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        # arr = [2,2,2,2,5,5,5,8], k = 3 threshold=4

        # I want to keep a window since beginning 
        currSum=sum(arr[:k-1]) # initially 2+2=4
        res=0
        for l in range(len(arr)-k+1): 
            currSum+=arr[l+k-1] #starts from index 2
            if (currSum/k)>=threshold:
                res+=1
            currSum-=arr[l]
        return res