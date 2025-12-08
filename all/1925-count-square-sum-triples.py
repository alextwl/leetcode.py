'''
2025/12/08 daily challenge

lookup table + O(n**2) search approach
'''


SQ = {i: i ** 2 for i in range(1, 251)}
SQRT = set(SQ.values())


class Solution:
    def countTriples(self, n: int) -> int:
        max_square = SQ[n]
        ans = 0

        for k0 in range(1, n):
            v0 = SQ[k0]  # a ** 2
            # for case in a == b
            if v0 + v0 in SQRT:
                ans += 1
            # for case in a < b
            for k1 in range(k0 + 1, n):
                target = v0 + SQ[k1]  # a ** 2 + b ** 2
                if target > max_square:
                    break
                if target in SQRT:
                    ans += 2
        return ans

