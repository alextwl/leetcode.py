'''
2023/11/27 daily challenge

dynamic programming approach
'''

import functools


class Solution:
    def knightDialer(self, n: int) -> int:
        # jump from any cell to next L-move destinations
        jump_from = {1: [6, 8],
                     2: [7, 9],
                     3: [4, 8],
                     4: [3, 9, 0],
                     5: [],
                     6: [1, 7, 0],
                     7: [2, 6],
                     8: [1, 3],
                     9: [2, 4],
                     0: [4, 6]}
        
        @functools.cache
        def dp(k, cell):
            if k == 0:
                # no more remaining jump
                return 1
            
            steps = 0
            for next_step in jump_from[cell]:
                steps = (steps + dp(k-1, next_step)) % 1_000_000_007
            
            return steps

        ans = 0
        for start_cell in range(10):
            ans = (ans + dp(n-1, start_cell)) % 1_000_000_007

        return ans

