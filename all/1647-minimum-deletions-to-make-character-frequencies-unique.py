'''
2023/09/12 daily challenge

counter approach
'''

import collections


class Solution:
    def minDeletions(self, s: str) -> int:
        char_counts = collections.Counter(s)
        
        # convert to freqs[freq] = the number of characters with the same frequency
        freqs = collections.defaultdict(int)
        for freq in char_counts.values():
            freqs[freq] += 1
        
        # find empty slots of unique frequencies
        dup_freqs = sorted(freq for freq, count in freqs.items() if count >= 2)
        if not dup_freqs:
            # there's no duplicate frequency, no need to go further.
            return 0

        left_slots = []
        
        ans = 0
        prev = 1
        for dup in dup_freqs:
            # check available left slots
            for i in range(prev, dup):
                if freqs[i] == 0:
                    left_slots.append(i)
            
            # search nearest slot and do deletion
            # to let only single alphabets with the specific frequency
            for _ in range(freqs[dup] - 1):
                if left_slots:
                    ans += dup - left_slots.pop()
                else:
                    # there's no space left. we can just delete all of the char
                    # because frequency of 0 is ignored.
                    ans += dup

            prev = dup + 1

        return ans

