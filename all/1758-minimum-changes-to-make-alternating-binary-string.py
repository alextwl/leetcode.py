'''
2023/12/24 daily challenge

just count operations in two ways '010101...' & '101010...'
and return the minimum.
'''


class Solution:
    def minOperations(self, s: str) -> int:
        def getOps(prev, bin_str):
            ops = 0
            for c in bin_str:
                if prev == c:
                    ops += 1
                    prev = '0' if prev == '1' else '1'
                else:
                    prev = c
            return ops

        return min(getOps('0', s), getOps('1', s))

