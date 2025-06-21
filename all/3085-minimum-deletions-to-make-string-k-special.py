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

