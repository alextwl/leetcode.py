'''
2022/09/16 daily challenge

learnt from official approach 4, optimized from approach 3
time=O(m**2), space=O(m)
'''

class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)  # max op (0 <= op < m)
        n = len(nums)  # pointer of right boundary of nums
        
        '''
        look carefully when approach 3 calculates dp[op][left]
        it always accumulate scores from dp[op+1] row
        so it's possible to reduce dp space from 2D to 1D
        by copying next row before iterating left.
        '''
        dp = [0] * (m+1)
        
        for op in range(m-1, -1, -1):
            next_row = dp.copy()
            for left in range(op, -1, -1):
                dp[left] = max(multipliers[op] * nums[left] + next_row[left+1],
                               multipliers[op] * nums[n-1 - (op-left)] + next_row[left])
        
        return dp[0]


'''
learnt from official approach 3
not good enough because it exceeded time limit
time=O(m**2), space=O(m**2)
'''

class Solution2:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)  # max op (0 <= op < m)
        n = len(nums)  # pointer of right boundary of nums
        
        '''
        dp[op][left] = max score when (op, left)
        it's a (m*1)^2 matrix, not a (m*1)*left matrix
        because the index of left will not exceed max operations (m)
        even if len(nums) > m, there's no need to allocate unused spaces
        for full width (left) of matrix.
        
        height: 0 <= op <= m
        width: 0 <= left <= m
        '''
        dp = [[0] * (m+1) for _ in range(m+1)]
        
        '''
        calculate from the last multiplier and accumulate scores from the next operation.
        '''
        for op in range(m-1, -1, -1):
            '''
            iterate all possible left end.
            right end var can be derived from op & left later.
            '''
            for left in range(op, -1, -1):
                '''
                find max scores with current (op,left).
                
                max(select left end, select right end)
                '''
                dp[op][left] = max(multipliers[op] * nums[left] + dp[op + 1][left + 1],
                                   multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left])
        '''
        dp[0][0] is eventually an optimal answer
        just like recursively invoking from function call dp(op=0, left=0)
        '''
        return dp[0][0]
