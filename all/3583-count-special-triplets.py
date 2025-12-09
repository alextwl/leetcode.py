'''
2025/12/09 daily challenge

counter approach
'''


import collections


class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        ans = 0
        cnt0 = collections.Counter()  # left counter
        cnt1 = collections.Counter(nums)  # right counter
        for v in nums:
            cnt1[v] -= 1
            j2 = v * 2
            ans = (ans + cnt0[j2] * cnt1[j2]) % 1_000_000_007
            cnt0[v] += 1

        return ans

