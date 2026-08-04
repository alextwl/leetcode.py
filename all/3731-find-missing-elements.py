'''
2026/08/04 daily challenge

set + sorting approach
'''


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_val, max_val = min(nums), max(nums)
        if len(nums) == (max_val - min_val + 1):
            return []

        return sorted(list(set(range(min_val, max_val + 1)) - set(nums)))

