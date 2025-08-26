'''
2025/08/26 daily challenge
'''


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_diag = 0.0
        max_area = 0

        for a, b in dimensions:
            c = (a ** 2 + b ** 2) ** 0.5
            if c == max_diag:
                max_area = max(max_area, a * b)
            elif c > max_diag:
                max_diag = c
                max_area = a * b

        return max_area

