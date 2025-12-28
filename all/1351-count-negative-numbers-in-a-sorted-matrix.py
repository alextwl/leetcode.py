'''
2023/06/08 daily challenge
2025/12/28 daily challenge

time=O(m+n) ver
'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        negs = 0

        bound = n-1  # column index of the first number to be checked from right.
        for i, row in enumerate(grid):
            for j in range(bound, -1, -1):
                if row[j] >= 0:
                    # update the rightmost index to be checked in the next round.
                    bound = j
                    break
            else:
                # numbers of the entire row are negative, stop.
                # count remaining rows (including the current row) and add it to the counter.
                negs += (m - i) * n
                break

            # count the negative part of row.
            negs += (n-1) - bound

        return negs


'''
refined linear search ver
'''


class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        ans = 0
        for i, row in enumerate(grid):
            if row[0] < 0:
                # shortcut for all-negative rows
                ans += (m - i) * n
                break
            for j, cell in enumerate(row):
                if cell < 0:
                    # negative cell found
                    ans += n - j
                    break
        return ans

