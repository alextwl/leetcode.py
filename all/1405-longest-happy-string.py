'''
2024/10/16 daily challenge

sorting & string manipulation approach
'''


import itertools


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        elems = []
        if a: elems.append([a, 'a'])
        if b: elems.append([b, 'b'])
        if c: elems.append([c, 'c'])        
        elems.sort()

        # get the max-length char
        s0_cnt, s0_char = elems.pop()
        # calculate the slots where the 2nd and 3rd (if avail) chars can be inserted into
        slots = (s0_cnt + 1) // 2
        # generate the max char and group by at most width-2 substrings
        s0 = s0_char * s0_cnt
        s0 = list(map(''.join, itertools.zip_longest(*[iter(s0)] * 2, fillvalue='')))

        # generate the 2nd & 3rd chars and convert to a serial string
        s1 = ''.join(c * cnt for cnt, c in elems)
        # distribute it to slots
        substrs = [list() for _ in range(slots)]
        i = 0
        for c in s1:
            substrs[i].append(c)
            i += 1
            if i >= slots:
                i = 0

        # pop empty slots to meet the condition
        while substrs:
            if not substrs[-1]:
                substrs.pop()
            else:
                break
        # reserve at most 1 empty slot which is allowed
        # so that we can make a longer string by appending 1 or 2 more max-chars
        if len(substrs) < slots:
            substrs.append([])

        ans = ''.join(x + y for x, y in zip(s0, map(''.join, substrs)))
        return ans

