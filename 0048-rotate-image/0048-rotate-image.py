class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l,r =0, len(matrix)-1

        while l<r:
            for i in range(r-l):
                top=l
                bottom=r

                topleft=matrix[top][l+i]

                matrix[top][l+i]=matrix[bottom-i][l]

                matrix[bottom-i][l]=matrix[bottom][r-i]

                matrix[bottom][r-i]=matrix[top+i][r]

                matrix[top+i][r]=topleft

            r-=1
            l+=1