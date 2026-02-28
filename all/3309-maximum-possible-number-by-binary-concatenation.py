'''
try all permutations
'''


class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
        v0, v1, v2 = nums
        l0, l1, l2 = v0.bit_length(), v1.bit_length(), v2.bit_length()
        ans = max((((v0 << l1) + v1) << l2) + v2,
                  (((v0 << l2) + v2) << l1) + v1,
                  (((v1 << l0) + v0) << l2) + v2,
                  (((v1 << l2) + v2) << l0) + v0,
                  (((v2 << l0) + v0) << l1) + v1,
                  (((v2 << l1) + v1) << l0) + v0)
        return ans

