'''
2023/11/26 daily challenge

sorting + input modification approach

iterate each row by assuming the bottom row is the base of width,
and multiplying it with the number of consecutive 1's of each column
to form a maximum submatrix.
'''


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        max_area = 0
        
        for i, row in enumerate(matrix):
            # check and modify the cell
            if i > 0:
                for j in range(n):
                    if row[j]:
                        row[j] += matrix[i-1][j]
            
            # sort only the current by descending order
            # so that we can try to iterate from the max height
            # to the max width to find a maximum submatrix.
            desc_row = sorted(row, reverse=True)
            for width, height in enumerate(desc_row):
                max_area = max(max_area, (width+1) * height)

        return max_area

