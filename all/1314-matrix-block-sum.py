'''
prefix sum approach

learnt from
https://leetcode.com/problems/matrix-block-sum/discuss/482730/PythonJSGoC%2B%2B-O(-m*n-)-Integral-Image-DP-w-Explanation
https://leetcode.com/problems/matrix-block-sum/discuss/620405/Easy-Prefix-Logic-Explanation-with-Matrix-Example-%3A-Python-Soution

first calculate prefix sums vertically and horizontally,
and then calculate the block sum by subtracting specific corner
'''

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        # declare a prefix sum matrix
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        # add prefix sum from left column
        for i in range(m):
            dp[i][0] = mat[i][0]
            for j in range(1, n):
                dp[i][j] = dp[i][j-1] + mat[i][j]
        
        # add prefix sum from upper row
        for j in range(n):
            for i in range(1, m):
                dp[i][j] += dp[i-1][j]
        
        # calculate the matrix sum of every 2k+1 block.
        for i in range(m):
            upper_bound, lower_bound = max(i-k, 0), min(i+k, m-1)
            for j in range(n):
                left_bound, right_bound = max(j-k, 0), min(j+k, n-1)
                # initialize from lower-right cornet's prefix sum
                blocksum = dp[lower_bound][right_bound]
                # subtract upper-right corner
                if upper_bound > 0:
                    blocksum -= dp[upper_bound-1][right_bound]
                # subtract lower-left corner
                if left_bound > 0:
                    blocksum -= dp[lower_bound][left_bound-1]
                # add upper-left corner which subtracted twice before
                if upper_bound > 0 and left_bound > 0:
                    blocksum += dp[upper_bound-1][left_bound-1]
                
                # use original space to store answer.
                mat[i][j] = blocksum
        
        return mat
