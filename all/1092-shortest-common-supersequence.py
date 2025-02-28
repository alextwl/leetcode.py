'''
2025/02/28 daily challenge

brute force (recursion) approach (TLE)
'''


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        if not str1 and not str2:
            return ""
        if not str1:
            return str2
        if not str2:
            return str1
        if str1[0] == str2[0]:
            # 1st char matched, place it into the SCS
            return str1[0] + self.shortestCommonSupersequence(str1[1:], str2[1:])
        # decision: place the char from either str1 or str2 into the SCS
        scs1 = str1[0] + self.shortestCommonSupersequence(str1[1:], str2)
        scs2 = str2[0] + self.shortestCommonSupersequence(str1, str2[1:])
        return scs1 if len(scs1) < len(scs2) else scs2


'''
dynamic programming (bottom-up) approach

learnt from official editorial 3:
https://leetcode.com/problems/shortest-common-supersequence/editorial/#approach-3-bottom-up-dynamic-programming
'''


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)

        # optimized from 2D dp space: dp[i][j]
        # scs dp space: empty str1, start from str2's every prefix
        prev = [str2[:i] for i in range(n2 + 1)]
        curr = [None] * (n2 + 1)

        # iterate each str1's prefix by row
        for i in range(1, n1 + 1):
            # scs dp space: current str1 prefix + empty str2 (reusing previous' prev space)
            curr[0] = str1[:i]
            for j in range(1, n2 + 1):
                if str1[i-1] == str2[j-1]:
                    # char matched
                    curr[j] = prev[j-1] + str1[i-1]  # == dp[i-1][j-1] + common char
                else:
                    # char mismatch, choose shorter common supersequence
                    scs1 = prev[j]    # == dp[i-1][j]
                    scs2 = curr[j-1]  # == dp[i][j-1]
                    curr[j] = scs1 + str1[i-1] if len(scs1) < len(scs2) else scs2 + str2[j-1]
            prev, curr = curr, prev
        return prev[-1]

