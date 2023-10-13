'''
dynamic programming + backtrace approach

learnt from official hints.

iterate from the top floor and calculate the minimum cost.
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [float('inf')] * (len(cost) + 2)
        dp[-2] = dp[-1] = 0  # the cost of the top floor reached by climbing one or two steps
        
        for i in range(len(cost)-1, -1, -1):
            # dp[i] = the minimum cost from i-th floor to i+1 or i+2 floor.
            dp[i] = cost[i] + min(dp[i+1], dp[i+2])
        
        '''
        think reversely:
        we can reach the top by starting from climbing 1 or 2 steps from the beginning.
        so the minimum cost is the minimum of dp[0], dp[1].
        '''
        return min(dp[0], dp[1])


'''
2023/10/13 daily challenge

space=O(1) ver
'''


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        it = iter(cost)
        prev2 = next(it)
        prev1 = next(it)

        for curr in it:
            curr += min(prev2, prev1)
            prev2, prev1 = prev1, curr

        return min(prev2, prev1)

