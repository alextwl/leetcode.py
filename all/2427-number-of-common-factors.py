'''
count factors of GCD of a & b.
'''


class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a < b:
            a, b = b, a
        # find gcd
        while b:
            a, b = b, a % b

        ans = 1
        for i in range(2, a + 1):
            if a % i == 0:
                ans += 1
        return ans

