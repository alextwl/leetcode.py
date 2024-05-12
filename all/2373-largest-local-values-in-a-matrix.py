'''
2024/05/12 daily challenge
'''


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        ans = []

        for i in range(1, n - 1):
            row = []
            for j in range(1, n - 1):
                row.append(max(*grid[i-1][j-1:j+2],
                               *grid[i][j-1:j+2],
                               *grid[i+1][j-1:j+2]))
            ans.append(row)

        return ans

