'''
2024/04/27 daily challenge

dynamic programming approach
'''

import collections


class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_len = len(ring)

        # char to the indices of the ring
        char_idx = collections.defaultdict(set)
        for i, c in enumerate(ring):
            char_idx[c].add(i)

        # dp space: prev[i], curr[i] = the minimum distance of spell ending at ring[i]
        prev = [0] * ring_len
        curr = [0] * ring_len

        # kickstart
        prev_ring_idx = 0
        it = iter(key)
        next_char = next(it)
        for next_char_idx in char_idx[next_char]:
            prev[next_char_idx] = min(next_char_idx, ring_len - next_char_idx) + 1
        prev_char = next_char
        #print("initial: %s" % str(prev))

        # proceed remaining key chars
        for next_char in it:
            prev_char_indices = char_idx[prev_char]
            next_char_indices = char_idx[next_char]
            for next_idx in next_char_indices:
                min_diff = float('inf')
                for prev_idx in prev_char_indices:
                    # find the minimum distance between two keys on the ring
                    # including clockwise & counterclockwise steps
                    # 3 cases:
                    # (1) the difference between 2 keys (does not across "12:00" direction) has the minimum
                    # (2) the previous key in the clockwise side from the next key (across "12:00" direction)
                    # (3) the next key in the clockwise side from the previous key (across "12:00" direction)
                    min_diff = min(min_diff,
                                   prev[prev_idx] + abs(next_idx - prev_idx),
                                   prev[prev_idx] + ring_len + prev_idx - next_idx,
                                   prev[prev_idx] + ring_len + next_idx - prev_idx)
                curr[next_idx] = min_diff + 1

            #print("%s: %s" % (next_char, str(curr)))
            prev_char = next_char
            prev, curr = curr, prev

        return min(steps for idx, steps in enumerate(prev) if ring[idx] == key[-1])

