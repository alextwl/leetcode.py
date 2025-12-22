'''
2025/12/22 daily challenge

dynamic programming approach

learnt from official editorial:
https://leetcode.com/problems/delete-columns-to-make-sorted-iii/editorial/#solution

similar to problem 300 longest increasing subsequence
'''


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])  # width of single element in strs
        # dp[k] = number of columns kept for all s[k:] in strs
        dp = [1] * n
        # find longest subsequence in lexicographic order
        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                if all(s[i] <= s[j] for s in strs):
                    # column i & j in all rows are lexicographically ordered.
                    # try to maximize dp[i] if we delete cols between i and j.
                    dp[i] = max(dp[i], 1 + dp[j])
        # n - longest == the minimal number of columns to be deleted
        return n - max(dp)

