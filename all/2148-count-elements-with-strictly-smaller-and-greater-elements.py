'''
counting approach

all elements except minimum & maximum
are with strictly smaller & greater elements.
'''


class Solution:
    def countElements(self, nums: List[int]) -> int:
        min_val = min(nums)
        max_val = max(nums)
        if min_val == max_val:
            return 0
        return len(nums) - nums.count(min_val) - nums.count(max_val)

