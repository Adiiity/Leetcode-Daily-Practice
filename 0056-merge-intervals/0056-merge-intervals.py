class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res=[intervals[0]]

        for i in range(1,len(intervals)):
            last_int=res[-1]
            if intervals[i][0]<=last_int[1]:
                res[-1]=[min(last_int[0],intervals[i][0]),
                        max(last_int[1],intervals[i][1])]
            else:
                res.append(intervals[i])
        
        return res


                

        