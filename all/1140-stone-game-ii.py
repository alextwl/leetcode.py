'''
2023/05/26 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/stone-game-ii/solutions/3563326/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        suffixSum = [0] * (n+1)
        prev = suffixSum[-2] = piles[-1]
        for i in range(n-2, -1, -1):
            suffixSum[i] = prev + piles[i]
            prev = suffixSum[i]
        
        '''
        dp[i][j] = the maximum stones Alice can earn at the position i
                   with j piles to take.
        '''
        dp = [[0] * (n+1) for _ in range(n)]
        
        # bottom-up iteration
        for i in range(n-1, -1, -1):
            # start from M=1
            for m in range(1, n+1):
                if i + 2*m >= n:
                    '''
                    taking next max X piles (2M) exceeds the end of pile,
                    so take all the remaining piles (== the suffix sum.)
                    '''
                    dp[i][m] = suffixSum[i]
                else:
                    '''
                    if alice could not take all remaining piles in one round at position i,
                    we need to consider all moves (1 <= X <= 2M) with bob's rounds.
                    '''
                    for x in range(1, 2*m + 1):
                        # Bob also takes optimal move
                        bob_stones = dp[i+x][max(x, m)]
                        # most stones Alice can take is (the remaining - Bob's next optimal move.)
                        alice_stones = suffixSum[i] - bob_stones
                        dp[i][m] = max(dp[i][m], alice_stones)
        
        '''
        the optimal answer is the maximum stones
        Alice is going to take starting from M=1 at position 0.
        '''
        return dp[0][1]

