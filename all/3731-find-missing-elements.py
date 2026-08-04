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


'''
sorting-only ver
'''


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        nums.sort()
        min_val, max_val = nums[0], nums[-1]
        if len(nums) == (max_val - min_val + 1):
            return []

        ans = []
        it = iter(nums)
        next_target = next(it)
        for v in range(min_val, max_val + 1):
            if v != next_target:
                ans.append(v)
            elif v < max_val:
                next_target = next(it)

        return ans

