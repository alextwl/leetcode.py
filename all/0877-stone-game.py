'''
dynamic programming approach
'''

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        '''
        dp[i][j] = the biggest number of stones Alice can get more than
                   opponent's in i-th ~ j-th piles.
        '''
        dp = [[0] * n for _ in range(n)]
        # init base case
        for i, stones in enumerate(piles):
            dp[i][i] = stones
        
        for k in range(1, n):
            # j=i+k, maximize stone diffs from picking in i-th to j-th pile
            for i in range(n - k):
                '''
                in this round:
                (1) if we pick piles[i], dp[i][j] = piles[i] - dp[i+1][j]
                (2) if we pick piles[j], dp[i][j] = piles[j] - dp[i][j-1]
                '''
                dp[i][i+k] = max(piles[i] - dp[i+1][i+k],
                                 piles[i+k] - dp[i][i+k-1])

        '''
        no matter Alice pick the leftmost (piles[0]) or the rightmost (piles[-1])
        in the beginning, if the difference dp[0][-1] > 0, that means Alice will win.
        '''
        if dp[0][-1] > 0:
            return True

        '''
        actually it won't happen because there are even piles
        and Alice can always pick maximum subsequence between odds and evens.
        '''
        return False

