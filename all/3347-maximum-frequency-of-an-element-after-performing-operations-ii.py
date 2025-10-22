'''
2025/10/22 daily challenge

counter + sorting + binary search approach

equivalent to problem 3346 with larger input.

enumerating nums[i] - k, nums[i], and nums[i] + k once only instead of
searching each value in nums is more optimal.
'''


import bisect
import collections


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        nums.sort()

        cnt = collections.Counter(nums)
        keys = set(cnt.keys())
        min_val, max_val = nums[0], nums[-1]
        for v in cnt.keys():
            if (minus_k := v - k) > min_val:
                keys.add(minus_k)
            if (plus_k := v + k) < max_val:
                keys.add(plus_k)

        ans = 0
        for v in sorted(keys):
            left = bisect.bisect_left(nums, v - k)
            right = bisect.bisect_right(nums, v + k) - 1
            ans = max(ans, min(right - left + 1, cnt[v] + numOperations))

        return ans

