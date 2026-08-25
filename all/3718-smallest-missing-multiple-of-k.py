'''
2026/08/25 daily challenge

sorting + linear search approach
'''


class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums.sort()
        target = k
        for v in nums:
            if v == target:
                # target found
                target += k
            elif v > target:
                # target missing from nums
                break
        return target

