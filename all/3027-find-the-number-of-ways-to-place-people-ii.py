'''
2025/09/03 daily challenge

brute force + sorting approach
'''


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        points.sort(key=lambda k: (k[0], -k[1]))

        ans = 0
        for i, (x0, y0) in enumerate(points):
            x_min, x_max = x0 - 1, float('inf')
            y_min, y_max = float('-inf'), y0 + 1
            for j in range(i + 1, n):
                x1, y1 = points[j]
                if x_min < x1 < x_max and y_min < y1 < y_max:
                    ans += 1
                    x_min, y_min = x1, y1
        return ans

