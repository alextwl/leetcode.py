'''
2023/08/27 daily challenge

dynamic programming approach

time=O(n**2), space=O(n**2)

so we need to evaluate if each stone could be reached
in all possible previous k units of jumps.
'''


class Solution:
    def canCross(self, stones: List[int]) -> bool:
        '''
        build a map of stone position to stones[] index
        to indicate if a position had a stone or not.
        
        stone2idx[pos] = an index of stones[] if it exists.
        '''
        stone2idx = {pos: i for i, pos in enumerate(stones)}
        
        '''
        dp space
        dp[i][prev_k] = stones[i] can be reached by jumping from previous k units.
        
        p.s. why we allocate 2001 spaces for prev_k?
        while the input is limited in 2 <= len(stones) <= 2000,
        that means there's at most 1999 jumps from stones[0] to stones[1999],
        the initial jump is always 1 unit,
        and the number of k units of each jump is limited in {prev_k-1, prev_k, prev_k+1},
        so we may move at most 2000 units in the last jump.
        '''
        dp = [[False] * 2001 for _ in range(2001)]
        dp[0][0] = True
        
        n = len(stones)
        for i in range(n):
            for prev_k in range(n+1):
                '''
                when stones[i] is reachable from previous k units
                '''
                if dp[i][prev_k]:
                    stone_pos = stones[i]
                    '''
                    determine if next stones after {k-1, k, k+1} units exist or not.
                    '''
                    if stone2idx.get(stone_pos + prev_k - 1) is not None:
                        '''
                        we can reach stone2idx[stone_pos + prev_k - 1] from i by jumping k-1 units
                        '''
                        dp[stone2idx[stone_pos + prev_k - 1]][prev_k - 1] = True

                    if stone2idx.get(stone_pos + prev_k) is not None:
                        '''
                        we can reach stone2idx[stone_pos + prev_k] from i by jumping k units
                        '''
                        dp[stone2idx[stone_pos + prev_k]][prev_k] = True

                    if stone2idx.get(stone_pos + prev_k + 1) is not None:
                        '''
                        we can reach stone2idx[stone_pos + prev_k + 1] from i by jumping k+1 units
                        '''
                        dp[stone2idx[stone_pos + prev_k + 1]][prev_k + 1] = True

        # check if the frog can reach the last stone
        return any(dp[n-1])

