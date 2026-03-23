'''
2026/03/23 daily challenge

breadth first search approach
'''


import collections


MOD = 1_000_000_007


class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dest = (m - 1, n - 1)
        # max_abs[is_negative][x][y]
        max_abs = [[[-1] * n for _ in range(m)] for _ in range(2)]
        # special variable: 0 if zero found
        seen_zero = -1
        # (x, y, current_absolute_product, is_negative)
        q = collections.deque([(0, 0, abs(grid[0][0]), 1 if grid[0][0] < 0 else 0)])
        while q:
            x, y, curr_prod, curr_sign = q.popleft()
            if curr_prod == 0:
                seen_zero = 0
            if curr_prod <= max_abs[curr_sign][x][y]:
                continue
            max_abs[curr_sign][x][y] = curr_prod
            if (x, y) == dest:
                continue
            for dx, dy in [(1, 0), (0, 1)]:
                dx += x
                dy += y
                if dx < m and dy < n:
                    next_prod = curr_prod * abs(grid[dx][dy])
                    if grid[dx][dy] < 0:
                        q.append((dx, dy, next_prod, curr_sign ^ 1))
                    else:
                        q.append((dx, dy, next_prod, curr_sign))

        if max_abs[0][m - 1][n - 1] < 0:
            return seen_zero

        # the product says the modulo is performed
        # **ONLY** after getting the maximum product.
        # no modulo performed during the search.
        return max_abs[0][m - 1][n - 1] % MOD

