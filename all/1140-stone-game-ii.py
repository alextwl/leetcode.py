'''
2023/05/26 daily challenge
2024/08/20 daily challenge
2026/08/09 daily challenge

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


'''
dynamic programming approach (recursive ver)
'''


import functools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix_sums = []
        running_sum = 0
        for stone in reversed(piles):
            running_sum += stone
            suffix_sums.append(running_sum)
        suffix_sums.reverse()
        
        @functools.cache
        def max_stones(pos, m):
            if pos + 2*m >= n:
                # take all remaining piles
                return suffix_sums[pos]
            
            opponents = float('inf')  # opponent's stone
            for x in range(1, 2 * m + 1):
                opponents = min(opponents, max_stones(pos + x, max(x, m)))
            
            return suffix_sums[pos] - opponents
        
        return max_stones(0, 1)  # start from pos=0, M=1


'''
dynamic programming approach (recursive ver + syntax sugar)
'''


import functools
import itertools


class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffixes = list(itertools.accumulate(piles[::-1]))[::-1]

        @functools.cache
        def dp(i, m):
            if i + 2*m >= n:
                return suffixes[i]

            another_score = float('inf')
            for x in range(1, 2*m + 1):
                another_score = min(another_score, dp(i + x, max(x, m)))
            return suffixes[i] - another_score

        return dp(0, 1)

