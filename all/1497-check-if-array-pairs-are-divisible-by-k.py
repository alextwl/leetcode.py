'''
2024/10/01 daily challenge

counter approach (counting the remainders)

derive the equations:

(a + b) % k = 0

(a%k + b%k) % k = (mod_a + mod_b) % k = 0

mod_b = k - mod_a (except mod_a = mod_b = 0 because its sum is also divisable by k.)
'''


import collections


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        rems = collections.defaultdict(int)
        
        for v in arr:
            # note -10^9 <= arr[i] <= 10^9,
            # in other lang (e.g. C) we also need to handle negative numbers manually,
            # but in python it's properly handled.
            rems[v % k] += 1
        
        for v in arr:
            mod = v % k
            if mod == 0:
                # for mod_a = mod_b = 0 case
                if rems[0] & 1 == 1:
                    # there should be even numbers of zero remainders.
                    return False
            elif rems[mod] != rems[k - mod]:
                # the amount of mod_a & mod_b pairs should be equivalent.
                return False

        return True

