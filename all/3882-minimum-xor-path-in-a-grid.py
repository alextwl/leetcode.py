'''
2026/10/28 daily challenge

brute force approach

traverse all possible pathes.
'''


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        seen = [[set() for _ in range(n)] for _ in range(m)]

        # generate first row
        seen[0][0].add(grid[0][0])
        for j in range(1, n):
            curr_val = grid[0][j]
            curr_xor = seen[0][j]
            for prev_xor in seen[0][j - 1]:
                curr_xor.add(prev_xor ^ curr_val)

        # generate first column
        for i in range(1, m):
            curr_val = grid[i][0]
            curr_xor = seen[i][0]
            for prev_xor in seen[i - 1][0]:
                curr_xor.add(prev_xor ^ curr_val)

        # traverse remaining cells
        for i in range(1, m):
            for j in range(1, n):
                curr_val = grid[i][j]
                curr_xor = seen[i][j]
                # from left
                for prev_xor in seen[i][j - 1]:
                    curr_xor.add(prev_xor ^ curr_val)
                # from up
                for prev_xor in seen[i - 1][j]:
                    curr_xor.add(prev_xor ^ curr_val)

        return min(seen[-1][-1])

