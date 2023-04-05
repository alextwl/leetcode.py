'''
2023/04/05 daily challenge

intuition:
(1) the sum of nums is unchanged no matter how many operations were done.
    for nums=[a,b], a+b == (a+1)+(b-1).
(2) the minimum possible value of the maximum integer depends on
    how do we decrease the latter value to the former one.
(3) start from the first 2 elements as the initial subarray,
    maximize the ceiled average and grow the subarray,
    the overall maximum average of the subarray is the answer,
    the minimum possible value.
'''

import math


class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        ans = 0
        total_sum = 0
        for i, val in enumerate(nums, start=1):
            total_sum += val
            ans = max(ans, math.ceil(total_sum / i))
        
        return ans

