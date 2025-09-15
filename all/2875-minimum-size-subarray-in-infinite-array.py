'''
sliding window approach
'''


class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        num_sum = sum(nums)
        # count the repeating times of nums
        multiplier, target = divmod(target, num_sum)

        arr = nums * 2
        window_sum = 0
        min_len = float('inf')
        left = 0
        for right, rval in enumerate(arr):
            window_sum += rval
            while window_sum > target and left <= right:
                window_sum -= arr[left]
                left += 1
            if window_sum == target:
                min_len = min(min_len, right - left + 1)
        if min_len == float('inf'):
            return -1
        return min_len + len(nums) * multiplier

