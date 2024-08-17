'''
2024/08/17 daily challenge

dynamic programming approach
'''


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        width = len(points[0])

        prev_row = [0] * width
        curr_row = [0] * width

        for row in points:
            # max_point is equalivent to the auxiliary space
            # max_points_from_left[] & max_points_from_right[]
            # by reusing the previous element in the left/right side,
            # we can always get the maximum point between i & j for all j
            # and it's also equalivent to
            # max(prev_row[i] - abs(i - j) for j in range(n)) + row[i].
            #
            # we need to scan both from left and from right
            # because we didn't actually perform the abs(i - j) part
            # but keep the maximum dp running in one direction.
            #
            # scan from left to right
            max_point = 0
            for j, j_point in enumerate(prev_row):
                max_point = max(max_point - 1, j_point)
                curr_row[j] = max_point

            # scan from right to left
            max_point = 0
            for k, k_point in enumerate(reversed(prev_row), start=1):
                max_point = max(max_point - 1, k_point)
                curr_row[-k] = max(curr_row[-k], max_point) + row[-k]

            prev_row = curr_row.copy()

        return max(prev_row)

