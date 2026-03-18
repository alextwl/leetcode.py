'''
2026/03/18 daily challenge

prefix sum approach
'''


class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        n = len(grid[0])
        # pfx[j] = prefix sum of grid[*][j]
        pfx = [0] * n

        ans = 0
        max_j = n
        for row in grid:
            curr_sum = 0
            for j in range(0, max_j):
                pfx[j] += row[j]
                curr_sum += pfx[j]
                if curr_sum <= k:
                    ans += 1
                else:
                    # sum exceeded k,
                    # no need to go through further columns.
                    max_j = j
                    break
        return ans

