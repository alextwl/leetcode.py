'''
2024/01/26 daily challenge

dynamic programming approach
'''


class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0
        
        dp0 = [[0 for _ in range(n)] for _ in range(m)]  # the number of pathes from the previous move
        dp1 = [[0 for _ in range(n)] for _ in range(m)]  # the number of pathes of the current move
        
        # base cases: add valid path count to all edge cells.
        for i in range(m):
            dp0[i][0] += 1
            dp0[i][-1] += 1
        
        for j in range(n):
            dp0[0][j] += 1
            dp0[-1][j] += 1
        
        # accumulate the valid pathes only from the start cell if maxMove==1.
        ans = dp0[startRow][startColumn]
        
        # time to iterate remaining moves.
        for _ in range(1, maxMove):
            for i in range(m):
                for j in range(n):
                    path = 0
                    for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                        if 0 <= x < m and 0 <= y < n:
                            path += dp0[x][y]
                    dp1[i][j] = path
            ans = (ans + dp1[startRow][startColumn]) % 1_000_000_007
            dp0, dp1 = dp1, dp0

        return ans

