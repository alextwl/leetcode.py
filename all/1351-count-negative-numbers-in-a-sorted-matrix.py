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
        j = n - 1  # pointer for latest visited column
        for i, row in enumerate(grid):
            if row[0] < 0:
                # shortcut for all-negative rows
                ans += (m - i) * n
                break
            # note it's sorted in non-increasing order
            # both row-wise & column-wise, we reuse the pointer of column
            # to reduce the complexity to O(m+n).
            for k in range(j, -1, -1):
                if row[k] >= 0:
                    j = k
                    ans += n - 1 - j
                    break
        return ans

