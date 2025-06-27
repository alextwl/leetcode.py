'''
2025/06/27 daily challenge

brute force method approach

learnt from official editorial:
https://leetcode.com/problems/longest-subsequence-repeated-k-times/editorial/#approach-brute-force-enumeration
'''


import collections


class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        cnt = collections.Counter(s)
        candidates = sorted([c for c, v in cnt.items() if v >= k], reverse=True)
        ans = ""
        q = collections.deque(candidates)
        while q:
            curr = q.popleft()
            if len(curr) > len(ans):
                ans = curr
            for c in candidates:
                next_subseq = curr + c
                # this checks k multiples of next_subseq existed in s by matching each char
                it = iter(s)
                # the inner __in__ iterates until next char found or end of string
                if all(char in it for char in next_subseq * k):
                    q.append(next_subseq)
        return ans

