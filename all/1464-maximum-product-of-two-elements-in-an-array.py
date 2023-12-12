'''
2023/12/12 daily challenge

find the maximum and 2nd largest numbers
'''


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        big1 = big2 = -1

        for v in nums:
            if v >= big1:
                big1, big2 = v, big1
            elif v > big2:
                big2 = v

        return (big1 - 1) * (big2 - 1)

