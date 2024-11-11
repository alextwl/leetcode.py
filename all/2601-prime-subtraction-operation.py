'''
2024/11/11 daily challenge

brute force with precalculated primes
'''


import bisect


PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
          53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
          109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167,
          173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229,
          233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283,
          293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359,
          367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431,
          433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491,
          499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571,
          577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641,
          643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709,
          719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787,
          797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859,
          863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941,
          947, 953, 967, 971, 977, 983, 991, 997]


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        prev = 0
        
        for v in nums:
            # try to reduce v by all primes in decreasing order
            for p in range(bisect.bisect_left(PRIMES, v) - 1, -1, -1):
                if (diff := v - PRIMES[p]) > prev:
                    prev = diff
                    break
            else:
                # no operation for the current value: in case there's no prime can be subtracted
                if v <= prev:
                    # if it couldn't be just strictly less than the previous
                    return False
                prev = v

        return True


'''
Sieve of Eratosthenes + two pointer approach

learnt from official solution 3:
https://leetcode.com/problems/prime-subtraction-operation/solution/
'''


import math


class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        n = len(nums)
        max_val = max(nums)
        # sieve[i] == 1 indicates unmarked, a prime number
        sieve = [1] * (max_val + 1)
        
        # mark all non-primes
        sieve[1] = 0
        for i in range(2, math.isqrt(max_val + 1) + 1):
            if sieve[i]:
                # mark all multiples of i starting from i's square
                for j in range(i * i, max_val + 1, i):
                    sieve[j] = 0
        
        curr = 1  # the target value of nums[i]
        i = 0
        while i < n:
            diff = nums[i] - curr
            if diff < 0:
                # nums[i] is already less than curr
                return False
            
            # try to grow curr and check if we can do operation on nums[i]
            if sieve[diff] or diff == 0:
                # we can subtract nums[i] by diff as a prime,
                # or nums[i] can equal to curr,
                # we can move to nums[i+1]
                i += 1
                curr += 1
            else:
                # just try for the next curr
                curr += 1

        return True

