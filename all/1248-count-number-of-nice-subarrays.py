'''
2024/06/22 daily challenge

sliding window approach

counting at most k is much easier than counting exact k.

exact k = at most k - at most (k-1)
'''


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def at_most_k(k):
            odds = 0
            subarrays = 0
            left = 0
            for right, v in enumerate(nums):
                if v & 1:
                    odds += 1
                while odds > k:
                    if nums[left] & 1:
                        odds -= 1
                    left += 1
                subarrays += right - left + 1
            return subarrays
        return at_most_k(k) - at_most_k(k - 1)

