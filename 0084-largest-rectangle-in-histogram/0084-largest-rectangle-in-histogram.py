class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maxArea=0

        for ind,hei in enumerate(heights):
            start=ind
            while stack and stack[-1][1]>hei:
                index,height=stack.pop()
                maxArea=max(maxArea, height*(ind-index))
                start=index
            stack.append((start,hei))

        for i,h in stack:
            maxArea=max(maxArea,h*(len(heights)-i))

        return maxArea

