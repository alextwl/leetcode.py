'''
2023/07/09 daily challenge

dynamic programming approach (modified Kadane's)

learnt from official solution
https://leetcode.com/problems/substring-with-largest-variance/
'''

import collections
import string


class Solution:
    def largestVariance(self, s: str) -> int:
        counter = collections.Counter(s)
        
        global_max = 0
        
        # iterate all pairs of (major, minor) twin lowercase alphabets
        for major in string.ascii_lowercase:
            for minor in string.ascii_lowercase:
                if major == minor or counter[major] == 0 or counter[minor] == 0:
                    # same char or inexistent char cannot form a valid substring.
                    continue
                
                major_count = minor_count = 0
                minor_remaining = counter[minor]
                
                # traverse the entire s and run Kadane's for major & minor chars.
                for c in s:
                    if c == major:
                        major_count += 1
                    elif c == minor:
                        minor_count += 1
                        minor_remaining -= 1
                    else:
                        # non-pair char, bypass.
                        continue
                    
                    '''
                    modified Kadane's:
                    a valid substring must contains at least one major and one minor,
                    if there's no minor char, we cannot accept current local max as global max.
                    '''
                    if minor_count > 0:
                        global_max = max(global_max, major_count - minor_count)
                    
                    '''
                    modified Kadane's:
                    we can reset the local counters only when local max comes negative
                    **and** there's more minor chars remaining
                    because if we reset here (== discard the substring from the beginning to here),
                    the further substring will be invalid if lack of minor chars.
                    '''
                    if major_count < minor_count and minor_remaining > 0:
                        major_count = minor_count = 0

        return global_max

