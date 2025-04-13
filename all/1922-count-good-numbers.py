'''
2025/04/13 daily challenge

combination approach (w/ builtin power function)
'''


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        # count indices by parity
        even = odd = n >> 1
        even += n & 1
        # even digits in even indices: [0, 2, 4, 6, 8], len=5
        ans = pow(5, even, 1_000_000_007)
        # prime digits in odd indices: [2, 3, 5, 7], len=4
        ans = ans * pow(4, odd, 1_000_000_007) % 1_000_000_007
        return ans

