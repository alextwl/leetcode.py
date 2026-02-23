'''
method of exhaustion approach

verify and compare with all permutations.
'''


import itertools


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        ans = ""

        for a, b, c, d in itertools.permutations(arr):
            hh = a * 10 + b
            mm = c * 10 + d
            if hh > 23 or mm > 59:
                continue
            ans = max(ans, "%02d:%02d" % (hh, mm))

        return ans

