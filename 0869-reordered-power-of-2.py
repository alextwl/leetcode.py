'''
list all power of 2's below 10**9 in advance
and compare amount of digits to find if input was possibly a power of 2.

learnt from
https://leetcode.com/problems/reordered-power-of-2/discuss/149843/C%2B%2BJavaPython-Straight-Forward
'''

from collections import Counter

class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        maxInt = 10**9
        all_powers = []
        
        # list all power of 2's
        num = 1
        while (num < maxInt):
            all_powers.append(str(num))
            num *= 2
        
        c = Counter(str(n))
        
        return any([c == Counter(p) for p in all_powers])
    
        # more pythonic returns
        # why range(30): 2**29 is the biggest power of 2 below 10**9.
        return any(c == Counter(str(1 << i)) for i in range(30))

        # extreme pythonic oneliner: just sort digits and compare strings of nums without counting.
        return sorted(str(N)) in [sorted(str(1 << i)) for i in range(30)]


'''
bruteforce: check all permutations
time=((logN)!*logN), actual runtime > 6s...
'''
class Solution2:
    def permute(self, s, pos=0):
        if pos >= len(s) - 1:
            # time to check if it's power of 2.
            if s[0] == '0':
                # leading zero excluded
                return False
            sbin = str(bin(int(''.join(s))))[2:]
            if sbin.count('1') > 1:
                # not a power of 2.
                return False
            if sbin[-1] != '0':
                return False
            # it's a power of 2.
            return True
        
        for j in range(pos, len(s)):
            s[pos], s[j] = s[j], s[pos]
            if self.permute(s, pos+1):
                # return immediately if we found a power of 2.
                return True
            s[pos], s[j] = s[j], s[pos]
        
        # power of 2 not found.
        return False
    
    def reorderedPowerOf2(self, n: int) -> bool:
        s = list(str(n))
        
        return self.permute(s)
