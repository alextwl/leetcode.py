'''
2023/04/23 daily challenge

dynamic programming approach

learnt from
https://leetcode.com/problems/restore-the-array/solutions/3445400/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        '''
        dp[i] = the number of the possible arays that can be printed as s[i:].
        base case s[n:] is an empty string which forms exactly _one_ empty array.
        '''
        dp = [0] * (n+1)
        dp[n] = 1

        # try to restore integers from the end of s.
        for i in range(n-1, -1, -1):
            if s[i] == '0':
                continue

            count = 0  # the number of the possible **numbers** that can be printed as s[i:*]
            '''
            validate characters starting from s[i] to its right chars
            until the restored integer is no longer valid.

            e.g. s="1317", k=200, i=0
            s[0:1] = "1" --> valid
            s[0:2] = "13" --> valid
            s[0:3] = "131" --> valid
            s[0:4] = "1317" > k --> invalid

            the number of the possible numbers is 3.
            '''
            j = i
            while j < n and int(s[i:j+1]) <= k:
                count += dp[j+1]  # accumulate the numbers from the next integers (s[j+1:*]... )
                j += 1
            dp[i] = count

        # the number of the possible arrays that can be printed as the full strings is the final ans
        return dp[0] % 1_000_000_007

