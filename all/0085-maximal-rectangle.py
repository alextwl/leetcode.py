'''
2024/04/13 daily challenge

prefix sum + stack approach
'''


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])

        heights = [0] * (n + 1)  # the vertical sums of each column
        max_area = 0

        for row in matrix:
            for j, cell in enumerate(row):
                if cell == '1':
                    heights[j] += 1
                else:
                    heights[j] = 0

            stack = []  # a stack of column indices which ends with a rectangle

            for sj in range(n + 1):
                # search the previous rectangles which had higher height
                # and calculate its width and area (to the column prior to sj)
                while stack and heights[stack[-1]] > heights[sj]:
                    area_height = heights[stack.pop()]
                    if not stack:
                        area_width = sj  # [0..sj-1]
                    else:
                        area_width = sj - stack[-1] - 1  # does not include 2nd stack[-1] column itself

                    max_area = max(max_area, area_width * area_height)
                stack.append(sj)

        return max_area

