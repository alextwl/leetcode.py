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

