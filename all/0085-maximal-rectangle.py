'''
2024/04/13 daily challenge
2026/01/11 daily challenge

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


'''
prefix sums + two pointers approach
'''


class Solution:
    def getLargestArea(self, heights):
        if not heights:
            return 0

        n = len(heights)
        left = [-1] * n
        right = [n] * n

        # two-way scanning
        # find left & right bounds of each rectangle
        for i in range(1, n):
            prev = i - 1
            while prev >= 0 and heights[prev] >= heights[i]:
                prev = left[prev]
            left[i] = prev

        for i in range(n - 2, -1, -1):
            prev = i + 1
            while prev < n and heights[prev] >= heights[i]:
                prev = right[prev]
            right[i] = prev

        # find max area of rectangle in matrix[:last_scanned_row+1]
        return max((r - l - 1) * h for l, r, h in zip(left, right, heights))

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        heights = [0] * n

        ans = 0
        for row in matrix:
            for i in range(n):
                # vertical prefix sum for consecutive 1's in a column
                if row[i] == '1':
                    heights[i] = heights[i] + 1
                else:
                    heights[i] = 0
            ans = max(ans, self.getLargestArea(heights))
        return ans

