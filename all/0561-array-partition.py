'''
sorting approach

to maximize min(ai, bi) we need to make the smaller one as big as possible,
the only way is to sort nums and pair every two consecutive numbers.
'''


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        return sum(sorted(nums)[::2])

