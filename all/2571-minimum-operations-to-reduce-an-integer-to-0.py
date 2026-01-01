'''
bitwise operations approach
'''


class Solution:
    def minOperations(self, n: int) -> int:
        ans = 0
        while n:
            if n & 1 == 0:
                # skip zero bits
                n >>= 1
            elif n & 0b10:
                # for consecutive 1's bits (len >= 2) case,
                # we will take at least two steps
                # (add a smallest power of two &
                # remove the additional MSB of the consecutive)
                # to remove it.
                # here we take the 1st step (add)
                n += 1
                ans += 1
                # 2nd step will be taken in further iteration
                #
                # e.g.
                # step 1: 0b0111 + 1 = 0b1000
                # step 2: 0b1000 - 0b1000 = 0
            else:
                # for only one 1's bit alone, just remove it in one step.
                n >>= 1
                ans += 1
        return ans

