'''
2023/11/30 daily challenge

bit manipulation

learnt from official solution
https://leetcode.com/problems/minimum-one-bit-operations-to-make-integers-zero/solution/

To flip k-th bit:

1. the (k-1)th bit must be an 1, so we need f(k-1) steps.
2. k-th & (k-1)th bits are already 1s and (k-2)th~ bits are zero,
   we need 1 step to flip k-th bit to zero.
3. recover (k-1)th bit to zero, so we need another f(k-1) steps.

f(k) = f(k-1) + 1 + f(k-1)
     = 2*f(k-1) + 1
     = 2**(k+1) - 1  # derived from the observation of f(k) values.

Divide the problem into 2 parts:

1. find the most significant bit (the leftmost bit), k=MSB index,
   so we need f(k) steps.
2. for (k-1)th to 0-th bit, split this part from n (so we get n' = n ^ MSB),
   and if there's 1-bit between (k-1)th ~ 0-th,
   we can save some steps from reusing these bits and
   subtract minimumOneBitOperations(n')==A(n') from f(k) steps.

e.g. minimumOneBitOperations(26)
     = minimumOneBitOperations(0b11010)
     = f(4) - minimumOneBitOperations(0b11010 ^ 0b10000)
     = f(4) - minimumOneBitOperations(0b1010)
     = f(4) - (f(3) - minimumOneBitOperations(0b1010 ^ 0b1000))
     = f(4) - (f(3) - minimumOneBitOperations(0b10))
     = f(4) - (f(3) - (f(1) - minimumOneBitOperations(0b10 ^ 0b10)))
     = f(4) - (f(3) - (f(1) - 0))
     = 31 - (15 - 3)
     = 19
'''


class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            # already zeroed, no need to flip
            return 0
        
        k = 0  # the index of target bit to be flipped
        curr = 1  # the MSB==2**k
        
        # find the most significant bit
        while (curr << 1) <= n:
            curr <<= 1
            k += 1

        # f(k) - A(n')
        return (2**(k+1)-1) - self.minimumOneBitOperations(n ^ curr)

