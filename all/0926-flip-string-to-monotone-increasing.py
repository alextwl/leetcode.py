'''
2023/01/17 daily challenge

dynamic programming approach

divide the problem into:
if s is monotone increasing, any prefix substring of s is also monotone increasing.
define dp[i] as the number of flips of s[:i].
'''


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [0] * (len(s)+1)  # dp[0] = 0 for empty prefix
        prefix1s = 0  # the number of 1's in prefix
        for i, c in enumerate(s):
            '''
            consider moving a char from the suffix (right) to the prefix (left).
            '''
            if c == '0':
                '''
                2 cases:
                (1) if we flip c, it's equivalent to append a '1' to the end of the previous prefix
                    which remains monotone increasing, we can simply increase the flip count.
                    dp[i+1] = dp[i] + 1
                (2) if we don't flip c, all 1s in s[:i] are going to be flipped.

                get the minimum between the cases.
                '''
                dp[i+1] = min(dp[i]+1, prefix1s)
            else:
                # c == '1':
                '''
                we do **not** flip c and it also appends a '1' to the end of the previous prefix
                which remains monotone increasing, we can simply inherit the flip count from the previous.
                '''
                prefix1s += 1
                dp[i+1] = dp[i]

        return dp[-1]

