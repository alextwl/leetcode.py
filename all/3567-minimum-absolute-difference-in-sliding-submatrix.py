'''
2026/03/20 daily challenge

brute force + sorting approach
'''


import itertools


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        if k == 1:
            # shortcut for 1x1 submatrix
            return [[0] * (n - k + 1) for _ in range(m - k + 1)]

        ans = []  # 2D array
        for i in range(m - k + 1):
            row_ans = []
            for j in range(n - k + 1):
                # flatten the submatrix
                arr = [grid[x][y] for x in range(i, i+k) for y in range(j, j+k)]
                arr.sort()
                min_diff = 200_001
                # the problem asks for minimum absolute difference
                # between any two **distinct** values.
                # two equivalent values do not definitively give a zero diff
                # except all values in the submatrix have the same value.
                for (a, _), (b, _) in itertools.pairwise(itertools.groupby(arr)):
                    min_diff = min(min_diff, abs(a - b))
                row_ans.append(min_diff if min_diff < 200_001 else 0)
            ans.append(row_ans)
        return ans

