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


'''
log prefix sum + binary search approach

learnt from official solution 2
https://leetcode.com/problems/subarray-product-less-than-k/solution/
'''

import bisect
import math


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        logk = math.log(k)
        
        # log(a*b) approximately equals to log(a) + log(b),
        # use the property to build prefix sum
        prefix_sum = [0]
        for v in nums:
            prefix_sum.append(prefix_sum[-1] + math.log(v))

        ans = 0
        for left, log_sum in enumerate(prefix_sum):
            # to mitigate the precision error
            # introduce 1e-9 subtraction to ensure in the most situation
            # prefix_sum[right] <= prefix_sum[left] + logk
            right = bisect.bisect(prefix_sum, log_sum + logk - 1e-9, left + 1)
            # note the left index is **excluded** from the sliding window
            ans += right - left - 1

        return ans

