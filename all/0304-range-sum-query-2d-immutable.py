'''
pre-calculated prefix sum approach

similar to problem 1314.

calculate a prefix sum matrix in advance,
and then calculate specified region sum by demand.
'''

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.m, self.n = len(matrix), len(matrix[0])
        
        # calculate prefix sum matrix in advance
        self.dp = [[0 for _ in range(self.n)] for _ in range(self.m)]
        
        for i in range(0, self.m):
            # accumulate prefix sum from left to right
            psum = 0
            for j in range(0, self.n):
                psum += self.matrix[i][j]
                self.dp[i][j] = psum
                
                if i > 0:
                    # add upper row's prefix sum
                    self.dp[i][j] += self.dp[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # initialized with lower-right corner's prefix sum
        ans = self.dp[row2][col2]
        if row1 > 0:
            # subtract upper-right corner's prefix sum
            ans -= self.dp[row1-1][col2]
        if col1 > 0:
            # subtract lower-left corner's prefix sum
            ans -= self.dp[row2][col1-1]
        if row1 > 0 and col1 > 0:
            # add upper-left corner which subtracted twice before
            ans += self.dp[row1-1][col1-1]
        
        return ans

