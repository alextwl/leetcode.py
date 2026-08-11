'''
2026/08/11 daily challenge

hash + linear search (simulation) approach
'''


class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        seen = set(nums)
        it = iter(nums)
        prefix = prev = next(it)
        # scan the sequential prefix
        for v in it:
            if prev + 1 != v:
                break
            prefix += v
            prev = v
        # find the smallest ans
        while prefix in seen:
            prefix += 1
        return prefix

