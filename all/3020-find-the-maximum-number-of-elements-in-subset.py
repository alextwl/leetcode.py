'''
2026/06/27 daily challenge

counter + brute force approach

brute force all distinct elements
'''


import collections


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)

        # base case: number 1's count rounded down to an odd
        ans = ctr.get(1, 0)
        if ans:
            ctr.pop(1)
            if ans & 1 == 0:
                ans -= 1

        seen = set()

        for v in ctr.keys():
            if v in seen:
                continue
            subset_len = 0
            # try to construct a valid subset,
            # any value except central element should have two or more occurances.
            while v in ctr and ctr[v] > 1:
                subset_len += 2
                seen.add(v)
                v = v * v
            ans = max(ans, subset_len + (1 if v in ctr else -1))

        return ans

