'''
2023/07/14 daily challenge

dynamic programming approach
'''


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        '''
        the length of longest arithmetic sequence is at least 1
        for each element as a subsequence.
        '''
        max_len = 1

        # dp[val] = the length of longest arithmetic subsequence ending at integer val.
        dp = {}

        for val in arr:
            '''
            for the current integer val, the previous val is (val - difference).
            if the previous val was not yet available,
            we can start a new subsequence at the current val.
            '''
            prev_val = dp.get(val - difference, 0)
            dp[val] = prev_val + 1
            max_len = max(max_len, dp[val])

        return max_len

