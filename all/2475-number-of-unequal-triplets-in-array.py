'''
O(n**3) brute-force approach
'''


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, v0 in enumerate(nums):
            for j in range(i + 1, n - 1):
                v1 = nums[j]
                if v0 == v1:
                    continue
                for k in range(j + 1, n):
                    v2 = nums[k]
                    if v0 != v2 and v1 != v2:
                        ans += 1
        return ans


'''
counter approach

use the count of middle element to calculate combinations of triplets.
counter also guarantees pairwise distinct condition by keys.
the actual values of triplets are not relevant.
'''


import collections


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        ans = 0
        left, right = 0, len(nums)  # possible counts of nums[i], nums[k]
        for cnt in collections.Counter(nums).values():
            right -= cnt
            # count of nums[i] * count of nums[j] * count of nums[k]
            ans += left * cnt * right
            left += cnt
        return ans

