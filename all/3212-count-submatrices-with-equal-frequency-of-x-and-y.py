'''
2026/03/19 daily challenge

prefix sum approach

build prefix differences for each column.
'''


class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        n = len(grid[0])
        # seen_x[col] = whether at least one X exists in col
        seen_x = [False] * n
        # diffs[col] = difference between X and Y by col
        diffs = [0] * n

        ans = 0
        for row in grid:
            diff_sum = 0
            x_flag = False
            for j, val in enumerate(row):
                if val == 'X':
                    diffs[j] += 1
                    seen_x[j] = True
                elif val == 'Y':
                    diffs[j] -= 1

                x_flag |= seen_x[j]
                diff_sum += diffs[j]
                if diff_sum == 0 and x_flag:
                    ans += 1

        return ans

