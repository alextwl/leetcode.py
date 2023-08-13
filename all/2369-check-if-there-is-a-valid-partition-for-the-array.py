'''
2023/08/13 daily challenge

dynamic programming approach
'''

class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        
        it = enumerate(iter(nums))
        '''
        check first 3 elements
        '''
        _, prev2 = next(it)
        _, prev1 = next(it)
        if prev2 == prev1:
            dp[1] = True
        if n < 3:
            return dp[1]

        _, curr = next(it)
        if (prev2 == prev1 == curr) or (prev2 + 2 == prev1 + 1 == curr):
            dp[2] = True

        prev2, prev1 = prev1, curr
        # check remaining elements
        for i, curr in it:
            if dp[i-2] and prev1 == curr:
                dp[i] = True
            elif dp[i-3] and \
                 ((prev2 == prev1 == curr) or \
                  (prev2 + 2 == prev1 + 1 == curr)):
                    dp[i] = True
            prev2, prev1 = prev1, curr

        return dp[-1]

