'''
2025/04/27 daily challenge

one-pass iteration approach
'''


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        it = iter(nums)
        v0 = next(it)
        v1 = next(it)
        for v2 in it:
            if v1 & 1 == 0 and (v0 + v2) == v1 >> 1:
                ans += 1
            v0, v1 = v1, v2
        return ans

