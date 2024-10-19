'''
2024/10/19 daily challenge

recursion (simulation) approach
'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f_si(i: int) -> list:
            if i == 1:
                return [0]
            si_1 = f_si(i - 1)
            return si_1 + [1] + list(map(lambda x: x ^ 1, reversed(si_1)))
        sn = f_si(n)
        return str(sn[k-1])

