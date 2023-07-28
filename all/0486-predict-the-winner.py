'''
2023/07/28 daily challenge

dynamic programming approach

equivalent to problem 877 stone game.
'''

class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        '''
        dp[i][j] = the maximum difference of scores of (P1 - P2)
        '''
        dp = [[0] * n for _ in range(n)]
        for i, points in enumerate(nums):
            '''
            for any length-1 arrays, player 1 always gets all points because player 1 always starts first.
            '''
            dp[i][i] = points
        
        for k in range(1, n):
            for i in range(n - k):
                j = i + k
                '''
                for subarray nums[i:j+1],
                player 1 picked either end of the subarray: nums[i] (left side) or nums[j] (right side).
                we can maximize the diff between the choices.
                '''
                dp[i][j] = max(nums[i] - dp[i+1][j],
                               nums[j] - dp[i][j-1])

        return dp[0][-1] >= 0

