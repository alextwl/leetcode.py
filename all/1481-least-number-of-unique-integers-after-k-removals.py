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


'''
min heap approach

learnt from official solution 2.
'''

import collections
import heapq


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # value to frequency
        v2f = collections.Counter(arr)
        # list of frequencies & convert from dict_keys to heap.
        # the remaining length of freqs will be the least number of unique integers. 
        freqs = list(v2f.values())
        heapq.heapify(freqs)
        
        removed = 0
        while(freqs):
            # try to remove numbers from the least frequency
            removed += heapq.heappop(freqs)

            if removed > k:
                # numbers of the current frequency were not totally removed,
                # that counts one unique number although it's popped from the heap.
                return len(freqs) + 1

        # the arr is entirely removed. (len(arr) == k case)
        return 0

