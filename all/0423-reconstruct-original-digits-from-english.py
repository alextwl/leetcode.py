'''
counter approach

it's also a hard-coded finite state machine.

the frequency of characters used by each dight's English word.

e 133577890
f 45
g 8
h 38
i 5689
n 1799
o 1240
r 340
s 67
t 238
u 4
v 57
w 2
x 6
z 0

phase 1: parse 02468 which have exclusive character

e 1335779
f 5
h 3
i 59
n 1799
o 1
r 3
s 7
t 3
v 57

phase 2: parse 1357 which have exclusive character in remaining subsequence

e 9
i 9
n 99

phase 3: count 9 by 'nine'
'''


import collections


class Solution:
    def originalDigits(self, s: str) -> str:
        ctr = collections.Counter(s)
        freq = [0] * 10

        # phase 1: parse 02468
        # zero
        if ctr['z']:
            freq[0] = ctr['z']
            ctr['e'] -= ctr['z']
            ctr['r'] -= ctr['z']
            ctr['o'] -= ctr['z']
        # two
        if ctr['w']:
            freq[2] = ctr['w']
            ctr['t'] -= ctr['w']
            ctr['o'] -= ctr['w']
        # four
        if ctr['u']:
            freq[4] = ctr['u']
            ctr['f'] -= ctr['u']
            ctr['o'] -= ctr['u']
            ctr['r'] -= ctr['u']
        # six
        if ctr['x']:
            freq[6] = ctr['x']
            ctr['s'] -= ctr['x']
            ctr['i'] -= ctr['x']
        # eight
        if ctr['g']:
            freq[8] = ctr['g']
            ctr['e'] -= ctr['g']
            ctr['i'] -= ctr['g']
            ctr['h'] -= ctr['g']
            ctr['t'] -= ctr['g']

        # phase 2: parse 1357
        # one
        if ctr['o']:
            freq[1] = ctr['o']
            ctr['n'] -= ctr['o']
            ctr['e'] -= ctr['o']
        # three
        if ctr['h']:
            freq[3] = ctr['h']
            ctr['e'] -= ctr['h'] * 2
            # 'thr' chars are already exclusive in this phase,
            # no need to remove.
        # five
        if ctr['f']:
            freq[5] = ctr['f']
            ctr['i'] -= ctr['f']
            # ctr['v'] -= ctr['f']
            ctr['e'] -= ctr['f']
        # seven
        if ctr['s']:
            freq[7] = ctr['s']
            ctr['e'] -= ctr['s'] * 2
            # ctr['n'] -= ctr['s']

        # phase 3: count 9
        if ctr['e']:
            # ctr['i'] or half of ctr['n'] are also valid
            freq[9] = ctr['e']

        return ''.join(str(i) * v for i, v in enumerate(freq))

