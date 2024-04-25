'''
2024/04/25 daily challenge

dynamic programming approach (iteration ver)

memorize the max length of subsequences ending with each lowercase alphabets.
'''


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        n = len(s)

        # dp[i] = the max length of subsequence ending with chr(i)
        dp = [0] * 26
        a = ord('a')

        for i, c in enumerate(s):
            val = ord(c) - a
            max_sublen = 0
            for prev_val in range(max(val - k, 0), min(val + k + 1, 26)):
                max_sublen = max(max_sublen, dp[prev_val])
            # append character c to the maximum length subsequence within k difference we've found in this round.
            dp[val] = max(dp[val], max_sublen + 1)

        return max(dp)

