'''
2025/06/17 daily challenge

combinatorics approach

learnt from official editorial:
https://leetcode.com/problems/count-the-number-of-arrays-with-k-matching-adjacent-elements/editorial/#approach-combinatorial-mathematics
'''


MOD = 1_000_000_007
MAX = 100_000

# fact[x] = x!
fact = [0] * MAX
# inv_fact[x] = (x!)**(-1)
inv_fact = [0] * MAX


def qpow(x, n):
    # quick power under modulus
    ret = 1
    while n:
        if n & 1:
            ret = ret * x % MOD
        x = x * x % MOD
        n >>= 1
    return ret


# initialization for factorial & its inversion
fact[0] = 1
for i in range(1, MAX):
    fact[i] = fact[i - 1] * i % MOD
# Fermat's little theorem:
# a**p = a (mod p)
# a**(p-1) = 1 (mod p)
# a**(p-2) = a**(-1) (mod p)
inv_fact[MAX - 1] = qpow(fact[MAX - 1], MOD - 2)
for i in range(MAX - 1, 0, -1):
    inv_fact[i - 1] = inv_fact[i] * i % MOD


def comb(n, m):
    '''
     n          1        1
    C  = n! * ----- * --------
     m          m!    (n - m)!
    '''
    return fact[n] * inv_fact[m] % MOD * inv_fact[n - m] % MOD


class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        '''
             n-1
        m * C    * (m-1)**(n-k-1)
             k
        
        (1) 1st segment: m choices
        (2) remaining n - 1 positions have n-1-k choices:
             n-1      n-1        n-1
            C      = C        = C    ways
             n-1-k    (n-1)-k    k
        (3) each subsequent segment (n-k-1 segments) must
            differ from the previous segment's value, so each segment has m-1 choices:
            (m-1)**(n-k-1)
        '''
        return m * comb(n - 1, k) % MOD * qpow(m - 1, n - k - 1) % MOD

