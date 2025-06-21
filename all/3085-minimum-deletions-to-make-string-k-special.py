'''
2025/06/21 daily challenge

counter + O(alphabets**2) approach
'''


import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ctr = collections.Counter(word)
        freqs = sorted(ctr.values())

        # without deleting least frequent chars
        threshold = freqs[0] + k
        ans = 0
        for v in reversed(freqs):
            if v <= threshold:
                break
            ans += v - threshold

        # with deleting lesser frequent chars
        deleted_base = 0
        for i in range(0, len(freqs) - 1):
            # try to remove freqs[:i+1] chars
            deleted_base += freqs[i]
            threshold = freqs[i+1] + k
            deleted = deleted_base
            for j in range(len(freqs) - 1, i, -1):
                if freqs[j] <= threshold:
                    break
                deleted += freqs[j] - threshold
            ans = min(ans, deleted)

        return ans


'''
slightly optimized ver

learnt from official editorial:
https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/editorial/#approach-hash-table--enumeration

just try to remove any kind of chars without sorting.
'''


import collections


class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ctr = collections.Counter(word)
        freqs = ctr.values()

        ans = len(word)
        for x in freqs:
            deleted = 0
            for y in freqs:
                if x > y:
                    # delete chars lesser frequent than x
                    deleted += y
                elif y > (threshold := x + k):
                    deleted += y - threshold
            ans = min(ans, deleted)
        return ans

