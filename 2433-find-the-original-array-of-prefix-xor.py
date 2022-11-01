'''
XOR cancel approach (time limit exceeded)

according to example 1:

pref[4] = 5 ^ 7 ^ 2 ^ 3 ^ 2 = 1.
pref[4] = arr[0] ^ arr[1] ^ arr[2] ^ arr[3]

to recover arr[3], we can rewrite it to:

pref[4] ^ arr[0] ^ arr[1] ^ arr[2]
= (arr[0] ^ arr[1] ^ arr[2] ^ arr[3]) ^ (arr[0] ^ arr[1] ^ arr[2])
= arr[3]

use reduce() to reiterate such annoying calculation:

arr[3] = (((pref[4] ^ arr[0]) ^ arr[1]) ^ arr[2])
'''

import functools

class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]]
        
        for i in range(1, len(pref)):
            # note initial number (pref[i]) is provided as the first x which is not in recovered arr.
            arr.append(functools.reduce(lambda x, y: x^y, arr, pref[i]))
        
        return arr
