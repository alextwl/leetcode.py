'''
2023/01/14 daily challenge

depth first search approach
'''

import string


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        # build the tree of equivalent chars
        conv = {c: set() for c in string.ascii_lowercase}
        for c1, c2 in zip(s1, s2):
            conv[c1].add(c2)
            conv[c2].add(c1)

        # traverse the tree and find each char's smallest equivalent char.
        smallest = dict()
        for k in string.ascii_lowercase:
            minChar = k
            # DFS
            q = [k]
            seen = {k}
            while(q):
                c = q.pop()
                if c == 'a':
                    '''
                    the lexicographically smallest character found.
                    no need to search further.
                    '''
                    minChar = c
                    break
                if c < minChar:
                    minChar = c

                # also need to search children (further equivalent chars)
                diff = conv[c] - seen
                q.extend(diff)
                seen.update(diff)

            # save the smallest equivalent char
            smallest[k] = minChar

        return ''.join([smallest[c] for c in baseStr])

