'''
sorting digits.
'''


import collections


class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:
            return 0
        if num > 0:
            # positive
            ctr = collections.Counter(str(num))
            keys = sorted(ctr.keys())
            # choose smallest digit as leftmost digit except leading zero
            s = []
            if keys[0] == '0':
                s.append(keys[1])
                ctr[keys[1]] -= 1
            for k in keys:
                s.append(k * ctr[k])
        else:
            # negative
            s = list(str(num)[1:])
            # sort digits in descending order
            s.sort(reverse=True)
            s.insert(0, '-')
        return int(''.join(s))

