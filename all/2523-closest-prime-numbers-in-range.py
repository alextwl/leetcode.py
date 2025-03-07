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

