'''
2026/01/17 daily challenge

exhaustive method approach

try all combinations of two rectangles.
intersecting of more than two rectangles does not provide larger area.
'''


class Solution:
    def largestSquareArea(self, bottomLeft: List[List[int]], topRight: List[List[int]]) -> int:
        max_width = 0
        seen = []  # (x0, y0, x1, y1)
        for (x0, y0), (x1, y1) in zip(bottomLeft, topRight):
            for x2, y2, x3, y3 in seen:
                width = min(x1, x3) - max(x0, x2)
                height = min(y1, y3) - max(y0, y2)
                max_width = max(max_width, min(width, height))
            seen.append((x0, y0, x1, y1))
        return max_width * max_width

