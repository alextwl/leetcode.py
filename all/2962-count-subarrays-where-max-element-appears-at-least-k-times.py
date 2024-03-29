'''
2024/03/29 daily challenge

sliding window approach

note the problem just asks for subarrays including **the maximum element**,
**NOT** the maximum frequency of elements.

there is only one distinct maximum element which has largest value.
'''


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)

        count = 0
        max_num_in_window = 0
        left = 0

        for right, right_num in enumerate(nums):
            if right_num == max_num:
                max_num_in_window += 1

            # shrink window
            while max_num_in_window >= k:
                if nums[left] == max_num:
                    max_num_in_window -= 1
                left += 1

            # there are `left` number of valid subarrays ending at nums[right]
            # including nums[0:right+1] to nums[left-1:right+1]
            count += left

        return count

