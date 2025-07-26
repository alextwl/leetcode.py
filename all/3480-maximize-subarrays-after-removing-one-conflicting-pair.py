'''
2025/07/26 daily challenge

sweeping approach

learnt from the solution by @tNikhil:
https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair/solutions/7005474/maximize-subarrays-a-single-pass-o-n-solution-python-c-java
'''


class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        right = [list() for _ in range(n + 1)]
        for u, v in conflictingPairs:
            if u > v:
                u, v = v, u
            right[v].append(u)

        ans = 0
        top1 = top2 = 0  # top 1st & 2nd `u` values
        bonus = [0] * (n + 1)  # total gain if conflict of `u` removed

        for r in range(1, n + 1):
            for l in right[r]:
                if l > top1:
                    top1, top2 = l, top1
                elif l > top2:
                    top1, top2 = top1, l
            ans += r - top1
            if top1 > 0:
                bonus[top1] += top1 - top2

        return ans + max(bonus)

