'''
2023/02/04 daily challenge

sliding window approach
'''

import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        pLen = len(s1)
        pSet = set(s1)
        charCounts = collections.Counter(s1)

        pCharNeeded = pLen
        nonCharSeen = 0
        q = collections.deque()  # fifo for chars in the window
        isPermutationFound = lambda: all(charCounts[ch] == 0 for ch in pSet)

        # initial lookup
        it = iter(s2)
        for _ in range(pLen):
            c = next(it)
            charCounts[c] -= 1
            if c in pSet:
                pCharNeeded -= 1
            else:
                nonCharSeen += 1
            q.append(c)
        
        if pCharNeeded == 0 and isPermutationFound():
            return True
        
        # continue searching
        for c in it:
            charCounts[c] -= 1
            if c in pSet:
                pCharNeeded -= 1
            else:
                nonCharSeen += 1
            q.append(c)

            # pop last char outside of window
            prev = q.popleft()
            charCounts[prev] += 1
            if prev in pSet:
                pCharNeeded += 1
            else:
                nonCharSeen -= 1
            
            # check permutation
            if pCharNeeded == 0 and isPermutationFound():
                return True

        # permutation not found after entire s2 iterated
        return False

