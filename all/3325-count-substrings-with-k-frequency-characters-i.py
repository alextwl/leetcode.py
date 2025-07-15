'''
sliding window approach

solve the problem reversely:

          (n + 1) * n
there are ----------- substrings,
                2

use sliding window to frame those invalids and remove it.
'''


import collections


class Solution:
    def numberOfSubstrings(self, s: str, k: int) -> int:
        n = len(s)
        ans = (n + 1) * n // 2
        ctr = collections.defaultdict(int)
        k_chars = 0
        i = 0
        for j, c in enumerate(s):
            ctr[c] += 1
            while ctr[c] >= k:
                ctr[s[i]] -= 1
                i += 1
            # remove invalid substrings
            ans -= j - i + 1
        return ans

