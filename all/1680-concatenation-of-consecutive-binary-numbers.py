'''
2022/09/23 daily challenge
2026/02/28 daily challenge

simulation approach
'''


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        ans = 0
        
        for x in range(1, n+1):
            '''
            1. shift the number of length of x in binary form.
               len(bin(x)) - 2 == len(bin(x)[2:])
            2. since shifted bits were zeroed in default, add x to write shifted bits.
            3. apply modulo
            '''
            ans = ((ans << (len(bin(x)) - 2)) + x) % modulo
        
        return ans


'''
recursion ver
'''


MOD = 1_000_000_007


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        if n == 1:
            return 1
        prev = self.concatenatedBinary(n - 1)
        return ((prev << n.bit_length()) + n) % MOD


'''
lookup table method (LUT) approach
'''


MOD = 1_000_000_007
TABLE = [0] * 100_001

# pre-compute all answers
curr = 0
# max bit length of input (10**5) is 17.
for sup in range(1, 18):
    for v in range(1 << (sup - 1), min(1 << sup, 100_001)):
        curr = ((curr << sup) | v) % MOD
        TABLE[v] = curr


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return TABLE[n]

