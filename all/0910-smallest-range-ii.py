'''
linear search approach
'''


class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0
        # remove duplicates
        nums = sorted(list(set(nums)))
        min_val, max_val = nums[0], nums[-1]
        min_diff = max_val - min_val
        # shortcut
        if min_diff <= k:
            return min_diff

        for a, b in zip(nums, nums[1:]):
            # no need to consider a-k & b+k because it definitely increases the diff.
            min_diff = min(min_diff, max(max_val - k, a + k) - min(min_val + k, b - k))
        return min_diff

