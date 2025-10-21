'''
2025/10/21 daily challenge

counter + sorting + binary search approach

learnt from official editorial:
https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/editorial/#approach-sort--enumerate--binary-search
'''


import bisect
import collections


class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        n = len(nums)
        cnt = collections.Counter(nums)
        ans = 0

        for v in range(nums[0], nums[-1] + 1):
            # inclusive left
            left = bisect.bisect_left(nums, v - k)
            # exclusive right - 1 == inclusive right (the last element in the range)
            right = bisect.bisect_right(nums, v + k) - 1
            ans = max(ans, min(right - left + 1, cnt[v] + numOperations))

        return ans

