'''
2024/03/27 daily challenge

sliding window approach
'''


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        product = 1
        for right, rval in enumerate(nums):
            if rval >= k:
                # shortcut: if rval is strictly equal to or larger than k,
                # restart the sliding window
                product = 1
                left = right + 1
            else:
                product *= rval

                while(product >= k and left <= right):
                    product //= nums[left]
                    left += 1

                ans += right - left + 1
        
        return ans

