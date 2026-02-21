'''
2026/02/21 daily challenge

set + method of exhaustion approach
'''


PRIMES = {2, 3, 5, 7, 11, 13, 17, 19}


class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1):
            if i.bit_count() in PRIMES:
                ans += 1
        return ans

