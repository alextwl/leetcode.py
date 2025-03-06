'''
2025/03/06 daily challenge

set + xor approach
'''


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        seen = set()
        a = b = 0

        xor = 0
        for row in grid:
            for v in row:
                if not a:
                    if v in seen:
                        a = v
                    seen.add(v)
                xor ^= v

        for v in range(1, len(grid) ** 2 + 1):
            xor ^= v

        b = xor ^ a

        return [a, b]


'''
perfect sum & perfect square sum approach

learnt from official editorial 2:
https://leetcode.com/problems/find-missing-and-repeated-values/editorial/#approach-2-math
'''


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        sqr = n * n

        perfect_sum = sqr * (sqr + 1) // 2
        perfect_sqr = sqr * (sqr + 1) * (2 * sqr + 1) // 6
        grid_sum = sum(v for row in grid for v in row)
        sqr_sum = sum(v*v for row in grid for v in row)

        sum_diff = grid_sum - perfect_sum  # sum(grid) - perfect_sum = a - b
        sqr_diff = sqr_sum - perfect_sqr  # square_sum(grid) - perfect_square = a**2 - b**2

        # axiom: x**2 - y**2 = (x+y)*(x-y)
        # sqr_diff = (x+y) * sum_diff
        x_plus_y = sqr_diff // sum_diff
        a = (x_plus_y + sum_diff) // 2
        b = (x_plus_y - sum_diff) // 2
        return [a, b]

