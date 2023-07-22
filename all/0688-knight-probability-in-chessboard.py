'''
2023/07/22 daily challenge

dynamic programming approach
'''

class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k == 0:
            # shortcut for corner case
            return 1.0

        '''
        dp space:
        dp[m][x][y] = the probability to reach coordinate (x, y) in m moves
        dp = n*n matrix * (k+1) moves including zero move.
        '''
        dp = [[[0] * n for _ in range(n)] for _ in range(k+1)]
        
        # the beginning cell has 1 probability for zero move.
        dp[0][row][column] = 1
        
        # deltas of 8 directions of knight's move
        dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                (2, 1), (-2, 1), (2, -1), (-2, -1)]
        
        # iterate from the 1st move to k-nd move
        prev_dp = dp[0]
        for m in range(1, k+1):
            curr_dp = dp[m]
            for x in range(n):
                for y in range(n):
                    '''
                    calculate the probability to reach (x, y) at m-th move
                    '''
                    for dx, dy in dirs:
                        # bottom-up: determine the previous coordinate from the previous move
                        px, py = x - dx, y - dy
                        
                        if (0 <= px < n) and (0 <= py < n):
                            curr_dp[x][y] += prev_dp[px][py]
                    '''
                    each probability accumulated from the previous coordinates
                    has 1/8 probability to reach the coordinate, so we need to divide it by 8.
                    '''
                    curr_dp[x][y] /= 8

            prev_dp = curr_dp

        return sum(prev_dp[x][y] for x in range(n) for y in range(n))

