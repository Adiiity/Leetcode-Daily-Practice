class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n=len(matrix[0])
        heights=[0]*n
        maxArea=0

        for row in matrix:
            for j in range(n):
                if row[j]=='1':
                    heights[j]+=1
                else: 
                    heights[j]=0
            
            maxArea=max(maxArea, self.findarea_row(heights))
        return maxArea
    
    def findarea_row(self,heights):

        stack=[]
        maxArea=0
        heights.append(0)
        for ind, hei in enumerate(heights):
            start=ind
            while stack and stack[-1][1]>hei:
                i,h=stack.pop()
                maxArea=max(maxArea,h*(ind-i))
                start=i
            stack.append((start,hei))
        
        for i,h in stack:
            maxArea=max(maxArea,h*(len(heights)-i))
        heights.pop()
        return maxArea
