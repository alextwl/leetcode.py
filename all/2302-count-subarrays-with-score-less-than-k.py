'''
2025/04/28 daily challenge

sliding window approach
'''


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        sub_sum = 0
        ans = 0
        left = 0
        for right, rval in enumerate(nums):
            sub_sum += rval
            while left <= right and sub_sum * (right - left + 1) >= k:
                # score >= k, shrink the window
                sub_sum -= nums[left]
                left += 1
            ans += right - left + 1

        return ans

