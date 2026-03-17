'''
2023/11/26 daily challenge
2026/03/17 daily challenge

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


'''
no sort + no modification ver

learnt from official solution 2
https://leetcode.com/problems/largest-submatrix-with-rearrangements/solution/
'''


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        max_area = 0
        
        # the previous row with descending order
        # element = (vertical-accumulated height, column)
        prev_desc_row = []
        
        for row in matrix:
            curr_desc_row = []
            # the set of column which height is accumulated from previous row.
            checked = set()
            
            # check if cells of the current row can be accmululated from the previous.
            for prev_height, j in prev_desc_row:
                if row[j]:
                    curr_desc_row.append((prev_height+1, j))
                    checked.add(j)
            
            # check the remaining cells which height == 1
            for j, cell in enumerate(row):
                if cell and j not in checked:
                    curr_desc_row.append((1, j))
            
            # curr_desc_row is already sorted due to the sequence of previous checking,
            # we can feel free to find the maximum submatrix from the max height to the max width.
            for width, (height, _) in enumerate(curr_desc_row):
                max_area = max(max_area, (width+1) * height)
            
            prev_desc_row = curr_desc_row

        return max_area


'''
sort heights for each row ver
'''


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])

        ans = 0
        # accumulated number of consecutive 1's for each column
        prev_row = [0] * n
        for row in matrix:
            curr_row = row[:]
            # build count of consecutive 1's for each column at the current row
            for j, (prev, curr) in enumerate(zip(prev_row, row)):
                if curr != 0:
                    curr_row[j] += prev
            # sort heights in descending order
            desc_row = sorted(curr_row, reverse=True)
            # maximize area of submatrix with current row as its bottom edge
            for width, height in enumerate(desc_row, start=1):
                if not height:
                    # cannot form a submatrix, no need to search further.
                    break
                ans = max(ans, width * height)

            prev_row = curr_row

        return ans

