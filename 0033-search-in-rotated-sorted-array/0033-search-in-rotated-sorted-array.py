class Solution:
    def search(self, num: List[int], target: int) -> int:
        # binary search 
        n=len(num)
        l,r=0,n-1
        while r>=l:
            mid=(l+r)//2

            if target==num[mid]:
                return mid

            if num[l]<=num[mid]:
                if num[l]<=target<num[mid]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if num[mid]<target<=num[r]:
                    l=mid+1
                else:
                    r=mid-1
        return -1
        