'''
2023/08/30 daily challenge

greedy approach
'''

import math


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        n = len(nums)
        ops = 0  # the minimum number of operations
        
        '''
        check nums reversely, so that we can ensure the suffix part remains sorted
        '''
        it = reversed(nums)
        prev = next(it)
        for curr in it:
            if curr <= prev:
                # the curr to the end of array is already sorted.
                prev = curr
                continue
            
            '''
            given two adjacent nums:
            
            +---+
            | 9 |
            |   |
            |   +---+
            |   | 3 |
            +---+---+
            
            we can break the left part "9" into multiple pieces and
            maximize the pieces <= the right part "3":
            
            +---+---+---+---+
            | 3 | 3 | 3 | 3 |
            +---+---+---+---+
            
            so that we will get a non-decreasing array.
            '''
            pieces = math.ceil(curr / prev)
            
            # 2 pieces by 1 op, 3 pieces by 2 ops, etc.
            ops += pieces - 1
            
            '''
            maximize the pieces to prevent more operations in further rounds.
            '''
            prev = curr // pieces

        return ops

