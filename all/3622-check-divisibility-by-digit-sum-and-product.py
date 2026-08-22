'''
2026/08/22 daily challenge

type conversion + simulation approach
'''


class Solution:
    def checkDivisibility(self, n: int) -> bool:
        dsum = 0
        dprod = 1
        for dig in map(int, str(n)):
            dsum += dig
            dprod *= dig
        return n % (dsum + dprod) == 0

