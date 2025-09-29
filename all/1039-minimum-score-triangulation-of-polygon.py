'''
2025/09/29 daily challenge

dynamic programming approach (bottom-up ver)
'''


class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i + 2, n):
                score = float('inf')
                for k in range(i + 1, j):
                    # score of current triangle + two subproblems
                    score = min(score, values[i] * values[k] * values[j] + dp[i][k] + dp[k][j])
                dp[i][j] = score

        return dp[0][-1]

