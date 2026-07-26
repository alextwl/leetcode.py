'''
2026/07/26 daily challenge

find largest & smallest multiplicands approach
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        top1 = top2 = top3 = -1001
        bom1 = bom2 = 1001

        for v in nums:
            if v > top1:
                top1, top2, top3 = v, top1, top2
            elif v > top2:
                top2, top3 = v, top2
            elif v > top3:
                top3 = v
            if v < bom1:
                bom1, bom2 = v, bom1
            elif v < bom2:
                bom2 = v
        # the product of 3 positive numbers or
        # the product of 1 positive & 2 negatives.
        return max(top1 * top2 * top3, top1 * bom1 * bom2)

