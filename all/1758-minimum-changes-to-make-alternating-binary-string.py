'''
2023/12/24 daily challenge
2026/03/05 daily challenge

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


'''
traverse the string once only.
'''


class Solution:
    def minOperations(self, s: str) -> int:
        prev_a = 0
        flip_a = 0
        prev_b = 1
        flip_b = 0

        for v in map(int, s):
            if prev_a == v:
                flip_a += 1
            if prev_b == v:
                flip_b += 1
            prev_a ^= 1
            prev_b ^= 1

        return min(flip_a, flip_b)

