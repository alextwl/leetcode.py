'''
2025/04/12 daily challenge

permutation + combination approach

learnt from official editorial:
https://leetcode.com/problems/find-the-count-of-good-integers/editorial/#approach-1-enumeration--permutations-and-combinations
'''


import math


FAC = [math.factorial(i) for i in range(11)]  # cache of 0! to 10!


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        # find all palindromes by enumerating prefixes.
        pd = set()
        start = 10 ** ((n-1) // 2)  # the bottom of prefix
        skip = n & 1  # if n is odd, skip copying the center digit to suffix
        for prefix in map(str, range(start, start * 10)):
            num_str = prefix + prefix[::-1][skip:]
            if int(num_str) % k == 0:
                # we may have same set of digits arranged from different
                # palindromes or good integers, add distinct set of digits
                # by sorting digits to avoid redundant calculation.
                pd.add(''.join(sorted(num_str)))

        ans = 0
        for num_str in pd:
            count = [0] * 10  # counter of digits
            for c in num_str:
                count[int(c)] += 1
            # 1 non-zero digit + (n-1) arbitrary digits
            total = (n - count[0]) * FAC[n - 1]
            for x in count:
                # remove repeated numbers
                total //= FAC[x]
            ans += total

        return ans

