'''
2024/12/11 daily challenge

sliding window approach

sort the nums array and the question becomes:
finding max length of subarray a[-1] - a[0] <= k*2.
'''


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        kk = k * 2
        left = 0
        for v in nums:
            if nums[left] < v - kk:
                # only once, no need to shrink more because
                # we also use the difference between n & left as the max length in the end
                left += 1
        return len(nums) - left

