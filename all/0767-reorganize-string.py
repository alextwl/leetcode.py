'''
2023/08/23 daily challenge

counter approach

use the most common char as the split char,
and fill the remaining chars to the slots.

e.g. "aab", the most common char is 'a',

 s =  a a
     ^ ^ ^
slot 0 1 2

and then sequentially fill 'b' from slot[1] back and forth.
'''

import collections


class Solution:
    def reorganizeString(self, s: str) -> str:
        d = collections.Counter(s)
        most_char, most_len = d.most_common(1)[0]
        
        '''
        if the remaining chars were not enough to fill (len(slot)-1) at least once,
        we cannot rearrange the s.
        '''
        if most_len > (len(s) - most_len + 1):
            return ""
        
        '''
        let's rearrange the string.
        '''
        del d[most_char]
        
        slots = [""] * (most_len+1)
        n = len(slots)
        '''
        we need to fill from the slot 1 in the first round,
        and from the second round and later we can fill the slot 0.
        '''
        i = 1
        for c, v in d.items():
            for _ in range(v):
                if i == n:
                    i = 0
                slots[i] += c
                i += 1

        return most_char.join(slots)


'''
even/odd approach

learnt from official solution
https://leetcode.com/problems/reorganize-string/solution/

count the number of alphabets by counter,
and fill the slots in 2 rounds with batchs of alphabets.

round 1: fill even slots (0, 2, 4, ...)
round 2: fill odd slots (1, 3, 5, ...)
'''


class Solution:
    def reorganizeString(self, s: str) -> str:
        d = collections.Counter(s)
        most_char, most_len = d.most_common(1)[0]

        '''
        if the remaining chars were not enough to fill (len(slot)-1) at least once,
        we cannot rearrange the s.
        '''
        if most_len > (len(s) - most_len + 1):
            return ""

        '''
        fill the slots in even/odd index order
        '''
        n = len(s)
        t = [''] * n
        seq = iter(list(range(0, n, 2)) + list(range(1, n, 2)))

        for char, clen in d.most_common():
            for _ in range(clen):
                t[next(seq)] = char

        return ''.join(t)

