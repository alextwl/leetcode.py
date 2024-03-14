'''
2024/03/14 daily challenge

prefix sum approach
'''

import collections


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        psum_freq = collections.defaultdict(int)

        ans = 0
        prefix_sum = 0
        for v in nums:
            prefix_sum += v
            
            if prefix_sum == goal:
                ans += 1

            if (diff := prefix_sum - goal) in psum_freq:
                ans += psum_freq[diff]

            psum_freq[prefix_sum] += 1

        return ans


'''
sliding window approach
'''


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        
        window_sum = 0
        leading_zero_count = 0  # count leading zeros in the sliding window
        left = 0
        for right, right_val in enumerate(nums):
            window_sum += right_val
            
            while left < right and \
                    (nums[left] == 0 or window_sum > goal):
                if nums[left] == 1:
                    window_sum -= 1
                    leading_zero_count = 0
                else:
                    leading_zero_count += 1
                
                left += 1

            if window_sum == goal:
                # accumulate valid window plus (leading zeros + current window)
                ans += 1 + leading_zero_count

        return ans

