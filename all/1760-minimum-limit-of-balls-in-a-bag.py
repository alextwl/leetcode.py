'''
2024/12/07 daily challenge

binary search approach

change the problem to "binary search the maximum size of a bag."
'''

import math


class Solution:
    def minimumSize(self, nums: List[int], maxops: int) -> int:
        def validate(max_size):
            # validate if the max size of a bag is possible
            # within the limitation of maxOperations.
            ops = 0
            for v in nums:
                if v > max_size:
                    ops += math.ceil(v / max_size) - 1
                    if ops > maxops:
                        return False
            return ops <= maxops

        left, right = 1, max(nums)  # max bag size
        while left < right:
            mid = (left + right) // 2
            if validate(mid):
                right = mid
            else:
                left = mid + 1

        return right

