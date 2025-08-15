'''
counter + greatest common divisor approach

find numsDivide's common divisors in nums in ascending order
'''


import collections
import math


class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        min_gcd = numsDivide[0]
        for v in numsDivide:
            min_gcd = math.gcd(min_gcd, v)
            if min_gcd == 1:
                break
        
        cnt = collections.Counter(nums)
        if min_gcd == 1:
            return 0 if 1 in cnt else -1

        ans = 0
        keys = sorted(v for v in cnt.keys() if v <= min_gcd)
        for k in keys:
            if min_gcd % k == 0:
                break
            ans += cnt[k]
        else:
            # numsDivide's common divisors not found in nums
            return -1
        return ans

