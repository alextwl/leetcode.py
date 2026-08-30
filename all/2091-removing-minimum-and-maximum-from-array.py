'''
2026/08/30 daily challenge

linear search the minimum & maximum and conditional logic approach
'''


class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        n = len(nums)
        # tracker vars for minimum value
        val0 = 100_001
        left0, right0 = -1, n
        # tracker vars for maximum value
        val1 = -100_001
        left1, right1 = -1, n

        # search the leftmost/rightmost positions of the minimum & maximum
        for i, v in enumerate(nums):
            if v < val0:
                val0 = v
                left0 = right0 = i
            elif v == val0:
                right0 = i
            if v > val1:
                val1 = v
                left1 = right1 = i
            elif v == val1:
                right1 = i

        # 4 scenarios:
        # (1) remove both min & max from left
        # (2) remove both min & max from right
        # (3) remove min from left and max from right
        # (4) remove max from left and min from right
        return min(1 + max(left0, left1),
                   n - min(right0, right1),
                   1 + left0 + n - right1,
                   1 + left1 + n - right0)

