'''
2024/02/16 daily challenge

sorting + frequency approach
'''

import collections
import math


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # value to frequency
        v2f = collections.Counter(arr)
        # frequency to the number of values
        f2c = collections.defaultdict(int)
        for f in v2f.values():
            f2c[f] += 1

        # remove k from least frequency
        for f in sorted(f2c.keys()):
            count = f * f2c[f]
            if k >= count:
                del f2c[f]
                k -= count
            else:
                f2c[f] = math.ceil((count - k) / f)
                break

        return sum(f2c.values())

