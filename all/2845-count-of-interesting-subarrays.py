'''
2025/04/25 daily challenge

prefix sum approach

learnt from official editorial:
https://leetcode.com/problems/count-of-interesting-subarrays/editorial/
'''


import collections


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)

        cnt = collections.Counter()
        prefix_sum = 0  # prefix of special elements
        ans = 0

        cnt[0] += 1
        for i, v in enumerate(nums):
            if v % modulo == k:
                prefix_sum += 1
            ans += cnt[(prefix_sum - k + modulo) % modulo]
            cnt[prefix_sum % modulo] += 1

        return ans

