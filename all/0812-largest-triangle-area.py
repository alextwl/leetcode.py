'''
2025/09/27 daily challenge

math approach

calculate all combinations of triangle points.
'''


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        def get_area(x, y, z):
            rec = abs(x[0] * y[1] + y[0] * z[1] + z[0] * x[1] - \
                      x[1] * y[0] - y[1] * z[0] - z[1] * x[0])
            return rec / 2.0

        n = len(points)
        max_area = 0
        for i, x in enumerate(points):
            for j in range(i + 1, n - 1):
                y = points[j]
                for k in range(j + 1, n):
                    z = points[k]
                    max_area = max(max_area, get_area(x, y, z))

        return max_area

