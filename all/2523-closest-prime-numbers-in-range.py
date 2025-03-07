'''
2025/03/07 daily challenge

Sieve of Eratosthenes approach
'''


import itertools


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        # use Sieve of Eratosthenes to mark non-primes.
        #
        # sieve[i] = boolean of i==prime
        sieve = [True] * (right + 1)
        sieve[0] = False
        sieve[1] = False

        for v in range(2, int(right**0.5) + 1):
            if sieve[v]:
                # for any v in [2, sqrt(upper bound)],
                # their multiples >= v**2 are not primes.
                for mul in range(v * v, right + 1, v):
                    sieve[mul] = False

        primes = [i for i, is_prime in enumerate(sieve) if is_prime and i >= left]
        min_diff = float('inf')
        closest = (-1, -1)

        if len(primes) < 2:
            return closest

        for a, b in itertools.pairwise(primes):
            diff = b - a
            if diff < min_diff:
                min_diff = diff
                closest = (a, b)

        return closest


'''
twin prime shortcut approach

learnt from official editorial 2:
https://leetcode.com/problems/closest-prime-numbers-in-range/editorial/#approach-2-analyze-distance-between-twin-primes

also see:
https://en.wikipedia.org/wiki/Twin_prime
'''


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def is_prime(p):
            for div in range(2, int(p**0.5) + 1):
                if p % div == 0:
                    return False
            return True

        prev = 0
        min_diff = float('inf')
        closest = (-1, -1)
        for v in range(max(2, left), right + 1):
            if v > 2 and v & 1 == 0:
                # skip even numbers (except 2)
                continue
            if is_prime(v):
                # we can return it immediately if it's a twin prime.
                if prev:
                    if v <= prev + 2:
                        return [prev, v]
                    diff = v - prev
                    if diff < min_diff:
                        min_diff = diff
                        closest = (prev, v)
                prev = v
        return closest

