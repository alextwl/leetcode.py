'''
2024/03/28 daily challenge

sliding window approach
'''

import collections


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)
        longest = 0

        left = 0
        for right, curr_num in enumerate(nums):
            freq[curr_num] += 1

            # shrink the window
            while(left <= right and freq[curr_num] > k):
                freq[nums[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


'''
non-shrinking window ver

just keep the size of window remains or grows,
no need to shrink it and no need to track maximum window size in the loop.
'''

import collections


class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = collections.defaultdict(int)

        exceeded_part = 0
        left = 0
        for curr_num in nums:
            freq[curr_num] += 1

            if freq[curr_num] > k:
                exceeded_part += 1

            if exceeded_part:
                # there are frequencies more than k, do not grow the window.
                if freq[nums[left]] > k:
                    exceeded_part -= 1
                freq[nums[left]] -= 1
                left += 1

        return len(nums) - left

