'''
2023/12/20 daily challenge

minimize the cost of chocolates or don't buy if in debt.
'''


class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min2 = 101

        for p in prices:
            if p <= min1:
                min1, min2 = p, min1
            elif p < min2:
                min2 = p

        leftover = money - min1 - min2

        return money if leftover < 0 else leftover

